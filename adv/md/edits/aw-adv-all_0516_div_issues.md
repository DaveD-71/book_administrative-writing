# Semantic Div Issues — aw-adv-all_0516.md
Scan date: 2026-05-16
Total issues found: 34

---

## Issue Type 1: Nesting
*A `::: classname` open appears inside another unclosed div block.*

| Outer div line | Outer div class | Inner div line | Inner div class | Notes |
|---|---|---|---|---|
| 109 | `activity-analysis` | 121 | `learn-process` | Inner closes at 125; outer continues to 147 |
| 109 | `activity-analysis` | 127 | `activity-analysis` | Nested same-class div; inner closes at 145 |
| 127 | `activity-analysis` | 141 | `learn-teaching` | Inner closes at 144 |
| 157 | `guidance-step` | 164 | `learn-language` | Inner closes at 172; outer closes at 186 |
| 188 | `guidance-step` | 193 | `learn-language` | Pattern repeats |
| 212 | `activity-language-control` | 243 | `activity-language-control` | Same-class nesting — inner opens at 243 (Focus: "Practice — Apply the Patterns"), still inside outer; inner closes at 274; outer closes at 276 |
| 212 | `activity-language-control` | 258 | `learn-language` | Inner `learn-language` at 258 inside inner `activity-language-control` inside outer |
| 212 | `activity-language-control` | 264 | `learn-language` | Second `learn-language` inside inner `activity-language-control` |
| 212 | `activity-language-control` | 270 | `learn-teaching` | `learn-teaching` nested inside inner `activity-language-control` |
| 300 | `activity-language-control` | 307 | `learn-note` | "Learn — Before You Write" inside language practice task |
| 564 | `activity-rewrite` | 573 | `learn-language` | Inner closes at 580; outer continues |
| 564 | `activity-rewrite` | 582 | `activity-rewrite` | Same-class `activity-rewrite` nested inside outer (line 582: "Focus: Practice — Rewrite Direct Questions") |
| 595 | `activity-analysis` | 604 | `worked-example` | Worked example nested in analysis task |
| 595 | `activity-analysis` | 616 | `activity-analysis` | Same-class nesting (line 616: "Focus: Practice — Choose the Appropriate Version") |
| 918 | `activity-rewrite` | 927 | `learn-language` | Inner closes at 931 |
| 918 | `activity-rewrite` | 933 | `activity-rewrite` | Same-class nesting ("Focus: Practice — Replace Repetition") |
| 946 | `activity-language-control` | 953 | `learn-language` | Inner closes at 963 |
| 946 | `activity-language-control` | 965 | `activity-language-control` | Same-class nesting ("Focus: Practice — Add Logical Connectors") |
| 981 | `activity-rewrite` | 998 | `activity-rewrite` | Same-class nesting ("Focus: Reorganise And Rewrite") |
| 998 | `activity-rewrite` | 1013 | `learn-transfer` | `learn-transfer` inside nested `activity-rewrite` |
| 1241 | `guidance-step` | 1252 | `worked-example` | Worked example inside guidance-step at line 1252 |
| 1629 | `activity-language-control` | 1648 | `worked-example` | Worked example inside language-control at 1648 |
| 2367 | `activity-rewrite` | 2374 | `model` | Model text inside rewrite task at 2374 |
| 2367 | `activity-rewrite` | 2388 | `worked-example` | Worked example inside rewrite task at 2388 |
| 2751 | `activity-rewrite` | 2756 | `learn-transfer` | Transfer note nested inside rewrite task |
| 2751 | `activity-rewrite` | 2766 | `model` | Model text inside rewrite task at 2766 |

**Summary note on nesting:** The file makes very widespread structural use of nesting — most `guidance-step` blocks contain `learn-language` and `activity-*` children; most `activity-*` blocks contain `learn-*` children. This is the consistent authoring pattern throughout the file and appears intentional by design. The most structurally anomalous cases are same-class nesting (e.g. `activity-analysis` inside `activity-analysis`, `activity-rewrite` inside `activity-rewrite`, `activity-language-control` inside `activity-language-control`). These are the cases most likely to cause rendering problems and are flagged as the priority nesting issues.

**Priority same-class nesting issues (most likely unintentional):**

| Line | Outer class | Inner class | Inner div title |
|---|---|---|---|
| 109/127 | `activity-analysis` | `activity-analysis` | "Focus: Noticing Task — Identify The Writing Pattern" (Unit 1 B) |
| 212/243 | `activity-language-control` | `activity-language-control` | "Focus: Practice — Apply the Patterns" (Unit 1 C) |
| 564/582 | `activity-rewrite` | `activity-rewrite` | "Focus: Practice — Rewrite Direct Questions" (Unit 2 C) |
| 595/616 | `activity-analysis` | `activity-analysis` | "Focus: Practice — Choose the Appropriate Version" (Unit 2 C) |
| 918/933 | `activity-rewrite` | `activity-rewrite` | "Focus: Practice — Replace Repetition" (Unit 3 C) |
| 946/965 | `activity-language-control` | `activity-language-control` | "Focus: Practice — Add Logical Connectors" (Unit 3 C) |
| 981/998 | `activity-rewrite` | `activity-rewrite` | "Focus: Reorganise And Rewrite" (Unit 3 D) |

---

## Issue Type 2: Wrong div assignment
*Content that is clearly mismatched with its div class.*

| Line | Div class | Issue | Context |
|---|---|---|---|
| 157 | `guidance-step` | "1. Coordination (Joining Equal Ideas)" — this is reference material / language focus content, not a guidance step in the procedural sense. The numbered heading suggests it belongs in a `learn-process` or `reference-support` block. | Unit 1 C, first language focus section |
| 188 | `guidance-step` | "2. Subordination (Showing Supporting Or Secondary Ideas)" — same issue; reference/explanatory content in a `guidance-step` frame | Unit 1 C |
| 1226 | `guidance-step` | "1. Structural Building Blocks" — describes email structure components; this is explanatory reference material, not a procedural guidance step | Unit 4 C |
| 1241 | `guidance-step` | "Useful Phrases" — a phrase-bank reference section assigned `guidance-step`; should be `reference-support` or `learn-language` | Unit 4 C |
| 2341 | `guidance-step` | "1. Sequencing and Prioritising Requests" — explanatory/reference content labelled as a guidance step | Unit 7 C |
| 3077 | `reference-support` | The `reference-support` block at line 3077 ("Change Management Notice Template") contains an activity task embedded in it: "Choose one situation: 1. Your team has changed…" — mixing template reference with active scenario task | Unit 9 D |
| 5197 | `activity-input` | "Reading-To-Write Input" at line 5197 (Unit 15 B) contains an embedded `learn-process` with task instructions, then the actual writing task is stated outside — the division of what is in the `activity-input` vs. what the learner actually does is blurred | Unit 15 B |
| 8443 | `rubric-assessment` | Contains an embedded `learn-note` block at 8446 — the annotation-within-rubric nesting is semantically odd; the `learn-note` should not sit inside a `rubric-assessment` | Unit 23 F |

---

## Issue Type 3: Numbered-header content inside a div
*A heading like `### 1.`, `#### A.`, or `**1.**` at the paragraph start inside a div class — these are structural headings/list labels and should not carry div styling.*

| Div open line | Div class | Content line | Content text |
|---|---|---|---|
| 157 | `guidance-step` | 157 | "1. Coordination (Joining Equal Ideas)" — numbered section heading inside `guidance-step` |
| 188 | `guidance-step` | 188 | "2. Subordination (Showing Supporting Or Secondary Ideas)" — numbered heading inside `guidance-step` |
| 2341 | `guidance-step` | 2341 | "1. Sequencing and Prioritising Requests" — numbered heading inside `guidance-step` |
| 2004 | `guidance-step` | 2005 | "1. Diplomatic Frames for Highlighting Errors" — numbered heading inside `guidance-step` |
| 2032 | `guidance-step` | 2033 | "2. Explaining Impact Without Assigning Blame" — numbered heading inside `guidance-step` |
| 4015 | `guidance-step` | 4016 | "1. Providing Background Context" — numbered heading inside `guidance-step` |
| 4070 | `guidance-step` | 4071 | "2. Asking Clear, Answerable Questions" — numbered heading inside `guidance-step` |
| 4425 | `guidance-step` | 4426 | "1. Describing Risk" — numbered heading inside `guidance-step` |
| 4465 | `guidance-step` | 4466 | "2. Explaining Impact and Proposing Mitigation" — numbered heading inside `guidance-step` |
| 4871 | `guidance-step` | 4872 | "1. Audience Signals and Layered Explanation" — numbered heading inside `guidance-step` |
| 4904 | `guidance-step` | 4905 | "2. Avoiding Assumed Knowledge" — numbered heading inside `guidance-step` |
| 5229 | `guidance-step` | 5229 | "1. Referencing Policy or Guidelines" — numbered heading inside `guidance-step` |
| 5262 | `guidance-step` | 5263 | "2. Building the Rationale: Reasoning and Benefits" — numbered heading inside `guidance-step` |
| 5577 | `guidance-step` | 5578 | "1. Structural Building Blocks" (Unit 4 equivalent in later unit) — numbered heading inside `guidance-step` |
| 6699 | `guidance-step` | 6699 | "1. Simplifying Technical References" — numbered heading inside `guidance-step` |
| 6731 | `guidance-step` | 6731 | "2. Explaining Purpose and Impact" — numbered heading inside `guidance-step` |
| 6777 | `guidance-step` | 6777 | "3. Stating Required Actions Clearly" — numbered heading inside `guidance-step` |
| 7079 | `guidance-step` | 7080 | "1. Stating the Decision Clearly" — numbered heading inside `guidance-step` |
| 7117 | `guidance-step` | 7118 | "2. Writing a Concise Rationale" — numbered heading inside `guidance-step` |
| 7155 | `guidance-step` | 7156 | "3. Stating Expected Benefits" — numbered heading inside `guidance-step` |
| 7193 | `guidance-step` | 7194 | "4. Structuring a Complete Justification" — numbered heading inside `guidance-step` |
| 7551 | `guidance-step` | 7552 | "1. Writing a Summary Opening" — numbered heading inside `guidance-step` |
| 7588 | `guidance-step` | 7589 | "2. Writing Clear Issue Descriptions" — numbered heading inside `guidance-step` |
| 7626 | `guidance-step` | 7627 | "3. Describing Actions Taken" — numbered heading inside `guidance-step` |
| 7661 | `guidance-step` | 7662 | "4. Writing Next Steps" — numbered heading inside `guidance-step` |

**Note:** All `guidance-step` divs use a numbered or named title line as their opening content. This appears to be the standard authoring pattern for `guidance-step` — the numbered title is the div's section heading, not a markdown heading. Because `guidance-step` maps to "Div Label Base" and presumably renders the title prominently, this may be intentional. Flag for review: if the numbered titles are meant to be navigational headings, they may need to be outside the div rather than inside it.

---

## Issue Type 4: Unnecessary divs around placeholders
*A div block whose entire body is just a `{{PH-#: ...}}` placeholder with nothing else meaningful.*

| Line | Div class | Placeholder text | Notes |
|---|---|---|---|
| 295 | `placeholder` | `{{PH-2: U01-D1-guided-rewrite}}` | Title "Draft" — placeholder-only div; the `placeholder` class is self-documenting |
| 321 | `placeholder` | `{{PH-2: U01-D2-version-1}}` | Placeholder-only |
| 325 | `placeholder` | `{{PH-2: U01-D2-version-2}}` | Placeholder-only |
| 329 | `placeholder` | `{{PH-2: U01-D2-version-3}}` | Placeholder-only |
| 333 | `placeholder` | `{{PH-1: U01-D2-version-choice-note}}` | Title "Planning Notes" — placeholder-only |
| 361 | `placeholder` | `{{PH-4: U01-E1-freer-write}}` | Placeholder-only |
| 399 | `placeholder` | `{{PH-2: U01-G1-editing-rewrite}}` | Title "Revised Draft" — placeholder-only |
| 421 | `placeholder` | `{{PH-4: U01-H3-homework-draft}}` | Placeholder-only |

**Note:** The `placeholder` class is used consistently throughout the file — every draft box is a `placeholder` div containing only a single `{{PH-N: ...}}` line. There are approximately 90–100 such divs in total. Since the `placeholder` class maps to "Div Label Placeholder" in the style map, it is arguably providing a useful visual container (the learner's response box). These are not technically unnecessary if the div renders a visible box. However, if the intent is that placeholders are self-documenting and the div adds no visual value beyond what a bare placeholder would show, all of these qualify under Issue 4. **Flagging the first 8 as representative examples; the pattern is consistent throughout.**

---

## Issue Type 5: Repeated redundancies
*Where the div title, an adjacent heading, a Focus line, or nearby instruction text repeat the same information.*

| Lines | Issue | Text involved |
|---|---|---|
| 69 / 72–73 | Heading "### A. Opening & Activation" is immediately followed by div `activity-analysis` with title "Analysis Task" and Focus "Identifying Confusing Sentences — Guided Skill Practice". The heading and the Focus line overlap in communicating the task type. | "### A. Opening & Activation" → "Analysis Task" / "Focus: Identifying Confusing Sentences..." |
| 92–95 / 96–100 | "### B. Model Text" heading followed by prose "Below are two versions of an excerpt from an internal explanation memo." then immediately `model-bad` "Original Text" — the section heading and the intro prose both announce "here are two model versions", then the model title repeats "Original Text". Three layers say the same thing. | Heading → intro sentence → div title "Original Text" |
| 108–110 / 121–124 | `activity-analysis` Focus says "Compare — Tone And Clarity Analysis"; immediately nested `learn-process` is titled "Learn — Why This Works". Both the focus label and the learn-process title tell the reader they are about to see an analytical comparison and explanation. Mild overlap. | "Focus: Compare — Tone And Clarity Analysis" → "Learn — Why This Works" |
| 278 / 281–283 | "### D. Guided Writing" heading then `activity-rewrite` titled "Rewrite Task" with Focus "Rewrite The Model Text — Model Revision Practice". The heading says "Guided Writing"; the div says "Guided" practice. The phrase "model revision practice" partly repeats the focus of the heading's intent. Low severity but present in almost every unit. | "### D. Guided Writing" → "Rewrite Task" / "Focus: Rewrite The Model Text — Model Revision Practice" |
| 337 / 340–341 | "### E. Freer Writing" → `activity-draft` "Writing Task" / "Focus: Scenario-Based Free Write — Realistic Administrative Response". The heading "Freer Writing" and the Focus "Freer Write" directly repeat the same label. | "### E. Freer Writing" → "Focus: Scenario-Based Free Write" |
| 365 / 368–369 | "### F. Review & Self-Assessment" → `activity-edit` "Editing Task" / "Focus: Self-Editing Checklist — Final Revision Audit". The section heading "Review & Self-Assessment" and the Focus "Self-Editing Checklist — Final Revision Audit" overlap. | "### F. Review & Self-Assessment" → "Self-Editing Checklist — Final Revision Audit" |
| 381 / 384–385 | "### G. Editing" → `activity-edit` "Editing Task" / "Focus: Editing Exercise…". Heading and div both say "Editing". Present in every unit. | Heading "Editing" → div title "Editing Task" |
| 403 / 406–407 | "### H. Homework & Extension" → `activity-draft` "Writing Task" / "Focus: Homework Writing Task — Independent Administrative Writing". Both announce homework. | "### H. Homework & Extension" → "Focus: Homework Writing Task" |

**Note:** The repetition between section headings (A–H) and div titles/Focus lines is a systemic feature of the unit template. The headings announce the section; the div titles and Focus lines echo the same label at div level. This is probably intentional as a navigational aid (heading for TOC, Focus line for the printed task card), but editors should confirm whether both layers are needed in the final output or whether one can be suppressed in the style map.

---

## Issue Type 6: Div goes directly to example with no instruction
*After the div title line, the very next content is a blockquote, model text, placeholder, or example — with no explanatory prose between the div open and the content.*

| Div open line | Div class | Div title | What appears instead of instruction |
|---|---|---|---|
| 96 | `model-bad` | "Original Text" | Immediately the blockquote model text — no instruction. (This is normal for `model-bad`/`model-good` which are display-only.) |
| 103 | `model-good` | "Revised Text" | Immediately the blockquote model text — same as above. |
| 294 | `placeholder` | "Draft" | `{{PH-2: U01-D1-guided-rewrite}}` — placeholder only; the instruction is in the parent div above. |
| 2626 | `model-good` | "Revised Text" | Line 2628: immediately closes with `:::` — the `model-good` div is empty (no text at all). This is a genuine structural gap. |
| 3601 | `model-good` | "Revised Text" | Line 3603: immediately closes — the `model-good` at line 3601 is empty. Another empty model-good div. |
| 5008 | `learn-process` | "Learn — Scenario:" | Immediately a scenario description with no instruction before it — but this is the intended learn-process pattern (scenario precedes the task). Low severity. |
| 6648 | `learn-process` | "Learn — Task:" | Title is "Learn — Task:" and then the content is a list of bullet points — no introductory prose before the bullets. The reader jumps from the label directly to requirements. | 
| 7534 | `learn-process` | "Learn — Task:" | Same issue: "Learn — Task:" followed immediately by bullet list with no prose transition. |

**Priority flags — empty model-good divs:**

These are genuine content gaps where the reader would see an empty div box:

| Line | Issue |
|---|---|
| 2626–2628 | `model-good` "Revised Text" at line 2626 closes at line 2628 with no content between. Unit 8 B model-good is empty. |
| 3601–3603 | `model-good` "Revised Text" at line 3601 closes at 3603 with no content. Unit 9 B model-good is empty. |

Both cases: the `model-good` div opens, there is only `:::` to close, with a `reference-support` div immediately following (lines 2629 and 3604). The content has been placed inside a `reference-support` div rather than `model-good`. This is a **wrong div assignment** and **missing content** issue combined.

---

## Issue Type 7: Heading immediately followed by div title with no body text
*A `##`, `###`, or `####` heading is immediately followed (within 1–3 lines, allowing blank lines) by a `::: classname` and its title, with no prose paragraph between.*

| Heading line | Heading text | Div open line | Div class | Div title |
|---|---|---|---|---|
| 69 | `### A. Opening & Activation` | 72 | `activity-analysis` | "Analysis Task" — 2 blank lines between heading and div open; no prose |
| 92 | `### B. Model Text` | 94 | (prose at 94: "Below are two versions...") | Prose present — not an issue |
| 148 | `### C. Language Focus` | 150 | `learn-principle` | "Learn — Key Principle:" — 1 blank line; no prose between heading and div |
| 278 | `### D. Guided Writing` | 281 | `activity-rewrite` | "Rewrite Task" — 2 blank lines; no prose |
| 337 | `### E. Freer Writing` | 340 | `activity-draft` | "Writing Task" — 2 blank lines; no prose |
| 365 | `### F. Review & Self-Assessment` | 368 | `activity-edit` | "Editing Task" — 2 blank lines; no prose |
| 381 | `### G. Editing` | 384 | `activity-edit` | "Editing Task" — 2 blank lines; no prose |
| 403 | `### H. Homework & Extension` | 406 | `activity-draft` | "Writing Task" — 2 blank lines; no prose |
| 448 | `### A. Opening & Activation` (Unit 2) | 451 | `activity-analysis` | "Analysis Task" — no prose |
| 469 | `### B. Model Text` (Unit 2) | 471 | `model-bad` | "Original Text" — no prose (model texts follow directly) |
| 518 | `### C. Language Focus` (Unit 2) | 520 | `activity-analysis` | "Analysis Task" — no prose |
| 638 | `### D. Guided Writing` (Unit 2) | 640 | `activity-rewrite` | "Rewrite Task" — no prose |
| 685 | `### E. Freer Writing` (Unit 2) | 687 | `activity-draft` | "Writing Task" — no prose |
| 712 | `### F. Review & Self-Assessment` (Unit 2) | 714 | `activity-edit` | "Editing Task" — no prose |
| 738 | `### G. Editing` (Unit 2) | 740 | `activity-edit` | "Editing Task" — no prose |
| 759 | `### H. Homework & Extension` (Unit 2) | 761 | `activity-draft` | "Writing Task" — no prose |
| 801 | `### A. Opening & Activation` (Unit 3) | 803 | `activity-analysis` | "Analysis Task" — no prose |
| 834 | `### B. Model Text` (Unit 3) | 836 | `model-bad` | "Original Text" — no prose |
| 884 | `### C. Language Focus` (Unit 3) | 886 | `activity-analysis` | "Analysis Task" — no prose |
| 979 | `### D. Guided Writing` (Unit 3) | 981 | `activity-rewrite` | "Rewrite Task" — no prose |
| 1027 | `### E. Freer Writing` (Unit 3) | 1029 | `activity-draft` | "Writing Task" — no prose |
| 1049 | `### F. Review & Self-Assessment` (Unit 3) | 1051 | `activity-edit` | "Editing Task" — no prose |
| 1075 | `### G. Editing` (Unit 3) | 1077 | `activity-edit` | "Editing Task" — no prose |
| 1095 | `### H. Homework & Extension` (Unit 3) | 1097 | `activity-draft` | "Writing Task" — no prose |

**Note:** The pattern of heading-immediately-to-div with no intervening prose is consistent across *every unit section* (A through H) throughout the entire file. This is clearly the established template — the div title and Focus line serve as the prose introduction. Editors should decide whether this is acceptable (if the rendered div title is prominent enough to orient the reader) or whether a one-sentence introduction is needed before each div. The most impactful cases for instructional clarity are **Section C (Language Focus)** in each unit, where a brief orientation sentence before the first div would help readers understand what the section is about.

---

## Summary table

| Issue type | Count | Notes |
|---|---|---|
| 1. Nesting | 26 total; 7 priority same-class | Pervasive by design; same-class nesting is the priority concern |
| 2. Wrong div assignment | 8 | Includes 2 critical empty `model-good` divs (content in `reference-support` instead) |
| 3. Numbered-header content inside a div | 25 | All in `guidance-step` divs; likely intentional template pattern |
| 4. Unnecessary divs around placeholders | ~100 (8 representative) | All `placeholder` divs follow this pattern; check if div box is needed for layout |
| 5. Repeated redundancies | 8 representative | Systemic: section heading ↔ div Focus line duplication is built into the template |
| 6. Div goes directly to example | 8; 2 critical (empty `model-good`) | Empty `model-good` at lines 2626 and 3601 are genuine content gaps |
| 7. Heading → div with no prose | 24 representative | Universal template pattern across all A–H unit sections |

---

## Critical issues requiring immediate attention

These issues may cause broken output or missing content in the rendered document:

1. **Empty `model-good` at line 2626 (Unit 8 B):** The "Revised Text" model-good div contains no content. The revised procedure text has been placed in a `reference-support` div at line 2629 instead. Reader would see an empty "Revised Text" box.

2. **Empty `model-good` at line 3601 (Unit 9 B):** Same issue — "Revised Text" div is empty; the content is in a `reference-support` div at line 3604.

3. **Same-class div nesting (7 cases):** `activity-analysis` inside `activity-analysis`, `activity-rewrite` inside `activity-rewrite`, and `activity-language-control` inside `activity-language-control` are the most likely to produce unexpected nesting behavior in the DOCX pipeline.

---

## Patterns worth noting for editorial review

- The **`guidance-step` pattern** of numbered section titles (e.g. "1. Coordination", "2. Subordination") is consistent across all units but these titles function as section headings, not procedural steps. The class name may be misleading or the style mapping may need reconsideration.
- The **heading → div without prose** pattern is universal and likely intentional but creates a very dense visual rhythm where the reader moves immediately from a navigation heading into boxed content with no transitional text.
- **`model-bad` / `model-good` pairs** occasionally appear inside `activity-analysis` divs (e.g. lines 1179/1185, 1525/1531, etc.) — the models are nested inside the analysis task rather than preceding it at the same level. This may be by design (to keep the comparison contained) but it means model texts carry the analysis-task styling in the rendered output.
- The **`reference-support` div** is used in two ways: (a) as a display container for formatted reference material (procedures, rubrics, meeting-summary templates) and (b) as a substitute for `model-good` in at least two places (Units 8 and 9 B sections). This dual use should be clarified.
