# The Cross Section

A daily zeitgeist digest of new arXiv postings — not a paper list, but a read on
*what the field is collectively thinking about today* and how it connects to the
recent past, at multiple timescales.

## How it works

Once a day (GitHub Actions cron), the pipeline:

1. **Fetches** the day's announcements for the categories in `config.yaml`
   (arXiv Atom feeds, free — abstracts only, never PDFs).
2. **Writes the daily digest** in one model call: today's abstracts + rolling
   memory context (week / month / season / year syntheses + last 7 dailies).
3. **Deep-dives** the digest's 3–5 picks from their arXiv HTML renderings.
4. **Refreshes memory tiers**: `week.md` daily; `month.md` on the 1st;
   `season.md` on academic-term boundaries (Sep 1 / Feb 1 / May 1:
   Autumn = Sep–Jan, Spring = Feb–Apr, Summer = May–Aug); `year.md` on Sep 1.
5. **Citation radar** (Fridays): queries INSPIRE-HEP for highly-cited recent
   papers the deep dives missed and covers them.
6. **Rebuilds the static site** into `site/` (committed — the repo is private,
   so open `site/index.html` locally, or read the digests right in GitHub),
   including `feed.xml` and any topic mirrors (below).

All state is files in this repo; the digests and memory tiers double as the
model's context. No server, no database.

## Cost

Development/testing runs on the **Gemini free tier** ($0). Production on
**Claude Opus 4.8** costs roughly **$0.75/day (~$18/month)** for hep-ex+hep-ph:
~40K input tokens for the digest, plus deep dives and the memory refresh.
Levers, cheapest first: `deep_dive.count: 0`, switch `llm.provider`/model
(e.g. `claude-sonnet-5`), or move calls to the Batches API (50% off, future work).

## Running locally

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export GEMINI_API_KEY=...        # free key from aistudio.google.com
# or: export ANTHROPIC_API_KEY=...  and set llm.provider: anthropic in config.yaml

python -m pipeline.fetch                 # today's papers → data/YYYY-MM-DD.jsonl
python -m pipeline.digest --dry-run      # token count + cost estimate, no API call
python -m pipeline.digest                # write digests/YYYY-MM-DD.md
python -m pipeline.deep_dive             # expand the digest's picks
python -m pipeline.memory                # refresh rolling syntheses
python -m pipeline.radar                 # (Fridays) INSPIRE citation sweep
python -m pipeline.build_site            # render site/ ; open site/index.html
```

Every stage accepts `--date YYYY-MM-DD` to rerun/backfill from stored data.

## Switching to Claude

Set `llm.provider: anthropic` in `config.yaml` and add the `ANTHROPIC_API_KEY`
secret. Note: prompt tuning for digest voice/synthesis quality should be
re-checked on the Claude backend — models write differently, and the prompts
were drafted with Claude in mind.

## Cross-posting to Substack

Substack has no official posting API, so this uses the unofficial
`python-substack` library, which authenticates with a browser **session
cookie**. Copy your `substack.com` cookies from browser dev tools
(Application → Cookies) as a `name=value; name=value` string:

```sh
export SUBSTACK_COOKIES='...'                    # your session cookie string
python -m pipeline.substack --date 2026-07-09    # creates a DRAFT to review
python -m pipeline.substack --date 2026-07-09 --dry-run   # preview markdown, no cookie needed
python -m pipeline.substack --date 2026-07-09 --publish   # publish + email (opt-in)
```

The default action creates a **draft** you review in Substack's editor; nothing
publishes without `--publish`. `--kind radar|watch` posts those instead, and
`--dry-run` prints the cleaned, paste-ready Markdown (also handy for a manual
copy-paste). Caveats: LaTeX math lands as literal text, and Markdown tables are
converted to bullet lists (the library drops tables otherwise). Set
`substack.publication_url` in `config.yaml` only if you have more than one
publication.

From CI, once the `SUBSTACK_COOKIES` repo secret is set (Settings → Secrets →
Actions), the daily digest workflow automatically mirrors each new issue to
Substack as a **draft** — so there's one waiting to review every morning without
pushing anything. That step never publishes and never fails the run if the
cookie is missing or expired. The separate **Post to Substack** workflow
(`.github/workflows/substack.yml`) is the manual path for backfills, radar/watch
posts, or actually publishing (`publish` input).

## Watchlist tracks and topic pages

`watchlist.topics` in `config.yaml` defines keyword tracks matched against each
day's titles and abstracts. When one fires, a focused technical briefing lands in
`watch/<date>.md` and renders on the "Standing waves" page (linked only from the
◈ in the footer).

A track can additionally be mirrored to a page and feed of its own — the same
briefings, split out of the shared watch entries at build time, no extra LLM
calls:

```yaml
- name: "Muon collider"
  page: true      # mirror to site/muon/index.html + site/muon/feed.xml
  slug: muon      # URL segment
  theme: muon     # renders with templates/topic_muon.html + static/muon.css
  tagline: "The 10 TeV frontier, one posting at a time"
  keywords: [...]
```

A topic matches on `keywords` and/or `authors`. An author entry is a name or
a list of one person's variants (`["Ben Nachman", "Benjamin Nachman"]`);
middle names and initials are ignored, and initials-only forms count only on
author lists of 25 or fewer so collaboration papers don't fire on every
"M. Williams". `brief: false` keeps a topic out of the LLM briefing: it is a
scan-only abstract stream, which is how the "Authors to watch" track runs.

Topics without `page` stay watch-page-only. Mirror pages paginate by year
(`<slug>/index.html` is the latest year, `<slug>/<year>.html` the archive).
Two themes ship: `default` (the
house-style stream, `templates/topic_default.html` extending `base.html`, used
by the jet-substructure and optimal-transport mirrors) and `muon`, a fully
standalone shell that deliberately shares nothing with `base.html` but the
KaTeX and analytics snippets. A new theme means a new
`templates/topic_<theme>.html` (plus whatever shell it extends) and, if it
doesn't reuse `style.css`, a matching `static/<theme>.css`.

### Backfilling a mirror without the LLM

`python -m pipeline.scan` re-runs the keyword match over every day of raw
paper data in `data/` and writes the hits no briefing covers to
`watch/scan/<date>.md`: same shape as a watch entry, but each paper's body is
its abstract with a "keyword hit" note. `build_site` merges these under the
day's briefing on mirrored topic pages and feeds (briefed papers win; the scan
fills gaps). The watch page itself ignores them. Zero API calls, so it is the
cheap way to seed a new track or a broadened keyword list with history, and
it is idempotent — rerun it after changing keywords.

For history before `data/` begins, `python -m pipeline.backfill --since
YYYY-MM-DD [--until YYYY-MM-DD]` pulls the raw hep-ex/hep-ph listings from the
arXiv export API (the RSS feeds carry only the current day), writes them to
the **gitignored** `data/backfill/<date>.jsonl`, and scans them. That
directory is a local database: after a fresh clone, rerun the backfill to
rebuild it; the small `watch/scan/` markdown it produces is what gets
committed, because the Pages build only sees the repo. The daily workflow also
runs the scan after the briefing, so `brief: false` topics and any hits the
LLM step missed land the same day. Papers are filed by
*submission* day, a day or two ahead of announcement, and carry
`"source": "export-api"`. Roughly 10k papers, 17 MB and 3 minutes per year;
still no LLM. Existing days are left alone unless `--overwrite`.

## Deep-dive mirror

The same split applies to the digests themselves: with `deep_dive.page: true`,
every issue's `## Deep dives` section is lifted out at build time into
`site/<slug>/index.html` (default `deep-dives/`, linked from the nav) plus a
per-paper feed. Each day links back to its issue. An issue whose deep-dive
section has no `### arXiv:…` headings (a malformed completion) is reported
and skipped rather than emitted as a garbage item.

## Feeds

`site/feed.xml` carries the last 30 daily issues, one item each. Every mirror
(watched topic or the deep dives) gets `site/<slug>/feed.xml` with **one item
per paper**, keyed on a stable `arxiv:<id>` guid and capped at the newest
`site.mirror_feed_items` (200); items link into the year pages. Currently:
`muon/`, `jets/`, `optimal-transport/`, `authors/`, `deep-dives/`. Feed bodies get the `latex_to_unicode` treatment from
`pipeline/substack.py` — readers don't run KaTeX, so the math is flattened to
Unicode rather than left as raw `\(…\)`.

Both feeds need absolute URLs, so `site.base_url` in `config.yaml` is the one
place the deployed location is recorded; change it if the site moves.

## Future ideas

- Hosted private site for the group: Cloudflare Pages + Cloudflare Access
  (free ≤ 50 users). If the site goes public: GitHub Pages toggle.
- Batches API (halves API cost), email delivery, theme trend charts,
  semantic search over the archive.
