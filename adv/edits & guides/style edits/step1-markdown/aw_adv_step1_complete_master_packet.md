# Administrative Writing Textbook — Step 1 Complete Master Packet

Generated: 2026-05-10 00:49

This document replaces the earlier short master spec. It preserves the decisions, the file inventory, and the detailed data generated during Step 1.

## 1. File Inventory And Status

| File | Purpose | Status |
|---|---|---|
| `aw_adv_step1_complete_master_packet.md` | This consolidated packet | NEW PRIMARY OVERVIEW |
| `aw_adv_markdown_edit_instruction_lines_REVISED.csv` | Revised line-by-line edit list aligned to final decisions | USE THIS, not the older CSV alone |
| `aw_adv_markdown_edit_instruction_lines.csv` | Original 776-row edit list | RETAIN AS RAW SCAN, but superseded where conflicts exist |
| `aw_adv_markdown_normalization_guide.md` | Earlier taxonomy and guide | PARTIALLY SUPERSEDED; use for background only |
| `aw_adv_pandoc_markdown_lint_report.csv` | Pandoc/Markdown lint report | RETAIN |
| `aw_adv_pandoc_markdown_lint_summary.md` | Lint summary | RETAIN, but metadata-code warnings are intentional |
| `activity_headings_missing_subtitles.csv` | 164 activity headings missing subtitles plus suggestions | RETAIN AND USE |
| `final_step1_decisions.md` | Decision log | RETAIN; integrated here |
| `aw_adv_step1_master_spec.md` | Earlier short master spec | SUPERSEDED by this packet |

## 2. Final Decisions Integrated

- Keep activity subheadings. They indicate activity type and provide variety.
- Standardize activity-heading punctuation and capitalization.
- Add subtitles to activity headings that are missing them.
- Keep activity codes such as `(B1)`, `(C2)`, `(H3)` in Markdown for QA, but remove/suppress them from Word/PDF output.
- Standardize model labels by replacing `Version` with `Text`: `Original Text`, `Revised Text`, etc.
- All learning notes use the root concept `Learn`, with functional subtypes.
- Normalize placeholder labels.
- Remove accidental visual emphasis where bold/heading styling already provides emphasis.
- Replace instructional blockquotes with semantic Divs today.
- Use Title Case for headings and labels.

## 3. Actual Data Summary

Original candidate edit lines: **776**

### Original Edit Categories

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

Revised line-by-line file created: `aw_adv_markdown_edit_instruction_lines_REVISED.csv`

### Revised Status Counts

- REVISE_INSTRUCTION: 285
- REVIEW: 259
- NORMALIZE_PLACEHOLDER: 116
- KEEP_OR_LIGHT_NORMALIZE: 52
- CONVERT_TO_LEARN_DIV: 51
- FIX_HIERARCHY: 7
- UPDATE_TO_MODEL_TEXT_POLICY: 6

Activity headings missing subtitles: **164**

Use `activity_headings_missing_subtitles.csv` to apply suggested subtitles. Review suggestions before bulk replacement.

### First 25 Missing-Subtitle Examples

| Line | Current Heading | Suggested Heading |
|---:|---|---|
| 60 | `Compare Two Versions (B1)` | `Compare Two Texts — Tone And Clarity Analysis` |
| 73 | `Noticing Task (B2)` | `Noticing Task — Identify The Writing Pattern` |
| 186 | `Rewrite the Model Text (D1)` | `Rewrite the Model Text (D1) — Activity Focus` |
| 201 | `Write Your Own Complex Sentence (D2)` | `Write Your Own Complex Sentence (D2) — Activity Focus` |
| 235 | `Scenario-Based Free Write (E1)` | `Scenario-Based Free Write — Realistic Administrative Response` |
| 257 | `Self-Editing Checklist (F3)` | `Self-Editing Checklist — Final Revision Audit` |
| 271 | `Editing Exercise (G1)` | `Editing Exercise — Improve Clarity And Flow` |
| 289 | `Homework Writing Task (H3)` | `Homework Writing Task — Independent Administrative Writing` |
| 305 | `Extension Task (H1)` | `Extension Task — Advanced Transfer Practice` |
| 358 | `Compare Two Versions (B1)` | `Compare Two Texts — Tone And Clarity Analysis` |
| 371 | `Noticing Task (B2)` | `Noticing Task — Identify The Writing Pattern` |
| 475 | `Rewrite the Model Text (D1)` | `Rewrite the Model Text (D1) — Activity Focus` |
| 512 | `Scenario-Based Free Write (E1)` | `Scenario-Based Free Write — Realistic Administrative Response` |
| 535 | `Guided Peer Review (F1)` | `Guided Peer Review — Structured Feedback Exchange` |
| 542 | `Self-Editing Checklist (F3)` | `Self-Editing Checklist — Final Revision Audit` |
| 556 | `Editing Exercise (G1)` | `Editing Exercise — Improve Clarity And Flow` |
| 575 | `Homework Writing Task (H3)` | `Homework Writing Task — Independent Administrative Writing` |
| 589 | `Extension Task (H1)` | `Extension Task — Advanced Transfer Practice` |
| 654 | `Compare Two Versions (B1)` | `Compare Two Texts — Tone And Clarity Analysis` |
| 667 | `Noticing Task (B2)` | `Noticing Task — Identify The Writing Pattern` |
| 779 | `Reorganise and Rewrite (D5)` | `Reorganise and Rewrite (D5) — Activity Focus` |
| 803 | `Scenario-Based Free Write (E1)` | `Scenario-Based Free Write — Realistic Administrative Response` |
| 821 | `Guided Peer Review (F1)` | `Guided Peer Review — Structured Feedback Exchange` |
| 828 | `Self-Editing Checklist (F3)` | `Self-Editing Checklist — Final Revision Audit` |
| 842 | `Editing Exercise (G1)` | `Editing Exercise — Improve Clarity And Flow` |

Lint report rows: **408**

### Lint Categories

- heading_contains_activity_code: 294
- blockquote_as_callout: 60
- multiple_spaces: 30
- missing_blank_before_heading: 10
- frequent_duplicate_heading: 8
- long_blockquote: 4
- trailing_space: 1
- missing_blank_after_heading: 1

## 4. Canonical Activity Heading Rule

Pattern:

```markdown
#### Activity Family — Subtitle (CODE)
```

Rules:
- Use Title Case.
- Use an em dash for subtitle separation.
- Keep the code in Markdown.
- Suppress or hide the code in Word/PDF.
- Do not convert activity headings to Divs today.

## 5. Learn Div Taxonomy

| Existing Label | Semantic Div | Use |
|---|---|---|
| Why This Works | `learn-process` | Post-model/post-example writing-process rationale |
| Note On Contrast / Note On... | `learn-language` | Language, phrase, grammar, vocabulary, register, contrast |
| Key Principle | `learn-principle` | Major conceptual principle |
| Transfer Reminder | `learn-transfer` | Application/transfer reminder |
| Teaching Point | `learn-teaching` | Teacher explanation or concept guidance |
| Additional Note / Rubric Note | `learn-note` | General note |

Example:

```markdown
::: learn-language
**Learn — Note On Contrast:** ...
:::
```

## 6. Model Text Policy

Standardize labels:
- `Original Version` → `Original Text`
- `Revised Version` → `Revised Text`
- `Original Version (too direct)` → `Original Text — Too Direct`
- `Revised Version (diplomatic)` → `Revised Text — Diplomatic`
- `Original (Disjointed)` → `Original Text — Disjointed`
- `Revised (Cohesive)` → `Revised Text — Cohesive`

Use semantic Divs:

```markdown
::: model-bad
**Original Text — Too Direct**
...
:::

::: model-good
**Revised Text — Diplomatic**
...
:::
```

## 7. Placeholder Policy

Normalize labels while preserving placeholder tokens:
- Draft
- Revised Draft
- Planning Notes
- Final Version

Example:

```markdown
::: placeholder
Draft {{PH-2: U01-D1-guided-rewrite}}
:::
```

## 8. Pandoc/Lint Notes

- Missing blank lines before headings should be fixed.
- Multiple consecutive spaces should be fixed unless intentional.
- Long blockquotes should be converted to semantic Divs.
- Activity codes in headings are not errors; they are intentional QA metadata.
- Unit 23 hierarchy needs explicit review/fix.

## 9. What To Use Next

For Codex or scripted editing, use files in this order:

1. `aw_adv_step1_complete_master_packet.md` — policy and priorities.
2. `aw_adv_markdown_edit_instruction_lines_REVISED.csv` — line-level actions.
3. `activity_headings_missing_subtitles.csv` — subtitle additions.
4. `aw_adv_pandoc_markdown_lint_report.csv` — source hygiene fixes.
5. `aw-adv-all.md` — source file to modify.
