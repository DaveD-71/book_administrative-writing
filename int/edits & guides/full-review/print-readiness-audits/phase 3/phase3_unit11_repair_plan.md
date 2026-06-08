# Phase 3 Unit 11 Repair Plan

Source: `int/md/working/aw-int-all_0519.md`

Answer key: `int/md/working/aw-int-answer-key.md`

Unit: Unit 11. Writing Simple Meeting Summaries

Date: 2026-06-08

## Assessment Summary

Unit 11 is structurally stable at the visible-shell level:

- visible sequence is `A B C D E F G H`
- placeholders all have explicit `rows=N`
- no duplicate placeholder IDs were found in the unit
- no stale generic labels such as `Write Here`, `Use this box`, `Homework Draft`, or `Transfer Extension` remain

The remaining issues are Phase 3 quality issues rather than first-pass shell issues.

## Findings

### 1. `A. Warm-Up` is front-loaded with explanation

Current order:

1. `Meeting Summary Basics`
2. `Which Summary Is Clearer?`
3. `A Useful Meeting Summary`

The learner comparison task should lead, with the explanation supporting it afterward.

### 2. `A` contains redundant prompt signaling

The `Discussion:` label is unnecessary because the activity title and task already define the learner action.

### 3. `H. Homework & Extension` is still redundant

Current `H` contains two overlapping transfer tasks:

- `Summary for a Manager`
- `Homework Task`

Both are end-of-unit transfer tasks built on the same summary structure and should be consolidated into one clearer transfer layer.

### 4. `G` and `H` answer-key guidance is too compressed

The answer key guidance for reflection and transfer should reflect the actual prompts and the final transfer purpose more explicitly after repair.

## Repair Plan

### Markdown source

1. Rework `A. Warm-Up` so the learner comparison task leads the section.
2. Move the concept framing and summary-quality explanation so they support the task instead of pre-empting it.
3. Remove the redundant `Discussion:` label and simplify the opening prompt flow.
4. Consolidate `H. Homework & Extension` into one distinct transfer task.

### Answer key

1. Update `A` naming if the opening activity title changes.
2. Expand `G` guidance so it reflects the real reflection prompts.
3. Rewrite `H` guidance to match the repaired single transfer task.

## Verification Targets After Repair

- visible sequence remains `A B C D E F G H`
- `A. Warm-Up` opens with the learner comparison task
- `H` no longer contains overlapping full-output tasks
- placeholders remain inside the correct divs
- answer-key labels and guidance match the repaired unit
