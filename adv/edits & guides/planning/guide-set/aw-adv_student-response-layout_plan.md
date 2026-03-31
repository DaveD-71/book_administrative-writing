# Student Response Layout Plan
## *Administrative Writing, Advanced*

---

> **Purpose of this document**
> This file defines the placeholder strategy for the advanced student book after text sign-off and before final print layout.
>
> It does **not** reopen content design. It decides:
> - how many placeholder types are needed
> - where placeholders should be inserted
> - what short layout labels or instructions should accompany them

---

## 1. Layout Assumption

The placeholders are being planned for **handwritten student responses**, not keyboard entry.

Therefore the layout should assume:

- generous ruled spacing rather than tight worksheet lines
- visibly distinct response zones for drafting, rewriting, and homework
- page-level control so longer writing tasks do not collapse into small leftover gaps

For planning purposes, use **five placeholder types**.

---

## 2. Placeholder Types

| ID | Name | Typical use | Relative size |
|---|---|---|---|
| `PH-1` | Short Response | one to three sentences, short opening lines, short rewrite output, brief planning note | small |
| `PH-2` | Paragraph Response | one developed paragraph, short guided rewrite, short editing rewrite | medium-small |
| `PH-3` | Short Document | short email, notice, explanation, justification, summary, or guided document draft | medium |
| `PH-4` | Long Document | full freer-writing / homework document, usually the main student-writing task of the unit | large |
| `PH-5` | Multi-Part Pack | tasks with two or more labeled outputs, especially portfolio and capstone work | composite |

Working interpretation:

- `PH-1` should feel like a short ruled block, not a full page box.
- `PH-2` should support a compact handwritten paragraph.
- `PH-3` should support one complete short document draft.
- `PH-4` should be treated as a major writing area and may need most of a page or a full page depending on trim size.
- `PH-5` should be built as labeled sub-boxes, not as one undifferentiated large box.

---

## 3. Where Placeholders Belong

### 3.1 Insert placeholders in these recurring zones

| Location pattern in the live book | Placeholder rule |
|---|---|
| `D` Guided Writing tasks (`D1` to `D7`) | insert `PH-2` or `PH-3` depending on whether the student is rewriting one paragraph or drafting a full short document |
| `E1`, `E2`, `E3` Freer Writing tasks | insert `PH-4` |
| `E4` Multi-Part Portfolio tasks | insert `PH-5` |
| `G1`, `G2`, `G3` Editing tasks when a clean revised version is required | insert `PH-2` or `PH-3` |
| `H3` Homework Writing Task | insert `PH-4` |
| `H2` Real-World Task when the book expects a written in-book response rather than outside collection only | insert `PH-3` |

### 3.2 Do not use large shaped placeholders in these zones by default

| Location pattern | Layout treatment |
|---|---|
| `A`, `B`, `C` short analytic tasks | use ordinary answer lines, numbering space, or tables rather than document-style boxes |
| `F` peer review and self-edit checklists | no handwriting box beyond existing checklist space |
| `H1` extension tasks | no dedicated placeholder by default; these can remain notebook / outside-book tasks unless a later layout decision says otherwise |

---

## 4. Advanced-Specific Placement Decisions

### 4.1 Standard unit-level pattern

For most advanced units, the placeholder-bearing writing flow should be:

1. guided draft box in `D`
2. main production box in `E`
3. revision / clean-copy box in `G`
4. homework box in `H3`

This means the advanced book should be laid out as a **student-writing book**, not only a reading-and-prompt book.

### 4.2 Units with two guided-writing outputs

Where a unit contains two distinct `D` tasks, do **not** merge them into one box if the tasks have different purposes.

Examples:

- model rewrite plus scenario writing
- rewrite plus two-audience adaptation
- rewrite plus format conversion
- rewrite plus revision chain

Rule:

- if the second task is a short transformation, use a second `PH-1` or `PH-2`
- if the second task is a full short draft, use a second `PH-3`

### 4.3 Module 6 portfolio and capstone tasks

Units 21 to 23 contain the clearest need for `PH-5`.

Use labeled sub-boxes rather than one large box for:

- Unit 21 `E4`
  - Part A: Summary + Issues Identified
  - Part B: Actions Taken + Outstanding Questions
  - Part C: Next Steps + closing
- Unit 22 `E4`
  - Part A: planning note (`PH-1`, explicitly marked not submitted)
  - Part B: full administrative document (`PH-4`)
- Unit 23 `E4`
  - Part A: planning note (`PH-1`, not submitted)
  - Part B: capstone document (`PH-4`)

The same split logic should also be used when the student book carries the matching homework responses in these late units.

---

## 5. Additional Headings / Instructions Needed

Current prompts are strong enough for content, but the layout layer needs more explicit box labels so students know what belongs in each response area.

Use these standardized labels:

- `Draft Here`
- `Write Your Revised Version`
- `Homework Draft`
- `Planning Notes (Not Submitted)`
- `Document 1`
- `Document 2`
- `Document 3`
- `Clean Copy`

Use these short instruction patterns where needed:

- `Use this space for your first full draft.`
- `Write one complete version only.`
- `Revise the text above and write the full corrected version below.`
- `Keep the same facts, but change the tone and structure for the new reader.`
- `Write each part in its own box.`

For `PH-5`, every sub-box should be purpose-labeled. Do not rely on `Write here`.

---

## 6. Recommended Marker System For Later Pandoc Work

If placeholders are inserted into the Markdown later, use a simple stable marker system rather than ad hoc prose.

Recommended pattern:

- `{{PH-1: unit-task-label}}`
- `{{PH-2: unit-task-label}}`
- `{{PH-3: unit-task-label}}`
- `{{PH-4: unit-task-label}}`
- `{{PH-5: unit-task-label}}`

Examples:

- `{{PH-3: U04-D1-guided-rewrite}}`
- `{{PH-4: U12-E1-freer-write}}`
- `{{PH-5: U21-E4-portfolio}}`

This keeps the Markdown source layout-neutral while allowing later Pandoc filters or post-processing scripts to replace the markers with final shapes or textboxes.

---

## 7. Stage Decision

Add a late-stage project task for:

- student-response placeholder planning
- placeholder insertion into the final student-book source
- page-layout preparation for print

This stage should happen **after text sign-off / full review** and **before final print production**.

---

*Document status: planning decision for the advanced student-book placeholder and page-layout stage.*
