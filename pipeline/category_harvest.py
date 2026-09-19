"""Harvest complete category metadata via arXiv's OAI-PMH bulk interface.

Serial requests, five-second gaps, transactional page checkpoints. Run again to
resume. --max-pages bounds a run without losing its continuation token.
"""
from __future__ import annotations

import argparse
import fcntl
import datetime as dt
import json
import re
import sqlite3
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import httpx

from .category_backfill import HEADERS, HISTORY_DIR, PAUSE
from .category_scan import SCAN_DIR, category_topics
from .common import load_config
from .scan import render
from .watchlist import TopicMatcher

URL = 'https://oaipmh.arxiv.org/oai'
NS = {'o': 'http://www.openarchives.org/OAI/2.0/', 'a': 'http://arxiv.org/OAI/arXiv/'}
SETS = {'physics.ins-det': 'physics:physics:ins-det',
        'cs.CV': 'cs:cs:CV', 'cs.AI': 'cs:cs:AI', 'cs.LG': 'cs:cs:LG'}
DB_PATH = HISTORY_DIR / 'oai.sqlite3'


def connect(path=DB_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.execute('CREATE TABLE IF NOT EXISTS papers (category TEXT, id TEXT, day TEXT, body TEXT, PRIMARY KEY(category,id))')
    db.execute('CREATE TABLE IF NOT EXISTS state (category TEXT PRIMARY KEY, token TEXT, complete INTEGER, last_stamp TEXT, pages INTEGER)')
    return db


def parse_page(content, category):
    root = ET.fromstring(content)
    if root.tag != '{'+NS['o']+'}OAI-PMH':
        raise ValueError('Response is not OAI-PMH XML')
    errors = root.findall('o:error', NS)
    if errors:
        error = errors[0]
        if error.get('code') == 'badResumptionToken':
            raise ExpiredToken(error.text)
        raise ValueError(f"OAI error {error.get('code')}: {error.text}")
    listing = root.find('o:ListRecords', NS)
    if listing is None:
        raise ValueError('Missing ListRecords response')
    rows, deleted, stamps = [], [], []
    for record in listing.findall('o:record', NS):
        header = record.find('o:header', NS)
        if header is None:
            raise ValueError('Missing record header')
        stamp = header.findtext('o:datestamp', namespaces=NS)
        if not stamp:
            raise ValueError('Missing record datestamp')
        stamps.append(stamp)
        if header.get('status') == 'deleted':
            deleted.append(header.findtext('o:identifier', namespaces=NS).removeprefix('oai:arXiv.org:'))
            continue
        meta = record.find('o:metadata/a:arXiv', NS)
        if meta is None:
            raise ValueError('Missing arXiv metadata')
        def value(name):
            return re.sub(r'\s+', ' ', meta.findtext('a:'+name, default='', namespaces=NS)).strip()
        categories = value('categories').split()
        if category not in categories:
            raise ValueError(f'Record outside requested category: {value("id")}')
        day = value('created')
        dt.date.fromisoformat(day)
        authors = [' '.join(filter(None, [a.findtext('a:forenames', namespaces=NS),
                                         a.findtext('a:keyname', namespaces=NS),
                                         a.findtext('a:suffix', namespaces=NS)]))
                   for a in meta.findall('a:authors/a:author', NS)]
        paper = dict(id=value('id'), title=value('title'), abstract=value('abstract'),
                     authors=authors, categories=categories, primary_category=categories[0],
                     source='oai-pmh', submitted=day)
        if not paper['id'] or not paper['title'] or not paper['abstract']:
            raise ValueError('Incomplete paper metadata')
        rows.append((category, paper['id'], day, json.dumps(paper)))
    token = listing.findtext('o:resumptionToken', default='', namespaces=NS).strip()
    if not rows and not deleted and token:
        raise ValueError('Empty page with continuation token')
    return rows, deleted, token, max(stamps, default='')


class ExpiredToken(ValueError):
    pass


def save_page(db, category, content):
    rows, deleted, token, stamp = parse_page(content, category)
    with db:
        db.executemany('INSERT OR REPLACE INTO papers VALUES (?,?,?,?)', rows)
        db.executemany('DELETE FROM papers WHERE category=? AND id=?', [(category, ident) for ident in deleted])
        db.execute('INSERT INTO state VALUES (?,?,?,?,1) ON CONFLICT(category) DO UPDATE SET token=excluded.token, complete=excluded.complete, last_stamp=excluded.last_stamp, pages=state.pages+1',
                   (category, token, int(not token), stamp))
    return len(rows), bool(token)


def render_history(db, topic):
    """Rebuild only this harvester's entries, separate from live/API scan files."""
    directory = SCAN_DIR / topic['slug'] / 'history' / 'oai'
    directory.mkdir(parents=True, exist_ok=True)
    matcher = TopicMatcher([topic])
    day, entries, written, count = None, [], set(), 0
    def flush():
        if entries:
            path = directory / f'{day}.md'
            body = render(day, {topic['name']: entries}).replace(
                'abstract only, not yet read for a briefing.', 'original abstract; no AI summary.')
            temporary = path.with_suffix('.tmp')
            temporary.write_text(body)
            temporary.replace(path)
            written.add(path)
    for submitted, body in db.execute('SELECT day,body FROM papers WHERE category=? ORDER BY day,id', (topic['category'],)):
        if submitted != day:
            flush()
            day, entries = submitted, []
        paper = json.loads(body)
        matched = matcher.hits(paper).get(topic['name'])
        if matched:
            entries.append((paper, matched))
            count += 1
    flush()
    for stale in directory.glob('????-??-??.md'):
        if stale not in written:
            stale.unlink()
    return count


def harvest(db, topics, max_pages=None):
    pages = 0
    with httpx.Client(timeout=90, follow_redirects=True, headers=HEADERS) as client:
        for topic in topics:
            category = topic['category']
            recovered = False
            initial = db.execute('SELECT complete FROM state WHERE category=?', (category,)).fetchone()
            if initial and initial[0]:
                continue
            while True:
                state = db.execute('SELECT token,complete,last_stamp FROM state WHERE category=?', (category,)).fetchone()
                if state and state[1]:
                    break
                params = {'verb':'ListRecords'}
                if state and state[0]:
                    params['resumptionToken'] = state[0]
                else:
                    params.update(metadataPrefix='arXiv', set=SETS[category])
                time.sleep(PAUSE)
                response = client.get(URL, params=params)
                if response.status_code in (429,503):
                    raise RuntimeError(f"Server requested a pause: HTTP {response.status_code}; "
                                       f"Retry-After={response.headers.get('retry-after', 'unspecified')}. Resume later.")
                response.raise_for_status()
                try:
                    size, more = save_page(db, category, response.content)
                except ExpiredToken:
                    if not state or recovered:
                        raise
                    with db:
                        # OAI does not guarantee date ordering. Restart the set
                        # safely on expiry; persisted IDs deduplicate replayed pages.
                        db.execute('UPDATE state SET token=?,last_stamp=? WHERE category=?', ('','',category))
                    recovered = True
                    continue
                pages += 1
                total = db.execute('SELECT COUNT(*) FROM papers WHERE category=?', (category,)).fetchone()[0]
                print(f'{category}: saved {size} records; {total} unique; '+('more pages' if more else 'COMPLETE'), flush=True)
                if max_pages is not None and pages >= max_pages:
                    print(f'Page limit reached; saved continuation. {render_history(db, topic)} matches rendered.', flush=True)
                    return
                if not more:
                    break
            print(f'{category}: {render_history(db, topic)} matches rendered.', flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--max-pages', type=int, help='stop after N downloaded pages; rerun to resume')
    ap.add_argument('--chunk-pages', type=int, default=20, help='pages between rests in a full run (default 20)')
    ap.add_argument('--rescan', action='store_true', help='reapply criteria to stored metadata, no network')
    args = ap.parse_args()
    if args.chunk_pages < 1:
        ap.error('--chunk-pages must be positive')
    if args.max_pages is not None and args.max_pages < 1:
        ap.error('--max-pages must be positive')
    topics = category_topics(load_config())
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    lock = DB_PATH.with_suffix('.lock').open('a')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock.close()
        print('Another category harvest/rescan is running; leaving it alone.', file=sys.stderr)
        return 1
    db = connect()
    try:
        if args.rescan:
            for topic in topics:
                print(f"{topic['category']}: {render_history(db, topic)} matches")
        elif args.max_pages is not None:
            harvest(db, topics, args.max_pages)
        else:
            while topics:
                harvest(db, topics, args.chunk_pages)
                completed = {row[0] for row in db.execute('SELECT category FROM state WHERE complete=1')}
                if all(t['category'] in completed for t in topics):
                    print('All category harvests COMPLETE.', flush=True)
                    break
                print('Resting 60 seconds before the next chunk.', flush=True)
                time.sleep(60)
    except (httpx.HTTPError, ValueError, RuntimeError, ET.ParseError) as exc:
        print(f'Harvest stopped: {exc}. Completed pages are saved.', file=sys.stderr)
        for topic in topics:
            print(f"{topic['category']}: {render_history(db, topic)} matches from saved metadata (harvest may be incomplete)", flush=True)
        return 1
    finally:
        db.close()
        lock.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
