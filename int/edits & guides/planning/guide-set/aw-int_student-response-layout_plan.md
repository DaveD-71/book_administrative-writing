# Student Response Layout Plan
## *Administrative Writing, Intermediate*

---

> **Purpose of this document**
> This file defines the placeholder strategy for the intermediate student book after text sign-off and before final print layout.
>
> It decides:
> - how many placeholder types are needed
> - where placeholders should be inserted
> - which extra labels or instructions are needed so students understand each writing space

---

## 1. Layout Assumption

The intermediate book is also a **handwritten student book**.

That means the layout must support:

- slower handwriting at A2-B1+ level
- visibly separated spaces for different document types
- clearer box labeling than the current plain `Write your email:` style prompts

Use the same **five placeholder types** as the advanced book so the series stays consistent.

---

## 2. Placeholder Types

| ID | Name | Typical use | Relative size |
|---|---|---|---|
| `PH-1` | Short Response | one to three sentences, one short opening line, one short correction, one planning note | small |
| `PH-2` | Paragraph Response | one short paragraph, one guided rewrite, one edited paragraph | medium-small |
| `PH-3` | Short Document | one short email, notice, explanation, procedure, or short manual section | medium |
| `PH-4` | Long Document | the largest single-response areas in the intermediate book, especially later integrated tasks | large |
| `PH-5` | Multi-Part Pack | paired or three-part document sets, especially Modules 6 and Unit 23 work | composite |

Series rule:

- use the same IDs across both books
- size the final boxes by page design, but keep the type logic stable

---

## 3. Where Placeholders Belong

### 3.1 Insert placeholders in these recurring zones

| Intermediate location pattern | Placeholder rule |
|---|---|
| `Guided Practice` that asks for a complete email / paragraph / notice / procedure | insert `PH-2` or `PH-3` |
| `Freer Practice` | insert `PH-2`, `PH-3`, or `PH-5` depending on whether the task asks for one text, two texts, or a document set |
| `Extended Writing Task` | insert `PH-3` or `PH-4` |
| `Editing Practice` where students rewrite the full corrected version | insert `PH-1` or `PH-2` |
| `Transfer Extension` when it produces a real written output | insert `PH-1` or `PH-2` |
| `Homework` | insert the same placeholder size as the main productive task for that unit, usually `PH-2`, `PH-3`, or `PH-5` |

### 3.2 Do not use large placeholders in these zones by default

| Location pattern | Layout treatment |
|---|---|
| Warm-Up / Model Check / self-check / reflection | keep as ordinary lines, bullets, or checkboxes |
| short sentence-level drills inside language sections | use normal answer lines rather than document-style boxes |
| phrase lists, examples, and mini contrast notes | no response placeholder needed |

---

## 4. Intermediate-Specific Placement Decisions

### 4.1 Units that ask for two texts

Many intermediate units explicitly ask for:

- two emails
- two notices
- two procedures
- two summaries
- two responses

These should **not** use one merged box.

Rule:

- use **two labeled `PH-2` or `PH-3` boxes**
- each box should be labeled by purpose or audience

Preferred labels:

- `Email 1`
- `Email 2`
- `Notice 1`
- `Notice 2`
- `Procedure 1`
- `Procedure 2`
- `External Version`
- `Internal Version`

### 4.2 Paragraph-style units

Where the book asks for one paragraph of roughly five to six sentences, use `PH-2`, not a full-page document box.

This applies especially to:

- paragraph writing units in Module 1
- report-style or summary paragraphs in Modules 2 to 4
- editing-revision paragraphs in Module 5

### 4.3 Module 6 integrated tasks

Module 6 contains the clearest need for `PH-5`.

Use labeled sub-boxes for:

- external email + internal explanation pairs
- revision message + internal notice pairs
- applicant reply + colleague explanation + internal notice sets
- multi-audience communication packs
- Unit 23 final portfolio / final-course task responses

Do not flatten these into one large placeholder. The layout should make the audience split visible.

### 4.4 Editing and revision units in Module 5

Module 5 contains more rewriting than first-draft writing.

Rule:

- use smaller revision boxes (`PH-1` or `PH-2`) for item-level repair
- use `PH-2` or `PH-3` when the task asks for a full rewritten paragraph or email

---

## 5. Additional Headings / Instructions Needed

The intermediate book needs clearer response-area labels than it currently has.

Use these standardized labels:

- `Write Here`
- `Write Your Email`
- `Write Your Paragraph`
- `Write Your Notice`
- `Write Your Revised Version`
- `Document 1`
- `Document 2`
- `Document 3`
- `Planning Notes`
- `Homework Draft`

Use these short instruction patterns where needed:

- `Use this box for one complete version.`
- `Write one sentence on each line where possible.`
- `Write the full corrected version below.`
- `Keep the facts the same, but change the audience and tone.`
- `Write each document in its own box.`

For paired and multi-document tasks, the audience or purpose must be named above each box. `Write here` alone is not enough.

---

## 6. Recommended Marker System For Later Pandoc Work

If placeholder markers are added to the Markdown later, use the same stable format as the advanced book:

- `{{PH-1: unit-task-label}}`
- `{{PH-2: unit-task-label}}`
- `{{PH-3: unit-task-label}}`
- `{{PH-4: unit-task-label}}`
- `{{PH-5: unit-task-label}}`

Examples:

- `{{PH-2: U03-guided-paragraph}}`
- `{{PH-3: U10-freer-email-1}}`
- `{{PH-5: U22-multi-audience-pack}}`

This keeps the source clean while making later replacement through Pandoc or a post-processing step straightforward.

---

## 7. Stage Decision

Add a late-stage project task for:

- student-response placeholder planning
- placeholder insertion into the final student-book source
- page-layout preparation for print

For the intermediate book, this should happen **after QA and full review** and against the final student-book source set, not against older draft-only reference files.

---

*Document status: planning decision for the intermediate student-book placeholder and page-layout stage.*
