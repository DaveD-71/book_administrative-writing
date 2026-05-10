
# Administrative Writing Textbook — Step 1 Master Specification

Version: Consolidated Step 1 Source Normalization + Semantic Architecture Spec

Purpose:
This document is now the authoritative source of truth for:
- Markdown normalization
- Semantic taxonomy
- Heading policy
- Activity-heading conventions
- Metadata strategy
- Semantic Div strategy
- Callout semantics
- Typography intent
- Pandoc conversion assumptions

This supersedes earlier partial recommendations where conflicts exist.

---

# 1. OVERALL ARCHITECTURE

The publishing workflow is:

Markdown
→ Pandoc
→ reference.docx
→ Word post-processing
→ PDF QA

The Markdown source should preserve:
- editorial QA visibility
- pedagogical structure
- activity traceability

The Word/PDF output should prioritize:
- readability
- calm hierarchy
- scanability
- instructional clarity
- semantic visual signalling

---

# 2. HEADING POLICY

## KEEP AS TRUE HEADINGS

The following remain Markdown headings:

| Level | Meaning |
|---|---|
| # | Book/module level only |
| ## | Unit level |
| ### | Major section level (A–H sections) |
| #### | Activity headings and true theory subsections |
| ##### | Rare micro-theory labels only |

Do NOT remove activity headings.

Activity headings are intentionally retained because:
- they improve scanability
- they provide pedagogical variety
- they help student orientation
- they support future icon replacement systems

---

# 3. ACTIVITY HEADING STANDARDIZATION

## Canonical Pattern

Activity headings should follow:

#### Activity Family — Subtitle (CODE)

Examples:
- #### Practice A — Match The Function (C2)
- #### Editing Exercise — Improve Clarity And Flow (G1)
- #### Guided Peer Review — Structured Feedback Exchange (F2)

## Rules

### Capitalization
Use Title Case consistently.

### Dash
Use em dash (—) consistently for subtitles.

### Metadata Codes
Keep inline codes like:
- (B1)
- (C2)
- (H3)

These are editorial QA metadata and remain in Markdown.

### Final Rendering
Metadata codes should later be:
- hidden
OR
- visually suppressed
OR
- rendered as muted metadata

in Word/PDF output.

Do NOT remove them from source Markdown.

---

# 4. THEORY SUBSECTIONS

True theory subsections may remain as #### headings.

Examples:
- #### Coordination
- #### Subordination
- #### Clarity Patterns For Administrative Writing

Avoid excessive metadata in theory headings.

---

# 5. MODEL TEXT STANDARDIZATION

## Standard Labels

Replace all uses of:
- Version

with:
- Text

## Canonical Pairs

Use:
- Original Text
- Revised Text

Optional subtitle examples:
- Original Text — Too Direct
- Revised Text — Diplomatic
- Original Text — Disjointed
- Revised Text — Cohesive

## Semantic Div Classes

Use:
- ::: model-bad
- ::: model-good

---

# 6. LEARNING CALLOUT SYSTEM

All instructional/learning notes should use semantic Divs.

Do NOT use Markdown blockquotes for instructional callouts.

Replace instructional blockquotes with semantic Div blocks.

---

# 7. LEARNING TAXONOMY

All pedagogical notes belong to the root concept:

Learn

But they MUST remain differentiated by function.

## Semantic Classes

| Semantic Class | Function |
|---|---|
| learn-process | Writing-process rationale after example/model |
| learn-language | Language/grammar/vocabulary/contrast explanation |
| learn-principle | Major conceptual principle |
| learn-transfer | Transfer/application reminder |
| learn-note | General explanatory note |
| learn-teaching | Teaching-point explanation |

---

# 8. PLACEHOLDER STANDARDIZATION

Use consistent student-response labels.

| Purpose | Label |
|---|---|
| drafting | Draft |
| revision | Revised Draft |
| planning | Planning Notes |
| final submission | Final Version |

Use semantic Div:
::: placeholder

---

# 9. BLOCKQUOTE POLICY

Instructional notes should NOT remain Markdown blockquotes.

Replace all instructional blockquotes with semantic Div blocks.

---

# 10. CAPITALIZATION POLICY

Use Title Case consistently for:
- activity headings
- instructional labels
- callout labels
- major pedagogical labels

---

# 11. PUNCTUATION POLICY

Use em dash (—) for:
- activity subtitles
- model-text subtitles

Use parentheses ONLY for metadata codes.

---

# 12. METADATA STRATEGY

Metadata codes remain in Markdown for:
- editorial QA
- structural verification
- completeness checking
- fast scanning

Final output strategy:
- hide
OR
- mute
OR
- minimize visually

in Word/PDF output.

---

# 13. VISUAL SEMANTICS

| Meaning | Semantic Role |
|---|---|
| Green | revised / improved / correct |
| Red | problematic / original / flawed |
| Blue | explanation / learning |
| Orange | reminder / transfer / caution |
| Grey | reflection / low-intensity note |

---

# 14. IMPLEMENTATION PRIORITIES

## High Priority
- semantic Div replacement for instructional blockquotes
- activity-heading standardization
- model-text standardization
- capitalization normalization
- punctuation normalization

## Medium Priority
- placeholder normalization
- metadata styling
- theory subsection cleanup

## Deferred
- icon replacement system
- advanced semantic Lua filters
- deep metadata extraction

---

# 15. AUTHORITATIVE STATUS

This document is now the canonical Step 1 specification.
