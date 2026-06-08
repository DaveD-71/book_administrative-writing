# Phase 3 Module 3 Repair Notes

Date: 2026-06-03

Scope: `int/md/working/aw-int-all_0519.md`, Units 8-11 and Module 3 Review Workshop; `int/md/working/aw-int-answer-key.md`.

## Changes Applied

- Normalized Units 8-11 to the visible sequence `A B C D E F G H`.
- Replaced duplicate concept-primer `A` headings with one visible `A. Warm-Up` per unit.
- Replaced the obsolete `F. Self-Check Before Freer Practice` pattern with `F. Editing Practice` followed by `G. Self-Check and Reflection`.
- Replaced separate `Transfer Extension` and `Homework` headings with one visible `H. Homework & Extension` section in each unit.
- Removed redundant `Write Here`, `Use this box`, `Write Your Revised Version`, and `Homework Draft` labels from Module 3.
- Moved Module 3 placeholders inside their relevant activity divs.
- Removed redundant aggregate placeholders after item-level rewrite placeholders.
- Consolidated repeated teaching blocks such as `Teaching Point`, duplicate `Why This Works` blocks, mini contrasts, planning grids, and extended writing tasks where they repeated the main activity requirement.
- Added controlled facts to Unit 10 guided practice so students write a problem explanation from supplied information rather than inventing all content.
- Changed Unit 11 guided practice from a prose situation to meeting notes, making the transformation task clearer.
- Removed the Module 3 Review Workshop `Possible Stronger Version` from the student book and moved the model answer to the answer key.
- Updated the Module 3 answer-key block to reflect the repaired Unit 8-11 activity sequence and the removed review-workshop model.

## Verification

- Unit 8 sequence: `A B C D E F G H`.
- Unit 9 sequence: `A B C D E F G H`.
- Unit 10 sequence: `A B C D E F G H`.
- Unit 11 sequence: `A B C D E F G H`.
- Module 3 div balance: 82 open / 82 close.
- Module 3 placeholders: 64 total, 0 outside activity divs.
- Whole-manuscript div balance: 520 open / 520 close.
- Whole-manuscript placeholder IDs: 404 total, 0 duplicate IDs.
- Module 3 stale-label scan: 0 hits for `Write Here`, `Write Your`, `Use this box`, `Homework Draft`, `Self-Check Before Freer Practice`, `Transfer Extension`, `Extended Writing Task`, `Teaching Point`, `Possible Stronger Version`, `Mini contrast`, or `Mini support example`.
- UTF-8/mojibake scan: no `窶` corruption detected in the student source or answer key.
- Pandoc parse with `..\textmaker\scripts\style_bridge.lua`: passed.

## Follow-Up

- Regenerate DOCX/PDF and visually inspect Module 3 pages, especially page breaks around long response placeholders and the Module 3 Review Workshop.
- Continue Phase 3 with Module 4 / Units 12-15, which still show the older duplicated `A`, `F/E/H`, and `Transfer Extension` patterns.
