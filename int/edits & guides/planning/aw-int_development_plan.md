# Intermediate Textbook Development Plan

## Summary

This plan sets the development model for the intermediate book in `int`.

The intermediate book should be developed as a **rigorous adaptation** of the advanced workflow, not as a direct clone of the advanced book's architecture. The goal is to reach the same overall level of editorial quality, pedagogical usefulness, and QA control while preserving the simpler, lower-level identity of the intermediate draft set.

The active working source should be:

- `int/int_writing_text_intro.md`
- `int/md/aw-int-01.md` to `int/md/aw-int-23.md`

For now, `int/aw-int-all.md` should be treated as a reference snapshot rather than the live source of truth. It can be regenerated later after the split-unit files have been revised and signed off.

Project defaults already chosen:

- workflow model: rigorous adaptation
- JPO scope: limited JPO contextualization only where it clearly improves realism
- rollout model: whole-book planning first, then module-by-module execution

## Planning And Control Layer

Before heavy content revision begins, create an intermediate control stack under `int/edits & guides` with these subfolders:

- `planning`
- `development`
- `qa`
- `references`
- `steps`

Create these core planning documents early:

- `planning/aw-int_project_todo_list.md`
- `planning/aw-int_project_context.md`
- `planning/aw-int_activity_framework.md`
- `planning/aw-int_unit_structural_profiles_revised.md`
- `planning/aw-int_prompt-writing-policy.md`
- `development/aw-int_language_instruction_framework.md`
- `qa/aw-int_qa_checklist.md`

Use this source hierarchy during development:

1. intermediate to-do list
2. intermediate revised structural profiles
3. intermediate activity framework
4. intermediate prompt-writing policy
5. intermediate language-instruction framework
6. active unit files in `int/md`
7. reference-only older combined draft and background notes

The intermediate book should **not** inherit the advanced `A-H` coded architecture wholesale. Instead, it should keep a simpler intermediate identity, but with a stable and explicitly defined framework for:

- focus and setup
- concept or model section
- controlled language or practice work
- guided writing
- freer writing
- extended writing
- reflection
- homework
- scenario-overview handling in later integrated units where needed

## Development Stages

### INT-0. Baseline Audit And Source Freeze

Before rewriting, produce a baseline audit in `int/edits & guides/steps` that records:

- the current 23-unit and 6-module structure
- recurring section patterns and unit outliers
- current sentence-count and output-length behavior
- repeated scenario families
- capstone structure in Units 19-23
- obvious cleanup classes such as duplication, thin explanations, inconsistent headings, or encoding issues

Lock these decisions at the same time:

- `int/md` is the live source set
- `int/aw-int-all.md` is reference-only until intentionally regenerated
- the intro file and the split-unit files must be brought into alignment during the planning pass

### INT-1. Planning Layer

Build the planning documents before starting broad content edits.

`aw-int_project_context.md` should define:

- learner profile: A2-B1+ workplace learners
- course purpose and intended professional range
- classroom and self-study use
- target document families
- what quality means for this book

`aw-int_activity_framework.md` should define:

- the standard intermediate unit architecture
- allowed section variants
- how integrated later units may differ
- what each recurring section is for pedagogically

`aw-int_prompt-writing-policy.md` should adapt the advanced lessons to the lower level:

- prompts must remain situation-anchored
- instructions must be shorter and more readable than advanced
- scenario choices must be parallel when options are offered
- guided tasks may be more explicit, but freer and homework tasks must still leave real work to the learner
- JPO contexts may be used only where they clearly add realism and remain level-appropriate
- avoid advanced-style density, overloading, and pseudo-realism

Also lock a documented output-length policy:

- guided tasks may use sentence counts where that is pedagogically helpful
- freer writing, extended writing, and homework should move toward a consistent word-range model
- integrated Module 6 tasks may use per-document guidance plus a total-pack expectation
- sentence-count versus word-count choices should no longer be ad hoc by unit

### INT-2. Revised Structural Profiles

Create `aw-int_unit_structural_profiles_revised.md` for all 23 units.

Each unit profile should include:

- module purpose
- unit learning goal
- 3 to 4 learner-facing Can-Do statements
- activity-by-activity purpose map
- output-length expectation
- content flags for revision
- any approved exception from the standard intermediate structure

This document becomes the planning source of truth for all later editing and QA.

Use it to front-load the issues that caused pain in the advanced project:

- weak alignment between unit goals and actual outputs
- thin or repetitive task structures
- unclear module progression
- scenario-family overconcentration
- capstone tasks that lack assessment logic
- later-unit integration work that is not sufficiently prepared by earlier units

### INT-3. Whole-Book Draft Revision Pass

Revise the book module by module, but against the full planning stack already in force.

Execution order:

1. Module 1
2. Module 2
3. Module 3
4. Module 4
5. Module 5
6. Module 6

This pass should fix:

- unit structure consistency
- prompt and task design
- scenario clarity and option parallelism
- self-study usability
- progression of writing demand
- alignment between intro, profiles, and live unit files
- capstone architecture in Units 19-23

Default editorial rules for this pass:

- preserve the simpler intermediate unit voice
- reduce repeated "write two" or "write several" patterns where they create load without value
- keep workplace realism concrete but ordinary, not over-specialized
- keep JPO contextualization limited and selective
- distribute applicant, colleague, internal-document, and external-inquiry contexts across the book rather than clustering one pattern too heavily

Add pinned later-stage items to the intermediate to-do list during this stage, including:

- Unit 23 rubric requirement before final full review
- answer key and sample responses as a later stage
- any integrated-task dependencies in Module 6
- Word-formatting work explicitly deferred until Markdown sign-off

### INT-4. Language-Instruction Strengthening Pass

Run a separate pedagogical pass after the structural and prompt revision pass.

Use `development/aw-int_language_instruction_framework.md` to check every unit for:

- explicit explanation of the writing principle, not just phrases
- enough support for A2-B1+ learners to transfer the skill
- clear model-comparison logic
- worked examples where the principle is not obvious
- a visible bridge from controlled work to guided and freer writing

Carry over the key advanced lesson explicitly:

- fixing prompts is not the same as teaching the skill

This pass must strengthen pedagogy, not just tidy wording.

Also complete the intermediate capstone support in this stage:

- add a Unit 23 learner-facing rubric
- add a companion teacher-facing rubric or marking note
- keep the rubric simpler than the advanced book, but aligned to the real cumulative skill strands of the intermediate book

### INT-5. Whole-Book QA And Full-Review Gate

Run a dedicated intermediate QA stage after INT-4 is complete.

Draft the checklist earlier, but do not execute final QA until the content passes are complete.

The QA checklist should mirror the successful advanced QA structure, adapted to intermediate level:

- design for purpose
- learner suitability
- language and learning
- prompt and task design
- consistency and cohesion
- model text quality
- structural-profile compliance
- activity-type fidelity
- progression
- self-study accessibility
- answer-key supportability
- formatting and production readiness
- pinned-item confirmation

The final QA process should include:

- preliminary cross-check against planning docs and known unresolved items
- module-by-module review
- whole-book anti-drift consolidation
- final sign-off gate

The anti-drift rule must be explicit:

- no category is considered clear until the whole-book pass is finished
- earlier round findings are historical evidence only
- repeated issue families must be recorded at book level, not collapsed into a few remembered examples

### INT-6. Post-Content Finish

Only after QA sign-off:

- full review
- answer key and sample responses
- Word formatting and production conversion
- regeneration of `int/aw-int-all.md` if the project still wants a combined Markdown deliverable

## Test Plan And Review Anchors

### Baseline checks

- confirm all 23 units are mapped to a stable module progression
- confirm the intro, profiles, and live units describe the same learner level and book purpose
- confirm there is no ambiguity about whether the split files or combined file are the active source

### Planning checks

- every unit has a learning goal, Can-Do statements, activity map, and revision flags
- every recurring section type has a defined pedagogical purpose
- output-length policy is documented before revision begins

### Draft-revision checks

- every writing task can be traced to a unit goal
- scenario choices are parallel where options exist
- JPO contexts are limited, level-appropriate, and non-dominant
- Module 6 integrated tasks feel prepared by earlier units rather than abruptly harder

### Language-instruction checks

- every unit teaches a principle, not only phrases or examples
- model text work explains why the better version works
- A2-B1+ learners have enough explicit support to complete later tasks independently

### Final QA checks

- every QA category appears explicitly in the final review record
- the final QA verdict is based on the whole-book pass, not inherited closure
- deferred items are named and controlled
- no unresolved structural or pedagogical blocker remains before full review

### Anchor units

Use these units as recurring spot-check anchors during development and QA:

- Unit 1 for readability and explicit-teaching baseline
- Unit 6 or 7 for first serious email-production pressure
- Unit 12 for external and international communication
- Unit 18 for editing and revision transfer
- Units 19-23 for integration and capstone readiness

## Assumptions

- the project remains Markdown-first until content and QA are complete
- the intermediate book should reach the same **process quality** as the advanced book, but not by becoming a lower-level copy of the advanced architecture
- the simpler intermediate identity is worth preserving
- JPO contextualization is a limited enhancement, not a universal pattern
- whole-book planning comes before module execution
- the Unit 23 rubric is a pre-full-review content requirement, not a late afterthought
- answer keys and Word formatting remain later-stage deliverables
