---
title: "RBK-0002 render"
id: RBK-0002
type: runbook
status: draft
created: "2026-11-27"
tags: [quarto, slides]
related: [RBK-0001]
---

- [Render slide decks](#render-slide-decks)
  - [Preview while editing](#preview-while-editing)
  - [Render one deck](#render-one-deck)
  - [Render all decks](#render-all-decks)
- [Render as PDF](#render-as-pdf)
- [Render as PowerPoint](#render-as-powerpoint)
- [Notes](#notes)

## Render slide decks

Run all commands from the repository root. Activate the environment first, because `kickoff.qmd` runs Python:

```bash
source .venv/bin/activate
```

Decks are in `site/slides/`. The format (reveal.js) comes from `site/slides/_metadata.yml`, so do not pass `--to`.

| Deck        | File                          |
| ----------- | ----------------------------- |
| WP3 kickoff | `site/slides/wp3-kickoff.qmd` |
| WP6 kickoff | `site/slides/wp6-kickoff.qmd` |
| Demo        | `site/slides/kickoff.qmd`     |

### Preview while editing

```bash
quarto preview site/slides/wp3-kickoff.qmd
```

```bash
quarto preview site/slides/wp6-kickoff.qmd
```

### Render one deck

```bash
quarto render site/slides/wp3-kickoff.qmd
```

```bash
quarto render site/slides/wp6-kickoff.qmd
```

### Render all decks

```bash
quarto render site/slides
```

Output goes to `_site/site/slides/<name>.html`. Each file is self-contained and opens without a server.

## Render as PDF

Slide-look PDFs (same design as the HTML) come from [decktape](https://github.com/astefanutti/decktape), a dev dependency in `package.json`. It needs Node and Google Chrome. First time only:

```bash
npm install
```

Render the deck to HTML first (see above), then export it. One command per deck:

```bash
quarto render site/slides/wp3-kickoff.qmd && \
npx decktape reveal --size 960x540 --chrome-path "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" _site/site/slides/wp3-kickoff.html _site/site/slides/wp3-kickoff.pdf

quarto render site/slides/wp6-kickoff.qmd && \
npx decktape reveal --size 960x540 --chrome-path "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" _site/site/slides/wp6-kickoff.html _site/site/slides/wp6-kickoff.pdf

quarto render site/slides/electricity.qmd && \
npx decktape reveal --size 960x540 --chrome-path "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" _site/site/slides/electricity.html _site/site/slides/electricity.pdf
```

The PDF has one page per slide, 16:9, with text and vector diagrams. Speaker notes are not included.

`quarto render ... --to pdf` (or `--to typst`, `--to beamer`) does not give this result: it produces a plain report without the design or diagrams.

## Render as PowerPoint

Uses the KTH template (`resources/kth_template_presentation.pptx`). Pandoc only recognises layouts with standard names, so first build a reference file from the template (needs the OneDrive file; repeat when the template changes):

```bash
uv run python scripts/make_reference_pptx.py
```

This writes `resources/kth_reference.pptx` (not tracked). Then render the deck:

```bash
quarto render site/slides/wp3-kickoff.qmd --to pptx -M reference-doc:../../resources/kth_reference.pptx -M date-format:"D MMMM YYYY"
```

Output goes to `_site/site/slides/wp3-kickoff.pptx`. Speaker notes are included. Diagrams, timelines and column boxes of the HTML deck become tables and lists, so polish them in PowerPoint if needed.

Only the WP3 deck has PowerPoint variants so far. In the `.qmd`, HTML-only parts are wrapped in `content-hidden when-format="pptx"` and the table or list replacement in `content-visible when-format="pptx"`. Keep text before a table, not after it, or Pandoc adds an extra slide.

## Notes

- The KTH logo is read from `resources/kth_logo.png`, a symlink into OneDrive. The OneDrive file must be available when rendering.
- Shared styles are in `site/slides/kth.scss`.
- Press `S` in a deck for speaker notes, `F` for full screen, `Esc` for the overview.
