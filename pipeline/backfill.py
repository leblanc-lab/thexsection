"""Backfill raw paper data from the arXiv export API, then keyword-scan it.

The rss.arxiv.org feeds carry only the current day, so history comes from the
export API, queried by submission date over the configured categories and
bucketed into data/backfill/YYYY-MM-DD.jsonl — same schema as the files
`pipeline.fetch` writes, but gitignored: this is a local database, rebuilt by
rerunning this script after a fresh clone. `load_papers` falls back to it, so
`pipeline.scan` (and nothing else) picks it up. No LLM anywhere: the result is
abstract-only entries on the mirrored topic pages and feeds, and those small
scan files *are* committed, since the Pages build only sees the repo.

Caveats, shared with `fetch --backfill`: a paper is filed under its
*submission* day, which runs a day or two ahead of its announcement day, and
the export API has no announce-type notion, so cross-lists appear on their
submission day too. Keeping the raw papers (rather than only the hits) means a
later keyword change is a free rescan, not a refetch.

Examples:
  python -m pipeline.backfill --since 2026-01-01        # up to the day before data/ starts
  python -m pipeline.backfill --since 2025-09-01 --until 2025-12-31
Days that already have a data file are left alone unless --overwrite.
Files are written window by window, so an interrupted run can simply be rerun.
Pre-April-2007 papers carry old-style ids ("hep-ph/0603004"); common.ARXIV_ID
accepts both, so history reaches back to the archive's start (1992 for hep-ph).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
import urllib.parse

import feedparser

from .common import BACKFILL_DIR, backfill_path, load_config, paper_dates, parse_date
from .fetch import _entry_to_paper
from .scan import scan_dates

EXPORT_URL = "http://export.arxiv.org/api/query?{params}"
PAGE = 500          # the API allows more, but big pages are the flaky ones
PAUSE = 3.0         # export API asks for >=3 s between requests
RETRIES = 4         # empty page with results outstanding is a known transient


def fetch_window(categories: list[str], start: dt.date, end: dt.date) -> list[tuple[dt.date, dict]]:
    """All papers in the categories submitted in [start, end], as (submitted day, paper)."""
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    query = (
        f"({cat_query}) AND submittedDate:"
        f"[{start:%Y%m%d}0000 TO {end:%Y%m%d}2359]"
    )
    out: list[tuple[dt.date, dict]] = []
    seen: set[str] = set()
    offset, total = 0, None
    while total is None or offset < total:
        params = urllib.parse.urlencode(
            {"search_query": query, "start": offset, "max_results": PAGE,
             "sortBy": "submittedDate", "sortOrder": "descending"}
        )
        for attempt in range(RETRIES):
            feed = feedparser.parse(EXPORT_URL.format(params=params))
            total = int(feed.feed.get("opensearch_totalresults", 0) or 0)
            if feed.entries or total == 0:
                break
            time.sleep(PAUSE * (attempt + 2))
        else:
            print(f"  ! gave up on {start}..{end} at offset {offset} ({total} expected)", file=sys.stderr)
            break
        for entry in feed.entries:
            paper = _entry_to_paper(entry)
            if not paper or paper["id"] in seen:
                continue
            seen.add(paper["id"])
            paper["primary_category"] = entry.get("arxiv_primary_category", {}).get(
                "term", paper["primary_category"]
            )
            paper["source"] = "export-api"  # submitted-date bucketing, not the announcement list
            day = dt.datetime.strptime(entry["published"][:10], "%Y-%m-%d").date()
            out.append((day, paper))
        offset += len(feed.entries)
        if not feed.entries:
            break
        time.sleep(PAUSE)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", required=True, help="first submission day, YYYY-MM-DD")
    ap.add_argument("--until", help="last submission day (default: the day before data/ starts)")
    ap.add_argument("--window", type=int, default=7, help="days per API query (default 7)")
    ap.add_argument("--overwrite", action="store_true", help="refetch days that already have data")
    ap.add_argument("--no-scan", action="store_true", help="fetch only; skip the keyword scan")
    args = ap.parse_args()

    cfg = load_config()
    categories = cfg["arxiv"]["categories"]
    existing = paper_dates()
    since = parse_date(args.since)
    if args.until:
        until = parse_date(args.until)
    elif existing:
        until = existing[0] - dt.timedelta(days=1)
    else:
        until = dt.date.today() - dt.timedelta(days=1)
    if until < since:
        print(f"Nothing to do: --until {until} is before --since {since}.")
        return 0

    have = set(existing)
    BACKFILL_DIR.mkdir(parents=True, exist_ok=True)
    written, n, skipped = [], 0, 0
    start = since
    while start <= until:
        end = min(start + dt.timedelta(days=args.window - 1), until)
        # Each day belongs to exactly one window, so a window can be written as
        # soon as it lands — an interrupted run keeps everything fetched so far.
        buckets: dict[dt.date, dict[str, dict]] = {}
        for day, paper in fetch_window(categories, start, end):
            if since <= day <= until:
                buckets.setdefault(day, {})[paper["id"]] = paper
        for day in sorted(buckets):
            if day in have and not args.overwrite:
                skipped += 1
                continue
            with open(backfill_path(day), "w") as f:
                for paper in sorted(buckets[day].values(), key=lambda p: p["id"]):
                    f.write(json.dumps(paper) + "\n")
            written.append(day)
            n += len(buckets[day])
        print(f"  {start}..{end}: {sum(map(len, buckets.values()))} papers", file=sys.stderr)
        start = end + dt.timedelta(days=1)

    print(f"Backfilled {len(written)} days, {n} papers ({since}..{until})"
          + (f"; left {skipped} existing days alone" if skipped else ""))

    if written and not args.no_scan:
        print(scan_dates(written, cfg["watchlist"]["topics"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
