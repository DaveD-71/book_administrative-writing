# Lines To Change CSV Summary

Source: `aw-adv-all.md`
Total lines in source: 6,850
Rows in change CSV: 744

## Counts By Change Type

- normalize_placeholder_line: 243
- add_activity_subtitle_and_standardize_heading: 241
- convert_or_review_blockquote_group: 75
- convert_blockquote_to_learn_div: 51
- normalize_bold_structural_label: 34
- review_blockquote_label: 24
- convert_label_to_div_or_label: 21
- convert_label_to_div: 20
- standardize_minor_heading_punctuation_capitalization: 11
- standardize_model_label_and_wrap_sample: 6
- convert_annotation_label: 6
- fix_rubric_subheading_hierarchy: 6
- standardize_activity_heading: 5
- fix_heading_hierarchy: 1

## Counts By Target Class

- activity-heading: 246
- placeholder: 243
- semantic-div: 75
- semantic-label: 34
- learn-note: 26
- learn-process: 23
- learn-transfer: 22
- example: 21
- worked-example: 20
- heading: 18
- annotation: 6
- model-good: 3
- model-bad: 3
- learn-language: 2
- learn-principle: 1
- learn-teaching: 1

## Notes

- Activity headings are kept as headings, but standardized.
- Activity codes remain in Markdown for QA.
- Instructional blockquotes are converted to semantic Divs.
- `Why This Works` uses `learn-process`; `Note On...` uses `learn-language`.
- Model labels use `Text`, not `Version`.
- Placeholder tokens must be preserved exactly.