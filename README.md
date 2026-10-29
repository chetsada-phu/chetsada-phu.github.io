# Chetsada Phummee | Portfolio

Personal portfolio covering data science, machine learning engineering, applied AI, and data analytics.

Static HTML/CSS and a small vanilla JavaScript navigation enhancement, hosted with GitHub Pages. No build step or package installation is required.

## Local preview

From this directory:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765. The layout and content live in `index.html`, design tokens and responsive styles in `assets/styles.css`, and mobile navigation in `assets/site.js`. Google Fonts provides Space Grotesk, Manrope, and IBM Plex Mono; system fonts remain available as fallbacks. The content and navigation also work with JavaScript disabled.

## Checks

```sh
python3 -m unittest discover -s tests -v
node --check assets/site.js
```

These check internal anchors, local assets and evidence links, unique IDs, image alternative text, external-link protection, and the mobile-menu accessibility attributes. Browser checks should additionally cover small-screen overflow, menu open/close and Escape handling, project disclosures, keyboard navigation, and reduced motion.

Team photographs, certificates, and project decks are included to document the portfolio projects. The KBTG logo belongs to KASIKORN Business-Technology Group and identifies a past internship; it does not imply endorsement.
