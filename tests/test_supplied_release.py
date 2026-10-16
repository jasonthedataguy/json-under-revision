"""A supplied design must publish the canonical manuscript without a JS dependency."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_site import render_chapter
from check_site import Page


class SuppliedReleaseTests(unittest.TestCase):
    def test_supplied_template_renders_original_without_generated_media_recipe(self):
        with tempfile.TemporaryDirectory() as temporary:
            chapter = Path(temporary)
            (chapter / 'source').mkdir()
            (chapter / 'web').mkdir()
            original = '# Fashion\n\nA$AP & an original sentence.\n\nPeace and love!\n'
            (chapter / 'source/original.md').write_text(original, encoding='utf-8')
            (chapter / 'source/revisions.log').write_text('Imported original.', encoding='utf-8')
            (chapter / 'web/template.html').write_text('<link rel="canonical" href="$url"><article class="prose">$story</article><a href="$next_url">$next_title</a>', encoding='utf-8')
            meta = {'release_stage': 'supplied', 'web_template': 'web/template.html',
                    'canonical_text': 'source/original.md', 'title': 'Fashion',
                    'subtitle': 'A room in revision', 'number': '02',
                    'canonical_path': 'chapters/02/', 'palette': {}, 'theme': [],
                    'artifact': 'wardrobe',
                    'reading_illustrations': [{'after_paragraph': 0, 'src': 'assets/cabin.jpg',
                                              'alt': 'Snow & light', 'width': 1500, 'height': 938}]}
            page, _ = render_chapter(chapter, meta, {'public_url': 'https://example.org/book/'},
                                     {'canonical_path': 'chapters/03/', 'title': 'Next & last'})
            self.assertEqual(Page(page).story, ['A$AP & an original sentence.', 'Peace and love!'])
            self.assertIn('https://example.org/book/chapters/02/', page)
            self.assertIn('href="../../chapters/03/">Next &amp; last', page)
            self.assertLess(page.index('A$AP &amp; an original sentence.'), page.index('assets/cabin.jpg'))
            self.assertLess(page.index('assets/cabin.jpg'), page.index('Peace and love!'))
            self.assertIn('alt="Snow &amp; light"', page)
            meta['reading_illustrations'][0]['after_paragraph'] = 2
            with self.assertRaises(ValueError):
                render_chapter(chapter, meta, {'public_url': 'https://example.org/'}, meta)
            meta['reading_illustrations'][0]['after_paragraph'] = 0
            meta['web_template'] = '../outside.html'
            with self.assertRaises(ValueError):
                render_chapter(chapter, meta, {'public_url': 'https://example.org/'}, meta)


if __name__ == '__main__':
    unittest.main()
