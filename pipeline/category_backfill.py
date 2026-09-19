"""Resumable, zero-LLM category history, dated by first submission.

Example: python -m pipeline.category_backfill --since 1991-01-01
Raw history is gitignored; matched abstracts are retained for Pages builds.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import time
import sys

import feedparser
import httpx

from .category_scan import DATA_DIR, category_topics, scan_file
from .common import load_config, parse_date
from .fetch import _entry_to_paper

HISTORY_DIR = DATA_DIR / "backfill"
PAGE_SIZE = 500
PAUSE = 5.0
HEADERS = {"User-Agent": "TheCrossSection/1.0 (https://leblanc-lab.github.io/thexsection/; metadata backfill)",
           "Accept": "application/atom+xml, application/xml;q=0.9"}


def fetch_window(categories, start, end):
    query = '(' + ' OR '.join(f'cat:{c}' for c in categories) + ')'
    query += f' AND submittedDate:[{start:%Y%m%d}0000 TO {end:%Y%m%d}2359]'
    papers, offset, total = {}, 0, None
    with httpx.Client(timeout=60, follow_redirects=True, headers=HEADERS) as client:
        while total is None or offset < total:
            for attempt in range(4):
                # Also applies between windows and retries, never parallel requests.
                time.sleep(PAUSE * (attempt + 1))
                try:
                    response = client.get('https://export.arxiv.org/api/query', params={
                        'search_query': query, 'start': offset, 'max_results': PAGE_SIZE,
                        'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
                    # Stop on refusal/throttling rather than repeatedly hitting the server.
                    if response.status_code == 429 or (response.status_code == 503 and response.headers.get('retry-after')):
                        raise RuntimeError(f"arXiv requested a pause (HTTP {response.status_code}, "
                                           f"Retry-After: {response.headers.get('retry-after', 'unspecified')}). "
                                           "Stopped; completed chunks are saved.")
                    if 400 <= response.status_code < 500:
                        raise RuntimeError(f"arXiv rejected the request (HTTP {response.status_code}). "
                                           "Stopped without retrying; completed chunks are saved.")
                    response.raise_for_status()
                    feed = feedparser.parse(response.content)
                    if feed.bozo or 'opensearch_totalresults' not in feed.feed:
                        raise ValueError('Invalid API response: missing result count or malformed XML')
                    count = int(feed.feed['opensearch_totalresults'])
                    if count < 0 or (total is not None and count != total):
                        raise ValueError('API result count changed during pagination; retry the window')
                    if not feed.entries and offset < count:
                        raise ValueError('API returned an incomplete result page')
                    break
                except (httpx.HTTPError, ValueError):
                    if attempt == 3:
                        raise
            total = count
            if total > 10000:
                # Avoid deep pagination: split dense windows before persisting anything.
                if start == end:
                    raise ValueError('More than 10000 results in one day; window cannot be completed')
                middle = start + (end - start) // 2
                return (fetch_window(categories, start, middle)
                        + fetch_window(categories, middle + dt.timedelta(days=1), end))
            for entry in feed.entries:
                paper = _entry_to_paper(entry)
                if not paper:
                    raise ValueError('Unrecognized paper in API response')
                day = dt.date.fromisoformat(entry['published'][:10])
                if not start <= day <= end:
                    raise ValueError('API returned a paper outside the requested window')
                paper['source'] = 'export-api'
                paper['primary_category'] = entry.get('arxiv_primary_category', {}).get(
                    'term', paper['primary_category'])
                papers[paper['id']] = (day, paper)
            offset += len(feed.entries)
            if not feed.entries:
                break
    if len(papers) != total:
        raise ValueError(f'Incomplete window: {len(papers)} distinct papers, expected {total}')
    return list(papers.values())


def backfill(topics, since, until, window=7, max_windows=None):
    start = since
    completed = 0
    while start <= until:
        end = min(start + dt.timedelta(days=window - 1), until)
        days = [start + dt.timedelta(days=i) for i in range((end-start).days+1)]
        paths = [(t, day, HISTORY_DIR/t['slug']/f'{day}.jsonl') for t in topics for day in days]
        if not all(path.exists() for _, _, path in paths):
            rows = fetch_window([t['category'] for t in topics], start, end)
            # Only complete validated windows reach disk. Empty days are checkpoints too.
            for topic, day, path in paths:
                if path.exists():
                    continue
                selected = sorted((p for d, p in rows if d == day and topic['category'] in p['categories']),
                                  key=lambda p: p['id'])
                path.parent.mkdir(parents=True, exist_ok=True)
                temporary = path.with_suffix('.tmp')
                temporary.write_text(''.join(json.dumps(p)+'\n' for p in selected))
                temporary.replace(path)
        hits = sum(scan_file(path, topic, history=True) for topic, _, path in paths)
        print(f'{start}..{end}: {hits} category matches (complete, no LLM)', flush=True)
        start = end + dt.timedelta(days=1)
        completed += 1
        if max_windows is not None and completed >= max_windows and start <= until:
            print(f'Chunk limit reached. Resume with --since {start} --until {until}', flush=True)
            return


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--since', required=True, help='first submission date; 1991-01-01 for full history')
    ap.add_argument('--until', help='last submission date, default yesterday')
    ap.add_argument('--window', type=int, default=7, help='days per query; dense windows split automatically')
    ap.add_argument('--max-windows', type=int, help='stop after this many completed date windows')
    args = ap.parse_args()
    since = parse_date(args.since)
    until = parse_date(args.until) if args.until else dt.date.today()-dt.timedelta(days=1)
    if args.window < 1 or since > until or (args.max_windows is not None and args.max_windows < 1):
        ap.error('require a positive window and since <= until')
    topics = category_topics(load_config())
    if topics:
        try:
            backfill(topics, since, until, args.window, args.max_windows)
        except (httpx.HTTPError, ValueError, RuntimeError) as exc:
            print(f'Backfill stopped: {exc}', file=sys.stderr)
            return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
