# The Cross Section

A daily zeitgeist digest of new arXiv postings — not a paper list, but a read on
*what the field is collectively thinking about today* and how it connects to the
recent past, at multiple timescales.

Read it at **https://leblanc-lab.github.io/thexsection/** (RSS: `feed.xml`) or on
Substack at **https://thexsection.substack.com**. Digests are written by an LLM
(Claude) from arXiv abstracts and full-text HTML; treat them as a starting
point, not a substitute for reading the papers.

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
6. **Rebuilds the static site** into `site/` (committed, and deployed to GitHub
   Pages by `.github/workflows/pages.yml`), including `feed.xml` and any topic
   mirrors (below).

Published content is files in this repo; the digests and memory tiers double as
the model's context. No server. The optional full-history category harvest uses
a local SQLite metadata cache.

## Cost

Development/testing runs on the **Gemini free tier** ($0). Production on
**Claude Opus 5.5** ($4/$20 per MTok) costs roughly **$0.60/day (~$14/month)** for
hep-ex+hep-ph before the Batches API discount: ~40K input tokens for the digest,
plus deep dives and the memory refresh. Levers, cheapest first: `deep_dive.count: 0`,
switch `llm.provider`/model (e.g. `claude-sonnet-5-5`), or keep `llm.batch: true`
(50% off, already on for the nightly run).

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
middle names and initials are ignored. Initials-only forms ("J. Thaler") match
only when listed as a variant, and then only on author lists of 25 or fewer,
so collaboration papers don't fire on every "M. Williams" and a bare
"J. Zhang" never counts for anyone. `brief: false` keeps a topic out of the LLM briefing: it is a
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

`site/feed.xml` carries the daily issues, one item each. Every mirror (watched
topic or the deep dives) gets `site/<slug>/feed.xml` with **one item per
paper**, keyed on a stable `arxiv:<id>` guid; items link into the year pages.
Currently: `muon/`, `jets/`, `optimal-transport/`, `authors/`, `deep-dives/`.
Feed bodies get the `latex_to_unicode` treatment from `pipeline/substack.py` —
readers don't run KaTeX, so the math is flattened to Unicode rather than left
as raw `\(…\)`.

All feeds are paginated rather than truncated: newest items land on
`feed.xml`, older ones spill to `feed-2.xml`, `feed-3.xml`, etc., with
`site.digest_feed_items` (30) / `site.mirror_feed_items` (200) items per page.
Pages chain forward with `<atom:link rel="next">` in the `<channel>`
(absolute URL, omitted on the last page) so a reader can walk the full
archive without knowing the naming scheme up front. It's distinct file paths
rather than `?page=2` because GitHub Pages serves static files and ignores
query strings.

Both feeds need absolute URLs, so `site.base_url` in `config.yaml` is the one
place the deployed location is recorded; change it if the site moves.

## Future ideas

- Theme trend charts, semantic search over the archive.

## Extra category feeds (no LLM)

`category_scan` creates separate keyword-and-author feeds for `physics.ins-det`,
`cs.CV`, `cs.AI`, and `cs.LG`, at `physics-ins-det/feed.xml`, `cs-cv/feed.xml`,
`cs-ai/feed.xml`, and `cs-lg/feed.xml`. Each has a matching web page linked from
the footer. Entries contain the original abstract, authors, arXiv link, and the
matching keywords/author names. There are no model calls or LLM API charges.

Author variants are inherited for every feed. Detector keywords inherit the
whole watchlist; the three CS feeds exclude the `Optimal transport` topic's
abstract/title keywords through `exclude_keyword_topics`. A separate
`title_keywords` list retains OT-focused titles (optimal transport, Wasserstein,
Sinkhorn, earth mover, Gromov-Wasserstein, and Schrödinger bridge, including listed
spelling variants). These terms appearing only in the abstract do not qualify a
CS paper. Title-only matches are explicitly labelled `title: ...` in the feed. Muon/jet keywords and the
shared `LHC`, `Large Hadron Collider`, `collider`, `colliders`, and `energy mover`
terms still qualify, as does any watched author. A keyword **or** author match
is sufficient; authors are not filtered by `exclude_keyword_topics`. This is an
interest filter, not an automatic assessment of scientific importance. Set `category_scan.extra_keywords` to extend the shared
criteria. Optional `keywords` and `authors` lists on a feed replace the inherited
list for that criterion (`[]` disables it). Cross-listed papers may appear in
more than one category feed; each feed deduplicates by arXiv ID.

```sh
python -m pipeline.category_scan          # fetch current announcements and match
python -m pipeline.category_scan --rescan # reapply criteria to all saved batches
python -m pipeline.build_site            # render the pages and RSS
```

`--rescan --date YYYY-MM-DD` selects one stored day. Live feeds only provide
current announcements; use `pipeline.category_backfill` below for historical papers.
Raw batches live in `data/category-scan/<slug>/`, and matched entries in
`watch/category-scan/<slug>/`. Neither is loaded by the paid digest or watchlist
briefing, and `arxiv.categories` remains hep-ex/hep-ph. A paper independently
announced in those HEP categories can still enter their existing digest.

The separate **Category scan** workflow runs daily without LLM credentials and
triggers Pages after success, independently of the paid digest. Changes to
criteria can be applied locally with `--rescan` before publishing.

### Backfill extra categories

```sh
python -m pipeline.category_backfill --since 1991-01-01
# Or choose a smaller inclusive interval:
python -m pipeline.category_backfill --since 2025-01-01 --until 2025-12-31
python -m pipeline.build_site
```

The full-history start is a query lower bound, not a claim that every category
has records from 1991. Queries fetch metadata/abstracts only, serially and with
rate limiting. Historical entries use first-submission dates and current category
assignments, rather than reconstructing past daily announcements. No LLM calls.

Validated windows are checkpointed, including empty days. Rerunning the same
command resumes completed downloads and reapplies the current matching criteria.
Malformed responses, HTTP failures, and incomplete pagination fail visibly;
they are never saved as empty history. Raw history stays in gitignored
`data/category-scan/backfill/`; matched entries in
`watch/category-scan/<slug>/history/` are retained for publishing. `category_scan
--rescan` also processes this history. Live announcements and history merge by
arXiv ID, keeping the earliest occurrence in each category feed.

### Full-history bulk harvest (preferred)

arXiv's [OAI-PMH interface](https://info.arxiv.org/help/oa/index.html) supports
complete category harvesting. It works independently of the search API and
provides continuation tokens. Use it for the full-history run:

```sh
python -m pipeline.category_harvest --max-pages 20
# Repeat the identical command for the next chunk; omit the limit to finish all.
python -m pipeline.category_harvest --rescan  # offline, after criteria changes
python -m pipeline.build_site
```

Without `--max-pages`, the full run uses 20-page chunks with a one-minute rest
between chunks (`--chunk-pages` changes the chunk size). A local lock prevents
concurrent harvest/rescan processes.

Requests are serial with five-second gaps, exceeding arXiv's required
[three-second minimum](https://info.arxiv.org/help/api/tou.html). Each response
page and its continuation token are saved together in a transaction in
`data/category-scan/backfill/oai.sqlite3` (gitignored). Do not run multiple
harvesters or other arXiv fetchers concurrently. Refusals and server-requested
pauses stop the run instead of repeatedly requesting the same page. Run again
later to resume. Expired continuation tokens restart that category safely;
stored IDs prevent duplicate records. Completed categories are skipped.

Matched abstracts are rendered to `watch/category-scan/<slug>/history/oai/`
after each completed category or bounded chunk, and also on a handled network
failure. They merge into the category pages and RSS with the live scan and any
search-API backfill. OAI harvests by metadata-update order, but we use each
paper's original `created` date for the historical feeds. A partially downloaded
category is not a complete historical date interval; only exhausting its
continuation token establishes full coverage at harvest time.

The search-API backfiller also accepts `--max-windows N` for bounded date chunks.
Both routes use no LLM calls.

### Grouped physics feeds and accelerator coverage

The following additional streams use the same free category scan:

- `methods/feed.xml` (**Data & computational methods**) combines
  `physics.data-an` and `physics.comp-ph`.
- `physics-perspectives/feed.xml` (**Physics perspectives**) combines
  `physics.gen-ph`, `physics.hist-ph`, `physics.pop-ph`, and `physics.ed-ph`.
- `physics.acc-ph` contributes only matches to the **Muon collider** topic's
  criteria to the existing `muon/feed.xml`. General LHC/collider keywords and
  unrelated watched-author matches do not qualify this accelerator source.
  These additional entries are original abstracts, with no LLM briefing.

The two grouped feeds use the watched authors, collider keywords, and title-only
OT rules. Configure multiple source categories with `categories: [...]` and a
shared `name` and `slug`. Each category has independent raw/scan storage beneath
that slug; the page and RSS merge and deduplicate their papers. `match_topic`
reuses one existing watchlist topic's criteria, and `merge_into_watch: true`
adds the results to its existing page/feed. Existing watch entries take
precedence over supplemental abstracts, even when their dates differ.

The initial grouped streams were seeded from metadata updated since 2026-08-19,
including revisions, not a complete historical backfill. The seed metadata is
cached without marking those categories as fully harvested. The existing daily
workflow fetches future announcements; `pipeline.category_harvest` can backfill
the remaining history using the same resumable, paced downloads.

### New experimental HEP announcements

`hep-ex/feed.xml` (**Experimental HEP**) contains every new primary `hep-ex`
announcement, with its original abstract. It excludes cross-listings and
replacements and does not require a keyword or watched-author match.

Enable it with `hep_ex_feed.enabled` in `config.yaml`. The site build reads
existing daily announcement snapshots in `data/`, so this feed requires no
additional fetching or LLM calls. Its initial coverage is limited to those
stored snapshots; export-API and OAI history are excluded because historical
metadata does not reconstruct daily announcement types. Future daily builds
include newly fetched announcements automatically.
