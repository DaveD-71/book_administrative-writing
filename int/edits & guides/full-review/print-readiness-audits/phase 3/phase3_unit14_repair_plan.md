# Phase 3 Unit 14 Repair Plan

Source: `int/md/working/aw-int-all_0519.md`

Answer key: `int/md/working/aw-int-answer-key.md`

Unit: Unit 14. Responding to Confusion

Date: 2026-06-08

## Assessment Summary

Unit 14 is structurally stable at the visible-shell level:

- visible sequence is `A B C D E F G H`
- div balance is `15 opens / 15 closes`
- placeholders total `18`
- all placeholders have explicit `rows=N`
- no duplicate placeholder IDs were found
- no stale generic labels such as `Write Here`, `Use this box`, `Homework Draft`, or `Transfer Extension` remain

The remaining issues are Phase 3 quality issues rather than first-pass shell issues.

## Findings

### 1. `A. Warm-Up` is front-loaded with explanation

Current order:

1. `Responding to Confusion Basics`
2. `What Is the Confusion?`

The learner task should lead, with the concept framing supporting it afterward.

### 2. `H. Homework & Extension` contains two related but distinct transfer layers

`Clarification for a Team Record` and `Homework Task` are not simple duplicates:

- the first creates an internal record of the confusion and correct information
- the second writes the actual polite corrective response

That distinction is pedagogically useful and should stay, but the answer key needs to reflect both functions more explicitly.

### 3. `G` and `H` answer-key guidance is too compressed

The answer key should reflect:

- the reflection prompts in `G`
- the internal-record purpose in the first `H` task
- the real-message or scenario-based clarification-response purpose in the homework task

### 4. Warm-up placeholders should be rechecked

The `U14-warmup-confusion-*` boxes are all `rows=1`. They may be adequate, but their fit should be considered after the warm-up wording is finalized.

## Repair Plan

### Markdown source

1. Rework `A. Warm-Up` so the learner task leads the section.
2. Move the concept framing so it supports the task instead of pre-empting it.
3. Keep both `H` subactivities because they serve distinct transfer functions.
4. Recheck warm-up placeholder sizes after the opening flow is repaired.

### Answer key

1. Keep `B-F` aligned with the current live tasks.
2. Expand `G` guidance so it reflects the actual reflection prompts.
3. Expand `H` guidance so both the team-record task and the homework clarification-response task are explicitly covered.

## Verification Targets After Repair

- visible sequence remains `A B C D E F G H`
- `A. Warm-Up` opens with the learner task
- the two `H` tasks remain distinct and readable
- placeholders remain inside the correct divs
- answer-key labels and guidance match the repaired unit
