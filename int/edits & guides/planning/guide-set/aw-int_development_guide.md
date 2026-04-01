# Intermediate Development Guide
## *Administrative Writing, Intermediate*

---

> **Purpose of this document**
> This file defines the authoritative planning-and-cross-check set for future intermediate-book development work.
>
> Use this subfolder as the first stop when:
> - continuing development work
> - checking the live book against planning/control documents
> - deciding which source-of-truth document governs a question

This subfolder is the current development guide set:

- `int/edits & guides/planning/guide-set`

---

## 1. What Belongs In This Guide Set

Only documents that actively govern ongoing development, review, or cross-checking belong here.

Current guide-set documents:

1. `aw-int_project_todo_list.md`
   - project state, stage order, active next steps, pinned later tasks, current priorities

2. `aw-int_activity_framework.md`
   - activity-type functions, section logic, approved structural variation, output-control rules

3. `aw-int_prompt-writing-policy.md`
   - prompt/task design standards for intermediate learners and intermediate workplace contexts

4. `aw-int_unit_structural_profiles.md`
   - planning source-of-truth for module purpose, unit goals, Can-Do statements, output expectations, and revision flags

5. `aw-int_qa_checklist.md`
   - source-of-truth definition of the whole-book QA gate that will be used after the main revision passes

6. `aw-int_Support-Parity Intervention Plan.md`
   - blocking intervention-stage control file defining how support-depth and volume parity must be restored before QA can resume

7. `aw-int_full-review_protocol.md`
   - source-of-truth definition of the post-QA full-review stage

---

## 2. Live Source Scope

For current intermediate development work, the live content source is:

- `int/edits & guides/planning/supporting/int_writing_text_intro.md`
- `int/md/final/modules/aw-int_mod1.md`
- `int/md/final/modules/aw-int_mod2.md`
- `int/md/final/modules/aw-int_mod3.md`
- `int/md/final/modules/aw-int_mod4.md`
- `int/md/final/modules/aw-int_mod5.md`
- `int/md/final/modules/aw-int_mod6.md`

Treat the following as reference-only unless a later control decision changes that:

- `int/archive/md/units/aw-int-01.md` to `aw-int-23.md`
- `int/md/aw-int-all.md`

Do not let the older split-unit baseline silently resume authority now that the module files are the live editing source.

---

## 3. How To Use The Guide Set

### 3.1 For current project status

Start with:

- `aw-int_project_todo_list.md`
- `aw-int_Support-Parity Intervention Plan.md` when `INT-5A` is active

Use it to determine:

- the current active stage
- what is done
- what is deferred
- what the next project step is
- which control files should govern the active stage

### 3.2 For planning or revising the live module files

Cross-check in this order:

1. `aw-int_unit_structural_profiles.md`
2. `aw-int_activity_framework.md`
3. `aw-int_prompt-writing-policy.md`

Use this sequence to answer:

- what the unit is supposed to do
- what section pattern and activity progression are allowed
- how prompts and tasks should be written for the target learners

### 3.3 For QA and post-QA review work

Use:

1. `aw-int_qa_checklist.md` for the future QA gate definition
2. `aw-int_full-review_protocol.md` for the later editorial review stage

These files define their stages before those stages begin.  
Their findings and round artifacts should live outside the guide set.

---

## 4. Separation Of Functions

This guide set deliberately separates functions that should not blur together:

- `project status / sequencing`
  - `aw-int_project_todo_list.md`

- `blocking intervention-stage authority`
  - `aw-int_Support-Parity Intervention Plan.md`

- `activity and section control`
  - `aw-int_activity_framework.md`

- `prompt-design rules`
  - `aw-int_prompt-writing-policy.md`

- `unit planning and cross-checking`
  - `aw-int_unit_structural_profiles.md`

- `QA stage definition`
  - `aw-int_qa_checklist.md`

- `full-review stage definition`
  - `aw-int_full-review_protocol.md`

Do not duplicate these functions across multiple current documents unless there is a strong reason.

---

## 5. What Does Not Belong In This Guide Set

The following types of documents should not be treated as current planning authority:

- background project summaries
- historical setup notes
- baseline-audit findings files
- round-by-round QA or full-review findings
- step prompts and working notes
- legacy source baselines kept only for traceability

Those belong in supporting, audit, review, or historical locations instead.

---

## 6. Supporting Material

Supporting but non-authoritative planning-adjacent files live in:

- `int/edits & guides/planning/supporting`

Use them for:

- book identity and audience background
- setup rationale
- historical development context

Use them only as background unless a guide-set document explicitly points back to them.

---

## 7. Maintenance Rule

When a new intermediate planning document is created, decide immediately whether it is:

- a current guide-set control document
- a supporting background document
- a stage artifact
- or a historical note

Do not leave documents in the planning area without a clear function.

When the live source set changes, update the guide set immediately so future sessions do not work from stale authority.

---

*Document status: authoritative index for the intermediate planning-and-cross-check guide set.*
