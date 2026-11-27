---
title: "RBK-0002 render"
id: RBK-0002
type: runbook
status: draft
created: "2026-11-27"
tags: [quarto, slides]
related: [RBK-0001]
---

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

## Notes

- The KTH logo is read from `resources/kth_logo.png`, a symlink into OneDrive. The OneDrive file must be available when rendering.
- Shared styles are in `site/slides/kth.scss`.
- Press `S` in a deck for speaker notes, `F` for full screen, `Esc` for the overview.
- `_site/` and `_freeze/` at the repository root are not yet in `.gitignore`.
