# Chetsada Phummee | Portfolio

Personal portfolio covering data science, machine learning engineering, applied AI, and data analytics.

Static HTML/CSS and a small vanilla JavaScript navigation enhancement, hosted with GitHub Pages. No build step or package installation is required.

## Local preview

From this directory:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765. The lavender-and-indigo design retains the original hackathon cards, internship panel, and project layouts, with a compact profile introduction, a text-only language toolkit, and a minimal “Let’s connect” ending. Content lives in `index.html`, design tokens and responsive styles in `assets/styles.css`, and mobile navigation in `assets/site.js`. Google Fonts provides Space Grotesk, Manrope, and IBM Plex Mono; system fonts remain available as fallbacks. The content and navigation also work with JavaScript disabled.

Languages appear as text-only chips. The original two-column About section places the biography on the left and four text-based skill groups on the right.

Unused language symbols remain in `assets/icons/`: Python and R symbols come from [Devicon v2.17.0](https://github.com/devicons/devicon/tree/v2.17.0) under its MIT license (included in `assets/icons/DEVICON-LICENSE.txt`); their respective trademarks remain with their owners. The SQL database symbol is original. The CP monogram is not a university or employer logo.

## Checks

```sh
python3 -m unittest discover -s tests -v
node --check assets/site.js
```

These check internal anchors, local assets and evidence links, unique IDs, image alternative text, external-link protection, mobile-menu accessibility attributes, section order, the original introduction, text-only language labels, the original About skill groups, and project disclosures. Browser checks should additionally cover small-screen overflow, menu open/close and Escape handling, project disclosures, keyboard navigation, and reduced motion.

Team photographs, certificates, and project decks are included to document the portfolio projects. CatMium and C-Canteen include thumbnail galleries, collapsed by default behind “View project images”; each image opens its full-size local asset in a new tab, with no JavaScript required. App screenshots retain their supplied resolution. The KBTG logo belongs to KASIKORN Business-Technology Group and identifies a past internship; it does not imply endorsement.
