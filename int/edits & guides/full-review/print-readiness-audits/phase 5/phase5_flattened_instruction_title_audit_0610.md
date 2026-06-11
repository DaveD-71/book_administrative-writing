## Phase 5 Flattened Instruction Title Audit

Date: 2026-06-10

Scope:
- `int/md/working/aw-int-all_0519.md`

Purpose:
- identify cases where a div title appears to be a promoted instruction line rather than a true activity or support title
- separate these from normal phrase-bank, checklist, or takeaway blocks that happen to contain only a list

## Definite flattened-title cases

1. Unit 19
- Section: `A. Warm-Up`
- Current div title: `Before You Write Two Texts from One Scenario`
- Issue:
  - this reads as an instruction, not as a stable support-block title
  - the div contains only a list, so the title is doing the job of the missing instruction line
- Recommended repair:
  - replace the title with a non-redundant support title
  - restore the instruction as a sentence below the title

2. Unit 20
- Section: `A. Warm-Up`
- Current div title: `For Connected Documents, Check`
- Issue:
  - this is an imperative checklist instruction promoted into the title
  - the block needs a clearer support title and a separate instruction line
- Recommended repair:
  - replace the title with a support title
  - keep the checklist as the content of the block

3. Unit 22
- Section: `A. Warm-Up`
- Current div title: `Before You Write a Multi-Document Set`
- Issue:
  - same flattening pattern as Units 19 and 20
  - the title is really an instruction line
- Recommended repair:
  - replace the title with a support title
  - restore the instruction as a sentence below the title

## Related structure issue

Unit 22 `C. Language`
- Current div title: `Three Audiences, Three Styles`
- Current internal labels:
  - `(A) Applicant Reply - Polite, supportive, clear`
  - `(B) Colleague Message - Neutral, cooperative`
  - `(C) Internal Notice - Concise, factual`
- Issue:
  - `A / B / C` implies options or answer choices, but this block is not a choice task
  - the labels are not needed because the three audience categories are already named explicitly
- Recommended repair:
  - remove `A / B / C`
  - keep the three audience names as plain bold subheads

## Not the same issue

The following blocks also match the broad `title + list only` surface pattern, but they should not be treated as the same defect without a separate decision:
- phrase banks such as `Useful Phrases for Requests`
- workshop recap blocks such as `Core Takeaways`
- short checklist supports such as `Quick Email Check`, `Quick Accuracy Check`, `Quick Clarity Check`, and `Quick Tone Check`

## Decision for this pass

- repair the three definite flattened-title cases in Units 19, 20, and 22
- repair the related Unit 22 `A / B / C` audience-label issue
