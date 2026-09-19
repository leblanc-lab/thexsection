"""Fetch and scan extra arXiv categories without calling an LLM.

Run without arguments for current announcements; --rescan reuses stored data.
Raw data and rendered entries are isolated from every paid pipeline stage.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import feedparser
import httpx

from .common import ROOT, load_config, parse_date
from .fetch import FEED_URL, _entry_to_paper
from .scan import render, scan_day

DATA_DIR = ROOT / "data" / "category-scan"
SCAN_DIR = ROOT / "watch" / "category-scan"


def category_topics(cfg: dict) -> list[dict]:
    """Inherit watch criteria unless a category explicitly overrides a list."""
    section = cfg.get("category_scan", {})
    if not section.get("enabled", False):
        return []
    watched = cfg.get("watchlist", {}).get("topics", [])
    keywords = list(dict.fromkeys(
        [k for t in watched for k in t.get("keywords", [])]
        + section.get("extra_keywords", [])
    ))
    authors = [a for t in watched for a in t.get("authors", [])]
    return [dict(t, name=t["category"], page=True, brief=False, theme="default",
                 keywords=t.get("keywords", keywords), authors=t.get("authors", authors),
                 blurb="Keyword and author matches. Original abstracts, no AI summaries.",
                 tagline=t.get("tagline", t["category"]))
            for t in section.get("feeds", [])]


def fetch_category(category: str, announce_types: list[str]) -> list[dict]:
    response = httpx.get(FEED_URL.format(cat=category), timeout=60, follow_redirects=True)
    response.raise_for_status()
    feed = feedparser.parse(response.content)
    if feed.bozo or not feed.version:
        raise ValueError(f"Invalid arXiv feed for {category}; leaving stored data intact")
    papers = {}
    for entry in feed.entries:
        paper = _entry_to_paper(entry)
        if paper and paper["announce_type"] in announce_types:
            papers.setdefault(paper["id"], paper)
    return sorted(papers.values(), key=lambda p: p["id"])


def scan_file(path: Path, topic: dict, *, history: bool = False) -> int:
    papers = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    hits = scan_day(papers, [topic], {})
    out = SCAN_DIR / topic["slug"]
    if history:
        out = out / "history"
    out = out / f"{path.stem}.md"
    if hits:
        out.parent.mkdir(parents=True, exist_ok=True)
        body = render(path.stem, hits).replace(
            "abstract only, not yet read for a briefing.", "original abstract; no AI summary.")
        out.write_text(body)
    else:
        out.unlink(missing_ok=True)
    return sum(len(entries) for entries in hits.values())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rescan", action="store_true", help="reuse saved announcements, no network")
    ap.add_argument("--date", help="stored date to rescan (requires --rescan)")
    args = ap.parse_args()
    if args.date and not args.rescan:
        ap.error("--date requires --rescan; live feeds only contain current announcements")
    cfg = load_config()
    for topic in category_topics(cfg):
        directory = DATA_DIR / topic["slug"]
        if args.rescan:
            history_dir = DATA_DIR / "backfill" / topic["slug"]
            history_paths = ([history_dir / f"{parse_date(args.date)}.jsonl"] if args.date
                             else sorted(history_dir.glob("????-??-??.jsonl")))
            for path in history_paths:
                if path.exists():
                    scan_file(path, topic, history=True)
            paths = ([directory / f"{parse_date(args.date)}.jsonl"] if args.date
                     else sorted(directory.glob("????-??-??.jsonl")))
        else:
            time.sleep(5)  # arXiv requires serial requests at least 3 seconds apart
            papers = fetch_category(topic["category"], cfg["arxiv"]["announce_types"])
            directory.mkdir(parents=True, exist_ok=True)
            path = directory / f"{parse_date(None)}.jsonl"
            # A valid empty feed on a later run must not erase today's earlier batch.
            if not papers and path.exists():
                print(f"{topic['category']}: empty feed; retaining today's stored announcements")
            else:
                path.write_text("".join(json.dumps(p) + "\n" for p in papers))
            paths = [path]
        for path in paths:
            if args.rescan and not path.exists():
                continue
            count = scan_file(path, topic)
            print(f"{topic['category']} {path.stem}: {count} matches (no LLM)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
