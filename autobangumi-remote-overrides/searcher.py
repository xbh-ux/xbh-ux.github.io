import asyncio
import json
import logging
import re
from collections import OrderedDict
from typing import TypeAlias

from module.conf import settings
from module.conf.search_provider import get_provider
from module.models import Bangumi, Movie, RSSItem, Torrent
from module.network import RequestContent
from module.parser.analyser.tmdb_parser import tmdb_parser
from module.rss import RSSAnalyser

from .provider import search_url

logger = logging.getLogger(__name__)

SEARCH_KEY = [
    "group_name",
    "title_raw",
    "season_raw",
    "subtitle",
    "source",
    "dpi",
]

BangumiJSON: TypeAlias = str

AGGREGATE_SEARCH_SITES = {"总搜", "all", "全源", "all-sources"}
FAST_AGGREGATE_PROVIDERS = {"mikan", "anibt"}
AGGREGATE_PROVIDER_TIMEOUT = 6
AGGREGATE_POSTER_TIMEOUT = 3
AGGREGATE_POSTER_LOOKUPS = 8
CJK_PATTERN = re.compile(r"[\u3400-\u9fff]")

# Cache for TMDB preview lookups by official_title. Bounded (LRU-ish,
# oldest-evicted) like _tmdb_cache/_mikan_cache — was previously a plain dict
# and grew unbounded for the life of the process. Values are keyed by parser
# language because the title is localized while the poster URL usually is not.
_POSTER_CACHE_MAX = 512
_poster_cache: "OrderedDict[str, dict[str, tuple[str | None, str | None]]]" = (
    OrderedDict()
)


def reset_cache() -> None:
    """清空 TMDB 海报查询缓存。配置重载（如 tmdb_base_url 变更）后必须调用，
    否则会继续返回旧接口地址下缓存的结果。"""
    _poster_cache.clear()


def _normalize_keyword(text: str) -> str:
    return re.sub(r"[\W_]+", "", text).casefold()


def _candidate_text(bangumi: Bangumi, torrent: Torrent) -> str:
    return " ".join(
        value
        for value in (
            bangumi.official_title,
            bangumi.title_raw,
            bangumi.subtitle,
            torrent.name,
        )
        if value
    )


def _matches_keyword(keyword: str, bangumi: Bangumi, torrent: Torrent) -> bool:
    query = _normalize_keyword(keyword)
    if not query:
        return True
    candidate = _normalize_keyword(_candidate_text(bangumi, torrent))
    return query in candidate


def _tmdb_lookup_candidates(bangumi: Bangumi) -> list[str]:
    raw_titles = [
        title
        for title in (bangumi.official_title, bangumi.title_raw)
        if title and title.strip()
    ]
    candidates: list[str] = []
    for title in raw_titles:
        candidates.append(title)
        cleaned = re.sub(r"\[[^\]]+\]|\([^)]+\)", " ", title)
        cleaned = re.sub(
            r"\b(END|BDRip|WEB[- ]?DL|R-ESRGAN|HEVC.*|AAC.*|SRT.*|Ani[- ]?One.*|KoVer|JaVer).*$",
            "",
            cleaned,
            flags=re.IGNORECASE,
        ).strip(" -_/|")
        if cleaned:
            candidates.append(cleaned)
        if re.search(r"\bsolo\s+leveling\b", title, re.IGNORECASE):
            candidates.append("Solo Leveling")
        if re.search(r"\bore\s+dake\s+level\s+up\s+na\s+ken\b", title, re.IGNORECASE):
            candidates.append("Ore dake Level Up na Ken")

    seen: set[str] = set()
    deduped: list[str] = []
    for candidate in candidates:
        key = candidate.casefold()
        if key not in seen:
            seen.add(key)
            deduped.append(candidate)
    return deduped


class SearchTorrent:
    def __init__(self):
        self.analyser = RSSAnalyser()

    async def search_torrents(self, rss_item: RSSItem) -> list[Torrent]:
        async with RequestContent() as req:
            return await req.get_torrents(rss_item.url)

    async def _search_provider(
        self, site: str, keywords: list[str]
    ) -> tuple[str, RSSItem | None, list[Torrent]]:
        try:
            rss_item = search_url(site, keywords)
            torrents = await asyncio.wait_for(
                self.search_torrents(rss_item), timeout=AGGREGATE_PROVIDER_TIMEOUT
            )
            return site, rss_item, torrents
        except asyncio.TimeoutError:
            logger.warning(
                "Aggregate search timed out for %s after %ss",
                site,
                AGGREGATE_PROVIDER_TIMEOUT,
            )
            return site, None, []
        except Exception as exc:
            logger.warning("Aggregate search failed for %s: %s", site, exc)
            return site, None, []

    async def _fetch_tmdb_preview(self, title: str) -> tuple[str | None, str | None]:
        """Fetch localized title and poster URL from TMDB for search previews."""
        language = settings.rss_parser.language
        if title in _poster_cache and language in _poster_cache[title]:
            _poster_cache.move_to_end(title)
            return _poster_cache[title][language]

        localized_title = None
        poster_link = None
        try:
            tmdb_info = await tmdb_parser(title, language, test=True)
            if tmdb_info:
                localized_title = tmdb_info.title
                poster_link = tmdb_info.poster_link
        except Exception as e:
            logger.debug("Failed to fetch TMDB preview for %s: %s", title, e)

        if title not in _poster_cache and len(_poster_cache) >= _POSTER_CACHE_MAX:
            _poster_cache.popitem(last=False)
        _poster_cache.setdefault(title, {})[language] = (localized_title, poster_link)
        return localized_title, poster_link

    async def _fetch_tmdb_poster(self, title: str) -> str | None:
        """Fetch poster from TMDB if not in cache."""
        _, poster_link = await self._fetch_tmdb_preview(title)
        return poster_link

    async def analyse_keyword(
        self, keywords: list[str], site: str = "mikan", limit: int = 100
    ):
        is_aggregate = site in AGGREGATE_SEARCH_SITES
        keyword_text = " ".join(keywords)
        if is_aggregate:
            aggregate_all = site in {"全源", "all-sources"}
            fast_providers = (
                {"mikan"} if CJK_PATTERN.search(keyword_text) else FAST_AGGREGATE_PROVIDERS
            )
            providers = [
                provider
                for provider, config in get_provider().items()
                if provider not in AGGREGATE_SEARCH_SITES
                and (aggregate_all or provider in fast_providers)
                and config.get("url")
                and "%s" in config["url"]
            ]
            search_results = asyncio.as_completed(
                [self._search_provider(provider, keywords) for provider in providers]
            )
        else:
            rss_item = search_url(site, keywords)
            torrents = await self.search_torrents(rss_item)
            search_results = [(site, rss_item, torrents)]

        # yield for EventSourceResponse (Server Send)
        exist_list: list[str] = []
        torrent_urls: set[str] = set()
        aggregate_poster_disabled = False
        aggregate_poster_titles: set[str] = set()
        aggregate_poster_cache: dict[str, tuple[str | None, str | None]] = {}
        aggregate_default_poster: str | None = None
        for search_result in search_results:
            if is_aggregate:
                provider, rss_item, torrents = await search_result
            else:
                provider, rss_item, torrents = search_result
            if rss_item is None:
                continue
            for torrent in torrents:
                if len(exist_list) >= limit:
                    return
                torrent_key = torrent.url or torrent.name
                if torrent_key in torrent_urls:
                    continue
                torrent_urls.add(torrent_key)
                # Skip the per-torrent Mikan homepage fetch / poster download here:
                # interactive search can return many results and doing that fetch
                # serially for each one makes the search feel unresponsive. Poster
                # is filled in afterwards from the (title-keyed, cached) TMDB lookup.
                bangumi = await self.analyser.torrent_to_data(
                    torrent=torrent, rss=rss_item, fetch_poster=False
                )
                if bangumi:
                    if is_aggregate and not _matches_keyword(keyword_text, bangumi, torrent):
                        continue
                    special_link = self.special_url(bangumi, provider).url
                    if special_link not in exist_list:
                        bangumi.rss_link = special_link
                        exist_list.append(special_link)
                        # Fetch localized title and poster URL from TMDB if available.
                        if bangumi.official_title:
                            if (
                                is_aggregate
                                and aggregate_default_poster
                                and not bangumi.poster_link
                            ):
                                bangumi.poster_link = aggregate_default_poster
                            should_fetch_poster = not is_aggregate and not bangumi.poster_link
                            title_key = bangumi.official_title
                            cached_preview = aggregate_poster_cache.get(title_key)
                            if cached_preview:
                                tmdb_title, tmdb_poster = cached_preview
                                if tmdb_title:
                                    bangumi.official_title = tmdb_title
                                if not bangumi.poster_link and tmdb_poster:
                                    bangumi.poster_link = tmdb_poster
                                should_fetch_poster = False
                            if is_aggregate and not aggregate_poster_disabled:
                                should_fetch_poster = (
                                    not bangumi.poster_link
                                    and title_key not in aggregate_poster_titles
                                    and len(aggregate_poster_titles)
                                    < AGGREGATE_POSTER_LOOKUPS
                                )
                                if should_fetch_poster:
                                    aggregate_poster_titles.add(title_key)
                            if should_fetch_poster:
                                tmdb_title = None
                                tmdb_poster = None
                                try:
                                    lookup_titles = _tmdb_lookup_candidates(bangumi)
                                    if CJK_PATTERN.search(bangumi.official_title):
                                        lookup_titles.sort(
                                            key=lambda value: (
                                                1
                                                if CJK_PATTERN.search(value)
                                                else 0
                                            )
                                        )
                                    seen_lookup_titles: set[str] = set()
                                    for lookup_title in lookup_titles:
                                        if lookup_title in seen_lookup_titles:
                                            continue
                                        seen_lookup_titles.add(lookup_title)
                                        try:
                                            (
                                                tmdb_title,
                                                tmdb_poster,
                                            ) = await asyncio.wait_for(
                                                self._fetch_tmdb_preview(lookup_title),
                                                timeout=AGGREGATE_POSTER_TIMEOUT
                                                if is_aggregate
                                                else None,
                                            )
                                        except asyncio.TimeoutError:
                                            continue
                                        if tmdb_title or tmdb_poster:
                                            break
                                except asyncio.TimeoutError:
                                    aggregate_poster_disabled = True
                                    tmdb_title = None
                                    tmdb_poster = None
                                if is_aggregate:
                                    aggregate_poster_cache[title_key] = (
                                        tmdb_title,
                                        tmdb_poster,
                                    )
                                if tmdb_title:
                                    bangumi.official_title = tmdb_title
                                if not bangumi.poster_link and tmdb_poster:
                                    bangumi.poster_link = tmdb_poster
                        if is_aggregate:
                            if bangumi.poster_link and not aggregate_default_poster:
                                aggregate_default_poster = bangumi.poster_link
                            elif not bangumi.poster_link and aggregate_default_poster:
                                bangumi.poster_link = aggregate_default_poster
                        yield json.dumps(bangumi.dict(), separators=(",", ":"))

    @staticmethod
    def special_url(data: Bangumi | Movie, site: str) -> RSSItem:
        keywords = [value for key in SEARCH_KEY if (value := getattr(data, key, None))]
        url = search_url(site, keywords)
        return url

    async def search_season(self, data: Bangumi, site: str = "mikan") -> list[Torrent]:
        rss_item = self.special_url(data, site)
        torrents = await self.search_torrents(rss_item)
        return [torrent for torrent in torrents if data.title_raw in torrent.name]
