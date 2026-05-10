# Markdown normalization instruction set for `aw-adv-all.md`

Source scanned: `/mnt/data/aw-adv-all.md`

## Scan summary

- Lines: 6,850
- Words: 49,206
- Candidate edit lines: 776
- Markdown headings: 592
- Bold-labelled lines detected: 426
- Pandoc fenced Div blocks currently present: 0

## Candidate edits by priority

- high: 525
- low: 162
- medium: 89

## Candidate edits by category

- activity_heading: 285
- bold_label_review: 125
- student_response_placeholder_label: 116
- bold_structural_label: 45
- theory_subsection: 37
- process_rationale_callout: 23
- transfer_reminder_callout: 22
- writing_goal_label: 22
- example_label: 21
- bold_activity_label: 20
- worked_example_label: 20
- minor_label_heading: 12
- model_label_heading: 6
- annotation_label: 6
- rubric_subsection_heading: 6
- micro_theory_label: 3
- language_usage_note: 2
- general_note_callout: 2
- teaching_point_callout: 1
- key_principle_callout: 1
- rubric_hierarchy_error: 1

## Important semantic correction

`why-this-works` must only be used for writing-process rationale after a model, example, comparison, or instruction. It should not be used for vocabulary, grammar, phrase usage, contrast notes, or general annotations.

Notes such as `Note on contrast` are language/usage notes. They need a separate semantic class, such as `language-note` or `note-contrast`.

## Note / callout taxonomy found in the file

| Current label type | Count in candidate list | Correct semantic class | Function |
|---|---:|---|---|
| Why this works | 23 | `why-this-works` | Writing-process rationale after model/example/comparison |
| Note on... | 2 | `language-note` / `note-contrast` | Language, vocabulary, grammar, phrase usage, or contrast explanation |
| Teaching point | 1 | `teaching-point` | Concept/rule explanation |
| Key principle | 1 | `key-principle` | High-significance theory principle |
| Transfer reminder | 22 | `transfer-reminder` | Transfer/application reminder |
| Additional/Rubric note | 2 | `note` | General note or rubric note |

## Recommended visual semantics

| Semantic class | Colour logic | Visual function |
|---|---|---|
| `model-bad` | Red border/accent | Original, flawed, too direct, disjointed, problematic source text |
| `model-good` | Green border/accent | Revised, improved, diplomatic, cohesive, model answer |
| `why-this-works` | Blue explanatory accent | Post-model writing-process rationale |
| `language-note` / `note-contrast` | Neutral/blue, lighter than key principle | Phrase, grammar, vocabulary, or contrast explanation |
| `key-principle` | Stronger blue/theory accent | Core principle that students should remember |
| `teaching-point` | Blue/neutral callout | Teacher explanation of a concept or rule |
| `transfer-reminder` | Orange/amber accent | Application warning/reminder across contexts |
| `activity.*` | Compact badge + title + muted code | Student task, not document hierarchy |
| `placeholder` | Quiet writable field style | Draft/answer space marker |

## Process rule

Do not convert all blockquotes into one style. First identify function:
1. Does it explain why a model or revision works? → `why-this-works`
2. Does it explain language/phrase/grammar/contrast? → `language-note` / `note-contrast`
3. Does it state a general learning rule? → `key-principle`
4. Does it warn/remind students to transfer a skill? → `transfer-reminder`
5. Does it identify a student response area? → `placeholder`

The complete line-by-line edit list is in:

`aw_adv_markdown_edit_instruction_lines.csv`
