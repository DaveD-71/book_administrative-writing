# Intermediate Round 1 Remediation Plan

## Summary

Address the current `INT-6` Round 1 fail set by fixing the live-text defects first, then removing the remaining control-layer and evidence-gap failures through a strict re-run of the same checklist.

Chosen Unit 21 direction:

- keep Unit 21 focused on applied rewriting and consistency work
- demote style-guide content to short support or transfer material rather than keeping it as the main freer output

## Key Changes

### Module 6 late-book repair

- rebuild Unit 21 so its core outputs stay in the same message-rewrite family from guided through extended work
- replace `Freer Practice - Create a Mini Style Guide` with an applied consistency-writing task using bounded message sets or paired emails
- rewrite Unit 21 Homework so it no longer requires a colleague's email; use learner-owned drafts or provided/earlier-book texts with an explicit fallback
- add explicit `Transfer Extension` sections to Units 21 and 22 in the same visible position used elsewhere in the book
- tighten Unit 22 so the difference between colleague explanation and internal notice is stated and reinforced in the task wording, self-check, and transfer layer

### Whole-book structural and self-study normalization

- normalize section sequencing across the live modules to one stable pattern wherever the current order drifts: guided work before self-check, self-check before freer work, transfer before extended writing, then reflection and homework
- normalize section-heading syntax book-wide so equivalent sections use the same punctuation and naming pattern
- remove hard dependence on real workplace or colleague material from homework and transfer tasks by adding explicit built-in fallbacks using provided unit scenarios or earlier-book texts

### Flagged prompt, option, and support fixes

- revise the flagged freer-practice sets in Units 5, 6, 7, 16, 17, and 18 so each set uses parallel, situation-anchored options with matched detail level, reader type, and output demand
- replace Unit 5's long uneven situation list with a shorter bounded option set
- add or clarify the worked mini-example support in Units 12 and 13 so phrase-bank use is demonstrated inside a full message, not left as list-only support
- tighten Unit 4's freer-task output control so its independent email task has an explicit sentence expectation aligned with the surrounding early-book scaffolding

### Control-layer cleanup after live edits

- update `aw-int_unit_structural_profiles.md` only after the live edits are complete
- remove or resolve every current `before sign-off` / `later revision should check` flag that the edits actually close
- keep only genuinely still-open risks; do not leave stale caution flags in place once the corresponding live text has been repaired
- re-run `aw-int_qa_review_round1.md` from the files, not from inherited earlier labels

## QA Re-Run / Acceptance Tests

- re-run the binary `Pass` / `Fail` checklist against the six live module files after all edits
- confirm:
  - Unit 21 no longer uses a style-guide document as its main freer output
  - Units 21 and 22 both contain explicit visible transfer sections in the standardized late-book position
  - no homework or transfer task requires inaccessible colleague or workplace material without a built-in fallback
  - Units 5, 6, 7, 16, 17, and 18 no longer carry unresolved option-parallelism issues
  - Units 12 and 13 visibly include the needed worked mini-example support
  - Unit 9 no longer places self-check ahead of guided practice
  - heading syntax and section-order conventions are normalized enough for `5E.1` and `5E.2` to be rejudged from the files
  - `python scripts/check_mojibake.py` still returns clean

## Assumptions And Defaults

- Unit 21 will be repaired with the minimal structural change needed to restore task-family coherence
- the target is to clear the current Round 1 fail families without reopening `INT-5A` or redesigning the book's overall structure
- later-stage items (`P3`, `P4`, `P5`, `P6`) remain deferred and are only checked for correct tracking
