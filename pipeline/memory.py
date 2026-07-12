"""Rolling memory tiers: week / month / season / year syntheses.

Each tier is compressed from the tier below on its cadence:
- week.md    — every run day, from the last N daily digests; snapshotted to
               archive/weekly/YYYY-Wnn.md (the week's final version survives)
- month.md   — on the 1st, from the previous month's weekly snapshots
- season.md  — on academic-term boundaries (Sep 1 / Feb 1 / May 1), from the
               finished term's monthly snapshots
- year.md    — on Sep 1, from the finished academic year's term snapshots

Falls back to the next tier down when snapshots are missing (early days).
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import frontmatter

from .common import (
    DIGEST_DIR,
    MEMORY_ARCHIVE_DIR,
    MEMORY_DIR,
    load_config,
    load_prompt,
    parse_date,
    season_of,
)
from .digest import linkify
from .llm import LLM

SEASON_MONTHS = {"autumn": (9, 10, 11, 12, 1), "spring": (2, 3, 4), "summer": (5, 6, 7, 8)}


def daily_digests_between(start: dt.date, end: dt.date) -> list[Path]:
    return [
        p
        for p in sorted(DIGEST_DIR.glob("????-??-??.md"))
        if start.isoformat() <= p.stem <= end.isoformat()
    ]


def digest_body(path: Path) -> str:
    """Digest content with the deep-dive section stripped (themes are what matter)."""
    content = frontmatter.load(path).content
    return content.split("## Deep dives")[0].strip()


def synthesize(llm: LLM, cfg: dict, tier: str, period_end: dt.date, inputs: list[tuple[str, str]]) -> str | None:
    if not inputs:
        print(f"[memory] no inputs for {tier} — skipped", file=sys.stderr)
        return None
    system = (
        load_prompt("memory_system")
        .replace("{TIER}", tier)
        .replace("{PERIOD_END}", period_end.isoformat())
    )
    user = "\n\n".join(f"# {label}\n\n{text}" for label, text in inputs)
    result = llm.complete(system, user, cfg["memory"]["max_output_tokens"])
    return linkify(result.text.strip(), set())


def write_tier(name: str, text: str, archive_rel: str) -> None:
    (MEMORY_DIR / f"{name}.md").write_text(text + "\n")
    archive = MEMORY_ARCHIVE_DIR / archive_rel
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text(text + "\n")
    print(f"[memory] wrote memory/{name}.md (+ archive/{archive_rel})")


def refresh_week(llm: LLM, cfg: dict, date: dt.date) -> None:
    lookback = cfg["memory"]["week_lookback_days"]
    paths = daily_digests_between(date - dt.timedelta(days=lookback - 1), date)
    inputs = [(f"Daily digest, {p.stem}", digest_body(p)) for p in paths]
    text = synthesize(llm, cfg, "week", date, inputs)
    if text:
        year, week, _ = date.isocalendar()
        write_tier("week", text, f"weekly/{year}-W{week:02d}.md")


def refresh_month(llm: LLM, cfg: dict, date: dt.date) -> None:
    """Called on the 1st: synthesize the month that just ended."""
    last = date - dt.timedelta(days=1)
    weeklies = []
    for p in sorted((MEMORY_ARCHIVE_DIR / "weekly").glob("????-W??.md")):
        y, w = int(p.stem[:4]), int(p.stem[6:8])
        thursday = dt.date.fromisocalendar(y, w, 4)
        if (thursday.year, thursday.month) == (last.year, last.month):
            weeklies.append((f"Week synthesis, {p.stem}", p.read_text()))
    if not weeklies:  # early days: fall back to the month's dailies
        paths = daily_digests_between(last.replace(day=1), last)
        weeklies = [(f"Daily digest, {p.stem}", digest_body(p)) for p in paths]
    text = synthesize(llm, cfg, "month", last, weeklies)
    if text:
        write_tier("month", text, f"monthly/{last:%Y-%m}.md")


def refresh_season(llm: LLM, cfg: dict, date: dt.date) -> None:
    """Called on Sep/Feb/May 1: synthesize the term that just ended."""
    last = date - dt.timedelta(days=1)
    term, ay = season_of(last)
    monthlies = []
    for p in sorted((MEMORY_ARCHIVE_DIR / "monthly").glob("????-??.md")):
        y, m = int(p.stem[:4]), int(p.stem[5:7])
        if m in SEASON_MONTHS[term] and season_of(dt.date(y, m, 15)) == (term, ay):
            monthlies.append((f"Month synthesis, {p.stem}", p.read_text()))
    text = synthesize(llm, cfg, "season (academic term)", last, monthlies)
    if text:
        write_tier("season", text, f"seasonal/{ay}-{term}.md")


def refresh_year(llm: LLM, cfg: dict, date: dt.date) -> None:
    """Called on Sep 1: synthesize the academic year that just ended."""
    last = date - dt.timedelta(days=1)
    _, ay = season_of(last)
    seasons = [
        (f"Term synthesis, {p.stem}", p.read_text())
        for p in sorted((MEMORY_ARCHIVE_DIR / "seasonal").glob(f"{ay}-*.md"))
    ]
    text = synthesize(llm, cfg, "academic year", last, seasons)
    if text:
        write_tier("year", text, f"yearly/{ay}-{str(ay + 1)[2:]}.md")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument(
        "--tier",
        choices=["week", "month", "season", "year"],
        help="force one tier regardless of the date",
    )
    args = ap.parse_args()

    cfg = load_config()
    date = parse_date(args.date)
    llm = LLM(cfg)

    if args.tier:
        {"week": refresh_week, "month": refresh_month, "season": refresh_season, "year": refresh_year}[
            args.tier
        ](llm, cfg, date)
        return 0

    from .common import digest_path

    if not digest_path(date).exists():
        print(f"No digest for {date} — memory unchanged.")
        return 0

    refresh_week(llm, cfg, date)
    if date.day == 1:
        refresh_month(llm, cfg, date)
        if date.month in (9, 2, 5):
            refresh_season(llm, cfg, date)
        if date.month == 9:
            refresh_year(llm, cfg, date)
    return 0


if __name__ == "__main__":
    sys.exit(main())
