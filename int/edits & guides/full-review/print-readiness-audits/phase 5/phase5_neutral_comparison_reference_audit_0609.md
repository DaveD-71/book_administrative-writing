# Phase 5 Neutral Comparison Reference Audit

Date: 2026-06-09

Source:
- `int/md/working/aw-int-all_0519.md`
- `int/md/working/aw-int-answer-key.md`

Scope:
- audit of comparison-task wording after neutralizing `example-bad` / `example-good` in student-judgment activities
- focus on whether follow-up wording still depends on the old judgment labels

## Why This Audit Was Needed

A first repair pass neutralized student-judgment comparison pairs by changing:

- `example-bad` / `example-good` -> `example`
- visible labels such as `Weak / Stronger` or `Inconsistent / Consistent` -> neutral labels such as `Version A / Version B`, `Email A / Email B`, `Notice A / Notice B`

That created a follow-up risk:
- later explanation lines or support notes could still refer to `the stronger version`, `the weak version`, or similar wording
- if the visible labels had been removed, those references could become unclear or broken

## Audit Method

### Step 1. Identify the changed comparison-label families

Neutral comparison labels now used in the manuscript include:

- `Version A / Version B`
- `Email A / Email B`
- `Notice A / Notice B`
- `Summary A / Summary B`
- `Question A / Question B`
- `Update A / Update B`
- `Request A / Request B`
- `Sentence A / Sentence B`
- `Message A / Message B`

### Step 2. Build a broader term family to check

The scan did not stop at `stronger`.

The following term families were reviewed:

- `weak`
- `strong`
- `stronger`
- `weaker`
- `better`
- `worse`
- `consistent`
- `inconsistent`
- `consistency`
- `inconsistency`

Also checked:

- explicit phrases such as `stronger version`, `weak version`, `stronger question`, `stronger update`

### Step 3. Classify findings

Each occurrence was treated as one of:

- `broken label-reference risk`
- `valid generic pedagogy`
- `valid explicit model / repair context`
- `valid reflection / self-comparison language`

## Confirmed Broken Label-Reference Risks

These were the cases where follow-up wording depended on removed judgment labels and therefore needed repair.

### Repaired in this pass

- `Unit 2`
  - `Version B is better because...`

- `Unit 5`
  - `Why Question B Works Better`
  - explanation now refers to `Question A / Question B`

- `Unit 6`
  - `Why Update B Works Better`
  - explanation now refers to `Update A / Update B`

- `Unit 7`
  - `Request B sounds cooperative...`

- `Unit 10`
  - explanation now refers to `Version B`

- `Unit 13`
  - explanation now refers to `Version B`

- `Unit 16`
  - explanation now refers to `Sentence B`

- `Unit 17`
  - explanation now refers to `Version B`

- `Unit 18`
  - explanation now refers to `Message B`

### Comparison-task labels neutralized in source

Comparison tasks using neutral div class `example` and neutral visible labels were confirmed in:

- Module 1 Review Workshop
- Module 2 Review Workshop
- Module 3 Review Workshop
- Module 4 Review Workshop
- Module 5 Review Workshop
- Module 6 Review Workshop
- Units 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 21

## Valid Generic Pedagogy

These uses still contain words like `weak`, `stronger`, or `better`, but they are not broken references to removed labels.

Examples:

- module-guide prose such as:
  - `compare a weaker version with a stronger version`
  - `read the explanation about why the stronger version works`

- discussion prompts such as:
  - `Which paragraph is better organised, and why?`

- explanation prose such as:
  - `Paragraph A is stronger because...`
  - `Paragraph B is weaker because...`

Judgment:
- these are acceptable when the prose itself identifies the judged item clearly or when the statement appears after the comparison has already been completed

## Valid Explicit Model / Repair Context

These uses should remain as-is because the student is not being asked to decide independently between two neutral examples.

Examples:

- `Weak Draft`
- `Improve the Weak Draft`
- `Possible Stronger Version`
- `Weak Email`
- `Weak Notice`
- `Weak Response`
- `Weak external draft`
- `Weak internal draft`
- `Mini contrast - Weak / Stronger`

Judgment:
- these are genuine teaching, editing, or repair contexts
- the source is intentionally identifying a poor or improved model
- these are not defects under the neutral-comparison rule

## Valid Reflection / Self-Comparison Language

These uses are acceptable because they refer to the student's own revision process rather than to a now-neutralized example pair.

Examples:

- `write the weak version`
- `write the stronger version`
- `one line explaining why the stronger version is easier for the reader`

Judgment:
- acceptable as self-comparison language
- not a broken reference, because the learner is producing both states themselves

## Findings Summary

### Rule confirmed

When the activity asks the student to decide which example is better, the examples must not be pre-labeled as `good` / `bad`, `weak` / `stronger`, or `consistent` / `inconsistent`.

### Secondary rule confirmed

After neutralizing the pair labels, every follow-up explanation in that same local activity must be checked for dependency on the old labels.

### Practical result

- the broken local reference-chain problem was real
- it was broader than the single phrase `stronger version`
- the follow-up repairs were applied where the label dependency was local and concrete

## Remaining Residual Risk

Low residual risk remains in broad module-guide or metaprompt language where `weaker`, `stronger`, `better`, or `weak` are still used generically.

Current judgment:
- these are not current source defects
- but if a later Phase 5 language-simplification pass is done, they are good candidates for consistency review

## Recommended Next-Time Rule

Whenever a comparison pair is relabeled from judgment labels to neutral labels:

1. identify the exact visible labels changed
2. derive a term family from those labels
3. scan the local activity and nearby explanation blocks for dependent wording
4. repair the explanation so it points to the neutral labels directly
5. then distinguish:
   - true broken reference chains
   - valid model/repair uses
   - valid generic pedagogy
