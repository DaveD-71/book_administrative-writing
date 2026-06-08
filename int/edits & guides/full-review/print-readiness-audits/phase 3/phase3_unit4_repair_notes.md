# Phase 3 Unit 4 Repair Notes

Source: `int/md/working/aw-int-all_0519.md`

Unit: Unit 4. Email Layout and Standard Phrases

Date: 2026-06-03

## Summary

Unit 4 was reviewed after an external Claude Code edit pass. The visible shell and most Phase 3 repairs were already in place, but a follow-up consistency check against the Module 1 repair standard found several remaining issues: the strong email model did not fully show the six-part email structure, one editing activity contained a nested example div, adjacent teaching blocks repeated the same purpose, and a few small response-label/title patterns remained.

## Repairs Applied

- Kept the visible unit shell as `A. Warm-Up`, `B. Example Check`, `C. Language`, `D. Guided Practice`, `E. Freer Practice`, `F. Editing Practice`, `G. Self-Check and Reflection`, and `H. Transfer and Homework`.
- Added a clear closing sentence to Email B so the model shows the taught six-part email structure: subject line, greeting, opening sentence, body/question, closing sentence, and sign-off.
- Updated the `Why Email B Works Better` teaching block so it describes the closing sentence and sign-off correctly.
- Merged the redundant `Why This Works` block into the main B teaching block.
- Tightened the language section labels:
  - changed internal bold title rows into short prose where possible
  - renamed `Useful Phrases` to `Opening Purpose Phrases`
  - renamed `Teaching Point` to `Opening Sentence Job`
- Removed leftover `Write your email:` response labels where the activity already had a clear scaffold or response placeholder.
- Flattened the nested `example-bad` div in `F. Editing Practice` so the original email is a sibling example block, followed by a separate edit response div.
- Updated the Unit 4 answer key so Email B guidance and the D model email match the revised source and the Ms. Kim scenario.

## Follow-Up Cleanup - 2026-06-03

- Unit 4 was briefly flattened to reduce list density, but that approach was reversed after review.
- Restored vocabulary, phrase, example, and structural-support lists because these lists help intermediate learners scan and reuse language.
- Follow-up decision: address excessive list density through layout, spacing, and local redundancy checks rather than flattening useful vocabulary or phrase lists into prose.
- Answer key update was not required for this cleanup because activity prompts, item numbering, expected outputs, and model answers did not change.

## Verification

- Visible heading sequence: `ABCDEFGH`.
- Unit-level fenced div balance: 22 opens / 22 closes.
- Unit-level nested div scan: none found.
- Whole-manuscript fenced div balance: 551 opens / 551 closes.
- Unit placeholders: 16 total, all with explicit `rows=N`.
- Duplicate placeholder IDs in Unit 4: none.
- Duplicate placeholder IDs in the whole manuscript: none.
- Unit 4 stale-label scan: no `Write Here`, `Use this box`, `Write Your Revised Version`, `Homework Draft`, `SVO-style`, `lower-level`, `Why This Works`, `Teaching Point`, or `Write your email:` remains.

## Phase 3 Checklist Result

- Focus alignment: pass. Activities support identifying email parts, writing subject lines, and writing complete professional emails.
- Activity sequencing: pass. The unit follows warm-up -> example -> language -> guided practice -> freer practice -> editing -> self-check/reflection -> transfer/homework.
- Instruction quality: pass after follow-up cleanup. Production tasks name the source or situation and keep response spaces inside the activity.
- Intermediate learner readability: pass. Technical and editor-facing wording from the old draft is removed.
- Formatting and Markdown: pass. No nested divs remain in Unit 4, and generic response labels have been removed.
- Response-space calibration: pass. Item-level language tasks use short boxes and full-email tasks use larger PH-3 boxes.
- Answer-key alignment: pass. The Unit 4 answer key now reflects the revised model email and scenario.

## Carry-Forward Notes

- When a unit teaches a named document structure, the primary model must visibly include every part in that structure. Do not rely on answer-key prose to supply a missing model component.
- Avoid nested semantic divs. If a task needs both an instruction wrapper and a styled example, use sibling divs and keep the response placeholder inside the relevant production/edit div.
- Adjacent `learn` blocks with generic titles such as `Why This Works` should be merged when they explain the same model or principle.
