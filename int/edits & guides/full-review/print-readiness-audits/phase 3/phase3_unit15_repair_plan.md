# Phase 3 Unit 15 Repair Plan

Source: `int/md/working/aw-int-all_0519.md`

Answer key: `int/md/working/aw-int-answer-key.md`

Unit: Unit 15. Maintaining Consistent Email Style

Date: 2026-06-08

## Assessment Summary

Unit 15 is structurally stable at the visible-shell level:

- visible sequence is `A B C D E F G H`
- div balance is stable
- placeholders use explicit `rows=N`
- no duplicate placeholder IDs were found
- no stale generic labels such as `Write Here`, `Use this box`, `Homework Draft`, or `Transfer Extension` remain

The remaining issues are Phase 3 quality issues rather than first-pass shell issues.

## Findings

### 1. `A. Warm-Up` is front-loaded with explanation

Current order:

1. `Email Consistency Basics`
2. `Identify the Inconsistencies`

The learner task should lead, with the concept framing supporting it afterward.

### 2. The first `H` task contains two outputs in one compact response box

`Mini Team Style Rules` currently asks students to:

- write three team style rules
- revise one Activity E email to match those rules

These are distinct outputs, but they are pushed into one `rows=5` box. That weakens the task boundary and under-sizes the response space.

### 3. `H. Homework & Extension` contains two distinct transfer layers

The visible `H` layer should keep both tasks because they are not duplicates:

- the first develops a team-level style rule set plus applied revision
- the second asks for a real-message or scenario-based rewrite

The distinction should be preserved and clarified in the answer key.

### 4. `G` and `H` answer-key guidance is too compressed

The answer key should reflect:

- the reflection prompts in `G`
- the two-output structure of the first `H` task
- the separate homework clarification / rewrite purpose in the second `H` task

## Repair Plan

### Markdown source

1. Rework `A. Warm-Up` so the learner task leads the section.
2. Move the concept framing so it supports the task instead of pre-empting it.
3. Keep both `H` subactivities because they serve distinct transfer functions.
4. Split the first `H` task into separate response spaces for team rules and the revised email.
5. Recheck placeholder sizing after the `H` split.

### Answer key

1. Keep `B-F` aligned with the current live tasks.
2. Expand `G` guidance so it reflects the actual reflection prompts.
3. Expand `H` guidance so the first `H` task covers both team rules and applied revision, and the second `H` task explicitly covers the real-message or scenario-based rewrite.

## Verification Targets After Repair

- visible sequence remains `A B C D E F G H`
- `A. Warm-Up` opens with the learner task
- the two `H` tasks remain distinct and readable
- the first `H` task uses separate response spaces for its two outputs
- placeholders remain inside the correct divs
- answer-key labels and guidance match the repaired unit
