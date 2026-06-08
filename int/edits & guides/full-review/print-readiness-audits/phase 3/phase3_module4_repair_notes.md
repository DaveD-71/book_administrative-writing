# Phase 3 Module 4 Repair Notes

Date: 2026-06-03

Scope: `int/md/working/aw-int-all_0519.md`, Units 12-15 and Module 4 Review Workshop; `int/md/working/aw-int-answer-key.md`.

## Repairs Applied

- Normalized Units 12-15 to the ordinary visible sequence `A-H`.
- Folded duplicate concept-primer `A` sections into the repaired `A. Warm-Up` / `B. Example Check` flow.
- Removed obsolete `F. Self-Check Before Freer Practice`, `E. Extended Writing Task`, split `H. Transfer Extension`, and split `H. Homework` headings.
- Restored the visible Section H standard as `H. Homework & Extension`.
- Moved Module 4 placeholders inside their relevant activity divs.
- Removed generic response labels such as `Write Here`, `Use this box`, `Write Your Revised Version`, `Write Your Paragraph`, and `Homework Draft`.
- Removed nested mini-example structures and converted the support into direct prose or properly classified sibling divs.
- Split multi-output freer-practice and extension tasks into separate placeholders where the task asks for separate messages.
- Increased response space where students are expected to write complete short emails, explanations, or clarification responses.
- Removed the Module 4 Review Workshop `Possible Stronger Version` spoiler from the student book and moved model guidance to the answer key.
- Updated the Module 4 answer key to match the repaired activity sequence and current placeholder/task structure.

## Verification

- Unit 12 visible sequence: `ABCDEFGH`.
- Unit 13 visible sequence: `ABCDEFGH`.
- Unit 14 visible sequence: `ABCDEFGH`.
- Unit 15 visible sequence: `ABCDEFGH`.
- Module 4 fenced divs: 75 open / 75 close.
- Whole manuscript fenced divs: 492 open / 492 close.
- Whole manuscript placeholder IDs: 407 total / 0 duplicates.
- Module 4 placeholders outside divs: 0.
- Module 4 nested div starts: 0.
- Module 4 stale-label scan passed for `Write Here`, `Write Your`, `Use this box`, `Homework Draft`, `Self-Check Before Freer Practice`, `Transfer Extension`, `Extended Writing Task`, `Teaching Point`, `Possible Stronger Version`, `Mini example`, `Mini comparison`, and `Mini report`.
- Bad-token scan passed for `窶` and `rows=1d`.
- Pandoc parse with `C:\Dev\Code\textmaker\scripts\style_bridge.lua` passed.

## Follow-Up

- Regenerate DOCX/PDF when ready for visual inspection.
- Visually check row counts for Module 4 Review Workshop transfer placeholders after conversion.
