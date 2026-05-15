# Advanced textbook — DOCX build guide

All commands assume the working directory is the `book_administrative-writing/` repo root.

---

## Prerequisites

- Pandoc installed and on PATH
- `python-docx`, `lxml`, and `pyyaml` installed (`pip install python-docx lxml pyyaml`)
- The `textmaker` repo checked out alongside this repo as a sibling directory

---

## Key files

| File | Purpose |
|---|---|
| `adv/md/final/aw-adv-all_0514.md` | Markdown source with YAML `style_map` metadata |
| `adv/md/final/aw-adv-styleref.docx` | Reference DOCX — single source of truth for all style definitions |
| `adv/style_specs/aw-div-label-styles.yaml` | YAML spec for Div label colors and fonts (manual maintenance input) |
| `../textmaker/scripts/style_bridge.lua` | Lua filter that maps Div classes to Word custom styles from YAML metadata |
| `../textmaker/scripts/postprocess_docx.py` | Structural DOCX cleanup (section breaks, page numbering, heading codes) |
| `../textmaker/scripts/manage_docx_styles.py` | Manual maintenance tool for updating reference DOCX styles |
| `../textmaker/scripts/audit_docx_styles.py` | Inspect reference DOCX style definitions without modifying |
| `../textmaker/scripts/validate_docx_against_reference.py` | Validate generated DOCX styles against reference DOCX |

---

## Step 1 — Pandoc conversion

```bash
pandoc adv/md/final/aw-adv-all_0514.md \
  --from markdown \
  --to docx \
  --reference-doc adv/md/final/aw-adv-styleref.docx \
  --lua-filter ../textmaker/scripts/style_bridge.lua \
  --toc --toc-depth=2 \
  -o adv/docx/aw-adv-all.docx
```

On Windows (cmd.exe):

```cmd
pandoc adv/md/final/aw-adv-all_0514.md ^
  --from markdown ^
  --to docx ^
  --reference-doc adv/md/final/aw-adv-styleref.docx ^
  --lua-filter ..\textmaker\scripts\style_bridge.lua ^
  --toc --toc-depth=2 ^
  -o adv/docx/aw-adv-all.docx
```

---

## Step 2 — Structural post-processing (default, safe)

```bash
python ../textmaker/scripts/postprocess_docx.py \
  adv/docx/aw-adv-all.docx \
  --toc \
  --reference-doc adv/md/final/aw-adv-styleref.docx
```

This applies structural cleanup only (section breaks, page numbering, heading codes).
It does **not** create or modify styles.

---

## Step 3 — Style validation

```bash
python ../textmaker/scripts/validate_docx_against_reference.py \
  adv/docx/aw-adv-all.docx \
  --reference adv/md/final/aw-adv-styleref.docx \
  --style-map adv/style_specs/aw-div-label-styles.yaml
```

Exit code 0 = all styles consistent. Non-zero = report printed, build should be treated as failed.

---

## Full build with semantic label rendering (Windows)

When you want emoji labels, Div label character styles, and unit title tables:

```cmd
python ..\textmaker\scripts\postprocess_docx.py ^
  adv\docx\aw-adv-all.docx ^
  --toc ^
  --reference-doc adv\md\final\aw-adv-styleref.docx ^
  --apply-semantic-labels
```

---

## Reference style maintenance (manual, separate workflow)

To update Div label colors or fonts in the reference DOCX:

```bash
python ../textmaker/scripts/manage_docx_styles.py \
  --input adv/md/final/aw-adv-styleref.docx \
  --spec adv/style_specs/aw-div-label-styles.yaml \
  --output adv/md/final/aw-adv-styleref.updated.docx
```

Review `aw-adv-styleref.updated.docx` in Word. If correct, replace the original:

```bash
python ../textmaker/scripts/manage_docx_styles.py \
  --input adv/md/final/aw-adv-styleref.docx \
  --spec adv/style_specs/aw-div-label-styles.yaml \
  --in-place
```

`--in-place` creates a `.bak` backup automatically before overwriting.

To audit the reference DOCX without modifying it:

```bash
python ../textmaker/scripts/audit_docx_styles.py \
  adv/md/final/aw-adv-styleref.docx \
  --filter "Div Label"
```

---

## Design rules

- The reference DOCX is the **only** place style definitions live.
- `postprocess_docx.py` never creates or redefines styles.
- `manage_docx_styles.py` is a manual maintenance tool, not part of the automated build.
- `style_bridge.lua` reads the `style_map` from the Markdown YAML front matter and passes
  Div classes to Pandoc as `custom-style` attributes — no style definitions of its own.
- If a mapped style is missing from the reference DOCX, validation fails loudly.
