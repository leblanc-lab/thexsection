"""Render digests, memory tiers, and radar posts into the static site (site/)."""

from __future__ import annotations

import datetime as dt
import shutil
import sys
from pathlib import Path

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader

from .common import (
    DIGEST_DIR,
    MEMORY_ARCHIVE_DIR,
    MEMORY_DIR,
    SITE_DIR,
    STATIC_DIR,
    TEMPLATE_DIR,
    load_config,
)

RADAR_DIR = DIGEST_DIR / "radar"

MD = markdown.Markdown(
    extensions=["tables", "smarty", "pymdownx.arithmatex"],
    extension_configs={"pymdownx.arithmatex": {"generic": True}},
)


def md_to_html(text: str) -> str:
    MD.reset()
    return MD.convert(text)


def pretty_date(iso: str) -> str:
    d = dt.date.fromisoformat(iso)
    return d.strftime("%A, %B %-d, %Y")


def load_posts(directory: Path) -> list[dict]:
    posts = []
    for path in sorted(directory.glob("????-??-??.md"), reverse=True):
        post = frontmatter.load(path)
        posts.append(
            {
                "date": path.stem,
                "pretty_date": pretty_date(path.stem),
                "themes": post.get("themes", []),
                "paper_count": post.get("paper_count"),
                "citations": post.get("citations", {}),
                "html": md_to_html(post.content),
            }
        )
    return posts


MEMORY_TIERS = [
    ("week", "This week", "The last seven days of postings, compressed."),
    ("month", "This month", "The month's trajectories."),
    ("season", "This term", "The academic term, in synthesis."),
    ("year", "This year", "The academic year's long arcs."),
]


def load_memory() -> list[dict]:
    tiers = []
    for name, label, blurb in MEMORY_TIERS:
        path = MEMORY_DIR / f"{name}.md"
        if path.exists():
            tiers.append(
                {"name": name, "label": label, "blurb": blurb,
                 "html": md_to_html(path.read_text())}
            )
    return tiers


def load_memory_archive() -> list[dict]:
    entries = []
    for sub in ("yearly", "seasonal", "monthly", "weekly"):
        for path in sorted((MEMORY_ARCHIVE_DIR / sub).glob("*.md"), reverse=True):
            entries.append({"tier": sub[:-2], "label": path.stem, "html": md_to_html(path.read_text())})
    return entries


def main() -> int:
    cfg = load_config()
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=False)
    env.globals.update(
        site=cfg["site"],
        categories=cfg["arxiv"]["categories"],
        built_at=dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
    )

    digests = load_posts(DIGEST_DIR)
    radar_posts = load_posts(RADAR_DIR) if RADAR_DIR.exists() else []
    memory_tiers = load_memory()

    # Group the archive by month for the back-issues page.
    by_month: dict[str, list[dict]] = {}
    for d in digests:
        by_month.setdefault(d["date"][:7], []).append(d)
    months = [
        {"label": dt.date.fromisoformat(k + "-01").strftime("%B %Y"), "digests": v}
        for k, v in sorted(by_month.items(), reverse=True)
    ]

    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    (SITE_DIR / "digest").mkdir(parents=True)

    def render(template: str, out: str, **ctx) -> None:
        (SITE_DIR / out).write_text(env.get_template(template).render(**ctx))

    render(
        "index.html", "index.html",
        digest=digests[0] if digests else None,
        recent=digests[1:8],
        has_radar=bool(radar_posts),
    )
    for i, d in enumerate(digests):
        render(
            "digest.html", f"digest/{d['date']}.html",
            digest=d,
            newer=digests[i - 1] if i > 0 else None,
            older=digests[i + 1] if i + 1 < len(digests) else None,
        )
    render("archive.html", "archive.html", months=months)
    render("radar.html", "radar.html", posts=radar_posts)
    render(
        "memory.html", "memory.html",
        tiers=memory_tiers, archive=load_memory_archive(),
    )

    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, SITE_DIR / "static")
    print(
        f"Built site/ — {len(digests)} digests, {len(radar_posts)} radar posts, "
        f"{len(memory_tiers)} memory tiers"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
