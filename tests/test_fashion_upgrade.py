"""Fashion chapter: truthful copy, accessible archive, and release safety checks."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FASHION = ROOT / "chapters" / "fashion"

class FashionUpgradeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = (FASHION / "web/template.html").read_text(encoding="utf-8")
        cls.script = (FASHION / "web/assets/chapter.js").read_text(encoding="utf-8")
        cls.css = (FASHION / "web/assets/upgrade.css").read_text(encoding="utf-8")
        cls.selected = (FASHION / "source/approved.md").read_text(encoding="utf-8")
        cls.previous = (FASHION / "source/original.md").read_text(encoding="utf-8")

    def test_actual_quotes_are_verbatim(self):
        match = re.search(r"const quotes = \[(.*?)\];", self.script, re.S)
        self.assertIsNotNone(match, "Six-step explorer needs curated quotations")
        quotes = json.loads("[" + match.group(1) + "]")
        self.assertEqual(len(quotes), 6)
        for quote in quotes:
            self.assertIn(quote, self.selected, quote)

    def test_revision_examples_represent_actual_versions(self):
        old = [
            "tôi lại rảnh rỗi lên đây ngồi viết tào lao",
            "spending là một phần của guồng máy",
            "Bản thân mình, cùng đống trải nghiệm đã đi qua, tự nó đã là một statement rồi."
        ]
        new = [
            "tôi lại có hứng lên đây ngồi viết tào lao",
            "một trong những động lực phát triển kinh tế chính là spending",
            "chính bản thân mình tự nó đã là 1 statement piece rồi."
        ]
        for phrase in old:
            self.assertIn(phrase, self.previous)
            self.assertIn(phrase, self.template)
        for phrase in new:
            self.assertIn(phrase, self.selected)
            self.assertIn(phrase, self.template)

    def test_immersive_reader_has_accessible_fallback(self):
        for marker in ('id="prose"', '$story', 'id="choices"', 'aria-pressed',
                       'id="previous-manuscript"', '$original', 'id="keep"',
                       'id="share-feedback"', 'id="wardrobe-counter"'):
            self.assertIn(marker, self.template)
        self.assertIn('role="status"', self.template)
        self.assertIn('prefers-reduced-motion', self.css)
        self.assertIn('event.key === "Home"', self.script)
        self.assertIn("Nothing is submitted or tracked", self.template)

    def test_real_routes_and_social_metadata(self):
        self.assertIn('rel="canonical" href="$url"', self.template)
        self.assertIn('property="og:image"', self.template)
        self.assertIn('name="twitter:card"', self.template)
        for name in ("Fashion-A5-print.pdf", "Fashion-A4-booklet.pdf",
                     "Fashion-A4-ink-saving.pdf", "Fashion-print-pack.zip",
                     "Fashion-social-pack.zip", "product-set.zip"):
            self.assertIn(name, self.template)

    def test_no_fake_sales_or_provenance(self):
        self.assertIn("chưa mở bán", self.template)
        self.assertIn("không phải ảnh tư liệu", self.template)
        self.assertNotIn('<form action="', self.template)
        self.assertNotIn("fetch(", self.script)
        self.assertNotIn("localStorage", self.script)
        self.assertNotIn("analytics", self.script.lower().split("no analytics requests")[-1])

if __name__ == "__main__":
    unittest.main()
