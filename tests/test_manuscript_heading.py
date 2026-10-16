"""An authorized title change must never allow changes to the author's prose."""
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_site import validate_author_manuscript

class ManuscriptHeadingTests(unittest.TestCase):
    def test_title_only_policy_preserves_body_bytes_and_rejects_edits(self):
        for ending in [b'\n',b'\r\n']:
            with self.subTest(ending=ending),tempfile.TemporaryDirectory() as directory:
                folder=Path(directory)
                original=ending.join([b'# 5. Original',b'',b'First *paragraph*.',b'',b'Final sentence. ',b''])
                (folder/'original.md').write_bytes(original)
                approved=b'# 06. New title'+ending+original.partition(b'\n')[2]
                (folder/'approved.md').write_bytes(approved)
                meta={'slug':'test','number':'06','title':'New title','canonical_text':'approved.md','text_policy':'verbatim-author-body','manuscript_source':{'path':'original.md','bytes':len(original),'sha256':hashlib.sha256(original).hexdigest()}}
                self.assertEqual(validate_author_manuscript(folder,meta),original)
                for unauthorized in [approved.replace(b'First',b'Rewritten'),approved.replace(b'06.',b'05.'),approved.replace(b'New title',b'Wrong title')]:
                    (folder/'approved.md').write_bytes(unauthorized)
                    with self.assertRaises(AssertionError):validate_author_manuscript(folder,meta)
                (folder/'approved.md').write_bytes(approved)
                meta['text_policy']='verbatim-author-original'
                with self.assertRaises(AssertionError):validate_author_manuscript(folder,meta)

if __name__=='__main__':unittest.main()
