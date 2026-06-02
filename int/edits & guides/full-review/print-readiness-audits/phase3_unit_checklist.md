# Phase 3 Unit Repair Checklist

Source: `aw-int_print_readiness_repair_plan_0530.md` Section 5, Phase 3

Use this checklist for each unit. Work through steps 1–17 in order. Record pass/fail notes per unit in a separate `phase3_unitN_repair_notes.md` file.

---

## Step 1 — Read Focus statements

- [ ] Focus statements use `By the end of this unit, I will be able to...` framing.
- [ ] Note: how many can-do statements? What skill does each map to?

## Step 2 — Read all activities without editing

- [ ] Read the full unit from Focus to end before marking anything.
- [ ] Note any immediate structural concerns.

## Step 3 — Write the teacher goal

- [ ] Write one sentence: what skill does this unit teach and how?
- [ ] Confirm: is this reflected in the Focus?

## Step 4 — Map activities to goal and learner action

- [ ] For each visible activity (A–H), name the learner action.
- [ ] Identify any activity that does not contribute to the unit goal.
- [ ] Flag any duplicate activities with the same function.

## Step 5 — Fix the visible heading order

- [ ] Confirm current H3 letter sequence from the heading audit.
- [ ] Target shell: `Focus → A Warm-Up → B Example Check → C Language → D Guided Practice → E Freer Practice → F Editing Practice → G Self-Check/Reflection/Review → H Transfer/Homework`.
  - Note: the Phase 2 unit shell plan Rule #3 ("keep first concept-primer `A` as structural A") is **superseded** by the 2026-06-01 book-wide warm-up standard. Do not use it.
- [ ] Duplicate `### A.` headings:
  - [ ] Keep `A. Warm-Up` (or equivalent opening learner activity) as the visible `### A.` — this is the book-wide standard.
  - [ ] Rehome concept-primer / definition / layout-explanation material by function: fold it into `B. Example Check` as a `:::learn` support block, or place it as a `:::learn` block at the start of A. before the comparison task begins. Do not preserve it as the visible `### A.`.
  - [ ] Do not preserve the first `A` mechanically if it is a concept primer rather than a genuine opening learner activity.
- [ ] F before E:
  - [ ] Move `F. Self-Check Before Freer Practice` after `E. Freer Practice`.
  - [ ] Rename as `F. Editing Practice` unless another F label is intentional.
- [ ] Duplicate `### F.` headings:
  - [ ] Confirm which F is the editing/practice section and which is reflection.
  - [ ] Merge `F. Reflection` into a combined `G. Self-Check and Reflection`.
- [ ] Duplicate `### H.` headings:
  - [ ] Merge `H. Transfer Extension` and `H. Homework` under one `H.` with homework as a subordinate label.
- [ ] Duplicate `### D.` or `### E.` headings (if present):
  - [ ] Convert extra D/E into subordinate div titles inside the activity.
- [ ] Result: single-letter visible sequence `ABCDEFGH` or documented exception.

## Step 6 — Repair activity information order

For each activity instruction, verify the order:

- [ ] Context or source material comes first.
- [ ] Student action comes second.
- [ ] Length, number, or output requirement comes third.
- [ ] Response space (placeholder) comes last.

Flag any activity where situation, source text, action, and output are out of this order.

## Step 7 — Repair instruction clarity and completeness

- [ ] Student knows exactly what to do.
- [ ] Student knows what source text, scenario, or previous activity to use.
- [ ] Expected length or number of items is stated where relevant.
- [ ] Vague references such as `the previous activity` are replaced with named references.
- [ ] Related instruction sentences are adjacent (not split across divs).
- [ ] No instruction restates the same task twice.

## Step 8 — Reorganize for logical information order

- [ ] Each activity keeps context, source, action, output, and response space together.
- [ ] No activity title or div title jumps directly to a list or placeholder with no explanatory prose.
- [ ] Check specifically: does a `### heading` or `div title` line appear with nothing after it before a list, box, or exercise begins?

## Step 9 — Remove advanced vocabulary and editor-facing wording

- [ ] Scan student-facing text for:
  - [ ] Technical terminology (e.g., `SVO-style`, `diagnostic baseline`, `calibrate`).
  - [ ] Idioms (e.g., `carry forward`, `standardise`, `surface the issue`).
  - [ ] Editor/teacher-facing planning language (e.g., `source-layer mismatch`, `pedagogical`, `realia`).
- [ ] Replace with plain intermediate-level English.

## Step 10 — Remove or relocate spoilers

- [ ] Identify any model, goal section, or sample answer placed immediately after the exercise it answers.
- [ ] Decision for each spoiler:
  - [ ] Keep before the task as a genuine model for a *different* prompt.
  - [ ] Move to the answer key.
  - [ ] Replace with a partial example.
  - [ ] Remove from the student book entirely.

## Step 11 — Check for missing prose after titles

- [ ] For every `### heading`, `#### heading`, or `div title` line: is there at least one sentence of prose, task instruction, or example context before the next exercise or placeholder?
- [ ] Flag any bare title-to-box or title-to-list jumps.

## Step 12 — Normalize list types

- [ ] Numbered lists are used only for ordered steps, ordered exercise items, or required sequences.
- [ ] Bullets are used for unordered features, options, or reminders.
- [ ] Checkboxes (`- [ ]`) appear only inside `:::edit` divs.
- [ ] Explanation-only bullet lists are converted to prose where bullets add no student action.
- [ ] List item punctuation: complete sentence/imperative items are capitalized and end with periods; fragment items completing a lead-in remain lowercase fragments without sentence periods.

## Step 13 — Repair div class choices and boundaries

- [ ] Each div class matches the activity function (see classification key in project-learning.md).
- [ ] No `:::write` is used for selection or observation tasks.
- [ ] No `:::notice` contains a production task.
- [ ] Div fences are balanced (equal opens and closes in the unit).
- [ ] No nested divs.
- [ ] Every student response placeholder sits inside the relevant activity div unless a production-pipeline exception is documented.
- [ ] No orphaned placeholders outside their div (except documented layout exceptions).
- [ ] No redundant placeholders that duplicate item-level boxes.

## Step 14 — Calibrate placeholder type and row count

For each placeholder in the unit:

- [ ] PH type reflects output type (PH-1 = sentence, PH-2 = paragraph, PH-3 = email/doc, PH-4/5 = longer).
- [ ] `rows=N` reflects expected student output using the working scale:
  - Phrase or label: `rows=1` max.
  - One sentence rewrite: `rows=2`.
  - Two to four sentence rewrites: separate `PH-1` boxes, `rows=2` each.
  - One 3–4 sentence message: `rows=6–8`.
  - One 5–6 sentence email/paragraph: `rows=8–10`.
  - Paired documents: separate labeled boxes.
- [ ] No unexplained outlier row counts (e.g., `rows=46`, `rows=22`).
- [ ] Every placeholder has a unique ID.
- [ ] Generic boxes after item-level boxes are removed unless the task explicitly requires a compiled final version.

## Step 15 — Proofread examples and model texts

- [ ] Spelling correct.
- [ ] Punctuation correct (email models use proper line breaks, not dense run-on paragraphs).
- [ ] Article and plural errors fixed.
- [ ] Consistent capitalization.
- [ ] Model emails show realistic formatting with a subject, greeting, body, and sign-off on separate lines.

## Step 16 — Update and validate the answer key

- [ ] Open `int/md/working/aw-int-answer-key.md` and locate the unit section.
- [ ] Update all changed activity labels.
- [ ] Update item numbers to match the repaired manuscript.
- [ ] Update model answers or guidance for revised tasks.
- [ ] Remove, merge, or reclassify answer-key entries for any deleted or reclassified activities.
- [ ] Mark open-ended writing tasks as model/guidance rather than fixed answers.

## Step 17 — Run local audits before moving to the next unit

Run these checks and confirm counts are as expected:

```bash
# Div balance in unit
grep -c "^::: " unit_section.txt
grep -c "^:::$" unit_section.txt
```

- [ ] Div open count = div close count.
- [ ] No duplicate placeholder IDs in unit.
- [ ] No generic `Write Here` or `Use this box` labels remain.
- [ ] No raw `->` arrow notation remains.
- [ ] No excessive blank-line runs (3+ consecutive blank lines).
- [ ] Visible heading sequence matches target shell.

---

## For Module Review Workshops (not ordinary A–H units)

- [ ] All visible headings use title-case.
- [ ] No repeated title rows where the `###` heading repeats the div title.
- [ ] Response placeholders are inside the relevant review, transfer, revision, or self-check div.
- [ ] Redundant strategy maps, planning boards, or notes that repeat the same review purpose are combined.
- [ ] The review task explicitly integrates the preceding units.
- [ ] Answer-key criteria exist for open-ended review tasks.
