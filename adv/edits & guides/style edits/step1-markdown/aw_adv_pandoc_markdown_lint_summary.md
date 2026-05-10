# Pandoc Markdown lint report: `aw-adv-all.md`

## Summary

- Total lint findings: 408
- High severity: 60
- Medium severity: 317
- Low severity: 31

## Findings by category

- heading_contains_activity_code: 294
- blockquote_as_callout: 60
- multiple_spaces: 30
- missing_blank_before_heading: 10
- frequent_duplicate_heading: 8
- long_blockquote: 4
- missing_blank_after_heading: 1
- trailing_space: 1

## Interpretation

The file is mostly clean for a long generated Markdown source. The main Pandoc-relevant risks are not syntax corruption, but semantic/styling issues that affect DOCX conversion:

1. `heading_contains_activity_code` (294 findings): activity codes such as `(B1)`, `(C2)`, `(H3)` are embedded in headings. These should become metadata styling where possible.
2. `blockquote_as_callout` (60 findings): labelled blockquotes are being used as callouts. Convert by function: `why-this-works`, `language-note`, `teaching-point`, `transfer-reminder`, etc.
3. `frequent_duplicate_heading` (8 findings): repeated headings such as `Homework Writing Task` and `Extension Task` are probably semantic components, not document hierarchy.
4. `missing_blank_before_heading` (10 findings): Pandoc usually handles these, but blank lines before headings reduce conversion ambiguity.
5. `multiple_spaces` (30 findings): review manually; most are probably harmless alignment/spacing artifacts.
6. `long_blockquote` (4 findings): verify whether these are true quotations/examples or should be converted to model/callout blocks.

## Recommended Step 1 completion criteria

Before moving to the reference DOCX:

- Apply or approve the semantic edit instruction list.
- Resolve high-severity lint findings.
- Resolve heading hierarchy issues around Unit 23.
- Decide whether activity codes remain visible in heading text for this quick Module 1 pass, or are moved to metadata later.
- Keep numbered-list lazy numbering (`1.` repeated) unless Word output is failing; Pandoc normally handles this correctly.
