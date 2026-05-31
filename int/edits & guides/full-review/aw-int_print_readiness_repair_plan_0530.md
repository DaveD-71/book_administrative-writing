# INT Print-Readiness Repair Plan
## Administrative Writing, Intermediate

**Date:** 2026-05-30
**Stage:** reopened editorial / print-readiness repair before final production
**Primary source for this repair:** `int/md/working/aw-int-all_0519.md`
**Reference source set:** `int/md/final/modules/aw-int_mod1.md` to `aw-int_mod6.md`, `int/md/final/aw-int-all.md`, and the current guide-set documents.

---

## 1. Why This Plan Exists

The current working manuscript is not ready for print even though earlier control documents marked the intermediate book as stable. A teacher-facing review of `int/md/working/aw-int-all_0519.md`, the recent manual-edit diff, and the current planning/memory layer shows that the remaining problem is not one small formatting defect. It is a combined **pedagogical structure + learner instruction + Markdown production** problem.

The repair must therefore be implemented as a controlled editorial pass, not as another broad regex cleanup or one-off style conversion.

This plan is written so that Codex, another LLM, or a human editor can implement the work without reinterpreting the project from scratch.

---

## 2. Current Evidence Snapshot

### 2.1 Source-of-truth conflict

The project guide still says the live source scope is the six canonical module files plus the intro, with `int/md/final/aw-int-all.md` reference-only. However, the user's current working target is `int/md/working/aw-int-all_0519.md`, and the latest manual edits were made in that combined working file. For this repair, treat `aw-int-all_0519.md` as the immediate active editing surface until the user explicitly changes that decision.

Operational rule:

1. Edit `int/md/working/aw-int-all_0519.md` first.
2. Do not overwrite it from module sources during the repair.
3. After print-readiness sign-off, back-port or regenerate the canonical module files only through a documented reconciliation step.

### 2.2 Recent manual edits are a useful style signal, not a representative sample

The latest manuscript commit made large manual changes to the first few units. Those units are **not representative of the entire book** because the user's manual cleanup has already changed their instruction style, placeholder spacing, and activity presentation. Do not infer whole-book quality from Units 1-4, and do not implement a repair that only touches those units.

Those edits still show useful preferences:

- cleaner, less decorated examples
- fewer redundant response prompts
- more explicit row sizing on placeholders
- less unnecessary bolding inside sentence examples
- more compact explanatory prose

However, the same diff also introduced or preserved problems that should **not** be copied blindly:

- numbered exercise items were sometimes removed completely, making individual tasks harder to reference
- several original sentences lost labels such as `Original:` or `Clear:`
- multiple blank-line runs appeared between prompts and placeholders
- some response spaces now sit outside their activity divs
- section order still places `F. Self-Check` before `E. Freer Practice` in many units

Use the manual edits as a signal about desired simplification, but reapply them through a consistent teacher-facing standard after checking later, less-edited units directly. The implementation standard must be derived from a whole-book audit, not from the manually edited opening units alone.

### 2.3 Confirmed structural defects in the working manuscript

A heading audit of `int/md/working/aw-int-all_0519.md` found:

- all 23 units exist
- no unit currently follows a clean `A B C D E F G H` sequence at the visible `###` layer
- Units 1-18 have duplicate visible section letters, usually `F` and `H`, and many also have duplicate `A`, `D`, or `E`
- Units 19-23 still contain lettered `####` subsections that should be normalized or intentionally treated as subordinate labels
- Unit 23 has `A B C F E D G H`, which is visibly misordered
- A later audit found the inverse failure in `int/md/working/aw-int-all_0519.md`: Units 3, 4, and 8-18 have concept-primer material demoted to unlettered `####` headings before the surviving `### A. Warm-Up`. These likely came from a duplicate-heading cleanup that kept the later `A. Warm-Up` instead of preserving the first intended `### A.` structural section.

These issues are severe because students, teachers, and answer-key writers need stable activity references.

### 2.4 Confirmed production / Markdown defects

A lightweight structural scan found:

- one more div opener than closer in the manuscript
- many three-or-more blank-line runs around placeholders and headings
- numerous generic `Write Here` labels, often immediately following already clear task instructions
- `->` arrow notation used inside visible prompt labels, sometimes without spacing
- inconsistent heading capitalization in module review workshops, especially headings beginning with lowercase `module`
- placeholder row values that include outliers such as `rows=22` and `rows=46`, which need verification against print layout and task demand

### 2.5 Confirmed pedagogical defects

Teacher review of Units 1, 2, 5, and 19 shows recurring issues:

- task instructions often ask students to write, then immediately restate the same instruction as `Write Here` or `Use this box...`
- activities sometimes ask learners to identify or notice a feature and then supply the answer too early
- examples and mini-models are sometimes inside the same div as the writing instruction, reducing the amount of independent thinking required
- response boxes are sometimes outside the instructional div, which weakens the activity boundary and causes formatting ambiguity
- productive tasks often fail to identify exactly which previous activity, scenario, or model text students should use
- paragraph and email examples are sometimes displayed as dense single paragraphs instead of readable workplace text blocks

### 2.6 Required whole-book sampling correction

Because the first few units have already been manually edited, they must be treated as a **pilot/style-reference area**, not as the diagnostic baseline. Before any implementation pass begins, the editor must review a representative sample from all modules and all major activity families.

Minimum sample before editing beyond the pilot:

| Area | Units to inspect | Why this area matters |
|---|---|---|
| Opening foundation units | Units 1-3 | shows the user's manual-edit direction, but not the untouched baseline |
| Routine email units | Units 4-7 | repeated email prompts, paired email tasks, tone and request instructions |
| Internal document units | Units 8-11 | procedures, notices, problem explanations, summaries, and sequence logic |
| External / explanation units | Units 12-15 | inquiry and response tasks with audience and detail-control problems |
| Editing module | Units 16-18 | accuracy / clarity / tone revision tasks, arrow notation, and rewrite-box sizing |
| Capstone module | Units 19-23 | integrated multi-document tasks, subordinate `#### A-H` headings, portfolio structure |
| Review workshops | all six module review workshops | lowercase headings, repeated title rows, and cumulative-task layout |

At least one unit from each row must be read in full before writing or applying a reusable standard. The final repair still must cover **all 23 units and all 6 module review workshops**. The first representative-reading note for this correction is `int/edits & guides/full-review/print-readiness-audits/representative_reading_notes_0531.md`.

### 2.7 Original request coverage check

The user's original problem list is the acceptance checklist for this plan. Do not treat the plan as complete unless each item below is handled in the repair workflow, the unit checklist, or the Definition of Done.

| Original issue from request | Where this plan addresses it | Required repair action |
|---|---|---|
| Hard-to-understand instructions | Sections 4.3, 4.4, 6.3, and 6.4 | Rewrite student-facing instructions in short, direct intermediate-level English. |
| Poorly organized instructions with related sentences separated | Sections 4.3, Phase 3 steps 6-7, 6.3, and Definition of Done item 6 | Move context, source text, action, output requirement, and response-space information into a logical order. |
| Insufficient instructions or unclear references to earlier work | Sections 4.3 and 6.3 | Name the exact source text, scenario, prior activity, or previous answer students must use. |
| Too much information, including answers or models immediately after questions | Sections 3.3, 3.4, 4.3, Phase 3 step 9, 6.3, and Definition of Done item 8 | Separate input, practice, and answer space; use a different model, a partial model, or teacher material when the model would answer the task. |
| Weak connection between activities and unit/module goals | Sections 3.1, 4.1, Phase 3 steps 1-4, and 6.1-6.2 | Map every activity to the unit Focus statements and to one learner action before rewriting. |
| Misordered activities, generally needing A-H order | Sections 2.3, 4.1, Phase 3 step 5, 6.2, 6.5, and Definition of Done items 1-2 | Normalize visible activity headings and document any capstone exception. |
| First structural `A` heading accidentally demoted | Sections 2.3, 4.1, Phase 1, Phase 2, and Definition of Done items 1-2 | Preserve the first intended `### A.` structural heading in each unit; do not treat a later warm-up heading as the only `A` when an earlier concept primer was originally the `A` section. |
| Incorrect list type or unnecessary list formatting | Sections 4.5, Phase 3 step 11, and 6.5 | Use numbered lists for ordered work, bullets for unordered options, checkboxes only for checks, and prose when no list is needed. |
| Excessive list usage | Sections 4.5 and 6.5 | Convert explanation-only lists into short prose when list formatting adds clutter without helping the task. |
| Writing examples lack appropriate paragraph structure | Sections 2.5, 4.9, 6.5, and Definition of Done item 10 | Format model emails, notes, paragraphs, and reports as readable workplace text blocks. |
| Incorrect div class choice and application | Sections 4.6, Phase 3 step 12, 6.5, and Definition of Done item 3 | Match each fenced div class to the activity function and keep activity boundaries clear. |
| Spelling, grammar, and punctuation errors | Sections 4.9, Phase 3 step 14, and Definition of Done item 11 | Proofread instructional prose and models as core content, not as a cosmetic final pass. |
| Incorrect student response placeholder row count | Sections 2.4, 4.7, Phase 3 step 13, 6.6, and Definition of Done item 4 | Match `rows=N` to the expected student output and flag outliers for layout review. |
| Redundant student response placeholders | Sections 2.4, 4.7, 6.6, and Definition of Done item 4 | Remove generic or duplicate boxes unless the activity explicitly needs a separate final version. |
| Excessive redundant titles | Sections 4.2 and 6.5 | Reduce stacked near-synonym titles to one clear activity/div title plus needed prose. |
| Missing prose after headers or title-like lines | Sections 4.3, Phase 3 step 10, 6.3, and Definition of Done item 9 | Add enough student-facing explanation, task language, or example context after each title/header-like line. |
| Page-layout defects found in rendered PDF review | Sections 2.8, 4.8, Phase 7, and Definition of Done items 14-18 | Fix running headers, raw Markdown/table rendering, split examples, split prompts/response areas, split tables, orphaned headings, and sparse final pages before print sign-off. |

### 2.8 PDF visual inspection defects added after Module 1-2 review

Visual inspection of `int/md/working/aw-int-all_0530.pdf` added production-layout issues that must feed back into the repair list. Detailed notes are recorded in:

- `int/edits & guides/full-review/print-readiness-audits/module1_pdf_layout_followup_0531.md`
- `int/edits & guides/full-review/print-readiness-audits/module2_pdf_layout_followup_0531.md`

New repair categories from the rendered PDF:

- running headers can carry stale context, including `Module Guide` on unit pages and a previous module review header on a new module title page
- section headings, div labels, short lists, and activity starts can be orphaned at page bottoms
- prompts and response areas can split so a page begins with answer lines detached from the task
- weak/strong examples, model boxes, and explanation bullets can split across pages in a way that weakens the comparison
- short tables and structured grids can split without a repeated header or enough context
- raw Markdown can leak into the PDF, confirmed by the Unit 7 `Politeness Scale` pipe-table rendering with visible `|` characters and literal `**` markers
- module endings can leave sparse trailing pages that look accidental rather than intentional

These are not a replacement for the source-level repair. They are additional print-readiness gates that must be checked after DOCX/PDF generation.

---

## 3. Repair Principles

Apply these principles throughout the book.

### 3.1 Preserve the teaching path

Do not delete a task merely because it looks repetitive. First identify its function:

- notice a feature
- understand a model
- practice a controlled form
- write with guidance
- self-check
- edit/revise
- transfer to a new situation
- reflect or prepare homework

Delete or merge only when two adjacent tasks have the same function and one does not add new learner work.

### 3.2 Keep activity references teachable

Every unit should support teacher language such as:

- `Look back at Activity B.`
- `Use the scenario in Activity D.`
- `Revise your draft from Activity E.`

Therefore, the top-level unit activities must be stable and easy to find.

### 3.3 Separate input, practice, and answer space

A student should be able to see:

1. what to read or notice
2. what to do
3. where to write
4. how much to write

Do not mix these in a way that gives away the response before the student has to think.

### 3.4 Use examples without spoiling the task

A model is useful when it illustrates the target skill before a different student task. It becomes a spoiler when it answers the same prompt the student is supposed to complete.

For each model or mini-example, decide whether it should be:

- kept before the task as a genuine model
- moved after the task as feedback / answer-key material
- changed to a partial example
- removed from the student book and preserved for the answer key

### 3.5 Write student-facing instructions for intermediate learners

This is a textbook for intermediate English learners, so student-facing text must be easier than the teacher-facing repair plan. When revising instructions, examples, checklists, and reminders, use clear intermediate-level English.

Student-facing writing rules:

- use short sentences where possible
- use common words before academic or idiomatic words
- avoid long noun phrases and embedded clauses
- avoid idioms such as `carry forward`, `diagnostic baseline`, or `calibrate` in student instructions
- explain necessary administrative terms the first time they appear
- give one action at a time when the task is difficult
- prefer direct verbs such as `read`, `choose`, `write`, `check`, `rewrite`, and `compare`
- keep teacher/editor language, production notes, and audit terms out of the student book

A good student-facing instruction says what to do in simple language, for example: `Read the email. Underline the sentence that explains the problem.`

A weak student-facing instruction uses editor language or advanced phrasing, for example: `Analyze the communicative purpose and identify the source-layer mismatch.`

### 3.6 Use response placeholders as page-design objects

Placeholder type and row count must reflect the actual learner output. They are not decoration.

Use this working scale unless the task clearly requires an exception:

| Output type | Default placeholder treatment |
|---|---|
| one short phrase / label | no table, inline blank, or `rows=1` only if needed |
| one sentence rewrite | `PH-1`, `rows=2` |
| two to four short sentence rewrites | separate `PH-1` boxes, usually `rows=2` each |
| one 3-4 sentence message | compact `PH-2` or `PH-3`, usually `rows=6-8` |
| one 5-6 sentence paragraph / email | `PH-3`, usually `rows=8-10` |
| paired documents | separate labeled boxes, not one generic box |
| three-document pack or final portfolio pack | composite labeled layout; verify page break manually |

---

## 4. Required End State

The manuscript is print-ready only when all of the following are true.

### 4.1 Unit structure

Each ordinary unit has this visible sequence unless a documented capstone exception applies:

1. `### Focus`
2. `### A. Warm-Up` or equivalent introductory activity
3. `### B. Example Check`
4. `### C. Language`
5. `### D. Guided Practice`
6. `### E. Freer Practice`
7. `### F. Editing Practice`
8. `### G. Self-Check / Reflection / Review` as appropriate
9. `### H. Transfer Extension / Homework` as appropriate

Important: do not use duplicate visible `### A.` to `### H.` headings in the same unit. When repairing duplicate `A` sections, preserve the first intended structural `### A.` heading unless the unit-specific design review deliberately chooses a different `A` activity. If a later warm-up must remain inside the same `A` section, demote it to a body subheading or div label rather than stripping the first `A` marker from the concept primer.

### 4.2 Activity titles

Each activity should have one clear title, not three stacked near-synonyms. A good pattern is:

```markdown
### C. Language

::: language
Clear Sentence Pattern

Short teaching text...
:::
```

Avoid patterns such as:

```markdown
### C. Language

::: language
Language Focus

Clear Sentence Pattern

Practice: Clear Sentence Pattern
```

### 4.3 Instructions

Every activity instruction must answer:

- what students do
- what content they use
- how long or how many items they write
- whether they work alone, compare, revise, or use a previous answer
- where they write

If an instruction says `use the previous activity`, replace it with a named reference such as `Use your sentence from Activity C, Practice 2.`

Additional Phase 3 checks:

- Put related information together. Do not split the situation, source text, output requirement, and response instruction across separate paragraphs or unrelated reminders.
- Put information in task order: context first, source text second, student action third, length or number requirement fourth, and response space last.
- Do not place the answer or a full model response immediately after the same question students must answer. If a model is needed, use a different example, a partial example, or move the full answer to teacher material.
- Check every activity title, div title, and header-like line. If it introduces a task or teaching point, add enough student-facing prose after it so the page does not jump from title to exercise, box, or list with no clear explanation.

### 4.4 Intermediate-level language

Every student-facing instruction must be understandable for intermediate learners. Use the teacher-facing plan only to guide the repair; do not copy its advanced wording into the textbook.

Before accepting a revised activity, check that the student-facing text:

- uses mostly simple sentence patterns
- avoids unnecessary passive voice
- avoids idioms and abstract editorial terms
- separates long instructions into short steps
- names the exact text or activity students should use
- keeps examples and reminders concrete

If a task needs a difficult administrative word, keep the word only if it is useful for the course and support it with context or a short explanation.

### 4.5 Lists

Use list formatting only when it helps the student perform the task.

- Use numbered lists for ordered steps, numbered exercise items, and sequences students must follow.
- Use bullets for unordered features, options, or reminders.
- Use checkboxes only for self-checks, editing checklists, or completion checks.
- Convert explanation-only bullet lists into short prose when bullets create visual clutter without a student action.

### 4.6 Div classes

Use the semantic class that matches the activity function:

| Class | Use for |
|---|---|
| `notice` | noticing, comparison, warm-up observation |
| `learn` | concise teaching explanation |
| `language` | language forms, sentence patterns, phrase control |
| `example` | neutral model or mini-model |
| `example-bad` | weak example only |
| `example-good` | stronger example only |
| `write` | new student composition |
| `rewrite` | sentence or text transformation |
| `edit` | checking, correcting, revising |
| `structure` | planning grids, document organization, sequence control |
| `revise` | substantial revision of an earlier draft |

The placeholder should normally remain inside the same div as the task unless the production pipeline requires a deliberate exception.

### 4.7 Student response space

Every placeholder must be justified by a real student response. Remove redundant boxes, especially generic boxes after item-by-item boxes unless the task explicitly asks for a final compiled version.

Every placeholder should have:

- a unique ID
- an appropriate `PH-*` type
- an explicit `rows=N`
- a nearby label only when the label adds information not already present in the instruction

### 4.8 Rendered page layout

Print readiness requires visual checks of rendered DOCX/PDF pages, not only Markdown audits. Source repairs must support clean page behavior in the generated book.

Fix or flag:

- stale or misleading running headers
- orphaned section headings, div labels, and short activity starts at page bottoms
- response lines separated from the prompt or task instruction
- weak/strong examples split across pages without enough context
- model boxes separated from their immediate explanation
- short checklists split so only one or two items continue on the next page
- tables or grids split without a repeated header or readable continuation
- raw Markdown syntax that appears in the rendered output
- module-ending pages with very little content and no intentional design reason

These issues should be addressed with source structure, style keep rules, table-format changes, placeholder row calibration, or intentional page-break controls. Do not rely on manual PDF cleanup.

### 4.9 Language correctness

Because this is an English writing textbook, proofreading is part of the content repair, not a final cosmetic pass. Fix:

- spelling
- punctuation
- spacing around symbols such as arrows
- article and plural errors in instructional prose
- inconsistent capitalization
- unidiomatic teacher instructions
- model texts that lack realistic paragraphing or email layout

---

## 5. Implementation Sequence

Do the repair in the following order. Do not skip ahead to DOCX/PDF production until the Markdown source passes the earlier gates.

### Phase 0 - Protect the current work

1. Confirm the branch and working tree status.
2. Save a copy or commit boundary before broad edits.
3. Record that `int/md/working/aw-int-all_0519.md` is the active editing surface for this repair.
4. Do not regenerate this file from module sources until reconciliation is planned.

### Phase 1 - Build audit inventories and representative reading notes

Create or update machine-readable audit files under `int/edits & guides/full-review/print-readiness-audits/`. Also create a short representative-reading note that records what was read outside Units 1-4 before implementation begins.

Required inventories:

1. unit heading sequence audit
2. duplicate `A-H` heading audit
3. first-`A` preservation audit, especially units where unlettered `####` concept-primer headings appear before `### A. Warm-Up`
4. `#### A-H` subordinate-heading audit
5. div balance and div-class audit
6. placeholder inventory with type, ID, rows, surrounding heading, and likely output type
7. placeholder size-risk audit for multi-item tasks where `rows=N` appears too small
8. generic label audit for `Write Here`, `Use this box`, and similar labels
9. excessive blank-line audit
10. visible arrow / spacing audit for `->` and missing spaces
11. list capitalization and punctuation audit for instructional lists
12. module review heading capitalization audit
13. representative unit-reading note covering the module-family sample in Section 2.6

These inventories should be reviewed before editing so the next LLM does not rediscover the same problems repeatedly. The editor must not rely on Units 1-4 as the whole-book baseline because those units have already been manually altered.

### Phase 2 - Define the unit shell before rewriting prose

For each unit, decide the final visible activity shell before editing the internal activity text.

Standard target:

- `Focus`
- `A. Warm-Up`
- `B. Example Check`
- `C. Language`
- `D. Guided Practice`
- `E. Freer Practice`
- `F. Editing Practice`
- `G. Self-Check and Reflection` or a comparable combined review section
- `H. Transfer / Homework`

Allowed exceptions:

- Module 6 capstone units may use more specialized `E`, `F`, `G`, and `H` labels, but they must still appear in a teachable order.
- Unit 23 may have portfolio-specific labels, but `D` cannot appear after `F`, and duplicate `F` headings must be removed or demoted.

For every duplicate visible heading, choose one of these treatments:

1. merge it into the main activity
2. demote it to bold text inside the current activity
3. convert it to an internal div title
4. delete it if it is only a redundant label

Do not let the duplicate-heading repair invert the activity shell. If the first `A` heading is the unit's concept primer and a later `A` heading is the warm-up, keep the concept primer as the structural `### A.` unless the unit design is explicitly changed, then fold the warm-up into that section as a subordinate activity.

### Phase 3 - Repair one unit at a time

Use this workflow for each unit.

1. Read the unit Focus statements.
2. Read all activities in the unit without editing.
3. Write a one-sentence teacher goal for the unit.
4. Map each activity to the goal and to one learner action.
5. Fix the visible heading order.
6. Repair activity information order before polishing wording: context or source first, student action second, length/number/output requirement third, response space last.
7. Repair instructions for clarity, completeness, information order, and intermediate-level readability.
8. Reorganize instructions so related sentences stay together and the student sees context, source, action, output requirement, and response space in a logical order.
9. Remove or replace advanced vocabulary, idioms, and editor-facing wording in student-facing text.
10. Remove or relocate spoilers, including full model answers placed immediately after the same question.
11. Check for activity titles or header-like lines with missing prose, and write the needed student-facing explanation or task sentence.
12. Normalize list types.
13. Repair div class choices and boundaries.
14. Calibrate placeholder type and row count.
15. Proofread examples and model texts.
16. Run local audits before moving to the next unit.

Do not batch-rewrite all 23 units at once. The previous failure pattern suggests that broad automated passes can damage structure faster than they improve it.

### Phase 4 - Apply high-priority fixes across the whole book

Work in this priority order. This is not a Units 1-4-only repair. The opening units are only the pilot area for validating the method.

1. **Representative cross-book sample**: read and note at least one full unit from each family in Section 2.6 before implementing a reusable standard.
2. **Unit 1 pilot**: use Unit 1 only to test the repair method on a small area; do not treat it as proof that the rest of the book is similar.
3. **Units 2-4**: use the user's manual edits as a style reference, but restore exercise numbering and activity boundaries where needed.
4. **Units 19-23**: normalize `#### A-H` headings and capstone order before changing prose, because these units are structurally different from the opening units.
5. **Units 5-18**: repair duplicate section letters and repeated `F/E/H` ordering problems, checking each unit family rather than applying a single opening-unit pattern.
6. **Module review workshops**: title-case lowercase headings and reduce repeated title rows.
7. **Whole-book placeholder pass**: verify all `rows=N` values after the activities are stable.
8. **Whole-book proofreading pass**: catch grammar, punctuation, capitalization, paragraphing, and email-layout issues.

### Phase 5 - Activity-level rewrite standard

When rewriting an activity, use this template mentally.

```markdown
::: class
Short Activity Title

One or two sentences that explain the situation or purpose.

Clear task instruction. Include the number of items, length, or output form.

1. First item, if this is an exercise.
2. Second item.
3. Third item.

Optional: one concise reminder that supports the task without giving the answer.

{{PH-X: unique-id | rows=N}}
:::
```

Avoid:

- `Write your answer below` if the placeholder already shows the answer space
- separate `Write Here` labels unless there are multiple boxes and the label distinguishes them
- blank lines inserted only to create visual spacing in Markdown
- model answers immediately under the same prompt students are supposed to complete

### Phase 6 - Reconcile source files

Only after the working manuscript is approved:

1. decide whether `aw-int-all_0519.md` becomes the new canonical combined source or is split back into module files
2. update `int/md/final/modules/aw-int_mod1.md` to `aw-int_mod6.md` from the approved combined source, or regenerate the combined source from updated modules
3. document the chosen direction in `project-learning.md` and `project-journal.md`
4. rerun answer-key alignment checks because activity labels and prompts may have changed

### Phase 7 - Production build

After Markdown sign-off only:

1. rebuild DOCX
2. inspect representative pages from each module in DOCX before PDF export
3. verify response boxes do not split badly across pages
4. verify headings, div labels, tables, model boxes, and running headers render correctly
5. rebuild PDF
6. visually inspect at least one full module from each major module family, plus every module title page and review workshop ending
7. check that prompts, examples, response areas, short tables, and checklists stay together or split with readable context
8. confirm no raw Markdown syntax appears in the PDF, especially pipe tables and emphasis markers
9. perform a final print-readiness checklist pass

---

## 6. Detailed Unit Repair Checklist

Use this checklist for each unit and record pass/fail notes.

### 6.1 Focus alignment

- [ ] Focus statements use consistent `By the end of this unit, I will be able to...` framing or another project-approved pattern.
- [ ] Each Focus statement maps to at least one visible activity.
- [ ] Activities do not introduce major outputs that are absent from the Focus.

### 6.2 Activity sequencing

- [ ] Warm-up activates the unit skill without requiring knowledge not yet taught.
- [ ] Example Check shows a model or contrast before production.
- [ ] Language section teaches the needed form, phrase, structure, or editing principle.
- [ ] Guided Practice gives enough support but does not complete the task for the student.
- [ ] Freer Practice asks students to produce a meaningful workplace text.
- [ ] Editing Practice requires revision or correction, not just rereading.
- [ ] Self-check / Reflection appears after production and editing, unless a pre-draft checklist clearly supports a specific larger draft.
- [ ] Transfer / Homework extends the unit skill to a new or later context.

### 6.3 Instruction quality

- [ ] The student knows exactly what to do.
- [ ] The student knows what source text, scenario, or previous answer to use.
- [ ] The expected length is stated where relevant.
- [ ] The instruction does not give away the answer.
- [ ] A model or example does not answer the exact same prompt students must complete.
- [ ] Related instruction sentences are adjacent.
- [ ] Context, source text, action, output requirement, and response space appear in a logical order.
- [ ] There is no redundant restatement of the same instruction.
- [ ] Every activity title, div title, and header-like line is followed by enough prose, task language, or example context for an intermediate learner.

### 6.4 Intermediate learner readability

- [ ] Student-facing instructions use short, direct sentences.
- [ ] Advanced editorial words are removed from student-facing text.
- [ ] Idioms and vague phrases are replaced with clear common words.
- [ ] Difficult administrative terms are explained or supported by context.
- [ ] Each difficult task is broken into clear steps.

### 6.5 Formatting and Markdown

- [ ] Top-level activity headings are in order.
- [ ] No duplicate visible `A-H` heading remains unless documented as an intentional exception.
- [ ] Div fences are balanced.
- [ ] Div class matches task function.
- [ ] Placeholder is inside the relevant activity div unless intentionally external.
- [ ] Lists use the correct type and are not used where short prose would be clearer.
- [ ] There are no excessive blank lines.
- [ ] Stacked or redundant titles have been reduced to one clear title plus useful prose.
- [ ] Examples use readable paragraphing or email layout.

### 6.6 Response-space calibration

- [ ] Every response space corresponds to a real task.
- [ ] No generic response box duplicates item-level response boxes.
- [ ] Row count matches expected student output.
- [ ] Paired or multi-document tasks have separate labels.
- [ ] Placeholder IDs are unique.

---

## 7. Suggested Automation Checks

Use scripts for detection, not blind rewriting. Suggested checks:

```bash
python scripts/check_mojibake.py int
```

```bash
python - <<'PY'
from pathlib import Path
import re, collections
p = Path('int/md/working/aw-int-all_0519.md')
lines = p.read_text(encoding='utf-8').splitlines()
unit_re = re.compile(r'^## Unit (\d+)\. (.*)')
sec_re = re.compile(r'^### (.*)')
cur = None
for i, line in enumerate(lines, 1):
    m = unit_re.match(line)
    if m:
        cur = {'n': int(m.group(1)), 'title': m.group(2), 'secs': []}
        continue
    if cur and line.startswith('## '):
        letters = [re.match(r'([A-H])\. ', s).group(1) for _, s in cur['secs'] if re.match(r'([A-H])\. ', s)]
        print(f"U{cur['n']:02d}: {''.join(letters)}")
        cur = None
        continue
    if cur:
        m = sec_re.match(line)
        if m:
            cur['secs'].append((i, m.group(1)))
PY
```

```bash
rg -n -- '#### [A-H]\. |\bWrite Here\b|Use this box for one complete version|->|rows=46|rows=22' int/md/working/aw-int-all_0519.md
```

```bash
python - <<'PY'
from pathlib import Path
import re, collections
text = Path('int/md/working/aw-int-all_0519.md').read_text(encoding='utf-8')
opens = re.findall(r'^:::[ \t]+[\w-]+', text, flags=re.M)
closes = re.findall(r'^:::[ \t]*$', text, flags=re.M)
print('div opens', len(opens), 'div closes', len(closes), 'net', len(opens)-len(closes))
print(collections.Counter(re.findall(r'^:::[ \t]+([\w-]+)', text, flags=re.M)))
print('placeholder ids', len(re.findall(r'\{\{PH-', text)))
print('without rows', len([m for m in re.findall(r'\{\{PH-[^}]+\}\}', text) if 'rows=' not in m]))
PY
```

```bash
python - <<'PY'
from pathlib import Path
import re
lines = Path('int/md/working/aw-int-all_0519.md').read_text(encoding='utf-8').splitlines()
for i, line in enumerate(lines[:-2], 1):
    # Heuristic only: flags stacked title-like lines or title-to-placeholder jumps for human review.
    if re.match(r'^(###|####|:::|[A-Z][A-Za-z /-]{2,40})$', line.strip()):
        nxt = [x.strip() for x in lines[i:i+4] if x.strip()]
        if nxt and (nxt[0].startswith('{{PH-') or re.match(r'^[A-Z][A-Za-z /-]{2,40}$', nxt[0])):
            print(i, line.strip(), '->', nxt[:2])
PY
```

---

## 8. Definition of Done

The repair is complete when:

1. the heading sequence audit shows every unit in a documented, teachable order
2. no accidental duplicate visible `A-H` headings remain
3. div open/close counts match and no activity contains an unintended nested div problem
4. placeholder inventory has no unjustified generic boxes, duplicate IDs, or unexplained outlier row counts
5. student-facing instructions are written in clear intermediate-level English
6. activity instructions keep related information together and present it in a logical task order
7. a teacher can follow every activity instruction without guessing the intended source or output
8. no student activity gives away the answer before requiring learner work
9. every activity title, div title, and header-like line has enough following prose or task language for students to understand what to do
10. examples and model texts use correct paragraphing and workplace formatting
11. the manuscript passes proofreading for spelling, grammar, punctuation, capitalization, and spacing
12. the answer key is rechecked against revised activity references
13. DOCX and PDF builds are produced only after Markdown sign-off
14. running headers show the correct module, unit, or review context and do not carry stale previous-section labels
15. rendered pages do not split prompts from their first response space or leave answer lines detached from the task
16. examples, weak/strong comparisons, model explanations, short checklists, and short tables are kept together or split only with clear continuation context
17. no raw Markdown syntax, pipe-table syntax, or emphasis markers appear in the DOCX/PDF output
18. module-ending pages are visually balanced or intentionally designed; sparse trailing pages are fixed or accepted deliberately
19. the first intended `### A.` structural heading is preserved in every unit, and no concept-primer section has been silently demoted while a later warm-up was kept as the only visible `A`

---

## 9. First Practical Next Step

Start with **a cross-book diagnostic sample plus a Unit 1 pilot**, not with a Units 1-4-only repair. The first few units were manually edited and are not representative of the whole book.

Step 1: create the representative-reading note required in Section 2.6 by reading at least one full unit from each major family outside the opening units.

Step 2: repair **Unit 1 only** as a pilot. Do not attempt the whole book in one patch, and do not assume the Unit 1 solution will transfer unchanged to later modules.

For the Unit 1 pilot:

1. restore clear item numbering in sentence rewrite tasks
2. keep the simplified prose style from the user's manual edits
3. remove redundant `Write Here` / `Use this box` labels unless they distinguish a complete-document box from item-level boxes
4. keep placeholders inside the correct divs
5. move `E. Freer Practice` before self-check, or rename and reposition the self-check so the visible sequence is teachable
6. decide whether `F. Reflection` and `H. Homework` should remain separate visible activities or be folded into a single final `H` area
7. run the local audits before proceeding to Unit 2

Once Unit 1 is accepted, compare it against the representative-reading notes from later modules before applying it to Units 2-4. Then proceed through all remaining units and all module review workshops using the whole-book audit inventories, not the opening units alone.
