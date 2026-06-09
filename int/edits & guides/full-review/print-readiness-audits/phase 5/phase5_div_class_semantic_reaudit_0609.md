# Phase 5 Div Class Semantic Re-Audit

Date: 2026-06-09

## Scope

This re-audit checks three issues in the intermediate full-book manuscript:

1. `language` / `learn` divs that may be more accurately classified as `structure`
2. `write` divs that may be more accurately classified as `rewrite` or `revise`
3. the status of `example-bad` / `example-good` relative to the approved core div system

Source references:

- `int/md/working/aw-int-all_0519.md`
- `adv/edits & guides/style edits/step3-div-reclassification/div_class_reclassification_0515.md`
- `adv/edits & guides/style edits/step3-div-reclassification/div_reclassification_full_0516.md`

## Approved Core Class List

The approved core semantic div system is:

- `learn`
- `language`
- `structure`
- `notice`
- `write`
- `rewrite`
- `revise`
- `edit`
- `example`

The current INT manuscript includes all nine approved classes.

## Current INT Class Counts

| Class | Count |
|---|---:|
| `write` | 119 |
| `edit` | 75 |
| `learn` | 67 |
| `example` | 50 |
| `rewrite` | 38 |
| `language` | 34 |
| `notice` | 23 |
| `revise` | 11 |
| `structure` | 8 |
| `example-bad` | 28 |
| `example-good` | 6 |

## High-Level Finding

The INT book now contains the full approved class set, but the distribution still shows semantic drift. The most obvious pattern is that `write` remains much more common than `rewrite`, `revise`, and `structure`, even though several live tasks are not true original drafting. A second pattern is that some lists of document parts, paragraph parts, or text-component sets are still classified as `language` or `learn` even when the primary teaching job is structural organisation.

## 1. `language` / `learn` -> `structure` Candidates

These are the strongest current candidates where the div mainly teaches text organisation, document parts, or a planning framework rather than grammar, vocabulary, or explanatory teaching input.

| Unit | Line | Current | Proposed | Div title | Reason |
|---|---:|---|---|---|---|
| 3 | 683 | `language` | `structure` | `Three-Part Paragraph Structure` | The div teaches paragraph roles `(T) / (S) / (C)` and how a paragraph is organised, not language forms. |
| 4 | 1093 | `learn` | `structure` | `Basic Email Layout` | The main content is the six-part structure of an email and the job of each part. |
| 9 | 2709 | `language` | `structure` | `Notice Structure` | The list gives the parts of a notice in sequence. This is document architecture rather than language systems. |
| 11 | 3237 | `language` | `structure` | `Key Elements of a Meeting Summary` | The div defines the parts of the summary and their function. The phrase list is secondary. |
| 12 | 3614 | `language` | `structure` | `Structure of an External Inquiry` | The numbered list teaches the parts of the inquiry email. The phrase bank is a subordinate support layer. |
| 15 | 4332 | `language` | `structure` | `Standard Email Elements` | The table is organised by email part and associated function. The primary logic is structural. |
| 21 | 6373 | `learn` | `structure` | `A shared team standard usually covers:` | The list names the parts that a team standard should control: opening, tone, body structure, formatting. This is a structural checklist. |

### Retain As `language` or `learn`

These nearby divs may look structural at first glance, but they still fit their current class better:

- Unit 1 `Basic Sentence Pattern` should remain `language`
  - it teaches sentence grammar patterning, not document structure
- Unit 8 `Clear Instruction Verbs` should remain `language`
  - this is a lexical / phrase-support bank
- Unit 21 `Standardising Team Writing` should remain `language`
  - although it includes one `Formatting Standards` subgroup, most of the div is a phrase bank of openings, purpose statements, and closings

## 2. `write` -> `rewrite` / `revise` / `structure` Candidates

These are the strongest current candidates where the main task is not true original drafting.

| Unit | Line | Current | Proposed | Div title | Reason |
|---|---:|---|---|---|---|
| 1 | 147 | `write` | `rewrite` | `Practice: Build Clear Sentences` | The instruction says `Rewrite the word groups as clear SVO or SVC sentences.` The learner transforms supplied content rather than drafting freely. |
| 3 | 729 | `write` | `structure` | `Build a Short Review Summary` | The first task is ordering given sentences into a logical sequence. The short follow-up sentence does not change the primary operation. |
| 6 | 1805 | `write` | `structure` | `Reorder to Make a Clear Update` | The learner orders given sentences into a clear sequence. This matches the advanced `structure` logic for sequencing tasks. |
| 6 | 1823 | `write` | `rewrite` | `Add Supporting Information` | The learner expands bare supplied messages into fuller versions. This is guided transformation, not original drafting. |
| 8 | 2519 | `write` | `structure` | `Add Missing Steps` | The learner completes an existing procedure frame by inserting missing steps. This is procedure completion / structure repair rather than free writing. |
| 10 | 3031 | `write` | `rewrite` | `Add Details` | The learner adds two supporting sentences to a supplied line. The task extends existing text. |
| 12 | 3661 | `write` | `rewrite` | `Add Background Information` | The learner adds background to given inquiry questions. This is sentence-level expansion of supplied material. |
| 13 | 3894 | `write` | `rewrite` | `Add a Reason or Background` | The learner adds specific support to existing main sentences. |
| 14 | 4132 | `write` | `rewrite` | `Add Clarifying Information` | The learner adds acknowledgement and clarification sentences to supplied statements. |
| 20 | 6257 | `write` | `revise` | `Rewrite One Earlier Message` | The task explicitly asks the learner to take an earlier message and recast it for a new document purpose. Because the source is earlier work, `revise` is the stronger semantic fit. |
| 21 | 6584 | `write` | `revise` | `Rewrite the Pair with a New Team Standard` | The learner reworks the earlier two-message set using a new consistency standard. This is revision of an earlier output set. |
| 22 | 6880 | `write` | `revise` | `Rewrite the Three-Document Set` | The learner revises the earlier three-document set with a changed tone or structure. |
| 23 | 7228 | `write` | `revise` | `Homework: Final Course Task` | The task explicitly requires a `third revision`, so `revise` is more accurate than `write`. |

### Retain As `write`

The following patterns may look close to `rewrite`, but they remain correctly classified as original production:

- Guided and freer tasks built from a scenario with no supplied source text
- reflection tasks where the learner writes original notes about their own work
- extension tasks that ask for a new internal note, communication pack, or transfer text based on the learner's own choice

## 3. `example-bad` / `example-good` Status

### Finding

The INT manuscript still contains:

- `example-bad`: 28
- `example-good`: 6

### Interpretation

These do not need to be treated as a separate top-level semantic family.

They can be understood as subtypes of `example`, used when the example itself carries a purposeful weak/strong instructional contrast. That is compatible with the earlier semantic simplification as long as:

- `example` remains the top-level reference class
- `example-bad` / `example-good` are treated as controlled sub-classes for styling or comparison logic
- they are not used in student-judgment tasks where the label itself gives away the answer

### Current risk

This is now less a classification problem than a deployment-control problem. The real question is whether each `example-bad` / `example-good` instance appears in:

- a true model / repair / editing context, where the subtype is acceptable, or
- a comparison-judgment context, where neutral labels are preferable

That second issue has already been reviewed elsewhere in the Phase 5 audit trail and does not need a fresh top-level class change here.

## Summary Judgment

### Confirmed

- the INT book includes the full approved 9-class core system
- `example-bad` and `example-good` can be treated as sub-classes of `example`

### Still weak

- structural teaching content is still underused as `structure`
- transformation and revision tasks are still overabsorbed into `write`
- `revise` is present but underused for explicit reworking of earlier learner output

## Recommended Next Step

Do not bulk-convert classes automatically. Instead:

1. confirm the `language/learn -> structure` candidates above
2. confirm the `write -> rewrite/revise/structure` candidates above
3. apply those source-level corrections in one controlled pass

This will improve the semantic accuracy of the INT div system without reopening the broader completed Phase 5 activity review.

## Implementation Record

The recommended controlled-pass corrections were applied in `int/md/working/aw-int-all_0519.md`.

### Applied `language` / `learn` -> `structure`

- Unit 3 `Three-Part Paragraph Structure`
- Unit 4 `Basic Email Layout`
- Unit 9 `Notice Structure`
- Unit 11 `Key Elements of a Meeting Summary`
- Unit 12 `Structure of an External Inquiry`
- Unit 15 `Standard Email Elements`
- Unit 21 `A shared team standard usually covers:`

### Applied `write` -> `rewrite`

- Unit 1 `Practice: Build Clear Sentences`
- Unit 6 `Add Supporting Information`
- Unit 10 `Add Details`
- Unit 12 `Add Background Information`
- Unit 13 `Add a Reason or Background`
- Unit 14 `Add Clarifying Information`

### Applied `write` -> `structure`

- Unit 3 `Build a Short Review Summary`
- Unit 6 `Reorder to Make a Clear Update`
- Unit 8 `Add Missing Steps`

### Applied `write` -> `revise`

- Unit 20 `Rewrite One Earlier Message`
- Unit 21 `Rewrite the Pair with a New Team Standard`
- Unit 22 `Rewrite the Three-Document Set`
- Unit 23 `Homework: Final Course Task`

## Result

The semantic drift identified in this re-audit has now been reduced at source level. The main remaining class-distribution imbalance is broader and historical rather than tied to these strongest confirmed mismatches.
