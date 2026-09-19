import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from pipeline import build_site


class HepExFeedTests(unittest.TestCase):
    def test_only_new_primary_announcements_and_deduplication(self):
        topic={'name':'Experimental HEP'}
        def paper(ident, **changes):
            result = dict(id=ident, title='Unrelated to every watchlist keyword',
                          authors=['Example Author'], abstract='Original abstract.',
                          primary_category='hep-ex', announce_type='new')
            result.update(changes)
            return result
        with tempfile.TemporaryDirectory() as tmp, patch.object(build_site,'DATA_DIR',Path(tmp)):
            papers=[paper('2609.00001'),paper('2609.00002',announce_type='cross'),
                    paper('2609.00003',announce_type='replace'),paper('2609.00004',primary_category='hep-ph'),
                    paper('2609.00005',source='export-api'),paper('2609.00006',source='oai-pmh')]
            (Path(tmp)/'2026-09-18.jsonl').write_text(''.join(json.dumps(p)+'\n' for p in papers))
            (Path(tmp)/'2026-09-19.jsonl').write_text(json.dumps(papers[0])+'\n')
            (Path(tmp)/'backfill').mkdir()
            (Path(tmp)/'backfill'/'2026-09-01.jsonl').write_text(json.dumps(paper('2609.00007'))+'\n')
            days=build_site.load_hep_ex_days(topic)
            self.assertEqual(len(days),1)
            self.assertEqual(days[0]['date'],'2026-09-18')
            self.assertEqual([p['id'] for p in days[0]['papers']],['2609.00001'])
            self.assertIn('New hep-ex announcement',days[0]['papers'][0]['md'])
            self.assertNotIn('Watchlist hit',days[0]['papers'][0]['md'])


if __name__=='__main__':unittest.main()
