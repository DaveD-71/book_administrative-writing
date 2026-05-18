# Intermediate Textbook — Pipeline Alignment Action List

Generated: 2026-05-18
Source: Advanced textbook pipeline (sessions 2–9, 2026-05-09 to 2026-05-18)
Target file: `int/md/final/aw-int-all.md`
Last edited: 2026-04-01 (git), 2026-04-23 (file timestamp)

---

## Priority 1 — Pipeline Blockers

These must be done before any conversion can run.

### 1. Add YAML front matter with `style_map`

- The build pipeline requires YAML front matter for `style_bridge.lua` to map div classes to Word styles
- Without it, Pandoc produces zero Div Label styles and the entire semantic formatting layer is skipped
- Model on `aw-adv-all_0516.md` YAML block (9 div classes → `Div Label *` styles)
- Also note `--no-pagebreak-filter` flag required in CLI

### 2. Create a reference DOCX for the intermediate book

- Options: copy `adv/md/working/aw-adv-styleref.docx` as starting point, or create a separate `aw-int-styleref.docx`
- Must contain all `Div Label *` paragraph styles (12), `AW Standard Table` and other AW table styles, `Checklist`, `AW Example Good/Bad`, `Body Text`, `ResponsePlaceholder` style, `DivTag` character style
- Must be placed in a working folder alongside the source markdown

### 3. Create working folder for intermediate book

- Equivalent to `adv/md/working/`
- Suggested: `int/md/working/`
- Copy `aw-int-all.md`, reference DOCX, and icon assets folder there

### 4. Copy icon assets to working folder

- Copy `adv/md/working/div-tags-icons-2_assets/` to `int/md/working/`
- Folder must be a sibling of the reference DOCX for `_resolve_div_tag_icon()` to find it

---

## Priority 2 — Source Markdown — Structural (required before build)

### 5. Add fenced div markup throughout source markdown

- **Largest single task** — the file currently has zero `:::` fences
- Mirrors sessions 2–3 on the advanced book (div classification and reclassification)
- 9 div classes to apply: `learn`, `language`, `structure`, `notice`, `write`, `rewrite`, `revise`, `edit`, `example` (+ `example-good`, `example-bad`)
- Requires content-by-content review of all 23 units
- After markup: run full balance check (opens == closes) and Pandoc spacing audit

### 6. Convert editing activity bullet lists to checklist format

- Current state: 0 checklist items (`- [ ]`), but editing activities exist throughout
- Advanced book converted 151 plain `-` bullets inside edit divs to `- [ ]`
- Identify all bullet lists inside `edit` div blocks and convert after div markup is applied

### 7. Audit and fix alphabetic option lists

- ~103 potential alpha list items detected (`A.`, `B.`, etc.)
- Advanced pipeline strips literal markers and applies `List Number 3` style
- Confirm which are genuine A/B/C option lists vs. other uses before build

### 8. Fix Pandoc div spacing issues

- After div markup is added, audit for:
  - Missing blank lines before `:::` open fences when preceded by non-empty content
  - Missing blank lines between `:::` open fence and immediately-following list
  - Double/redundant close fences from nested div patterns
- Use the same systematic scan approach as applied to the advanced book

### 9. Review and adjust PH marker sizing

- File already uses `{{PH-1}}` through `{{PH-5}}` with task IDs — 163 markers total
- Current size scheme: PH-1=2 rows, PH-3=9 rows, PH-4=15 rows, PH-5=22 rows
- Review whether the assigned sizes match the writing task expectations for each unit
- PH-5 (U21 homework pack at L7529) — decide: composite type or sequence of standard types

---

## Priority 3 — Build Pipeline Setup

### 10. Write and test the CLI build command

- Equivalent to the advanced build command:

  ```
  C:\Dev\Code\textmaker\textmaker.cmd markdown-to-docx
    --input int\md\working\aw-int-all.md
    --reference int\md\working\aw-int-styleref.docx
    --lua-filter ..\textmaker\scripts\style_bridge.lua
    --output int\md\working\aw-int-all_MMDD.docx
    --no-pagebreak-filter
    --apply-semantic-labels
  ```

- Run from `book_administrative-writing\`

### 11. Verify unit heading format for title table insertion

- `replace_unit_headings_with_title_tables()` matches headings via `UNIT_HEADING_RE`
- Confirm the intermediate book's unit headings match the expected pattern
- Adjust regex or heading text if needed

### 12. Run post-build validation

- Run `validate_docx_against_reference.py` after first build
- Check: all used styles present in reference DOCX, no extra style definitions, no fallback styles

---

## Priority 4 — Reference DOCX Decisions

### 13. Decide: shared or separate reference DOCX

- **Shared**: use the same `aw-adv-styleref.docx` for both books — simpler, single source of truth
- **Separate**: `aw-int-styleref.docx` — allows different color schemes, font sizes, or style variants for the intermediate level
- Recommendation: start with a copy of the advanced reference DOCX and diverge only if needed

### 14. Confirm AW Table styles apply correctly

- All 4 AW Table styles now have: 100% width, autofit, left-align, no hyphenation, cell margins 0.1/0.2 cm, first-row dark blue header
- Verify these are appropriate for the intermediate book's table types

---

## Status Tracking

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | YAML front matter | ☐ Pending | |
| 2 | Reference DOCX | ☐ Pending | |
| 3 | Working folder | ☐ Pending | |
| 4 | Icon assets | ☐ Pending | |
| 5 | Fenced div markup | ☐ Pending | Largest task |
| 6 | Checklist conversion | ☐ Pending | After #5 |
| 7 | Alpha list audit | ☐ Pending | |
| 8 | Div spacing fixes | ☐ Pending | After #5 |
| 9 | PH marker sizing review | ☐ Pending | |
| 10 | CLI build command | ☐ Pending | After #1–4 |
| 11 | Unit heading format check | ☐ Pending | |
| 12 | Post-build validation | ☐ Pending | After #10 |
| 13 | Shared vs separate styleref | ☐ Decision needed | |
| 14 | AW Table style review | ☐ Pending | After #13 |

## Requests from Dave

I think each step needs more specific details, such as

- the goal for each step
- issues that came up when working on the advanced text related to the step
- how to avoid those issues with the intermediate text.
- requirements that must be met to satisfy successful completion of the step

Treat each stage as its own project that needs to be satisfied before moving on.

If any stages can be run in parallel, identify the process order clearly and the gates that prevent it from moving forward.

In addition to the above, **both** books need **answers to each task** the student is asked to do. That is a large task that needs to be handled this week.
