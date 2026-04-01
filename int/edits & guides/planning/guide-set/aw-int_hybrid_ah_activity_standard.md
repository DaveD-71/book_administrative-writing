# Intermediate Hybrid A-H Activity Standard

## Purpose

This standard introduces a **hybrid A-H activity overlay** for the Intermediate book.

The goal is:

- to align the Intermediate book more clearly with the Advanced book's visible activity architecture
- to keep the Intermediate book's learner-friendly functional labels
- to avoid importing the Advanced system wholesale in a way that would make the Intermediate book harder to read

In practice, this means the Intermediate book will now use **section letters plus readable labels**, for example:

- `### A. Warm-Up: ...`
- `### B. Model Check: ...`
- `### C. Language 1 - ...`
- `### D. Guided Practice - ...`
- `### E. Freer Practice - ...`
- `### F. Reflection`
- `### G. Editing Practice: ...`
- `### H. Homework`

`### Focus` remains uncoded front matter.

## Core Rule

Each unit keeps its existing learner-facing section names, but the live section headings must now be grouped into the following hybrid A-H shell:

- `A` = opening / activation / orientation
- `B` = model reading / model check / explanation of why the model works
- `C` = language building and controlled practice
- `D` = guided writing or guided production
- `E` = freer writing and extended independent production
- `F` = review / self-check / reflection
- `G` = editing / revision / repair
- `H` = transfer / homework / later-use extension

## Mapping Standard

### Front Matter

- `### Focus` stays unchanged
- it is not assigned an A-H letter
- it remains the learner-facing unit goal and scope frame

### A. Opening / Activation

Apply `A` to headings that prepare the learner before model analysis, including:

- `Warm-Up`
- concept-introduction headings such as `What Is ...`, `When Should ...`, `Why Team Consistency Matters`, and similar early orientation frames
- scenario-orientation headings such as `Scenario Overview`

### B. Model Layer

Apply `B` to the main model-analysis layer:

- `Model Check: ...`

Use `B` for learner-visible model comparison / explanation headings only.

### C. Language And Controlled Practice

Apply `C` to headings that build the target skill before full guided production, including:

- `Language ...`
- phrase-bank / useful-phrases headings
- controlled practice headings such as `Practice A`, `Practice B`, `Practice C`

### D. Guided Production

Apply `D` to scaffolded production headings, including:

- `Guided Practice - ...`
- `Extended Guided Practice - ...`

### E. Freer / Extended Production

Apply `E` to independent or semi-independent output layers, including:

- `Freer Practice - ...`
- `Extended Writing Task - ...`
- planning-board or production-board headings that directly prepare the freer or final output
- final production headings such as `Final Portfolio Submission`

### F. Review / Self-Check / Reflection

Apply `F` to headings that ask the learner to evaluate readiness, review output, or reflect on learning, including:

- `Self-Check ...`
- `Reflection`
- review / rubric / balance-check headings that function as learner self-review

### G. Editing / Revision

Apply `G` to headings that require repair, correction, revision, or explicit editing decisions, including:

- `Editing Practice: ...`
- rebuild / revision-routine headings whose main function is text repair

### H. Transfer / Homework

Apply `H` to headings that extend the unit skill beyond the main unit output, including:

- `Transfer Extension: ...`
- `Homework`
- `Homework (Final Course Task)`
- end-of-unit transfer-plan headings that clearly function as later-use carry-forward work

## Implementation Rules

- Keep the current wording after the letter prefix.
- Do not replace learner-friendly labels with advanced-only terminology such as `Opening & Activation` or `Freer Writing`.
- Do not add sub-activity codes like `(A2)` or `(C3)` in this pass.
- Do not apply the hybrid A-H shell to `### Focus`.
- Apply the hybrid shell to unit-level activity headings, not to module-review support sections in this pass.

## Examples

- `### Warm-Up: What Makes a Sentence Clear?` -> `### A. Warm-Up: What Makes a Sentence Clear?`
- `### Model Check: Why the Stronger Sentence Works` -> `### B. Model Check: Why the Stronger Sentence Works`
- `### Language 1 - Basic Sentence Pattern (SVO / SVC)` -> `### C. Language 1 - Basic Sentence Pattern (SVO / SVC)`
- `### Guided Practice - Rewrite for Clarity` -> `### D. Guided Practice - Rewrite for Clarity`
- `### Freer Practice - Write Clear Administrative Sentences` -> `### E. Freer Practice - Write Clear Administrative Sentences`
- `### Reflection` -> `### F. Reflection`
- `### Editing Practice: Fix the Reader Problem` -> `### G. Editing Practice: Fix the Reader Problem`
- `### Transfer Extension: Turn Sentences into a Mini Message` -> `### H. Transfer Extension: Turn Sentences into a Mini Message`
- `### Homework` -> `### H. Homework`

## Scope

This standard applies to:

- `int/md/final/modules/*.md`
- the rebuilt combined file `int/md/final/aw-int-all.md`

This standard does not yet require:

- a full Advanced-style sub-activity code layer such as `(B1)` or `(F3)`
- renaming module-review support sections to A-H labels
- rewriting the Intermediate book into the exact Advanced section inventory
