# Full Review Protocol
## *Administrative Writing, Advanced*

---

> **Purpose of this document**
> This file defines what the advanced-book **full review** is, what it is not, what source files govern it, how findings should be recorded, and what counts as completion.
>
> This is the source-of-truth definition for the post-`N11` full-review stage.

---

## 1. What Full Review Is

Full review is the first whole-book editorial pass conducted **after** the advanced book has cleared the final `N11` QA gate.

Its purpose is to evaluate the completed live book as a finished learner-facing product rather than as a draft still undergoing structural QA.

It asks questions such as:

- does the book read coherently from Unit 1 to Unit 23
- does progression feel consistent across units and modules
- do tasks, explanations, and review layers work together as a book rather than only as local units
- are there any remaining planning/live mismatches, usability gaps, calibration dips, or editorial inconsistencies significant enough to matter before answer-key work begins

Full review is therefore a **post-QA editorial control stage**, not a drafting stage and not a replacement for `N11`.

---

## 2. What Full Review Is Not

Full review is **not**:

- another `N11` pass
- a prompt-repair campaign by default
- a language-instruction redesign pass by default
- a structural rewrite stage unless the review surfaces a genuine blocker that requires one

`N11` already decided whether the book met the agreed quality gate for entering full review. The authoritative final `N11` record remains:

- `adv/edits & guides/n11/aw-adv_n11_qa_review_round4.md`

Do not reopen `N11` findings by default during full review. Reopen only if new evidence shows that a significant issue remains live in the current source.

---

## 3. Review Baseline And Source Hierarchy

### 3.1 Primary source under review

The object under review is the live advanced `n10` source set:

- `adv/md/n10/aw-adv_mod1_n10.md`
- `adv/md/n10/aw-adv_mod2_n10.md`
- `adv/md/n10/aw-adv_mod3_n10.md`
- `adv/md/n10/aw-adv_mod4_n10.md`
- `adv/md/n10/aw-adv_mod5_n10.md`
- `adv/md/n10/aw-adv_mod6_n10.md`

These files are the finished content baseline for full review.

### 3.2 Supporting control references

Use these as source-of-truth control documents when needed:

- `adv/edits & guides/planning/guide-set/aw-adv_project_todo_list.md`
- `adv/edits & guides/planning/guide-set/aw-adv_unit_structural_profiles_revised.md`
- `adv/edits & guides/planning/guide-set/aw-adv_prompt-writing-policy.md`
- `adv/edits & guides/planning/guide-set/aw-master_activity_menu.md`
- `adv/edits & guides/n11/aw-adv_n11_qa_review_round4.md`

Use older step files, earlier `N11` rounds, and historical issue lists only as secondary historical references when a current inconsistency needs tracing.

---

## 4. Main Review Questions

Full review should focus on the finished-book level questions that remain after `N11`:

1. **Whole-book coherence**
   - Does the book feel internally coherent in sequencing, tone, and expectations?

2. **Progression**
   - Do unit and module demands rise in a way that feels intentional rather than uneven or locally distorted?

3. **Live/planning alignment**
   - Do the live `n10` files and the planning/control documents still describe the same book?

4. **Learner usability**
   - Can a learner or teacher actually use the task flow, review chain, and support structure as written, especially in self-study or interrupted-use contexts?

5. **Editorial readiness for `P4`**
   - Is the book stable enough that answer-key / sample-response work can begin without writing against moving targets?

---

## 5. Finding Types

During full review, findings should usually fall into one of these categories:

- **Planning/live mismatch**
  - the control documents no longer match the live source

- **Usability gap**
  - the book assumes a learner action, teacher mediation, or document carry-forward step that is not clearly supported in the live text

- **Calibration / progression issue**
  - a task or unit sits oddly against the surrounding difficulty or output band

- **Editorial consistency issue**
  - wording, framing, or sequencing is technically acceptable but noticeably uneven at whole-book level

- **New blocker**
  - a newly confirmed issue serious enough to block continuation into `P4`

---

## 6. Severity Levels

Use these severity labels in full-review findings:

- `Revise`
  - should be corrected before the review stage is considered stable

- `Should revise`
  - materially worth fixing, but not a stage blocker on its own

- `Monitor / possible revise`
  - a real question or asymmetry that requires an explicit editorial decision, even if the final decision is to retain it

- `Blocker`
  - significant enough that the book should not proceed to `P4` until resolved

Do not use `Revise` casually. Full review is not meant to recreate an endless cleanup loop.

---

## 7. How Findings Must Be Recorded

Each round of full review should be recorded as a standalone file in:

- `adv/edits & guides/full-review`

Recommended naming pattern:

- `aw-adv_full-review_round1.md`
- `aw-adv_full-review_round2.md`

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

- update `adv/edits & guides/planning/guide-set/aw-adv_project_todo_list.md`
- update `project-learning.md` for durable state changes
- update `project-journal.md` for dated review events

The full-review folder holds the review artifacts themselves.  
The project control files hold the project-level state and chronology.

---

## 9. Definition Of Done For Full Review

The advanced full-review stage is complete when:

1. the live `n10` source set has been reviewed as a whole-book baseline
2. any findings recorded in the full-review files have been:
   - corrected
   - explicitly accepted by editorial decision
   - or deferred with a clear reason
3. no unresolved full-review finding remains severe enough to block answer-key work
4. the project control files explicitly state that full review is complete
5. the project is ready to move to:
   - `P4 — answer key / sample responses`

---

## 10. Current Starting Point

At the time this protocol was created:

- the authoritative final QA gate is `adv/edits & guides/n11/aw-adv_n11_qa_review_round4.md`
- the first full-review findings file is `adv/edits & guides/full-review/aw-adv_full-review_round1.md`
- `P4` remains deferred until the full-review findings are resolved or explicitly accepted

---

*Document status: Source-of-truth protocol for the advanced-book full-review stage.*

