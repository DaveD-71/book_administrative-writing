# Module 1 PDF Layout Follow-Up - 2026-05-31

Source reviewed: `int/md/working/aw-int-all_0530.pdf`

Scope: Module 1 only, PDF pages 1-33. Page 34 starts Module 2.

## Summary

The first module does not show obvious clipping, overlapping text, missing glyphs, or unreadable tables. The main layout problem is page-break control. Headings, examples, prompts, answer lines, and explanatory blocks are often separated across page breaks, which makes the workbook harder to use.

## Category 1 - Running Header Problems

Follow-up action: adjust running header logic so content pages show the current module/unit/review context instead of retaining `Module Guide` after the guide section ends.

- Pages 4, 6, 8, 10, 14, 16, 18, 20, 22, 24, 26, and 28: even-page running headers say `Module Guide` while the content is inside Units 1-3.

## Category 2 - Orphaned Section Or Subsection Starts

Follow-up action: apply keep-with-next behavior to section headings, div labels, and the first paragraph or first activity item after them.

- Page 3 to page 4: `B. Example Check` starts at the bottom of page 3 and immediately continues on page 4.
- Page 5 to page 6: `Simplify the Sentence` starts near the bottom of page 5, but the sentence prompts begin on page 6.
- Page 15 to page 16: `Useful Phrases by Function` starts at the bottom of page 15 with only the first bullet, then continues on page 16.
- Page 32 to page 33: `MODULE 1 REBUILDING NOTE` starts at the very bottom of page 32 and continues onto an almost-empty page 33.

## Category 3 - Split Prompts And Response Areas

Follow-up action: keep activity prompt text with its first response area and avoid page breaks between an instruction and the first ruled lines.

- Page 25 to page 26: `D. Guided Practice` leaves only one visible answer line on page 25; most response lines continue at the top of page 26.
- Page 27 to page 28: `H. Transfer Extension` starts on page 27, but response lines continue at the top of page 28 before `REFLECTION`.
- Several pages begin with detached answer lines from the previous activity, especially pages 7, 9, 10, 14, 17, 26, 27, and 28.

## Category 4 - Split Examples, Comparisons, And Explanations

Follow-up action: keep weak/strong pairs, model boxes, and their immediate explanation together when feasible. If they cannot fit, move the whole unit of content to the next page.

- Page 12 to page 13: Unit 2 weak/strong comparison is split, with `Weak` on page 12 and `Stronger` on page 13.
- Page 22: the `Discussion:` question appears inside the Paragraph B example box, making it read as part of the model paragraph rather than a follow-up instruction.
- Page 24 to page 25: the `Reorder and Extend` sentence set is split; page 24 has A and B, while page 25 starts with C and the answer instruction.
- Page 31 to page 32: the `Possible Stronger Version` box includes `Why this stronger version works:` at the bottom of page 31, but the bullet explanation appears separately on page 32.

## Category 5 - Split Lists And Checklists

Follow-up action: keep short numbered reflection lists and checklist blocks together where possible, especially when only one or two list items would be pushed to the next page.

- Page 10 to page 11: Unit 1 reflection list is split; page 11 opens with item `3.` separated from the `REFLECTION` heading and earlier questions.
- Page 29 to page 30: `MODULE 1 SELF-EDIT ROUTINE` is split, with the final checklist items pushed onto page 30 before the next section.

## Category 6 - Poorly Balanced Final Pages

Follow-up action: rebalance the Module 1 review workshop ending so the final page is either removed or given enough content to feel intentional.

- Page 33: almost-empty trailing page with only the continuation of the rebuilding note and three bullets.

## Suggested Fix Order

1. Fix the running header source first, because it is a global page-template issue.
2. Add keep-with-next / keep-lines controls for headings, div labels, short checklists, and boxed model text.
3. Tune response-area placement so prompts do not split from their first ruled writing space.
4. Re-render Module 1 and recheck pages 3-33 against this list.
5. If the same patterns repeat, extend the same checks to Modules 2-6.

