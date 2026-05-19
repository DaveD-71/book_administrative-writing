# Intermediate Semantic Heading And Example Reclassification Plan

Date: 2026-05-19

Scope: `int/md/working/aw-int-all.md`

Purpose: align the Intermediate book with the Advanced semantic-div standard before final DOCX visual cleanup.

Reference Advanced documents:

- `adv/edits & guides/style edits/step3-div-reclassification/div_class_reclassification_0515.md`
- `adv/edits & guides/style edits/step3-div-reclassification/div_reclassification_review_0516.md`
- `adv/edits & guides/style edits/step3-div-reclassification/div_reclassification_full_0516.md`

## Summary

The Intermediate Stage 2 div pass successfully added semantic fenced divs, but it did not complete the Advanced-style semantic reclassification pass. The skipped work is mainly:

- converting only non-structural pedagogical headings to semantic divs
- removing `####` headings from inside semantic divs
- classifying example/source/sample texts as `example`, `example-good`, or `example-bad`
- preserving meaningful student-facing title information during conversion
- normalizing alphabetic option lists that currently render incorrectly in DOCX

Current audit findings:

- 456 divs exist in `int/md/working/aw-int-all.md`
- 129 `####` headings are currently inside semantic divs
- 14 current `example` divs exist
- 0 current `example-good` and `example-bad` divs exist
- multiple weak/strong, original/revised, example, and versioned examples remain outside the example-class system

## Governing Rules

### Structural Heading Treatment

`### Focus` in the Intermediate book is structurally equivalent to `Unit Overview` in the Advanced book. It should receive the same treatment as the Advanced overview layer.

The Intermediate `A-H` headings are structurally equivalent to the Advanced `A-H` headings. They should receive the same treatment as the Advanced activity shell.

These headings are not conversion candidates by default:

- `### Focus`
- `##`, `###`, and `####` headings that begin with structural letters `A.` through `H.`

The open design problem is duplication: the current source can create a structural `###` heading followed immediately by a semantic div whose title repeats or closely matches that heading. This produces a redundant heading-plus-label pair.

Stage 7A must decide how to handle those duplicated pairs consistently. Candidate treatments:

1. Keep both heading and div label when the heading gives navigation and the div label adds a different learner action or narrower task focus.
2. Keep the structural heading and shorten or retitle the div label when the div title merely repeats the heading.
3. Keep the structural heading and remove the redundant div title only if the build pipeline can still render the semantic styling correctly without losing the visible label requirement.
4. Merge the heading detail into the div label only for non-structural headings; do not apply this to `### Focus` or A-H structural headings.

Only non-structural pedagogical headings remain conversion candidates. Examples include uncoded practice/example subheadings, redundant labels inside divs, and source-sample headings that do not belong to the book's structural navigation layer.

Non-structural headings inside semantic divs should not remain as headings. Convert them to one of:

- the visible div label
- a short bold/plain body sublabel
- a separate semantic div
- an instruction sentence that preserves the useful information

### Title Preservation

Reclassification changes the semantic container or label relationship; it must not erase useful student-facing information.

Do not flatten meaningful activity titles into repeated generic labels such as only:

- `Practice`
- `Example`
- `Rewrite`
- `Notice`
- `Language`
- `Edit`

When a heading or div label names a document type, audience, purpose, scenario, language feature, decision point, or task condition, preserve that information in one of these places:

- the structural heading
- the div label
- a short body sublabel
- the first instruction line

Good non-structural conversion pattern:

```markdown
### Practice - Soften A Direct Request
```

becomes:

```markdown
::: rewrite
Soften A Direct Request

Rewrite the request so it sounds clear and respectful.
:::
```

Weak non-structural conversion pattern:

```markdown
::: rewrite
Practice

Rewrite the request.
:::
```

The second version is too generic because it loses the specific student orientation.

For structural heading plus div-label duplication, preserve the structural heading and retitle the div label only when the new label adds semantic value. Do not collapse `### Focus` or A-H headings into div labels.

### Div Classification

Class is determined by what the learner does, not by the Focus/A-H structural section heading or by heading wording alone.

Use this classification set:

| Content or learner action | Class |
|---|---|
| Reads teaching input, principle, explanation, reminder, or worked guidance | `learn` |
| Uses grammar, vocabulary, phrases, sentence patterns, or reference language | `language` |
| Produces original text from a scenario | `write` |
| Transforms given text into a better or different version | `rewrite` |
| Improves the learner's own earlier draft | `revise` |
| Observes, identifies, compares, evaluates, or analyses given text | `notice` |
| Plans, sequences, organizes, or works inside a template/framework | `structure` |
| Corrects, polishes, proofs, checks, or fixes language/mechanics | `edit` |
| Reads a source, example, sample, comparison text, or reference example | `example`, `example-good`, `example-bad` |

High-risk distinctions:

- `language` is wrong for explanation-only blocks. Use `learn`.
- `language` is wrong for transformation tasks. Use `rewrite`.
- `language` is wrong for analysis tasks. Use `notice`.
- `edit` is for correction/proofreading/checking. If the learner rewrites a supplied text substantially, use `rewrite`.
- `revise` is only for improving the learner's own earlier draft.
- `structure` is for organization, sequencing, templates, and document frameworks.

## Example Classification Plan

### Class Definitions

Use `example-bad` for intentionally weak or problematic text. Signals include:

- weak
- original, when followed by revision or diagnosis
- unclear
- inconsistent
- too direct
- too vague
- incomplete
- problem version
- less effective version

Use `example-good` for target or improved text. Signals include:

- stronger
- revised
- improved
- example
- possible answer
- preferred version
- consistent
- polished
- effective version

Use `example` for neutral input/reference text. Signals include:

- source email
- scenario text
- report excerpt
- meeting note
- form entry
- document sample used for analysis
- worked example where good/bad quality is not the point

### Paired Examples

Weak/strong, original/revised, inconsistent/consistent, and before/after pairs should normally become adjacent example blocks:

```markdown
::: example-bad
Weak Version

...
:::

::: example-good
Stronger Version

...
:::
```

Keep the pair labels specific. Do not reduce them to only `Bad Example` and `Good Example` if the original title contains useful context.

### Ambiguous Examples

If a text is called "example" but is used only as neutral input for analysis, classify it as `example`.

If a text is called "example" and is presented as the recommended target standard, classify it as `example-good`.

If `Version A` and `Version B` are compared but the text does not identify which is stronger, classify both as `example` unless the surrounding instruction makes the evaluation clear.

## Work Phases

### Phase 1 - Create Inventory

Create a reclassification inventory before editing the source.

Recommended output file:

`int/edits & guides/style edits/step7a-semantic-reclassification/semantic_reclassification_inventory_0519.md`

Inventory columns:

| Line | Current heading/class | Current text | Proposed action | Proposed class | Title preservation | Reason |
|---|---|---|---|---|---|---|

Include:

- all `### Focus` and A-H structural heading plus div-label pairs where the title repeats or nearly repeats
- all non-structural pedagogical headings that may need conversion
- all non-structural `####` headings inside divs
- all existing `example` divs
- all candidate weak/strong, original/revised, example, versioned, and comparison examples
- any `language` divs that are actually `learn`, `notice`, `rewrite`, `write`, or `structure`

Search terms:

```text
Weak
Stronger
Original
Revised
Version A
Version B
Example
Inconsistent
Consistent
Before
After
```

### Phase 2 - Classify Headings

For each structural heading plus semantic div pair:

1. Confirm whether the heading is `### Focus` or begins with `A.` through `H.`.
2. Keep the heading as structural.
3. Compare the heading text and the following div label.
4. If the div label repeats the heading, decide whether to keep it, shorten it, or retitle it with a narrower learner action.
5. Preserve specific title information in either the structural heading or the div label.

For each non-structural candidate heading:

1. Decide whether it is structural or non-structural.
2. If structural, leave it as a heading and mark it as structural in the inventory.
3. If non-structural, convert it to a semantic div or body sublabel as appropriate.
4. Preserve specific title information in the div label, body sublabel, or instruction line.
5. Check that no placeholder block is pulled inside the div.

For each non-structural `####` heading inside a div:

1. Decide whether it is a task label, example label, local sublabel, or structural mistake.
2. Convert it to a div label, body sublabel, or separate semantic block.
3. Split the surrounding div if the `####` starts a different learner action.
4. Do not introduce nested divs.

### Phase 3 - Classify Examples

For each candidate example:

1. Identify the example's function: neutral source, weak/problem sample, target example, or comparison pair.
2. Assign `example`, `example-good`, or `example-bad`.
3. Split pairs into separate adjacent divs where needed.
4. Preserve useful original labels such as document type, audience, or problem focus.
5. Keep setup instructions outside the example div unless they are part of the example text itself.

Likely first targets among existing `example` divs:

- `Possible stronger version` likely becomes `example-good`
- `Stronger version` likely becomes `example-good`
- `Example Paragraph` likely becomes `example-good` if presented as a target example
- `Example Notice` likely becomes `example-good` if presented as target wording
- `Example - Inconsistent vs. Consistent` likely splits into `example-bad` and `example-good`
- larger source excerpts stay `example` unless explicitly presented as preferred examples

### Phase 4 - Normalize Alpha Lists

During the same source cleanup, normalize alphabetic option lists so Pandoc emits separate list items.

Known issue: some current `A./B./C.` lists render in DOCX with embedded markers in one paragraph, such as `A...B...C...`.

Fix pattern:

- keep genuine option lists as proper Markdown lists
- ensure each option is a separate paragraph/list item
- avoid hard line breaks that Pandoc treats as one paragraph
- retest DOCX output for embedded `B.` / `C.` / `D.` markers inside `List Number 3` paragraphs

### Phase 5 - Rebuild And Verify

After source edits:

1. Rebuild the Intermediate DOCX with the shared reference DOCX.
2. Run reference validation.
3. Run structural source checks.
4. Inspect DOCX list rendering and semantic label rendering.

Required checks:

```powershell
$lines = Get-Content int/md/working/aw-int-all.md
$opens = ($lines | Where-Object { $_ -match '^:::\s+[\w-]+\s*$' }).Count
$closes = ($lines | Where-Object { $_ -match '^:::\s*$' }).Count
"Opens: $opens  Closes: $closes  Match: $($opens -eq $closes)"
```

Completion gates:

- `### Focus` remains structurally aligned with Advanced `Unit Overview`
- all `##`/`###`/`####` headings beginning with `A.` through `H.` remain structurally aligned with the Advanced A-H shell
- duplicate structural-heading-plus-div-label pairs have a documented treatment
- zero non-structural pedagogical headings remain outside divs unless documented as intentionally structural
- zero non-structural `###` or `####` headings remain inside semantic divs
- zero nested divs
- div open and close counts match
- no placeholders are inside semantic divs
- checklist items remain only in `edit`
- all examples are classified as `example`, `example-good`, or `example-bad`
- converted headings preserve useful student-facing specificity
- alphabetic option lists render as separate list items in DOCX
- DOCX validates against `adv/md/working/aw-adv-styleref.docx`

## Non-Goals

Do not rewrite the content for pedagogy beyond what is necessary to preserve or clarify labels during reclassification.

Do not create a separate Intermediate style reference DOCX.

Do not change structural unit architecture. In particular, do not convert `A.` through `F.` letter-coded headings at `##`, `###`, or `####` level.

Do not use generic labels merely for visual consistency if they erase helpful student orientation.

## Deliverables

1. Reclassification inventory.
2. Edited `int/md/working/aw-int-all.md`.
3. Rebuilt Intermediate DOCX.
4. Verification notes with counts before and after.
5. Any unresolved ambiguous headings/examples listed for manual decision.
