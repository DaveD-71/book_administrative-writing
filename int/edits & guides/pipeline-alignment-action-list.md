# Intermediate Textbook — Pipeline Alignment Plan

Generated: 2026-05-19 (expanded from 2026-05-18 draft)
Source experience: Advanced textbook pipeline, sessions 2–11 (2026-05-09 to 2026-05-19)
Target file: `int/md/final/aw-int-all.md` (8,540 lines, 23 units, 0 divs)

---

## How to use this plan

Each stage is a self-contained project with its own goal, advanced-pipeline lessons, avoidance strategy, and a hard **completion gate** — the measurable check that must pass before the next stage begins. Process order is strict unless stages are marked as parallel tracks.

> **Symbol key**
> ☐ Pending  ✓ Done  ⚠ Blocked  → Gate passed

---

## Stage 0 — Setup (Parallel to Stage 1)

Stages 0A, 0B, and 0C can all be prepared concurrently. None depend on each other. They must all be complete before Stage 2 can start.

### 0A — Create working folder

**Goal:** Establish a stable, isolated working location for the intermediate pipeline, mirroring the structure of `adv/md/working/`.

**Lessons from advanced pipeline:**
- The final output file, reference DOCX, icon assets, and source markdown must be siblings in the same folder for the postprocessor's `_resolve_div_tag_icon()` to locate PNG files correctly.
- Working outputs were initially placed in a different folder (`adv/docx/`) before being moved — this caused broken path arguments and wasted builds.

**Avoidance strategy:**
- Create `int/md/working/` before touching anything else.
- Never run a build with source and reference in separate folders.

**Steps:**
1. Create `int/md/working/`
2. Copy `int/md/final/aw-int-all.md` → `int/md/working/aw-int-all.md` (working copy; `final/` is read-only source of truth)

**Completion gate:**
- `int/md/working/` exists and contains `aw-int-all.md`
- `int/md/final/aw-int-all.md` is unmodified

---

### 0B — Reference DOCX decision and setup

**Goal:** Place a reference DOCX in the working folder that contains all styles required by the intermediate pipeline. Decide whether to share or fork the advanced reference.

**Lessons from advanced pipeline:**
- The reference DOCX is the single source of truth for all style definitions. The build pipeline must never create or redefine styles.
- Three-location color synchronisation rule: `DivLabel*` styles must keep `w:rPr/w:color`, `w14:srgbClr`, and linked character style color in sync — these go out of sync silently if styles are manually edited in Word.
- `autoRedefine` on DivLabel styles caused silent style corruption; it must not be present.
- Styles renamed or absent in the reference DOCX cause hard failures at post-build validation — easier to start clean than patch.
- `DivTag` must be a **character** style (not paragraph); if defined as paragraph the `w:rStyle` icon references are silently ignored.
- `AW Table Header` and `AW Table Body` paragraph styles are required for table cell formatting to override Word's table-style `rPr`.

**Avoidance strategy:**
- Start with a direct copy of `aw-adv-styleref.docx` renamed to `aw-int-styleref.docx` in `int/md/working/`.
- Run `audit_docx_styles.py` on the copy immediately to confirm all required styles are present and colours are consistent.
- Do not edit the DOCX copy in Word unless a specific style change is confirmed necessary — Word silently adds styles and modifies inheritance on save.

**Decision: shared vs separate:**
- **Recommendation: use a copy.** Starting from a copy means the intermediate book can diverge in colour scheme or style variants later without touching the advanced reference. If both books prove identical in styling, they can be re-consolidated at that point.
- **If truly shared:** symlinks don't work with the Pandoc `--reference-doc` flag path; use `--reference` pointing to the single `adv/md/working/aw-adv-styleref.docx`. Any style change then affects both books simultaneously.

**Steps:**
1. Copy `adv/md/working/aw-adv-styleref.docx` → `int/md/working/aw-int-styleref.docx`
2. Run `python scripts/audit_docx_styles.py --reference int/md/working/aw-int-styleref.docx` and confirm no colour-mismatch warnings

**Completion gate:**
- `int/md/working/aw-int-styleref.docx` exists
- `audit_docx_styles.py` reports zero colour-mismatch errors
- All required styles are present: `Div Label *` (×10 minimum), `DivTag` (character), `AW Table Header`, `AW Table Body`, `Checklist`, `Body Text`, `ResponsePlaceholder`

---

### 0C — Copy icon assets

**Goal:** Make PNG icon assets available in `int/md/working/` so the postprocessor can insert inline tag icons for each div class.

**Lessons from advanced pipeline:**
- Icon assets must be in a folder named `div-tags-icons-2_assets` immediately sibling to the reference DOCX.
- All icon PNGs must be tight-cropped to content bounds + 1px padding. Uncropped PNGs (4px white margin) misalign the icon against label text.
- Two sets exist: `tag_filled_*` and `tag_outline_*`. The `--tag-style filled|outline` CLI flag selects between them. Both sets must be present.
- Missing icon PNG for a given class causes that div's label to be inserted without an icon (silent skip — not an error).

**Avoidance strategy:**
- Copy the entire cropped `div-tags-icons-2_assets/` folder from the advanced working folder — do not copy from an older source that may have uncropped originals.
- After copying, verify both `tag_filled_*` and `tag_outline_*` sets are present for all 9 div classes.

**Steps:**
1. Copy `adv/md/working/div-tags-icons-2_assets/` → `int/md/working/div-tags-icons-2_assets/`
2. Verify both icon sets are present for: `learn`, `language`, `structure`, `notice`, `write`, `rewrite`, `revise`, `edit`, `example`

**Completion gate:**
- `int/md/working/div-tags-icons-2_assets/` contains both `tag_filled_*` and `tag_outline_*` PNGs for all 9 div classes (minimum 18 PNGs)

---

## Stage 1 — YAML Front Matter

**Depends on:** Stage 0A complete

**Goal:** Add YAML front matter to the working source file so `style_bridge.lua` can map fenced div classes to Word paragraph styles. Without this, Pandoc produces no Div Label styles and the entire semantic formatting layer is skipped.

**Lessons from advanced pipeline:**
- Front matter must use exact `style_map` key-value pairs matching the reference DOCX paragraph style names. A single spelling mismatch silently drops that div class to an unstyled paragraph.
- `remove_horizontal_rules: true` prevents Pandoc from emitting `---` as horizontal rule XML into the DOCX.
- `preserve_div_line_breaks: true` prevents Pandoc from collapsing intentional line breaks inside divs.
- `--no-pagebreak-filter` CLI flag is required at build time — the advanced Lua filter suppresses standalone `---` separators while Textmaker's built-in `pagebreak.lua` would incorrectly convert them to page breaks.

**Avoidance strategy:**
- Copy the YAML block verbatim from `aw-adv-all_0516.md`. Do not retype; transcription errors are invisible until a build is run.

**Front matter to add** (insert at line 1 of `int/md/working/aw-int-all.md`):

```yaml
---
style_bridge:
  remove_horizontal_rules: true
  preserve_div_line_breaks: true
style_map:
  learn: "Div Label Learn"
  language: "Div Label Language"
  structure: "Div Label Structure"
  notice: "Div Label Notice"
  write: "Div Label Write"
  rewrite: "Div Label Rewrite"
  revise: "Div Label Revise"
  edit: "Div Label Edit"
  example: "Div Label Example"
  example-good: "Div Label Example Good"
  example-bad: "Div Label Example Bad"
---
```

**Completion gate:**
- File begins with `---` on line 1 and the YAML block closes before the first `#` heading
- All 11 `style_map` entries are present and exactly match the style names in `aw-int-styleref.docx`
- Confirmed with: `python -c "import yaml; d=open('int/md/working/aw-int-all.md').read(); print(yaml.safe_load(d.split('---')[1]))"`

---

## Stage 2 — Fenced Div Markup  *(largest single task)*

**Depends on:** Stage 0A complete (working file must exist); Stage 1 not strictly required but should be in place to avoid double-editing

**Goal:** Apply `:::class` / `:::` fenced div markup throughout all 23 units of `aw-int-all.md` to wrap content in the correct semantic category. The current file has zero fences. This is the primary content-authoring stage and directly determines the quality of the styled output.

---

### Classification framework

The correct class is determined by **what the learner does** in the block — not by which section (A–H) it sits in. The A–H section heading provides orientation but does not determine the class; a single `### C. Language Focus` section typically contains `learn`, `language`, `rewrite`, and `notice` divs depending on content.

| Learner action | → class |
|---|---|
| Reads teaching input, principle, explanation | `learn` |
| Reads a reference list of language forms/patterns | `language` |
| Produces original text from a scenario | `write` |
| Transforms or rewrites given text | `rewrite` |
| Improves their own previously drafted text | `revise` |
| Observes, identifies, compares, classifies given text | `notice` |
| Orders or structures given content into a framework | `structure` |
| Applies a checklist or corrects errors in given text | `edit` |
| Reads model or example text | `example` / `example-good` / `example-bad` |

**`language` is the most error-prone class.** It is correct only when the div's primary content is a reference list of language forms — connectors, phrases, sentence patterns — with no task attached. It is wrong when the block contains teaching explanation (`learn`), a sentence-transformation task (`rewrite`), a phrase-sorting task (`notice`), or original sentence production (`write`). The advanced audit found 21 out of 54 `language` divs were misclassified this way.

**`edit` vs `rewrite`:** `edit` is correct only for self-editing checklists and error-identification tasks. Tasks whose primary instruction is "rewrite these sentences" are `rewrite` even if they sit in a `### G. Editing` section.

**`notice` vs `learn`:** `notice` is for observation/analysis tasks on given text. Divs that contain a teaching reference table or explanatory principle with no learner task are `learn`, even if positioned in a noticing section.

**`revise` vs `rewrite`:** `revise` is for tasks where the learner returns to and improves their own previously written text. `rewrite` is for transforming someone else's given text.

**`write` vs `structure`:** `write` is for original production from a scenario. If the learner is filling in a given structural template, it is `structure`.

---

### Div label text

The first line inside the fence is the visible label in the DOCX output. It comes from:
- An existing `####` sub-heading on the block → use its text (remove the `####` prefix)
- A bold label (`**Why This Works**`) → use its text (remove the `**` markers)
- If no heading or label exists, write a short noun-phrase that describes the block

---

### Lessons from advanced pipeline

1. **Pandoc spacing rule — blank line before `:::`:** A `:::class` open fence must be preceded by a blank line when the preceding content line is non-empty. Violation causes Pandoc to render the fence as literal text. The systematic danger pattern: a bold label line (`**Input N — ...**`) immediately followed by `:::class` with no blank line. This burned multiple builds before being caught.

2. **Blank line after `:::` before a list:** A list (`-`, `1.`, `A.`) must not immediately follow a `:::class` open fence without a blank line gap. Pandoc does not enter div context cleanly when a list item is the first child.

3. **No nested divs:** Pandoc does not support nested fenced divs — an inner `:::` close terminates the outer div. Do not place a `:::class` div inside another `:::class` div. Advanced book had 233 substantive nested divs that required manual resolution.

4. **Misplaced setup instructions:** Two `rewrite` divs in the advanced book had their setup instruction line (plus an `example` sub-div) placed inside the `:::rewrite` fence instead of before it. Setup/context lines belong **outside and above** the div; the div should contain only the student task content.

5. **Thin nested labels:** Several advanced divs had title-only sub-labels (`learn "Functions"`, `language "Learn — Sentences"`) that added no student learning value and caused nesting errors. These were removed. Apply the same judgement to the intermediate book.

6. **Extra blank lines inside divs:** Advanced source had ~186 blank lines inserted immediately after `:::` open fences. These create empty paragraphs in the DOCX output. Strip them.

**Avoidance strategy:**
- Work unit by unit (23 units). Commit after each unit or small batch.
- After each unit, run a balance check: count of `:::` open fences == count of close-only `:::` lines.
- Check for blank-line violations after every unit.
- Explicitly forbid div nesting: use bold inline labels for sub-category distinctions instead.
- Place setup instructions (e.g. "Read the following and then...") outside the div, above it.
- Classify by learner action, not section letter. When uncertain, ask: what does the learner actually do with this content?

**Div balance check command (PowerShell):**
```powershell
$lines = Get-Content int/md/working/aw-int-all.md
$opens = ($lines | Where-Object { $_ -match '^:::[\w-]+' }).Count
$closes = ($lines | Where-Object { $_ -match '^:::\s*$' }).Count
"Opens: $opens  Closes: $closes  Match: $($opens -eq $closes)"
```

**Spacing violation check command (PowerShell):**
```powershell
$lines = Get-Content int/md/working/aw-int-all.md
for ($i = 1; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^:::[\w-]+' -and $lines[$i-1] -ne '') {
        "Line $($i+1): missing blank line before fence — prev: '$($lines[$i-1])'"
    }
}
```

**Completion gate:**
- Open fence count equals close fence count (balance check passes)
- Zero spacing violations (blank-line-before-fence check passes)
- Zero blank lines immediately after `:::` open fences
- Zero nested divs (no `:::class` line inside another open/close pair)
- Human review: each unit's div classifications make pedagogical sense (correct class for content type)

---

## Stage 3 — Checklist Conversion

**Depends on:** Stage 2 complete (edit divs must be in place)

**Goal:** Convert plain `-` bullet list items inside `edit` div blocks to `- [ ]` checklist syntax so the postprocessor applies the `Checklist` paragraph style.

**Lessons from advanced pipeline:**
- The advanced book had 151 checklist items converted across its edit divs. All were plain `-` bullets.
- The `apply_checklist_style()` postprocessor function identifies checklist items by the `Checklist` paragraph style — this is applied only when the source uses `- [ ]` syntax and the style exists in the reference DOCX.
- Converting bullets to checklists **inside non-edit divs** or outside divs entirely creates unwanted checklist styling on regular list items.

**Avoidance strategy:**
- Convert only bullet items that are directly inside an `:::edit` div block.
- Do not convert bullets inside `write`, `revise`, `rewrite`, `learn`, or `notice` divs.
- After conversion, a quick grep confirms no `- [ ]` items appear outside of `edit` div blocks.

**Completion gate:**
- All bullet list items inside `:::edit` ... `:::` blocks use `- [ ]` syntax
- Zero `- [ ]` items appear outside `:::edit` blocks
- Count reported: N checklist items converted across M edit divs

---

## Stage 4 — Alphabetic Option List Audit

**Depends on:** Stage 0A complete (independent of Stage 2–3; can run in parallel with them)

**Goal:** Identify which of the ~103 `A.`, `B.`, `C.` list markers in `aw-int-all.md` are genuine alphabetic option lists (multiple-choice questions, comparison options) and which are section labels, answer keys, or decorative use of capital letters.

**Lessons from advanced pipeline:**
- The pipeline strips literal `A.` markers and applies `List Number 3` style in the postprocessor. If a non-list occurrence is incorrectly tagged, the leading letter disappears from the published text.
- Advanced pipeline found false positives in: appendix section labels, answer keys formatted as `A. Correct`, and some table cells with `A.`/`B.` as column headers.
- The postprocessor's alpha-list logic keys on Pandoc's `ordered_list` with `UpperAlpha` numbering style — this is correct only when the source uses `A.` as the start of a proper ordered list block.

**Avoidance strategy:**
- Use grep to list all lines matching `/^[A-D]\./` and review in context.
- Flag any that are: part of answer key sections, headers/labels, or table content.
- For confirmed genuine option lists, ensure the markdown uses proper Pandoc ordered list syntax (item starts at column 0, consistent indentation for continuation).

**Completion gate:**
- All genuine `A./B./C.` option lists use standard ordered-list Pandoc syntax
- All false positives (answer keys, labels, table content) are documented and confirmed as non-list
- No `A.` markers exist that would be stripped by the postprocessor incorrectly

---

## Stage 5 — PH Marker Review

**Depends on:** Stage 0A complete (independent; can run in parallel with Stage 2–4)

**Goal:** Review all 163 `{{PH-N}}` placeholder markers to confirm the assigned size tier matches the expected writing task for each location.

**Current size scheme:** PH-1=2 rows, PH-2=5 rows (assumed), PH-3=9 rows, PH-4=15 rows, PH-5=22 rows

**Lessons from advanced pipeline:**
- Placeholder sizes were revised several times as builds revealed that the visual space was too tight or too generous for specific tasks.
- PH-5 at U21 (L7529 in the final file) is a composite homework pack — it may need a sequence of standard placeholders rather than a single large PH-5.
- `SPACER_HEIGHT` was increased to `'280'` (14pt) for visual separation between consecutive placeholder tables — confirm this looks right in the first intermediate build.

**Avoidance strategy:**
- Review each unit's writing tasks (especially `write` and `rewrite` divs after Stage 2) and cross-check assigned PH tier against task scope.
- Prepare a revised PH-size table before first build rather than re-building multiple times.

**Completion gate:**
- All 163 PH markers have confirmed size assignments documented in a reference table
- Any composite-type PHs (like U21) are documented with a decision (sequence vs. single large block)

---

## Stage 6 — First Build

**Depends on:** Stages 0A, 0B, 0C, 1, 2, 3 all complete (Stage 4 and 5 highly recommended but not strictly blocking)

**Goal:** Run the Textmaker CLI pipeline to produce the first DOCX output for the intermediate book.

**Build command** (run from `book_administrative-writing\`):
```
textmaker.cmd markdown-to-docx ^
  --input int\md\working\aw-int-all.md ^
  --reference int\md\working\aw-int-styleref.docx ^
  --lua-filter ..\textmaker\scripts\style_bridge.lua ^
  --output int\md\working\aw-int-all_MMDD.docx ^
  --no-pagebreak-filter ^
  --apply-semantic-labels
```
Replace `MMDD` with today's date (e.g. `0519`).

**Lessons from advanced pipeline:**
- `--no-pagebreak-filter` is required; omitting it converts `---` separators to page breaks.
- `--lua-filter` must point to the absolute or relative-to-cwd path of `style_bridge.lua`.
- Output path must not contain shell metacharacters (`&`, `(`, `)`, `%`). Windows `cmd.exe` path handling requires either quoting or a temp copy to a safe path.
- Pandoc fallback styles (`Compact`, `VerbatimChar`) appear in output when the source uses code spans or compact list spacing — these must be treated as cleanup targets in the next build cycle.
- `replace_unit_headings_with_title_tables()` runs whenever `--reference-doc` is supplied. Unit heading regex (`UNIT_HEADING_RE`) must match the intermediate book's heading text format. Check `unit NN` lowercase vs title case.

**Post-build validation command:**
```
python ..\textmaker\scripts\validate_docx_against_reference.py ^
  --docx int\md\working\aw-int-all_MMDD.docx ^
  --reference int\md\working\aw-int-styleref.docx
```

**Completion gate:**
- Build completes with zero Python exceptions
- `validate_docx_against_reference.py` reports zero missing-style errors
- DOCX opens in Word without repair prompts
- Visual spot check: all 23 units have title tables, at least one div label per unit shows the icon+label layout, table styles are correct in at least one table

---

## Stage 7 — Post-Build Fixes

**Depends on:** Stage 6 complete

**Goal:** Identify and fix all formatting defects found in the Stage 6 build output, then rebuild to a clean verified DOCX.

**Expected defect categories from advanced pipeline experience:**

| Defect | Cause | Fix |
|--------|-------|-----|
| Literal `:::` text in output | Missing blank line before open fence | Add blank line in source markdown |
| Empty paragraph inside div | Blank line immediately after `:::` open | Remove blank line in source |
| Missing icon on label line | PNG not found for that class | Check assets folder; verify file naming |
| `Compact` or `VerbatimChar` styles in output | Pandoc fallback for code or compact lists | Map to approved style in postprocessor |
| Wrong PH size | PH tier mismatch | Update `{{PH-N}}` tier in source or PH size table |
| Unit heading not replaced by title table | Regex mismatch | Check `UNIT_HEADING_RE` against actual heading text |
| Checklist items not styled | `- [ ]` outside edit div, or `Checklist` style missing | Fix source or add style to reference DOCX |
| Alpha list label remaining in text | Non-list `A.` marker encountered | Review Stage 4 audit results |
| Section break on wrong page size | `sectPr` missing `pgSz`/`pgMar` copy | Already fixed in postprocessor — verify it was not regressed |

**Completion gate:**
- Rebuild passes Stage 6 completion gate
- Zero known defect categories remain in rebuilt DOCX
- PDF generated from final DOCX (using `textmaker.cmd docx-to-pdf`) and visually confirmed

---

## Stage 8 — PDF Output  *(parallel with Stage 7)*

**Depends on:** Stage 6 complete

**Goal:** Convert the verified DOCX to PDF using Word COM via `docx-to-pdf`.

**Command:**
```
textmaker.cmd docx-to-pdf ^
  --input int\md\working\aw-int-all_MMDD.docx ^
  --output int\md\working\aw-int-all_MMDD.pdf
```

**Lessons from advanced pipeline:**
- `docx2pdf` uses Word COM and requires Word to be installed and licensed on the machine.
- Output PDF path must be writable — if the path contains OneDrive-synced folders, a sync lock can cause a COM error. Use a local path.
- The PDF is a final verification artifact — visual pagination, font embedding, and colour rendering should be checked against the DOCX.

**Completion gate:**
- PDF file exists and is non-zero bytes
- First and last page render correctly in a PDF viewer
- Fonts are embedded (check with Acrobat or similar: File > Properties > Fonts)

---

## Parallel Track — Answer Keys  *(both books, this week)*

**Independent of all other stages; can begin immediately**

**Goal:** Write complete answer keys for all student tasks in both the Intermediate and Advanced books. This is a separate content-authoring task that does not block the pipeline stages above and can proceed at any time.

**Scope:**
- Advanced book: all tasks in `adv/md/working/aw-adv-all_0516.md` — `write`, `rewrite`, `revise`, `edit`, and `example` task prompts
- Intermediate book: all tasks in `int/md/final/aw-int-all.md` — same div categories

**Suggested format:**
- Separate Markdown file per book: `adv/md/working/aw-adv-answer-key.md` and `int/md/final/aw-int-answer-key.md`
- Each entry: task heading from source → model answer paragraph(s)
- Optionally: second answer demonstrating a common error for discussion

**Gate (this week):**
- All student task prompts have at least one model answer
- Both answer key files committed to git

---

## Process Order Summary

```
[0A] Working folder ──────────────────────────────┐
[0B] Reference DOCX ──────────────────────────────┤
[0C] Icon assets  ────────────────────────────────┤ All 0x done → Stage 1
                                                  │
[Stage 1] YAML front matter ──────────────────────┤
                                                  │
[Stage 2] Div markup ─────────────────────────────┤ Stage 2 done → Stage 3
                                                  │
[Stage 3] Checklist conversion ───────────────────┤ Stages 0–3 done → Stage 6 (first build)
[Stage 4] Alpha list audit ─── (parallel to 2–3) ─┤
[Stage 5] PH marker review ─── (parallel to 2–5) ─┤
                                                  │
[Stage 6] First build ────────────────────────────┤ Stage 6 done → Stage 7 + 8
                                                  │
[Stage 7] Post-build fixes ───────────────────────┤ Final DOCX
[Stage 8] PDF output ─────────────────────────────┘ Final PDF

[Answer Keys] ────── Parallel track, any time, this week
```

---

## Status Tracking

| Stage | Task | Status | Gate |
|-------|------|--------|------|
| 0A | Working folder created | ☐ Pending | `int/md/working/aw-int-all.md` exists |
| 0B | Reference DOCX in place + audited | ☐ Pending | `audit_docx_styles.py` passes |
| 0C | Icon assets copied | ☐ Pending | 18+ PNGs in assets folder |
| 1 | YAML front matter added | ☐ Pending | YAML parses, 11 style_map entries |
| 2 | Fenced div markup complete | ☐ Pending | Balance check passes, spacing clean |
| 3 | Checklist conversion done | ☐ Pending | All edit-div bullets → `- [ ]` |
| 4 | Alpha list audit done | ☐ Pending | Confirmed list vs. non-list items |
| 5 | PH marker review done | ☐ Pending | Size assignments documented |
| 6 | First build completes | ☐ Pending | Validation passes, opens in Word |
| 7 | Post-build fixes applied | ☐ Pending | Zero known defects in rebuild |
| 8 | PDF generated | ☐ Pending | PDF renders correctly |
| AK-adv | Advanced answer key | ☐ Pending | All tasks answered, committed |
| AK-int | Intermediate answer key | ☐ Pending | All tasks answered, committed |
