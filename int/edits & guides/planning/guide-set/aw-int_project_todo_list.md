# Project To-Do List
## *Administrative Writing, Intermediate* — Editorial & Development Tasks

---

> **How to use this document**
> This file is the current project-control document for the intermediate book.
>
> Use it to track:
> - the active stage
> - what each stage must actually produce
> - which source files govern the stage
> - which items are confirmed for later rather than currently active

Update status as work progresses. Treat the detail fields as operational control requirements, not as loose reminders.

---

## NOW — Active Tasks

| # | Task | Detail | Status |
|---|---|---|---|
| INT-0 | Freeze live source set | Treat `int/edits & guides/planning/supporting/int_writing_text_intro.md` plus `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md` as the live working source. Treat `int/md/units/aw-int-01.md` to `aw-int-23.md` and `int/md/aw-int-all.md` as reference-only unless a later control decision replaces this. | Done |
| INT-1 | Establish planning control stack | Create the intermediate `guide-set` / `supporting` planning structure and seed the core control documents. | Done |
| INT-2 | Run baseline audit | Record current unit patterns, section logic, output-length behavior, repeated scenario families, and obvious cleanup classes before broad revision. Baseline record now exists at `int/edits & guides/baseline-audit/aw-int_baseline_audit_round1.md`. | Done |
| INT-3 | Build revised structural profiles | Complete all 23 unit profiles in `aw-int_unit_structural_profiles.md`. For each unit, record: module purpose, unit learning goal, 3 to 4 learner-facing Can-Do statements, activity-purpose map, current output expectations, revision flags, and approved exceptions. Build from the live module files rather than from the advanced book or the old split-unit baseline. | Done |
| INT-4 | Run whole-book draft revision pass | Revise the live module files only against the completed planning stack. For each module, align unit structure, task sequencing, prompts, output expectations, and scenario spread with the structural profiles, activity framework, and prompt-writing policy. Do not continue active editing in the split unit files unless a later control decision explicitly reopens them as the live source. | Done |
| INT-5 | Run language-instruction strengthening pass | After the structural revision pass, sharpen actual teaching inside the module files. Add or improve concise conceptual framing, model-text explanation, and guided support where the book still relies too heavily on exposure, phrase lists, or implicit noticing. Keep the teaching lighter and more explicit than the advanced book rather than importing advanced pedagogical density directly. | Done |
| INT-5A | Run support-parity intervention stage | Execute the blocking intervention defined in `aw-int_Support-Parity Intervention Plan.md`. Revise the control layer and the six live module files until the intermediate book reaches advanced-equivalent support depth, development completeness, and the required `80-90%` module-volume parity band while remaining readable for A2-B1+ learners. | In Progress |
| INT-6 | Run whole-book QA gate | Execute the dedicated QA stage only after `INT-5A` is complete. Use `aw-int_qa_checklist.md` as the operative standard and check the completed module files against learner suitability, prompt/task quality, structural-profile compliance, progression, self-study usability, answer-key supportability, formatting readiness, pinned-item confirmation, support-depth parity, and module-volume parity. | Blocked |
| INT-7 | Run full review | Conduct a post-QA whole-book editorial review using `aw-int_full-review_protocol.md` as the stage definition. Record findings by round outside the planning folder, keep full-review findings distinct from QA findings, and do not proceed to answer-key work until the live module set is stable enough for final support materials. | Pending |

---

## PINNED — Confirmed For Later

These items are agreed and will be handled at the appropriate later stage. They are not in question; only deferred.

| # | Task | Detail | Depends on | Status |
|---|---|---|---|---|
| P1 | Add Unit 23 learner-facing rubric | Implemented in `int/md/first_draft_modules/aw-int_mod6.md` as the Unit 23 `Portfolio Review Rubric`. The rubric keeps an intermediate-level self-review structure and points back to taught units. | INT-5 | Done |
| P2 | Add companion teacher-facing rubric or marking note | Implemented in `int/edits & guides/qa/aw-int_unit23_portfolio_marking_note.md` as the aligned teacher / QA companion note for Unit 23. | INT-5 | Done |
| P3 | Develop answer key / sample responses | Write answer-key and sample-response support only after the content, QA, and full review are stable. The answer-key layer should be based on the final module files, not on the earlier split-unit baseline. | INT-7 | Deferred |
| P4 | Regenerate combined draft | Rebuild `int/md/aw-int-all.md` only after the module-file source set is revised and signed off. Do not treat the current combined draft as an editable working file. | INT-7 | Deferred |
| P5 | Defer Word-formatting work until Markdown sign-off | Production formatting should follow content sign-off, not compete with revision control. Word-format work should happen only after the intermediate Markdown source is stable. | Late-stage | Deferred |

---

## REFERENCE — Agreed Task Sequence

The agreed order for completing the intermediate book is:

1. `INT-2` baseline audit
2. `INT-3` revised structural profiles
3. `INT-4` whole-book draft revision pass
4. `INT-5` language-instruction strengthening pass
5. `INT-5A` support-parity intervention stage
6. pinned capstone / rubric follow-through that remains valid after the intervention rebuild
7. `INT-6` whole-book QA gate
8. `INT-7` full review
9. `P3` answer key / sample responses
10. `P4` regenerate combined draft

Current active point in that sequence:

- `INT-5A` is in progress
- `INT-6` is blocked until the intervention stage is complete

---

## REFERENCE — Stage Outputs And Control Files

| Stage | Main Output / Control File |
|---|---|
| Baseline audit | `int/edits & guides/baseline-audit/aw-int_baseline_audit_round1.md` |
| Structural profiles | `int/edits & guides/planning/guide-set/aw-int_unit_structural_profiles.md` |
| Activity / section control | `int/edits & guides/planning/guide-set/aw-int_activity_framework.md` |
| Prompt / task control | `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md` |
| Support-parity intervention | `int/edits & guides/planning/guide-set/aw-int_Support-Parity Intervention Plan.md` |
| Activity-gap worklist | `int/edits & guides/planning/guide-set/aw-int_activity_gap_worklist.md` |
| Wave 4 execution brief | `int/edits & guides/planning/guide-set/aw-int_wave4_execution_brief.md` |
| QA stage definition | `int/edits & guides/planning/guide-set/aw-int_qa_checklist.md` |
| Full-review stage definition | `int/edits & guides/planning/guide-set/aw-int_full-review_protocol.md` |
| Live editing source | `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md` |
| Reference-only unit baseline | `int/md/units/aw-int-01.md` to `aw-int-23.md` |
| Reference-only combined draft | `int/md/aw-int-all.md` |

---

## REFERENCE — Key Decisions Already Made

| Decision | Detail |
|---|---|
| Live editing source | Edit the intermediate book in the six module files only: `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md` |
| Unit-file role | `int/md/units/aw-int-01.md` to `aw-int-23.md` are reference-only baseline files unless a later control decision restores them as active source |
| Combined draft role | `int/md/aw-int-all.md` is reference-only until intentional regeneration |
| Workflow model | rigorous adaptation of the advanced workflow, not direct cloning |
| Book identity | keep a simpler, more scaffolded, and more teachable intermediate structure and voice than the advanced book |
| Learner level | A2-B1+ workplace learners |
| Structural model | do not import the advanced `A-H` coded architecture wholesale; keep the intermediate structure readable and lower-load |
| Prompt policy | prompts must stay short, concrete, explicit, and teachable for A2-B1+ workplace learners |
| JPO scope | limited JPO contextualization only where it clearly improves realism |
| Output-control baseline | record and preserve the current sentence-band scaffolding before deciding later where word-range normalization is appropriate |
| Module structure | 23 units across 6 modules with a `3 + 4 + 4 + 4 + 3 + 5` distribution |
| Late-book complexity | later integrated units may be more complex, but that complexity must be prepared by earlier units and remain readable |
| Support parity | lower level does not justify thinner pedagogy; the intermediate book must reach advanced-equivalent support depth and development completeness |
| Volume parity | intermediate modules must reach the `80-90%` parity band recorded in `aw-int_Support-Parity Intervention Plan.md` unless an explicit approved exception is recorded |

---

## REFERENCE — Current Priorities Inside INT-5A

The immediate revision priorities are:

1. treat `int/edits & guides/planning/guide-set/aw-int_Support-Parity Intervention Plan.md` as the blocking source of truth for the current stage
2. revise the planning stack so support-depth parity and module-volume parity are binding rather than implied
3. use `int/edits & guides/planning/guide-set/aw-int_activity_gap_worklist.md` as the activity-level diagnosis for the next intervention passes
4. use `int/edits & guides/planning/guide-set/aw-int_wave4_execution_brief.md` as the operative control brief for the next broader rebuild wave
5. continue the live rebuild beyond the earlier support waves, with the heaviest remaining expansion focus on Module 6 first, then Modules 3 and 4, then Modules 2 and 5
6. keep the first rebuild-wave gains stable:
   - explicit model/example support
   - why-this-works teaching notes
   - self-check routines
   - editing-practice routines
   - module guides and module review workshops
7. keep the second rebuild-wave gains stable:
   - module strategy maps
   - module revision labs
   - module-level transfer and carry-forward tasks
8. preserve the now-corrected local Round 1 fixes in `Unit 16 - Editing for Accuracy` and `Unit 23 - Portfolio Writing & Final Revision` while not letting those local corrections hide the larger book-level blocker
9. transfer the structural-profile Can-Do statements into the live `### Focus` sections across all 23 units so planning intent and learner-facing content are back in sync
10. revise the flagged freer-practice choice lists in Units 5, 6, 7, 16, 17, and 18 so the options stay situation-anchored and parallel in scope and detail
11. add the missing profile-control notes for Units 12 and 13 phrase-bank mini-examples, book-level scenario distribution, and reflection progression in Modules 4 to 6
12. use the reclassified `int/edits & guides/qa/aw-int_qa_round1.md` as the continuity QA record while the intervention stage remains active
13. keep later-stage items visible, but do not resume `INT-6` until the intervention stage is complete

---

*Document status: authoritative intermediate project-control file, expanded to function as the operational equivalent of the advanced to-do list while the intermediate track remains in earlier-stage execution.*
