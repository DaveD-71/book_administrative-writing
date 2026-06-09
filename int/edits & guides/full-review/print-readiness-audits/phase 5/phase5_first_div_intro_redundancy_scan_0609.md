# Phase 5 First-Div Intro Redundancy Scan

Date: 2026-06-09

Source:
- `int/md/working/aw-int-all_0519.md`
- Phase 5 standard in `int/edits & guides/full-review/aw-int_print_readiness_repair_plan_0530.md`

Scope:
- full INT manuscript
- focused scan for sections where a visible heading is followed immediately by a short `notice` or `learn` div
- target pattern: the first div mainly introduces the next block rather than functioning as the main activity block itself

Inclusion rule:
- the heading is followed immediately by a `notice` or `learn` div
- that first div has no placeholder
- another div follows immediately after it
- the first div is short and mostly acts as a lead-in to the next content block

Exclusion rule:
- the first div is itself the main example/model block
- the first div is a substantive `language`, `edit`, `write`, or other activity block that is already doing the main work of the section
- the first div contains the real response task rather than only setting it up

## Overall Judgment

This pattern occurs often enough to justify a dedicated cleanup pass.

Main repeated pattern:
- a section heading is immediately followed by a thin `notice` or `learn` div
- that div gives a short instruction or comparison lead-in
- the real content begins only in the next div
- the result is unnecessary micro-fragmentation and extra semantic styling where plain section-intro text would usually be clearer

The strongest cleanup candidates are `B. Example Check` sections and module-review comparison sections.

## High-Confidence Matches

These sections match the pattern cleanly and are good candidates for removing the first intro div or converting its content to plain text under the heading.

### Example Check Sections

- `Unit 1` `B. Example Check`
  - line: `86`
  - first div: `notice`
  - next div: `notice`
  - issue: two thin intro/support divs appear before the real example material; at least the first one is redundant as a styled block

- `Unit 2` `B. Example Check`
  - line: `385`
  - first div: `learn`
  - next div: `example-bad`
  - issue: the first `learn` div is a short lead-in to the model comparison, not a separate activity

- `Unit 5` `B. Example Check`
  - line: `1419`
  - first div: `learn`
  - next div: `example-bad`
  - issue: the first `learn` div only introduces the weak/strong comparison

- `Unit 16` `B. Example Check`
  - line: `4742`
  - first div: `learn`
  - next div: `example-bad`
  - issue: the first `learn` div is only `Why Accuracy Matters to the Reader / Compare:`

- `Unit 17` `B. Example Check`
  - line: `5073`
  - first div: `learn`
  - next div: `example-bad`
  - issue: the first `learn` div is only `Why the Clearer Version Works / Compare:`

- `Unit 18` `B. Example Check`
  - line: `5370`
  - first div: `learn`
  - next div: `example-bad`
  - issue: the first `learn` div is only `Why the Softer Version Works / Compare:`

### Module Review Comparison Sections

- `Module 1 Review Workshop` `Weak vs. Strong Review Case`
  - line: `891`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div is only a comparison lead-in before the actual example set

- `Module 3 Review Workshop` `Reader-Purpose Comparison`
  - line: `3450`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div introduces the comparison but does not need to be a separate styled block

- `Module 4 Review Workshop` `Audience-Control Comparison`
  - line: `4568`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div is a short lead-in before the example pair

- `Module 5 Review Workshop` `Revision Comparison`
  - line: `5681`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div only frames the comparison task

- `Module 6 Review Workshop` `Multi-Document Comparison`
  - line: `7307`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div introduces the two-text comparison but is not doing distinct support work

### Warm-Up Comparison Sections With Example Immediately After

- `Unit 3` `A. Warm-Up`
  - line: `668`
  - first div: `notice`
  - next div: `example`
  - issue: the first div is a short prompt before the paragraph examples; likely clearer as plain intro text under the heading

- `Unit 4` `A. Warm-Up`
  - line: `1046`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div is only a short comparison instruction before the email models

- `Unit 8` `A. Warm-Up`
  - line: `2444`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div is only a short prompt before the procedure models

- `Unit 11` `A. Warm-Up`
  - line: `3219`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div is only a short comparison prompt before the summary models

- `Unit 12` `A. Warm-Up`
  - line: `3603`
  - first div: `notice`
  - next div: `example-bad`
  - issue: the first div is only a short comparison prompt before the inquiry-email models

## Borderline Cases

These also show the pattern, but the first div may be carrying enough real task framing that it should be reviewed manually before any cleanup.

- `Unit 2` `A. Warm-Up`
  - line: `359`
  - first div: `notice`
  - next div: `learn`
  - note: the first div contains the row-choice task and the table, so it may be functioning as the real warm-up rather than only an intro

- `Unit 9` `A. Warm-Up`
  - line: `2691`
  - first div: `notice`
  - next div: `learn`
  - note: the first div already contains the compare task plus the first notice text, so this is less clearly redundant than the other warm-up cases

## Cleanup Recommendation

Default fix pattern:
- keep the visible section heading
- move the lead-in sentence or short instruction out of the first `notice` or `learn` div
- place that lead-in as plain text directly under the heading
- keep the next div only if it carries the real example, model, or teaching content

Where two thin intro divs stack, as in `Unit 1 B. Example Check`:
- convert the first intro layer to plain text
- then review whether the second support div should remain, merge with the heading intro, or be absorbed into the explanation after the example

Expected benefit:
- fewer micro-divs
- clearer section flow
- less redundant semantic styling
- cleaner separation between section introduction and real activity content

## Implementation Result

Applied on 2026-06-09 in `int/md/working/aw-int-all_0519.md`.

Implemented:
- all high-confidence matches listed above were repaired by removing the redundant first intro div and keeping the real example/model content in place

Left unchanged on purpose:
- `Unit 2` `A. Warm-Up`
- `Unit 9` `A. Warm-Up`

Reason for leaving these two:
- in both cases, the first `notice` div still carries the real warm-up task plus the first content layer, so removing it would not be a clean redundancy fix

Post-edit verification:
- the conservative redundancy scan now returns only those two borderline cases
- manuscript div balance remains valid: `opens=461`, `closes=461`

## Follow-Up Boundary Check: Sections A And B

After the initial redundancy cleanup, a second pass checked all unit `A. Warm-Up` and `B. Example Check` pairs for a deeper structural problem:

- `A` carrying most of the model-analysis or teaching load
- `B` reduced to a short explanation or debrief
- the warm-up / example-check boundary therefore collapsing

### Confirmed structural problem

- `Unit 9`
  - status: `repaired`
  - issue: `A. Warm-Up` carried the notice pair, the compare task, the concept definition, and the checklist, while `B` only explained why Notice B worked
  - action taken: `A` was rewritten as a short activation task, the notice pair moved into `B`, and the concept/checklist support moved into `C`

### Comparable problems found

- `Unit 4`
  - status: `repaired`
  - issue: `A. Warm-Up` carries the model pair plus `Basic Email Layout` and `Quick Email Check`, while `B` is only the explanation of why Email B works better
  - action taken: `A` was rewritten as a short activation task with a response space, the email pair stayed in `B`, and the layout/checklist support moved into `C`

- `Unit 21`
  - status: `repaired`
  - issue: `A. Warm-Up` carries the compare task, the reasons inconsistency matters, and the team-standard coverage list, while `B` is only the explanation of why consistency helps
  - action taken: `A` was rewritten as a short standard-setting task with a response space, the email comparison stayed in `B`, and the broader consistency-support material moved into `C`

### Lighter drift, but not the same fundamental problem

- `Unit 11`
  - `A` includes two short support notes, but `B` still contains a real example block plus the explanation layer

- `Unit 12`
  - `A` includes one concept note, but `B` still contains a real example block plus the explanation layer

### Not treated as comparable in this pass

- `Unit 2`
  - user-reviewed and accepted as-is

- `Units 19, 20, 22, 23`
  - these units have thin `B` sections, but the pattern is different: `A` is scenario activation or selection work, not a collapsed model-comparison block

### Current follow-up status

- confirmed repaired in this pass: `Units 4, 9, 21`
- lighter drift still worth later review: `Units 11, 12`

## Additional Phase 5 Rule: Neutral Labels In Student-Judgment Comparisons

Problem:
- in several units and review workshops, students were asked to decide which example was better, clearer, stronger, or more useful
- however, the source had already classified the examples as `example-bad` / `example-good` and sometimes labeled them visibly as `Weak` / `Stronger`, `Inconsistent` / `Consistent`
- that classification effectively answered the task before the student did the comparison

Rule:
- when a student must judge between two example texts, both examples should use neutral styling and neutral visible labels
- preferred labels are `Version A / Version B`, `Email A / Email B`, `Notice A / Notice B`, `Summary A / Summary B`, or another neutral pair that matches the task
- reserve `example-bad`, `example-good`, `Weak`, `Stronger`, `Inconsistent`, and `Consistent` for sections where the student is not being asked to make that judgment independently, such as explicit model presentation or repair work

Implementation result:
- comparison tasks across the manuscript were neutralized in the source
- affected areas included Unit-level comparison activities and Module 1-5 and Module 6 comparison workshops
- Module 1 workshop title was also neutralized from `Weak vs. Strong Review Case` to `Review Case Comparison`

Verification:
- no remaining comparison task now depends on visible `example-bad` / `example-good` labels to present the paired texts
- remaining `example-bad` / `example-good` usage is limited to true model, repair, or editing contexts
