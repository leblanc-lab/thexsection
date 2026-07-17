"""Push a digest (or radar / watch / longview post) to Substack as a draft.

Uses the unofficial `python-substack` library, which authenticates with a
browser *session cookie* — Substack has no official posting API. Supply the
cookie via the SUBSTACK_COOKIES env var (copy it from your browser dev tools:
Application → Cookies → substack.com, as a "name=value; name=value" string).
Nothing is hardcoded and the cookie is never printed.

By default this creates a **draft** you review in Substack's editor; it never
publishes on its own. `--publish` opts in to publishing (and emailing) an issue.

`--dry-run` prints the cleaned, paste-ready Markdown without touching the
network or needing a cookie — useful for a manual copy-paste, or to preview
exactly what would be sent.

Known limitations of the Markdown → Substack conversion:
  - Substack has no LaTeX/math node we can post to via this library, so inline
    `$...$` math is flattened to Unicode instead (μ, →, Λ, √, superscripts…);
    see `latex_to_unicode` below. Subscripts stay as literal `_x` (Unicode has
    no uppercase subscripts) — standard in plain-text physics writing.
  - Markdown tables aren't supported by the library, so we convert them to
    bullet lists before sending (otherwise they'd be silently dropped).
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

import frontmatter

from .common import DIGEST_DIR, MEMORY_DIR, digest_path, load_config, parse_date

WATCH_DIR = DIGEST_DIR.parent / "watch"
RADAR_DIR = DIGEST_DIR / "radar"
# The rolling weekly "Long View" synthesis. Unlike the issue kinds it isn't
# date-keyed on disk — memory/week.md always holds the current week — and it
# carries no frontmatter, so its title/date are derived from the content below.
LONGVIEW_SRC = MEMORY_DIR / "week.md"
WEEK_ENDING_RE = re.compile(r"Week Ending\s+(\d{4}-\d{2}-\d{2})", re.I)

TABLE_ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]+\|?\s*$")

# Inline math spans: `$ ... $`, ignoring escaped `\$` (e.g. a literal dollar).
INLINE_MATH_RE = re.compile(r"(?<!\\)\$(.+?)(?<!\\)\$", re.S)
# Chars that have Unicode superscript forms; a run right after `^` becomes them
# (pylatexenc strips the TeX braces, so `10^{-9}` reaches us as `10^-9`).
_SUPERSCRIPT = str.maketrans("0123456789+-=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ")
_SUPERSCRIPT_RUN_RE = re.compile(r"\^([0-9+\-=()n]+)")
# Symbol-diacritic accents outside math (mostly author names: Sch\"oneberg).
# Only the punctuation accents — the letter macros (\c \v \u …) collide with
# math command names like \chi, \varepsilon, so we deliberately skip those.
_ACCENT_RE = re.compile(r"""\\(["'`^~])\{?([A-Za-z])\}?""")


def latex_to_unicode(md: str) -> str:
    """Flatten inline `$...$` LaTeX to readable Unicode for Substack.

    Substack exposes no math node through python-substack, so left alone the TeX
    shows up raw (``$K_L\\to\\mu\\mu$``). pylatexenc turns the body of each span
    into Unicode (Greek letters, →, √, accents…), then we lift digit/charge
    superscripts (``B^+`` → ``B⁺``, ``m^2`` → ``m²``) that pylatexenc leaves as
    ``^``. Subscripts stay literal — Unicode has no uppercase subscripts, and
    ``K_L`` reads fine. Raw accents in author names outside math (``Sch\\"o``)
    are folded too. If pylatexenc isn't installed we only drop the ``$``
    delimiters, so the text is still cleaner than raw math.
    """
    try:
        from pylatexenc.latex2text import LatexNodes2Text
    except ImportError:
        return INLINE_MATH_RE.sub(lambda m: m.group(1), md)

    converter = LatexNodes2Text(math_mode="text", keep_comments=True)

    def render_math(match: re.Match) -> str:
        text = converter.latex_to_text(match.group(1)).strip()
        return _SUPERSCRIPT_RUN_RE.sub(lambda m: m.group(1).translate(_SUPERSCRIPT), text)

    # Math spans first; that clears every in-math backslash, so the accent pass
    # below only ever sees stray accents in ordinary prose (e.g. author names).
    md = INLINE_MATH_RE.sub(render_math, md)
    return _ACCENT_RE.sub(lambda m: converter.latex_to_text("\\" + m.group(1) + m.group(2)), md)


def pretty_date(iso: str) -> str:
    return dt.date.fromisoformat(iso).strftime("%A, %B %-d, %Y")


def tables_to_lists(md: str) -> str:
    """Rewrite GitHub-style pipe tables as bullet lists.

    The Substack library ignores tables entirely, so left alone they vanish.
    A data row `| a | b | c |` becomes `- a — b — c`, preserving each cell's own
    Markdown; the header and `|---|` separator rows are dropped.
    """
    out: list[str] = []
    row_block: list[list[str]] = []

    def flush() -> None:
        for cells in row_block:
            bullet = "- " + " — ".join(c for c in cells if c)
            out.append(bullet)
        row_block.clear()

    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = TABLE_ROW_RE.match(line)
        if m and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]) and "|" in lines[i + 1]:
            # Header row + separator + data rows: gather the whole table.
            i += 2  # skip header and separator
            while i < len(lines) and TABLE_ROW_RE.match(lines[i]):
                cells = [c.strip() for c in TABLE_ROW_RE.match(lines[i]).group(1).split("|")]
                row_block.append(cells)
                i += 1
            flush()
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


KIND_DIRS = {"digest": DIGEST_DIR, "radar": RADAR_DIR, "watch": WATCH_DIR}
# CLI-selectable kinds: the date-keyed issue dirs plus the rolling Long View.
KINDS = [*KIND_DIRS, "longview"]


def load_source(kind: str, date: dt.date) -> tuple[frontmatter.Post, Path]:
    path = LONGVIEW_SRC if kind == "longview" else KIND_DIRS[kind] / f"{date.isoformat()}.md"
    if not path.exists():
        raise FileNotFoundError(path)
    return frontmatter.load(path), path


def theme_text(theme) -> str:
    """A theme is normally a string, but a theme containing a colon (e.g.
    "Hadron spectroscopy: new states") is parsed by YAML as a one-key mapping.
    Flatten that back to "key: value" so it renders as the author intended."""
    if isinstance(theme, dict):
        return "; ".join(f"{k}: {v}" for k, v in theme.items())
    return str(theme)


def build_title_subtitle(kind: str, post: frontmatter.Post, cfg: dict, date: dt.date) -> tuple[str, str]:
    site_title = cfg["site"]["title"]
    if kind == "longview":
        # No frontmatter: read the "week ending" date off the H1, fall back to the run date.
        m = WEEK_ENDING_RE.search(post.content)
        iso = m.group(1) if m else date.isoformat()
        return f"The long view — week ending {pretty_date(iso)}", cfg["site"]["tagline"]
    when = pretty_date(post.get("date") or post.metadata.get("date"))
    if kind == "digest":
        themes = [theme_text(t) for t in (post.get("themes", []) or [])]
        return when, " · ".join(themes) if themes else cfg["site"]["tagline"]
    if kind == "radar":
        return f"Citation radar — week of {when}", f"{site_title}: what the field is citing"
    return f"{cfg.get('watchlist', {}).get('page_title', 'Watch')} — {when}", site_title


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--kind", choices=KINDS, default="digest",
                    help="which post to send (longview = the rolling weekly synthesis)")
    ap.add_argument("--title", help="override the draft title")
    ap.add_argument("--subtitle", help="override the draft subtitle")
    ap.add_argument("--dry-run", action="store_true", help="print cleaned markdown; no network, no cookie needed")
    ap.add_argument("--publish", action="store_true", help="publish (and email) instead of leaving a draft")
    ap.add_argument("--no-send", action="store_true", help="with --publish, don't email subscribers")
    args = ap.parse_args()

    cfg = load_config()
    date = parse_date(args.date)

    try:
        post, path = load_source(args.kind, date)
    except FileNotFoundError as e:
        print(f"No {args.kind} at {e} — nothing to send.")
        return 0

    title = args.title or None
    subtitle = args.subtitle or None
    if not title or not subtitle:
        auto_title, auto_subtitle = build_title_subtitle(args.kind, post, cfg, date)
        title = title or auto_title
        subtitle = subtitle or auto_subtitle

    content = post.content.strip()
    if args.kind == "longview":
        # Drop the leading "# Rolling Synthesis — …" H1; it's redundant with the draft title.
        content = re.sub(r"\A#[^\n]*\n+", "", content, count=1)
    body = tables_to_lists(latex_to_unicode(content))

    if args.dry_run:
        print(f"# {title}\n_{subtitle}_\n\n{body}")
        print(f"\n---\n[dry-run] would create a {'published post' if args.publish else 'draft'} "
              f"from {path} ({len(body)} chars)", file=sys.stderr)
        return 0

    cookies = os.environ.get("SUBSTACK_COOKIES")
    if not cookies:
        print("SUBSTACK_COOKIES is not set. Copy your substack.com session cookies from "
              "browser dev tools (a 'name=value; name=value' string) into that env var, "
              "then re-run. Use --dry-run to preview without a cookie.", file=sys.stderr)
        return 1

    pub_url = cfg.get("substack", {}).get("publication_url") or os.environ.get("SUBSTACK_PUBLICATION_URL")

    try:
        from substack import Api
    except ImportError:
        print("python-substack is not installed (pip install python-substack).", file=sys.stderr)
        return 1

    api = Api(cookies_string=cookies, publication_url=pub_url)
    result = api.create_draft_from_markdown(
        title=title,
        markdown=body,
        subtitle=subtitle,
        publish=args.publish,
        send=not args.no_send,
    )
    draft_id = (result.get("draft") or {}).get("id")
    if args.publish:
        print(f"Published '{title}' (draft id {draft_id}).")
    else:
        print(f"Created draft '{title}' (id {draft_id}) — review it in Substack before publishing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
