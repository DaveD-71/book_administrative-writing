# Phase 3 Unit 5 Repair Notes

Source: `int/md/working/aw-int-all_0519.md`

Unit: Unit 5. Requesting Clarification

Date: 2026-06-03

## Summary

Unit 5 was repaired as part of the first paired Phase 3 batch pass after Units 1-4. The unit previously followed the old repeated-heading pattern (`ABCDDFEGHEFH`) with duplicate D/E/F/H sections, generic response labels, redundant full-version boxes, and many placeholders outside activity divs. The repair keeps the unit goal but reorganises the activities into the current ordinary-unit shell and removes the old response-label clutter.

## Repairs Applied

- Normalized the visible unit shell to `A. Warm-Up`, `B. Example Check`, `C. Language`, `D. Guided Practice`, `E. Freer Practice`, `F. Editing Practice`, `G. Self-Check and Reflection`, and `H. Transfer and Homework`.
- Merged the old `D. Extended Guided Practice` into `C. Language` as controlled rewrite practice.
- Rebuilt `D. Guided Practice` as the single guided clarification-email task with situation, output length, ordered scaffold, and response space inside the div.
- Rebuilt `E. Freer Practice` as a two-email task with both email response spaces inside the same write div.
- Reclassified the old `G. Editing Practice` as the visible `F. Editing Practice` and removed the redundant full-version response box.
- Merged the old pre-writing self-check and reflection into `G. Self-Check and Reflection`.
- Merged transfer paragraph work and homework under one visible `H. Transfer and Homework`.
- Added written response space for the warm-up and reflection tasks.
- Removed generic labels such as `Write Here`, `Use this box for one complete version`, `Write Your Revised Version`, `Write Your Paragraph`, and `Homework Draft` from Unit 5.
- Moved every Unit 5 placeholder inside its relevant activity div.
- Renamed stale placeholder IDs from the old D extended practice so C-language practice no longer carries old D IDs.
- Updated the Unit 5 answer-key section to match the repaired activity labels, item numbering, and open-ended E/G/H guidance.

## Verification

- Visible heading sequence: `ABCDEFGH`.
- Unit-level fenced div balance: 21 opens / 21 closes.
- Unit-level nested div scan: none found.
- Unit placeholders: 26 total, all with explicit `rows=N`.
- Duplicate placeholder IDs in Unit 5: none.
- Unit 5 placeholders outside divs: none found.
- Unit 5 stale-label scan: no `Write Here`, `Use this box`, `Write Your Revised Version`, `Homework Draft`, `Write your email:`, `Write your emails:`, `Write your paragraph:`, `Write the full corrected version below`, `Mini contrast`, `Why This Works`, `Teaching Point`, or stale `U05-D-rewrite` remains.

## Phase 3 Checklist Result

- Focus alignment: pass. The repaired sequence supports specific clarification questions, clarification emails, and a short explanatory paragraph about why clarification is needed.
- Activity sequencing: pass. The unit now follows warm-up -> example -> language -> guided email -> freer emails -> editing -> self-check/reflection -> transfer/homework.
- Instruction quality: pass. Production tasks name the source situation, output type, and response space.
- Intermediate learner readability: pass. Student-facing instructions are shorter and use common verbs.
- Formatting and Markdown: pass. No duplicate visible A-H headings remain and placeholders are inside divs.
- Response-space calibration: pass. Sentence/question tasks use PH-1 boxes, emails use PH-3 boxes, and the paragraph transfer uses a PH-2 box.
- Answer-key alignment: pass. The answer key now reflects the repaired Unit 5 labels and open-ended tasks.

## Carry-Forward Notes

- Units with old `Extended Guided Practice` sections can often be repaired by folding controlled rewrite items back into `C. Language`, then keeping one visible `D. Guided Practice`.
- When a freer-practice task asks for two documents, separate labelled response boxes are useful and should remain inside the same write div.
