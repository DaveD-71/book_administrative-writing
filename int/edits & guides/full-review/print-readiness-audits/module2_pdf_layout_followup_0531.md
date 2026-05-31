# Module 2 PDF Layout Follow-Up - 2026-05-31

Source reviewed: `int/md/working/aw-int-all_0530.pdf`

Scope: Module 2 only, PDF pages 34-84. Page 85 starts Module 3.

## Summary

Module 2 has the same main layout pattern seen in Module 1: no obvious clipping, overlapping body text, missing glyphs, or generally unreadable pages, but page-break control is weak. Several examples, tables, prompts, checklists, and response areas are split across pages. The most serious Module 2-specific defect is a raw pipe-table rendering failure in Unit 7.

## Category 1 - Running Header Problems

Follow-up action: correct running-header logic so title pages and content pages show the current module/unit/review context.

- Page 34: the Module 2 title page still shows `Module 1 Review Workshop` in the running header.
- Pages 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, and 76: even-page running headers say `Module Guide` even though the pages are inside Units 4-7.

## Category 2 - Raw Markdown Or Table Rendering Failure

Follow-up action: repair the source table syntax or convert the table to a supported table format before PDF generation.

- Page 67: `Politeness Scale (From Direct to Most Polite)` renders as raw pipe-table text, including visible `|` characters, separator marks, and literal `**` bold markers. This is a content-rendering defect, not just a pagination issue.

## Category 3 - Split Examples, Comparisons, And Model Explanations

Follow-up action: keep weak/strong examples, model boxes, and their immediate explanation together when feasible.

- Page 36 to page 37: Email B is split across pages. Page 36 shows only the first line of the green Email B box, while the rest appears on page 37.
- Page 78: `Then answer:` checklist is visually attached to Version B as a second green box, making it read partly like model content instead of follow-up questions.
- Page 81: the stronger-version model email ends with `Why this stronger version works:`, but the explanation bullets appear in a separate green box below.

## Category 4 - Orphaned Section Or Subsection Starts

Follow-up action: apply keep-with-next behavior to section headings, div labels, and first activity paragraphs.

- Page 37: `C. Language` starts at the very bottom with only the heading and first two bullets before the page break.
- Page 49 to page 50: `Extended Guided Practice` starts on page 49 and continues on page 50 before `D. Guided Practice` starts low on the page.
- Page 52 to page 53: `G. Editing Practice` starts on page 52 with only the first prompt; the remaining prompts continue on page 53.

## Category 5 - Split Prompts And Response Areas

Follow-up action: keep activity instructions with their first response lines. Avoid starting a page with answer lines whose prompt is on the previous page.

- Page 40 to page 41: page 41 opens with continuation response lines from the previous activity before `D. Guided Practice`.
- Page 50 to page 51: the guided-practice email prompt is split; page 50 contains most of the task, while page 51 starts with only `Sign-off:` and response lines.
- Page 54 to page 55: the extended writing task setup and model frame are on page 54, while the response label and answer lines start on page 55.
- Page 60 to page 61: `D. Guided Practice` starts on page 60 but the remaining email components and response lines continue on page 61.
- Page 64 to page 65: Unit 6 ending is split; page 65 begins with detached response lines before `Reflection`.
- Page 68 to page 69: final prompt `Give me the information.` appears at the bottom of page 68, while its response lines continue on page 69 before a new subsection starts.
- Page 73 to page 74: Unit 7 freer-practice response area is split; page 73 gives `Email 1` with only a few lines, and page 74 starts with detached lines plus `Email 2`.

## Category 6 - Split Tables And Structured Blocks

Follow-up action: keep short tables and grids on one page where possible; if a table must split, repeat the header row.

- Page 82 to page 83: `Module 2 Audience-and-Detail Grid` is split. Page 82 shows the heading and first row; page 83 contains the remaining rows.

## Category 7 - Poorly Balanced Final Pages

Follow-up action: rebalance the Module 2 review workshop ending so the final page feels intentional or is pulled back.

- Page 84: very sparse final Module 2 page with only the end of the review material and large blank space before Module 3 begins on page 85.

## Suggested Fix Order

1. Fix the raw Unit 7 pipe-table rendering on page 67 first.
2. Fix running headers, including title-page carryover from the previous module.
3. Add keep-with-next / keep-together controls for example boxes, section headings, checklists, short tables, and response labels.
4. Re-render Module 2 and recheck pages 34-84 against this list.
5. If fixes are made globally, recheck Module 1 as well because the same pagination controls affect both modules.

