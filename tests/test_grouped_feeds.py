import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline.category_scan import category_topics, source_slug, scan_file, scan_day
from pipeline.common import load_config
from pipeline import build_site, category_scan


class GroupedFeedTests(unittest.TestCase):
    def test_grouped_sources_have_independent_caches_and_deduplicate(self):
        topics=[t for t in category_topics(load_config()) if t['slug']=='methods']
        self.assertEqual({t['category'] for t in topics},{'physics.data-an','physics.comp-ph'})
        self.assertEqual(len({source_slug(t) for t in topics}),2)
        with tempfile.TemporaryDirectory() as tmp, patch.object(category_scan,'SCAN_DIR',Path(tmp)/'scan'):
            path=Path(tmp)/'2026-09-19.jsonl'
            path.write_text(json.dumps(dict(id='2609.12345',title='Collider simulation',abstract='test',authors=[]))+'\n')
            for topic in topics:
                scan_file(path,topic)
                self.assertTrue((Path(tmp)/'scan'/source_slug(topic)/'2026-09-19.md').exists())
            days=build_site.load_topic_days(topics[0]['name'],Path(tmp)/'scan'/'methods')
            self.assertEqual(sum(len(d['papers']) for d in days),1)

    def test_accelerator_source_is_muc_only(self):
        topic=next(t for t in category_topics(load_config()) if t['category']=='physics.acc-ph')
        for title,authors,expected in [('LHC optics',[],False),('Unrelated',['Jesse Thaler'],False),
                                      ('Cooling for a muon collider',[],True),('MAIA Detector studies',[],True)]:
            paper=dict(id='2609.12345',title=title,abstract='',authors=authors)
            self.assertEqual(bool(scan_day([paper],[topic],{})),expected)
        self.assertTrue(topic['merge_into_watch'])
        self.assertFalse(topic['brief'])

    def test_existing_muon_briefing_wins_across_dates(self):
        primary=[dict(date='2026-09-19',papers=[dict(id='2609.12345',md='briefing')])]
        extra=[dict(date='2026-09-17',papers=[dict(id='2609.12345',md='abstract'),dict(id='2609.00001',md='new')])]
        merged=build_site.merge_topic_days(primary,extra)
        self.assertEqual([p['md'] for d in merged for p in d['papers']],['briefing','new'])
        self.assertEqual(len(primary[0]['papers']),1)


if __name__=='__main__':
    unittest.main()
