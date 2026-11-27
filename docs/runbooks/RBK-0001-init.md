---
title: "RBK-0001 init"
id: RBK-0001
type: runbook
status: draft
created: "2026-11-27"
tags: []
related: []
---

## Project init

```bash
uv init --bare --name plenergy --python 3.12
uv python pin 3.12
uv venv
uv add jupyter
uv add pyyaml
uv add pandas
uv add matplotlib
uv add plotly
uv add python-pptx
source .venv/bin/activate
quarto create project default . --no-prompt
```

### quarto.yml

```txt
project:
  title: "Plenergy AI"
  output-dir: _site

# Applies to every .qmd in the project
execute:
  engine: jupyter
  echo: true                 # show code in the output
  warning: false             # hide library warnings
  freeze: auto               # re-run only files that changed (cached in _freeze/)

format:
  html:
    theme: cosmo
    toc: true
    code-fold: true
    embed-resources: true    # single self-contained HTML file
```

### gitignore

```txt
/.quarto/
**/*.quarto_ipynb
.venv/
__pycache__/
site/_site/
site/_freeze/
site/.quarto/
*_files/
```

### npm

```bash
npm init -y
PUPPETEER_SKIP_DOWNLOAD=true npm install --save-dev decktape
npx decktape reveal --size 960x540 --chrome-path "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" _site/site/slides/wp3-kickoff.html _site/site/slides/wp3-kickoff.pdf
```
