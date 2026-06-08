# Phase 3 Unit 9 Repair Plan

Source: `int/md/working/aw-int-all_0519.md`

Answer key: `int/md/working/aw-int-answer-key.md`

Unit: Unit 9. Internal Notices

Date: 2026-06-08

## Assessment Summary

Unit 9 is structurally stable at the visible-shell level:

- visible sequence is `A B C D E F G H`
- div balance is `18 opens / 18 closes`
- placeholders total `15`
- all placeholders have explicit `rows=N`
- no duplicate placeholder IDs were found
- no stale generic labels such as `Write Here`, `Use this box`, `Homework Draft`, or `Transfer Extension` remain

The remaining issues are Phase 3 quality issues rather than first-pass shell-repair issues. The main problems are:

- `A. Warm-Up` is not functioning cleanly as the book-standard opening activity
- `H. Homework & Extension` is still redundant
- the answer key is not fully aligned with the live task details
- some response-space sizing should be reconsidered after the transfer layer is simplified

## Findings

### 1. `A. Warm-Up` is front-loaded with explanation instead of opening with the learner task

Current order:

1. `Internal Notice Basics`
2. `Which Notice Is Clearer?`
3. `Quick Notice Check`

This weakens the book-wide `A. Warm-Up` standard and the activity-framework expectation that the opening should make the target visible through a bounded comparison before the main teaching begins.

Phase 3 implication:

- keep `A. Warm-Up` as the visible opening activity
- lead with the contrastive notice-comparison task
- move the concept primer and short notice checklist so they support the warm-up instead of pre-empting it

### 2. `A` contains redundant prompt signaling that should be simplified

Examples:

- `Which Notice Is Clearer?` already signals the comparison task, so `**Discussion:**` is unnecessary
- the follow-up question can be folded into one direct learner instruction

Phase 3 implication:

- rewrite the A-level prompt flow as input -> action -> short output/discussion requirement
- remove extra prompt labels when the div title already identifies the task

### 3. `H. Homework & Extension` still duplicates the transfer demand

Current `H` contains two overlapping productive tasks:

- `From Notice to Bulletin`
- `Homework Task`

Both ask learners to take a short notice and produce a stronger or longer internal message using the same unit structure.

Phase 3 implication:

- consolidate `H` into one clear transfer/homework design, or
- keep two tasks only if their functions are clearly distinct, for example:
  - one in-book extension of a unit notice into a fuller bulletin
  - one real-world homework task based on an external or authentic notice

At the moment the distinction is not strong enough.

### 4. The answer key is not fully aligned with the live guided-practice task

Live `D. Guided Practice` situation:

- system update tomorrow
- time window `9:00-12:00`
- certain functions may be unavailable

Current answer-key guidance:

- `System maintenance this weekend`

This is a direct alignment failure under Section `6.7 Answer-key alignment` of the repair plan because the model guidance does not match the revised manuscript task.

Phase 3 implication:

- update the guided-practice answer-key guidance to match the actual live scenario
- confirm that `E`, `G`, and `H` guidance also matches the repaired task purposes after Unit 9 editing

### 5. `G` and `H` answer-key guidance is too compressed for the current activity purposes

Current answer-key treatment:

- `G` is reduced to a short generic summary
- `H` is reduced to a broad open-ended note

That is serviceable but thinner than the current project standard when tasks have specific structure expectations.

Phase 3 implication:

- keep open-ended tasks open-ended
- but make the guidance reflect the actual unit prompts, expected structure, and transfer purpose more explicitly

### 6. Placeholder sizes should be rechecked after the `H` rewrite

Current notable placeholders:

- `U09-reflection | rows=4`
- `U09-transfer-response | rows=6`
- `U09-homework-document | rows=8`

These may be acceptable or may become mismatched depending on how `H` is consolidated. The row-count decision should follow the content repair, not precede it.

## Repair Plan

### Markdown source

1. Rework `A. Warm-Up` so the contrastive notice task leads the section.
2. Reposition `Internal Notice Basics` and `Quick Notice Check` so they support the warm-up and `B/C` progression instead of front-loading explanation.
3. Simplify the warm-up instruction language and remove redundant labels such as `Discussion:` where the div title already signals the task.
4. Review `B` and the early `C` flow to make sure the learner move is:
   - compare
   - notice why the stronger text works
   - identify the structural parts
   - rewrite for neutrality and clarity
5. Consolidate `H. Homework & Extension` into a cleaner transfer design with distinct function and less duplication.
6. Re-size `G/H` placeholders only after the final task shapes are settled.

### Answer key

1. Update `D. Guided Practice` so the scenario and model guidance match the live task exactly.
2. Re-check `E. Freer Practice` guidance against the final repaired task wording.
3. Expand `G` guidance enough to reflect the actual reflection prompts.
4. Rewrite `H` guidance to match the repaired transfer/homework design.

## Verification Targets After Repair

- visible sequence remains `A B C D E F G H`
- `A. Warm-Up` opens with the learner-facing comparison task, not the concept primer
- no redundant prompt labels remain when the activity title already defines the task
- `H` no longer contains overlapping full-output tasks
- placeholders remain inside the correct activity divs
- row counts match the final task demand
- answer-key activity labels and scenario details match the repaired unit
- open-ended answer-key guidance remains guidance, not a fixed required answer
