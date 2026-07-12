"""Shared config, paths, and date helpers for the arXiv Vibes pipeline."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DIGEST_DIR = ROOT / "digests"
MEMORY_DIR = ROOT / "memory"
MEMORY_ARCHIVE_DIR = MEMORY_DIR / "archive"
PROMPT_DIR = ROOT / "prompts"
SITE_DIR = ROOT / "site"
TEMPLATE_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"


def load_config() -> dict:
    with open(ROOT / "config.yaml") as f:
        return yaml.safe_load(f)


def parse_date(s: str | None) -> dt.date:
    return dt.date.fromisoformat(s) if s else dt.date.today()


def data_path(date: dt.date) -> Path:
    return DATA_DIR / f"{date.isoformat()}.jsonl"


def digest_path(date: dt.date) -> Path:
    return DIGEST_DIR / f"{date.isoformat()}.md"


def load_papers(date: dt.date) -> list[dict]:
    path = data_path(date)
    if not path.exists():
        return []
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def load_prompt(name: str) -> str:
    return (PROMPT_DIR / f"{name}.md").read_text()


# --- academic-year seasons: Autumn = Sep-Jan, Spring = Feb-Apr, Summer = May-Aug ---

SEASON_BOUNDARY_MONTHS = (9, 2, 5)  # term starts: Sep 1, Feb 1, May 1


def season_of(date: dt.date) -> tuple[str, int]:
    """Return (term name, academic year the term belongs to).

    Academic years are labeled by their starting calendar year: academic year
    2026 runs Sep 2026 - Aug 2027, so its Autumn term spans Sep 2026 - Jan 2027
    and its Spring (Feb-Apr) and Summer (May-Aug) terms fall in calendar 2027.
    """
    m, y = date.month, date.year
    if m >= 9:
        return "autumn", y
    if m <= 1:
        return "autumn", y - 1
    if m <= 4:
        return "spring", y - 1
    return "summer", y - 1


def academic_year_of(date: dt.date) -> int:
    """Academic year (labeled by starting calendar year; rolls on Sep 1)."""
    return date.year if date.month >= 9 else date.year - 1
