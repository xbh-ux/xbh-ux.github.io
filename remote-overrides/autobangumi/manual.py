import re
from collections import defaultdict
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from module.database import Database
from module.downloader import AddResult, DownloadClient
from module.models import Bangumi, Torrent
from module.network import RequestContent
from module.parser.analyser.selector import parse_configured_release_title_outcome
from module.rss import RSSEngine
from module.searcher.provider import search_url
from module.security.api import get_current_user


router = APIRouter(prefix="/manual", tags=["manual"])


class EpisodeTorrent(BaseModel):
    name: str
    url: str
    homepage: str | None = None


class EpisodeStatus(BaseModel):
    state: str | None = None
    progress: float = 0
    save_path: str | None = None
    torrent_name: str | None = None


class EpisodeItem(BaseModel):
    episode: int
    available_count: int
    candidate: EpisodeTorrent | None = None
    status: EpisodeStatus | None = None
    can_download: bool


class EpisodeListResponse(BaseModel):
    bangumi_id: int
    title: str
    latest_episode: int
    episodes: list[EpisodeItem]


class ManualDownloadRequest(BaseModel):
    bangumi_id: int = Field(..., gt=0)
    episode: int = Field(..., gt=0)


class ManualDownloadResponse(BaseModel):
    status: bool
    result: str
    msg_zh: str
    torrent: EpisodeTorrent | None = None


def _episode_number(name: str) -> int | None:
    release = parse_configured_release_title_outcome(name).result
    episode = getattr(release, "episode", None) if release is not None else None
    if episode is None:
        return None
    try:
        value = float(episode)
    except (TypeError, ValueError):
        return None
    if value <= 0 or not value.is_integer():
        return None
    return int(value)


def _download_rank(torrent: Torrent) -> tuple[int, str]:
    name = torrent.name.lower()
    score = 0
    if "1080" in name:
        score += 20
    if "cht" in name or "繁" in name:
        score += 8
    if "chs" in name or "简" in name:
        score += 4
    if "hevc" in name or "h265" in name:
        score += 2
    return (-score, torrent.name)


def _dedupe_torrents(torrents: list[Torrent]) -> list[Torrent]:
    seen: set[str] = set()
    result: list[Torrent] = []
    for torrent in torrents:
        key = torrent.url
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(torrent)
    return result


async def _search_episode_candidates(
    bangumi: Bangumi, engine: RSSEngine
) -> dict[int, list[Torrent]]:
    keywords = []
    for value in (bangumi.title_raw, bangumi.official_title):
        if value and value not in keywords:
            keywords.append(value)
    if bangumi.title_aliases:
        import json

        try:
            for alias in json.loads(bangumi.title_aliases):
                if alias and alias not in keywords:
                    keywords.append(alias)
        except (TypeError, ValueError):
            pass

    candidates: list[Torrent] = []
    async with RequestContent() as req:
        for keyword in keywords:
            rss_item = search_url("mikan", [keyword])
            candidates.extend(await req.get_torrents(rss_item.url, bangumi.filter))

    grouped: dict[int, list[Torrent]] = defaultdict(list)
    for torrent in _dedupe_torrents(candidates):
        matched = engine.match_torrent(torrent, [bangumi])
        episode = _episode_number(torrent.name)
        if matched and episode is not None:
            grouped[episode].append(torrent)

    for episode in list(grouped):
        grouped[episode].sort(key=_download_rank)
    local_episodes = [episode for episode in grouped if episode <= 30]
    if local_episodes:
        # Some release groups number long-running shows by absolute episode
        # count (for example 69-78) while other releases use season-local
        # numbering (1-12). When local numbering exists, keep the manual grid
        # season-local so "1-latest" stays usable.
        grouped = {
            episode: items
            for episode, items in grouped.items()
            if episode <= max(local_episodes)
        }
    return dict(grouped)


def _status_by_episode(torrents: list[dict[str, Any]], bangumi_id: int) -> dict[int, EpisodeStatus]:
    statuses: dict[int, EpisodeStatus] = {}
    tag = f"ab:{bangumi_id}"
    for item in torrents:
        tags = {part.strip() for part in str(item.get("tags", "")).split(",")}
        if tag not in tags:
            continue
        episode = _episode_number(str(item.get("name") or item.get("content_path") or ""))
        if episode is None:
            continue
        progress = float(item.get("progress") or 0)
        current = statuses.get(episode)
        if current is None or progress > current.progress:
            statuses[episode] = EpisodeStatus(
                state=item.get("state"),
                progress=progress,
                save_path=item.get("save_path"),
                torrent_name=item.get("name"),
            )
    return statuses


@router.get(
    "/episodes/{bangumi_id}",
    response_model=EpisodeListResponse,
    dependencies=[Depends(get_current_user)],
)
async def list_episodes(bangumi_id: int):
    async with Database() as db:
        bangumi = await db.bangumi.search_id(bangumi_id)
        if not bangumi or bangumi.deleted:
            raise HTTPException(status_code=404, detail="Bangumi not found")
        engine = RSSEngine(db)
        candidates = await _search_episode_candidates(bangumi, engine)

    async with DownloadClient() as client:
        qbit_torrents = await client.get_torrent_info(
            category="Bangumi", status_filter=None
        )
    statuses = _status_by_episode(qbit_torrents, bangumi_id)

    latest = max([0, *candidates.keys(), *statuses.keys()])
    episodes: list[EpisodeItem] = []
    for episode in range(1, latest + 1):
        episode_candidates = candidates.get(episode, [])
        first = episode_candidates[0] if episode_candidates else None
        status = statuses.get(episode)
        episodes.append(
            EpisodeItem(
                episode=episode,
                available_count=len(episode_candidates),
                candidate=(
                    EpisodeTorrent(
                        name=first.name,
                        url=first.url,
                        homepage=first.homepage,
                    )
                    if first
                    else None
                ),
                status=status,
                can_download=bool(first),
            )
        )
    return EpisodeListResponse(
        bangumi_id=bangumi_id,
        title=bangumi.official_title,
        latest_episode=latest,
        episodes=episodes,
    )


@router.post(
    "/download",
    response_model=ManualDownloadResponse,
    dependencies=[Depends(get_current_user)],
)
async def download_episode(req: ManualDownloadRequest):
    async with Database() as db:
        bangumi = await db.bangumi.search_id(req.bangumi_id)
        if not bangumi or bangumi.deleted:
            raise HTTPException(status_code=404, detail="Bangumi not found")
        engine = RSSEngine(db)
        candidates = await _search_episode_candidates(bangumi, engine)
        selected = (candidates.get(req.episode) or [None])[0]
        if selected is None:
            return ManualDownloadResponse(
                status=False,
                result="not_found",
                msg_zh=f"未找到第 {req.episode} 集候选种子",
            )

        async with DownloadClient() as client:
            result = await client.add_torrent(selected, bangumi)
        if result is AddResult.FAILED:
            return ManualDownloadResponse(
                status=False,
                result=result.value,
                msg_zh="投递到下载器失败",
                torrent=EpisodeTorrent(
                    name=selected.name,
                    url=selected.url,
                    homepage=selected.homepage,
                ),
            )

        selected.downloaded = True
        selected.bangumi_id = bangumi.id
        existing = await db.torrent.search_by_url(selected.url)
        if existing:
            existing.downloaded = True
            existing.bangumi_id = bangumi.id
            db.add(existing)
        else:
            db.add(selected)
        db.add(bangumi)
        await db.commit()

    return ManualDownloadResponse(
        status=True,
        result=result.value,
        msg_zh=f"第 {req.episode} 集已投递到 qBittorrent",
        torrent=EpisodeTorrent(
            name=selected.name,
            url=selected.url,
            homepage=selected.homepage,
        ),
    )
