# Complete Step 1 Markdown Implementation Plan For `aw-adv-all_0510.md`

## Read Status And Summary

I found and read the new Step 1 Markdown summary file in `adv/edits & guides/style edits/step1-markdown`: `aw_adv_all_lines_to_change_summary.md`. I also inspected the new implementation CSV, `aw_adv_all_lines_to_change.csv`, which contains 744 direct line-level change records. I only found one new Markdown file in that folder; no second new `.md`/`.markdown` file is currently present there.

Apply the full Step 1 Markdown normalization package to `adv/md/final/aw-adv-all_0510.md` only. This implementation uses the newest 744-row implementation CSV as the practical checklist, with the earlier Step 1 files as policy and backup context.

After confirmation, save this plan as `adv/edits & guides/style edits/step1-markdown/codex_step1_implementation_plan.md`.

## Scope And Authorities

- Edit only `adv/md/final/aw-adv-all_0510.md`.
- Do not edit `adv/md/final/aw-adv-all.md` or module source files.
- Before modifying the target, create a timestamped backup copy beside it: `adv/md/final/aw-adv-all_0510_backup_YYYYMMDD-HHMMSS.md`.
- Preserve the target file’s original line endings and UTF-8 encoding; validate UTF-8 integrity after edits.
- Use `aw_adv_all_lines_to_change.csv` as the direct line-level implementation checklist.
- Use `aw_adv_all_lines_to_change_summary.md` for the latest count summary.
- Use `aw_adv_markdown_edit_instruction_lines_REVISED.csv` as supporting policy/background where needed.
- Use `activity_headings_missing_subtitles.csv` for subtitle candidates, but review and normalize suggestions before applying.
- Retain `aw_adv_markdown_edit_instruction_lines.csv` as raw scan data only; it is superseded where conflicts exist.
- Treat `aw_adv_step1_file_inventory.csv` as checked inventory, not an edit source.
- Defer Stage 2 work: no reference DOCX creation, Word style work, icon replacement, Lua filters, or deep metadata extraction in this pass.

## Core Rules

- Preserve editorial QA visibility, pedagogical structure, and activity traceability in Markdown.
- Do not reorder activities, callouts, examples, model texts, sections, or tasks.
- Do not rewrite educational content, simplify explanations, paraphrase model texts, or alter pedagogical meaning.
- Apply transformations contextually; do not globally replace ordinary prose occurrences of words such as `version`, `note`, `example`, or `text`.
- Keep activity codes such as `(B1)`, `(C2)`, and `(H3)` in Markdown; later Word/PDF output may suppress, hide, mute, or minimize them.
- Preserve every `{{PH-*}}` placeholder token exactly.
- Preserve existing `★` activity markers and place them after the code: `#### Title — Subtitle (CODE) ★`.
- Preserve lazy numbered lists using repeated `1.`; do not renumber intentionally lazy Markdown ordered lists.
- Do not wrap partial Markdown list structures in Divs if doing so would break list continuity, list nesting, or indentation.
- Preserve true quoted model/example text unless it is an instructional callout.
- Use parentheses only for metadata codes in normalized headings and labels.

## Semantic Class Registry

Use only these Step 1 semantic classes when adding Divs or semantic labels:

| Class | Use |
|---|---|
| `learn-process` | Why a model, revision, or writing process works |
| `learn-language` | Language, grammar, vocabulary, phrase, register, or contrast explanation |
| `learn-principle` | Major conceptual principle |
| `learn-transfer` | Transfer/application reminder |
| `learn-note` | General note, rubric note, or low-intensity explanation |
| `learn-teaching` | Teaching-point explanation |
| `model-bad` | Original, flawed, too direct, unclear, disjointed, or problematic writing sample |
| `model-good` | Revised, improved, diplomatic, cohesive, or model writing sample |
| `placeholder` | Student response area |
| `self-study` | Self-study or independent study support block, if explicitly present |
| `worked-example` | Procedural demonstration or explained process, not simply a revised writing sample |
| `example` | Example block or label where not a model comparison |
| `annotation` | Annotation explaining a model or text feature |

Do not use older class names such as `why-this-works`, `language-note`, `teaching-point`, or `transfer-reminder`.

## Semantic Div Formatting

- Add a blank line before every opening `:::`.
- Add a blank line after every closing `:::`.
- Add a blank line between a heading and any following Div.
- Avoid accidental nested Divs; nest only when intentionally required by the content structure.
- Wrap the entire contiguous block associated with a semantic label, not just the first paragraph.
- If the associated block is part of a Markdown list, either wrap the complete list item/list block safely or preserve the list structure and use a semantic label/comment instead of a Div.
- Preserve Markdown readability and Pandoc parse safety.

## Punctuation And Capitalization

- Use Title Case for activity headings, instructional labels, model labels, callout labels, and major pedagogical labels.
- Preserve existing acronym capitalization, placeholder tokens, metadata codes, and intentionally lower-case technical notation when applying Title Case normalization.
- Use an em dash (`—`) for activity subtitles and model-text subtitles.
- Do not use parentheses for model-label subtitles; convert them to em-dash subtitles.
- Keep activity metadata codes at the end of headings: `#### Activity Family — Subtitle (CODE)`.
- Remove accidental repeated spaces and trailing spaces unless spacing is required inside a Markdown table.

## Detailed Changes

- Activity headings: normalize all activity-heading rows identified in `aw_adv_all_lines_to_change.csv`, plus any remaining `REVISE_INSTRUCTION` activity rows from the revised edit list. The latest implementation CSV identifies 246 activity-heading change rows. Use `#### Activity Family — Subtitle (CODE)` or `#### Activity Family — Subtitle (CODE) ★`. Do not convert activity headings to Divs.
- Missing subtitles: use `activity_headings_missing_subtitles.csv` as a suggestion source, but correct any `(CODE) — Subtitle` ordering and replace generic `Activity Focus` with a meaningful subtitle before applying.
- Model labels: normalize visible model labels to `Original Text` or `Revised Text`. If the original label includes a meaningful descriptor, keep it as an em-dash subtitle in Title Case. Examples: `Original Version` -> `Original Text`; `Revised Version` -> `Revised Text`; `Original Version (too direct)` -> `Original Text — Too Direct`; `Revised Version (diplomatic)` -> `Revised Text — Diplomatic`. Do not rewrite ordinary prose such as “the revised version.”
- Model blocks: where a problematic/original sample directly follows a model label, wrap the entire contiguous associated sample block in `::: model-bad`; where a revised/improved sample follows, wrap the entire contiguous associated sample block in `::: model-good`. Keep sample wording intact. If the model sample is embedded inside a Markdown list, do not wrap only part of the list; preserve list integrity and use the least disruptive semantic treatment.
- Learn callouts: convert all implementation-CSV learn/callout rows to final `learn-*` Divs. `Why This Works` becomes `learn-process`; `Note On...` becomes `learn-language`; `Key Principle` becomes `learn-principle`; `Transfer Reminder` becomes `learn-transfer`; `Teaching Point` becomes `learn-teaching`; general/rubric notes become `learn-note`.
- Placeholder lines: normalize all placeholder-label lines identified in `aw_adv_all_lines_to_change.csv`. The latest implementation CSV identifies 243 placeholder-line changes. Preserve every `{{PH-*}}` token exactly and validate by comparing baseline and final unique placeholder IDs plus total placeholder-token count.
- Examples and worked examples: convert or normalize `example`, `worked-example`, and related semantic-label rows according to the implementation CSV. Use `model-good` only for revised/model writing samples; use `worked-example` for procedural demonstrations or explained processes. Do not wrap partial list structures in `example` or `worked-example` Divs.
- Annotations: convert annotation rows to `annotation` labels/Divs unless the annotation is better included inside a surrounding model block or list structure.
- Theory and minor headings: keep true theory/micro-theory headings as headings. Lightly normalize Title Case and punctuation only. Avoid excessive metadata in theory headings.
- Review rows: keep bold local labels when they structure examples, lists, writing goals, templates, or worked examples. Remove/reduce bold only when it is accidental emphasis already handled by a heading or Div.
- Ambiguous rows: if classification is unclear, preserve the original structure and add a non-rendering HTML review comment adjacent to the item, using `<!-- REVIEW: Step 1 semantic classification unclear; original structure preserved. -->`.
- Unit 23 rubric hierarchy: keep all main unit headings as `## Unit N ...`. Do not demote book unit headers. Demote only the supplemental rubric block so it sits under Unit 23: `# Unit 23 Capstone Assessment Rubric` -> `### Unit 23 Capstone Assessment Rubric`; rubric subsections such as `## How To Use This Rubric`, `## Analytic Rubric`, and `## Overall Judgment` -> `#### ...`.
- Lint cleanup: resolve instructional blockquote findings, missing blank lines before/after headings, accidental multiple spaces, trailing space, and long blockquotes that are actually instructional templates/callouts. Treat activity-code heading lint as acceptable once headings follow the canonical pattern.

## Implementation Order

1. Capture baseline counts for headings, placeholders, blockquotes, semantic-label candidates, model labels, key callout labels, line endings, and encoding.
2. Create the timestamped backup copy.
3. Work through `aw_adv_all_lines_to_change.csv` by `change_type`, using `current_text` as the stable match if line numbers shift.
4. Apply deterministic punctuation, capitalization, model-label, placeholder-label, and spacing fixes.
5. Normalize activity headings and missing subtitles.
6. Convert instructional callouts, examples, annotations, and worked examples to approved semantic classes where required, preserving list continuity.
7. Apply model and placeholder Div wrappers where practical.
8. Fix the Unit 23 rubric hierarchy without changing normal `## Unit N` headers.
9. Cross-check against `aw_adv_markdown_edit_instruction_lines_REVISED.csv` for any older policy row not represented in the newest implementation CSV.
10. Run validation checks and inspect representative early, middle, Unit 23, and list-heavy sections.

## Validation And Acceptance

- All 744 rows in `aw_adv_all_lines_to_change.csv` are applied or intentionally retained under the rules above.
- Any remaining relevant rows from `aw_adv_markdown_edit_instruction_lines_REVISED.csv` are applied or explicitly deemed superseded by the newest CSV.
- All activity headings identified by the latest implementation CSV and any remaining revised-list activity rows retain codes and follow the canonical subtitle pattern.
- No activity heading uses `(CODE) — Subtitle` or generic `— Activity Focus`.
- Parentheses are used only for metadata codes in normalized headings and labels.
- Model-label descriptors, where retained, use em-dash subtitles rather than parentheses.
- All instructional callouts use approved semantic classes from the registry.
- Placeholder token count and unique placeholder IDs match the baseline exactly.
- No visible model labels remain as `Original Version`, `Revised Version`, `Original (Disjointed)`, or `Revised (Cohesive)`.
- Main unit headings remain `## Unit N ...`.
- The supplemental Unit 23 rubric no longer appears as a `#` heading, and rubric subsections no longer appear as `##`.
- Div fences are balanced, separated by blank lines, and not accidentally nested.
- Markdown list continuity, numbering, and indentation remain intact after Div conversion.
- The file remains valid UTF-8 with no mojibake introduced.
- Run `python scripts/check_mojibake.py adv` if available.
