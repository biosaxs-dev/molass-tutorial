<!-- AI Context Standard v0.8.9 - Adopted: 2026-04-02 -->
# AI Assistant Initialization Guide — molass-tutorial

**Purpose**: Initialize AI context for working in this repository  
**Created**: March 24, 2026

---

## What this repository is about

This repository holds the Jupyter Book source for the [Molass Library Tutorial](https://biosaxs-dev.github.io/molass-tutorial/) web book.

For first-time molass users, direct them to the [Beginner Onboarding repository](https://github.com/biosaxs-dev/molass-beginner) — open it in VS Code Agent mode and say "I want to begin with molass".

---

## Repository-specific conventions

- **Format**: [MyST Markdown syntax](https://jupyterbook.org/en/stable/reference/cheatsheet.html) is used throughout unless otherwise stated
- **Tone**: All documentation, instructions, and examples must be **beginner-friendly** — clear, easy to follow, suitable for users with no Python background. Use simple language, explain technical terms, provide step-by-step guidance wherever possible.
- **Build tool**: Jupyter Book

---

## Multi-root workspace context

| Repository | Role | Tool |
|------------|------|------|
| `molass-library` | Main library (Python source) | Python / Sphinx |
| `molass-legacy` | Legacy GUI predecessor; required runtime dep | Python / Sphinx |
| `modeling-vs-model_free` | Research: decomposition criteria | Markdown / Notebooks |
| `molass-tutorial` | **This repo**: usage documentation | Jupyter Book / MyST |
| `molass-essence` | Theory documentation | Jupyter Book / MyST |
| `molass-technical` | Technical report | Jupyter Book / MyST |
| `molass-develop` | Developer handbook | Jupyter Book / MyST |
| `molass-beginner` | Beginner onboarding (Agent mode) | Markdown |

---

## Building the book

```bash
jupyter-book build .
```

Output goes to `_build/html/`.

---

## Notebook workflow

Read [NOTEBOOK_CONVENTIONS.md v0.2.5](https://github.com/freesemt/ai-context-standard/blob/main/NOTEBOOK_CONVENTIONS.md) before working with any notebook in this repo.  
Kernel preference: global Python (`py`). Do not create venvs.

---

## Response language

**Response language**: English

---

## 🔄 Updates

**Latest**: March 25, 2026 — Updated to AI Context Standard v0.8; added `init.prompt.md` and `vscode-version.txt`  
**Previous**: March 24, 2026 — Created `.github/copilot-instructions.md` (AI Context Standard v0.7); migrated from `COPILOT_CONTEXT.md`
