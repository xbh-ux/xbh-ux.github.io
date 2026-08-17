#!/usr/bin/env python3
import argparse
import asyncio
import datetime as dt
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict

from module.database import Database
from module.models import Torrent
from module.rss import RSSEngine

MIKAN_NS = '{https://mikanime.tv/0.1/}'
WEEKDAY_ZH = ['一', '二', '三', '四', '五', '六', '日']


def log(message):
    now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{now}] {message}', flush=True)


def parse_pub_date(value):
    if not value:
        return None
    value = value.strip().replace('Z', '')
    try:
        return dt.datetime.fromisoformat(value)
    except ValueError:
        return None


def normalize_url(url):
    parsed = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(parsed.path, safe='/%')
    query = urllib.parse.quote(parsed.query, safe='=&%+')
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, query, parsed.fragment))


def parse_rss(url):
    req = urllib.request.Request(normalize_url(url), headers={'User-Agent': 'weekday-linker/1.0'})
    with urllib.request.urlopen(req, timeout=20) as resp:
        root = ET.fromstring(resp.read())
    for item in root.findall('.//item'):
        title = (item.findtext('title') or '').strip()
        homepage = (item.findtext('link') or '').strip() or None
        enclosure = item.find('enclosure')
        torrent_url = enclosure.get('url') if enclosure is not None else None
        pub_text = item.findtext(f'.//{MIKAN_NS}pubDate')
        pub_date = parse_pub_date(pub_text)
        if title and torrent_url and pub_date:
            yield Torrent(name=title, url=torrent_url, homepage=homepage), pub_date


def choose_weekday(samples):
    # samples: list[datetime]. Pick most common weekday; tie by latest sample.
    grouped = defaultdict(list)
    for value in samples:
        grouped[value.weekday()].append(value)
    return max(grouped, key=lambda weekday: (len(grouped[weekday]), max(grouped[weekday])))


async def infer_weekdays(dry_run=False):
    async with Database() as db:
        rss_items = await db.rss.search_active()
        bangumi_list = [b for b in await db.bangumi.search_all() if not b.deleted]
        engine = RSSEngine(db)
        samples_by_id = defaultdict(list)

        for rss in rss_items:
            try:
                parsed = list(parse_rss(rss.url))
            except Exception as exc:
                log(f'skip rss {rss.name or rss.url}: {exc}')
                continue
            for torrent, pub_date in parsed:
                matched = engine.match_torrent(torrent, bangumi_list)
                if matched and matched.id is not None:
                    samples_by_id[matched.id].append(pub_date)

        changed = 0
        for bangumi in bangumi_list:
            if bangumi.weekday_locked:
                log(f'locked skip: {bangumi.id} {bangumi.official_title}')
                continue
            samples = samples_by_id.get(bangumi.id, [])
            if not samples:
                log(f'no sample: {bangumi.id} {bangumi.official_title}')
                continue
            weekday = choose_weekday(samples)
            old = bangumi.air_weekday
            latest = max(samples).strftime('%Y-%m-%d %H:%M')
            if old == weekday:
                log(f'keep 周{WEEKDAY_ZH[weekday]}: {bangumi.id} {bangumi.official_title} samples={len(samples)} latest={latest}')
                continue
            log(f'set 周{WEEKDAY_ZH[weekday]}: {bangumi.id} {bangumi.official_title} old={old} samples={len(samples)} latest={latest}')
            if not dry_run:
                bangumi.air_weekday = weekday
                bangumi.weekday_locked = False
                db.add(bangumi)
                changed += 1
        if changed and not dry_run:
            await db.commit()
        log(f'changed={changed} dry_run={dry_run}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    asyncio.run(infer_weekdays(dry_run=args.dry_run))


if __name__ == '__main__':
    main()
