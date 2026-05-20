# Administrative Writing — DOCX & PDF build guide

All commands assume the working directory is the `book_administrative-writing/` repo root.

---

## Key files

| File | Purpose |
|---|---|
| `adv/md/working/<date>.md` | ADV active Markdown source (e.g. `aw-adv-all_0516.md`) |
| `int/md/working/<date>.md` | INT active Markdown source (e.g. `aw-int-all_0519.md`) |
| `adv/md/working/aw-adv-styleref.docx` | **Single shared reference DOCX for both books** — canonical source for all style definitions, headers/footers, and page setup |
| `adv/style_specs/aw-div-label-styles.yaml` | YAML spec for Div label colors/fonts (manual maintenance only) |
| `../textmaker/scripts/style_bridge.lua` | Lua filter — maps fenced Div classes to Word styles via YAML `style_map` in Markdown front matter |
| `../textmaker/scripts/postprocess_docx.py` | Structural DOCX cleanup (run automatically by `markdown-to-docx`) |
| `../textmaker/scripts/manage_docx_styles.py` | Manual reference DOCX style maintenance — not part of the automated build |
| `../textmaker/scripts/validate_docx_against_reference.py` | Post-build style validator |

---

## Canonical build command — both books

The single CLI entry point for all DOCX generation is `textmaker.cmd markdown-to-docx`. Run from `book_administrative-writing/`:

**Advanced book:**
```cmd
textmaker.cmd markdown-to-docx ^
  --input adv\md\working\aw-adv-all_0516.md ^
  --reference adv\md\working\aw-adv-styleref.docx ^
  --lua-filter ..\textmaker\scripts\style_bridge.lua ^
  --output adv\md\working\aw-adv-all_0516.docx ^
  --no-pagebreak-filter ^
  --apply-semantic-labels ^
  --tag-style outline
```

**Intermediate book:**
```cmd
textmaker.cmd markdown-to-docx ^
  --input int\md\working\aw-int-all_0519.md ^
  --reference adv\md\working\aw-adv-styleref.docx ^
  --lua-filter ..\textmaker\scripts\style_bridge.lua ^
  --output int\md\working\aw-int-all_0519.docx ^
  --no-pagebreak-filter ^
  --apply-semantic-labels ^
  --tag-style outline
```

**The command is identical for both books** except for `--input` and `--output`. Both use the same `aw-adv-styleref.docx` reference.

### Flag rationale

| Flag | Why |
|---|---|
| `--reference adv\md\working\aw-adv-styleref.docx` | Shared single source of truth for styles, headers/footers, and page setup for both books |
| `--lua-filter ..\textmaker\scripts\style_bridge.lua` | Maps fenced Div classes to Word styles defined in Markdown YAML `style_map` |
| `--no-pagebreak-filter` | Prevents Textmaker's `pagebreak.lua` from converting `---` separators into page breaks; `style_bridge.lua` suppresses them correctly |
| `--apply-semantic-labels` | Enables icon label tables, Div label character styles, and unit title table insertion |
| `--tag-style outline` | Uses the outline icon variant before Div label text |
| *(no `--h1-sections`)* | H1 headings already have `pageBreakBefore` set in the styleref — adding section breaks via postprocess breaks header/footer inheritance across the document |
| *(no `--toc`)* | TOC is not used in this project |

---

## PDF conversion

Pass **absolute paths** when running `docx-to-pdf` from outside the Textmaker repo root. Relative paths resolve under the Textmaker directory and fail silently.

```powershell
$t = "\\<server>\...\textmaker"

& "$t\textmaker.cmd" docx-to-pdf `
  --input  "\\<server>\...\book_administrative-writing\adv\md\working\aw-adv-all_0516.docx" `
  --output "\\<server>\...\book_administrative-writing\adv\md\working\aw-adv-all_0516.pdf"

& "$t\textmaker.cmd" docx-to-pdf `
  --input  "\\<server>\...\book_administrative-writing\int\md\working\aw-int-all_0519.docx" `
  --output "\\<server>\...\book_administrative-writing\int\md\working\aw-int-all_0519.pdf"
```

`docx-to-pdf` uses Word COM and typically completes in under 60 seconds per book.

---

## Style validation (optional, post-build)

```cmd
python ..\textmaker\scripts\validate_docx_against_reference.py ^
  adv\md\working\aw-adv-all_0516.docx ^
  --reference adv\md\working\aw-adv-styleref.docx ^
  --style-map adv\style_specs\aw-div-label-styles.yaml
```

Exit code 0 = all styles consistent with the reference. Non-zero = mismatch report printed.

---

## Reference style maintenance (manual, separate workflow)

To update Div label colors or fonts in the reference DOCX:

```cmd
python ..\textmaker\scripts\manage_docx_styles.py ^
  --input adv\md\working\aw-adv-styleref.docx ^
  --spec adv\style_specs\aw-div-label-styles.yaml ^
  --in-place
```

`--in-place` creates a `.bak` backup automatically before overwriting.

---

## Design rules

- `aw-adv-styleref.docx` is the **only** place style definitions live. Both books share it.
- `postprocess_docx.py` never creates or redefines styles.
- `manage_docx_styles.py` is a manual maintenance tool — never add it to the automated build.
- `style_bridge.lua` reads the `style_map` from the Markdown YAML front matter — no hardcoded style names.
- If a mapped style is missing from the reference DOCX, `validate_docx_against_reference.py` fails loudly.
