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
        for section in ('main', 'personal', 'research', 'wins', 'experience', 'about', 'technologies', 'contact'):
            self.assertIn(section, self.page.ids)

    def test_hackathons_precede_internship_and_projects(self):
        sections = ('wins', 'experience', 'personal', 'research', 'about', 'technologies', 'contact')
        positions = [self.page.ids.index(section) for section in sections]
        self.assertEqual(positions, sorted(positions))

    def test_original_introduction_is_preserved(self):
        text = ' '.join((ROOT / 'index.html').read_text().split())
        introduction = (
            "I'm an Economics student working across Data Science, ML Engineering, Applied AI, and "
            'Data Analytics. I analyze data, build and evaluate models, and develop AI applications '
            'that support practical decisions.'
        )
        self.assertIn(introduction, text)

    def test_languages_are_text_only(self):
        html = (ROOT / 'index.html').read_text()
        languages = html.split('<ul class="technology-list languages">', 1)[1].split('</ul>', 1)[0]
        self.assertNotIn('<img', languages)
        for name in ('Python', 'SQL', 'R'):
            self.assertIn(f'<li>{name}</li>', languages)

    def test_about_has_original_skill_rows(self):
        html = (ROOT / 'index.html').read_text()
        about = html.split('id="about">', 1)[1].split('</section>', 1)[0]
        self.assertEqual(about.count('class="skillrow"'), 4)
        self.assertNotIn('class="education"', about)
        for label in ('Analysis and modeling', 'Evaluation', 'Data and reporting', 'Supporting engineering'):
            self.assertIn(f'<strong>{label}</strong>', about)

    def test_requested_version_two_sections_remain(self):
        html = (ROOT / 'index.html').read_text()
        self.assertIn('<h1>Chetsada Phummee<span>.</span></h1>', html)
        self.assertIn('<div class="eyebrow">My toolkit</div>', html)
        self.assertIn('<h2>Languages & technologies</h2>', html)
        self.assertIn('<h2>Let’s connect<span>.</span></h2>', html)
        self.assertNotIn('hero-panel', html)

    def test_project_disclosures_remain(self):
        html = (ROOT / 'index.html').read_text()
        self.assertEqual(html.count('<details>'), 7)


if __name__ == '__main__':
    unittest.main()
