"""Dependency-free checks for the GitHub Pages portfolio."""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.resources = []
        self.images = []
        self.menu = None
        self.feed((ROOT / 'index.html').read_text())

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if 'id' in attributes:
            self.ids.append(attributes['id'])
        if tag == 'a':
            self.links.append(attributes)
        if tag in ('img', 'script'):
            self.resources.append(attributes.get('src', ''))
        if tag == 'link' and attributes.get('rel') in ('stylesheet', 'icon'):
            self.resources.append(attributes.get('href', ''))
        if tag == 'img':
            self.images.append(attributes)
        if tag == 'button' and attributes.get('class') == 'menu-toggle':
            self.menu = attributes


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.page = Page()

    def test_unique_ids(self):
        self.assertEqual(len(self.page.ids), len(set(self.page.ids)))

    def test_all_navigation_targets_exist(self):
        for link in self.page.links:
            href = link.get('href', '')
            if href.startswith('#'):
                self.assertIn(href[1:], self.page.ids)

    def test_local_resources_and_evidence_exist(self):
        paths = self.page.resources + [link.get('href', '') for link in self.page.links]
        for href in paths:
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            with self.subTest(path=url.path):
                self.assertTrue((ROOT / unquote(url.path)).is_file())

    def test_images_have_alternative_text(self):
        for image in self.page.images:
            self.assertTrue(image.get('alt', '').strip())

    def test_external_tabs_are_protected(self):
        for link in self.page.links:
            if link.get('target') == '_blank':
                self.assertIn('noopener', link.get('rel', ''))

    def test_mobile_menu_accessibility_contract(self):
        self.assertIsNotNone(self.page.menu)
        self.assertEqual(self.page.menu['aria-expanded'], 'false')
        self.assertIn(self.page.menu['aria-controls'], self.page.ids)

    def test_all_portfolio_sections_remain(self):
        for section in ('main', 'personal', 'research', 'wins', 'experience', 'about', 'contact'):
            self.assertIn(section, self.page.ids)


if __name__ == '__main__':
    unittest.main()
