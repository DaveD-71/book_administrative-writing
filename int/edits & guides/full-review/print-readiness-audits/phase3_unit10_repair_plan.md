# Phase 3 Unit 10 Repair Plan

Source: `int/md/working/aw-int-all_0519.md`

Answer key: `int/md/working/aw-int-answer-key.md`

Unit: Unit 10. Explaining Problems Clearly

Date: 2026-06-08

## Assessment Summary

Unit 10 is structurally stable at the visible-shell level:

- visible sequence is `A B C D E F G H`
- div balance is `16 opens / 16 closes`
- placeholders total `18`
- all placeholders have explicit `rows=N`
- no duplicate placeholder IDs were found
- no stale generic labels such as `Write Here`, `Use this box`, `Homework Draft`, or `Transfer Extension` remain

The remaining issues are Phase 3 quality issues rather than first-pass shell issues.

## Findings

### 1. `A. Warm-Up` is front-loaded with explanation

Current order:

1. `Problem Explanation Basics`
2. `Identify the Missing Information`

This weakens the book-wide `A. Warm-Up` pattern. The learner task should lead, with the concept framing supporting it.

### 2. `H. Homework & Extension` is still redundant

Current `H` contains two overlapping transfer tasks:

- `Problem Note for a Manager`
- `Homework Task`

Both ask for a rewrite or fresh explanation using the same unit structure. Their functions are not distinct enough to justify two full productive tasks.

### 3. `G` and `H` answer-key guidance is too compressed

The answer key currently gives only broad notes for `G` and `H`. This is thinner than the current project standard and should be expanded to reflect the actual reflection prompts and the final transfer design.

### 4. Warm-up response spaces should be rechecked

The `U10-warmup-missing-*` placeholders are all `rows=1`. That may be enough for short questions, but it should be verified after the warm-up is reordered and the final prompt wording is settled.

## Repair Plan

### Markdown source

1. Rework `A. Warm-Up` so the learner task leads the section.
2. Reposition `Problem Explanation Basics` so it supports the task instead of pre-empting it.
3. Simplify the `A` prompt flow so the learner action is clearer.
4. Consolidate `H. Homework & Extension` into one distinct transfer task.
5. Recheck `A` and `H` placeholder row counts after the content repair.

### Answer key

1. Keep `D`, `E`, and `F` aligned with the current live tasks.
2. Expand `G` guidance to reflect the actual self-check and reflection prompts.
3. Rewrite `H` guidance to match the repaired single transfer task.

## Verification Targets After Repair

- visible sequence remains `A B C D E F G H`
- `A. Warm-Up` opens with the learner task
- `H` no longer contains overlapping full-output tasks
- placeholders remain inside the correct divs
- row counts match final task demand
- answer-key labels and guidance match the repaired unit
