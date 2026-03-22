# Intermediate Full Review Protocol
## *Administrative Writing, Intermediate*

---

> **Purpose of this document**
> This file defines what the intermediate-book full review is, what it is not, what source files govern it, how findings should be recorded, and what counts as completion.
>
> This is the source-of-truth definition for the post-QA full-review stage.

---

## 1. What Full Review Is

Full review is the first whole-book editorial pass conducted **after** the intermediate book has cleared its QA gate.

Its purpose is to evaluate the completed live module set as a finished learner-facing book rather than as a draft still undergoing structural revision.

It asks questions such as:

- does the book read coherently from Module 1 to Module 6
- does progression feel consistent and teachable for the target learners
- do tasks, explanations, examples, and support layers work together as a book
- are there any remaining planning/live mismatches, usability gaps, calibration dips, or editorial inconsistencies significant enough to matter before answer-key work begins

Full review is therefore a post-QA editorial control stage, not a drafting stage and not a replacement for QA.

---

## 2. What Full Review Is Not

Full review is **not**:

- another structural-profile drafting pass
- another QA gate
- a default prompt-repair campaign
- a default language-instruction redesign pass
- a reason to reopen every earlier design decision

By the time full review begins, the book should already be:

- structurally revised
- instructionally strengthened
- QA-cleared

Full review focuses on the finished-book reading and usability level.

---

## 3. Review Baseline And Source Hierarchy

### 3.1 Primary source under review

The object under review is the live intermediate module source set:

- `int/md/first_draft_modules/aw-int_mod1.md`
- `int/md/first_draft_modules/aw-int_mod2.md`
- `int/md/first_draft_modules/aw-int_mod3.md`
- `int/md/first_draft_modules/aw-int_mod4.md`
- `int/md/first_draft_modules/aw-int_mod5.md`
- `int/md/first_draft_modules/aw-int_mod6.md`

These files are the finished content baseline for full review.

### 3.2 Supporting control references

Use these as source-of-truth control documents when needed:

- `int/edits & guides/planning/guide-set/aw-int_project_todo_list.md`
- `int/edits & guides/planning/guide-set/aw-int_unit_structural_profiles_revised.md`
- `int/edits & guides/planning/guide-set/aw-int_activity_framework.md`
- `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md`
- `int/edits & guides/planning/guide-set/aw-int_qa_checklist.md`

Use supporting notes, baseline audits, and older unit-file baselines only as secondary historical references when a current inconsistency needs tracing.

---

## 4. Main Review Questions

Full review should focus on finished-book questions such as:

1. **Whole-book coherence**
   - Does the book feel internally coherent in sequencing, tone, and support style?

2. **Progression**
   - Does demand rise in a controlled and teachable way from early sentence work to later integrated tasks?

3. **Live/planning alignment**
   - Do the live module files and planning/control documents still describe the same book?

4. **Learner usability**
   - Can a learner actually use the task flow, support layers, revision chains, and later integrated tasks as written?

5. **Editorial readiness for support materials**
   - Is the book stable enough that answer-key, rubric, and sample-response work can begin without moving targets?

---

## 5. Finding Types

During full review, findings should usually fall into one of these categories:

- **Planning/live mismatch**
  - the control documents no longer match the live source

- **Usability gap**
  - the book assumes a learner action, support step, or carry-forward logic that is not clearly supported

- **Calibration / progression issue**
  - a task, unit, or module sits oddly against surrounding difficulty or output expectations

- **Editorial consistency issue**
  - wording, framing, or sequencing is technically acceptable but noticeably uneven at book level

- **New blocker**
  - a newly confirmed issue serious enough to block final support-material work

---

## 6. Severity Levels

Use these severity labels in full-review findings:

- `Revise`
  - should be corrected before the review stage is considered stable

- `Should revise`
  - materially worth fixing, but not a stage blocker on its own

- `Monitor / possible revise`
  - a real question that needs an explicit editorial decision, even if the final decision is to retain it

- `Blocker`
  - significant enough that the book should not proceed to final support-material work until resolved

Do not use `Revise` casually.  
Full review is not meant to recreate an endless cleanup loop.

---

## 7. How Findings Must Be Recorded

Each round of full review should be recorded as a standalone file in:

- `int/edits & guides/full-review`

Recommended naming pattern:

- `aw-int_full-review_round1.md`
- `aw-int_full-review_round2.md`

Each review file should include:

- scope note
- review baseline
- findings first
- file and line references for each finding
- why the issue matters at book level
- recommended action
- short review summary
- next suggested actions

The findings file is the authoritative record of what the round actually discovered.

---

## 8. Relationship To Project Control Files

When full review begins or materially changes state:

- update `int/edits & guides/planning/guide-set/aw-int_project_todo_list.md`
- update `project-learning.md` for durable state changes
- update `project-journal.md` for dated review events

The full-review folder holds the review artifacts themselves.  
The project control files hold project-level state and chronology.

---

## 9. Definition Of Done For Full Review

The intermediate full-review stage is complete when:

1. the live module source set has been reviewed as a whole-book baseline
2. any findings recorded in the full-review files have been:
   - corrected
   - explicitly accepted by editorial decision
   - or deferred with a clear reason
3. no unresolved finding remains severe enough to block answer-key or rubric-support work
4. the project control files explicitly state that full review is complete
5. the project is ready to move to:
   - answer key / sample responses
   - final rubric support
   - combined-draft regeneration

---

## 10. Current Starting Point

At the current project stage:

- this protocol is a forward control document
- the book is still earlier than QA and full review
- the current active work remains structural-profile completion under `INT-3`
- this file defines the review standard in advance so the earlier stages can build toward it deliberately

---

*Document status: source-of-truth protocol for the intermediate-book full-review stage.*
