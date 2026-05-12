# Administrative Writing Textbook — Full Style Sheet

## Design Direction

This style sheet defines the visual system for a new clean Pandoc reference DOCX for an educational textbook.

The design approach is modern, clean, professional, and educational. It uses restrained typography, strong but controlled semantic accents, generous spacing, and consistent object formatting.

The book should feel:

- readable
- calm
- modern
- editorial
- structured
- professional
- pedagogically clear

The book should not feel:

- corporate
- worksheet-heavy
- presentation-like
- visually cluttered
- randomly formatted
- overly dense

---

## 1. Document Setup

| Area | Setting | Value |
|---|---|---:|
| Page | Paper size | A4 portrait |
| Page | Top margin | 2.2 cm |
| Page | Bottom margin | 2.2 cm |
| Page | Left margin | 3.0 cm |
| Page | Right margin | 3.0 cm |
| Page | Gutter | 0 cm |
| Page | Mirror margins | Off |
| Page | Different odd/even pages | On |
| Page | Different first page | On |
| Page | Header distance from edge | 1.0 cm |
| Page | Footer distance from edge | 1.0 cm |
| Body | Default body font | Congenial |
| Headings | Heading font | Roboto Condensed |
| Code | Monospace font | Consolas |
| Language | Proofing language | English |
| Paragraphs | Widow/orphan control | On |
| Paragraphs | Hyphenation | Off |
| Paragraphs | Snap to grid | Off |
| Output | PDF target | Digital and print |

---

## 2. Colour System

| Role | Colour Name | RGB | Hex |
|---|---|---:|---|
| Body text | Charcoal | 45,45,45 | #2D2D2D |
| Heading text | Near black | 35,35,35 | #232323 |
| Muted text | Grey | 110,110,110 | #6E6E6E |
| Learning blue | Muted blue | 63,110,180 | #3F6EB4 |
| Language blue-grey | Blue-grey | 86,118,140 | #56768C |
| Good green | Muted green | 82,143,74 | #528F4A |
| Bad red | Muted red | 176,62,62 | #B03E3E |
| Transfer orange | Muted orange | 196,125,42 | #C47D2A |
| Neutral grey | Soft grey | 150,150,150 | #969696 |
| Module fill | Dark navy-grey | 45,65,85 | #2D4155 |
| Unit fill | Medium blue-grey | 70,100,125 | #46647D |
| Light blue fill | Very light blue | 242,247,252 | #F2F7FC |
| Light grey fill | Very light grey | 247,247,247 | #F7F7F7 |
| Light green fill | Very light green | 244,250,242 | #F4FAF2 |
| Light red fill | Very light red | 252,244,244 | #FCF4F4 |
| Light orange fill | Very light orange | 253,248,240 | #FDF8F0 |
| Border grey | Light border grey | 205,210,214 | #CDD2D6 |

---

## 3. Spacing Scale

| Role | Value | Use |
|---|---:|---|
| Micro | 2 pt | Tight inline relationships |
| Tight | 4 pt | Closely related elements |
| Normal | 6 pt | Ordinary paragraph grouping |
| Reading | 7 pt | Main body paragraph after-spacing |
| Recovery | 8 pt | After lists and compact blocks |
| Block | 10 pt | Semantic block before/after |
| Activity | 14 pt | Activity heading before-spacing |
| Section | 18 pt | Major section before-spacing |
| Module | 24 pt | Large transitions |

Spacing rules:

| Rule | Value |
|---|---|
| Body line spacing | 1.30 |
| Body paragraph after | 7 pt |
| List item after | 3 pt |
| After-list recovery | 8 pt |
| Semantic block before/after | 10 pt |
| Heading before greater than heading after | Yes |
| Heading attached to following content | Yes |
| Arbitrary spacing values | Not used |

---

## 4. Paragraph Styles

Actual Markdown heading audit after Step 1:

| Markdown level | Present in latest source | Required Word style |
|---|---:|---|
| `#` | 1 planned | Heading 1 — book title/front matter title |
| `##` | 29 | Heading 2 |
| `###` | 214 | Heading 3 |
| `####` | 328 | Heading 4 |
| `#####` | 7 | Heading 5 |
| `######` | 0 | Not required; do not define/use Heading 6 |

Therefore the active heading hierarchy for the current normalized Markdown is:

- Heading 1 — book title/front matter title
- Heading 2 — module and unit titles
- Heading 3 — module introduction, unit overview, A–H sections, rubric subsections
- Heading 4 — activity headings and true theory headings
- Heading 5 — rare micro-theory labels

Semantic Div content is not part of the heading hierarchy.

All main text styles are defined as Word **linked paragraph and character styles** unless explicitly stated otherwise. This is important because Pandoc and Word may apply the same named style at paragraph level or character level depending on the conversion context.

| Style Name | Word Style Type | Purpose | Based On | Next Style | Font | Size | Weight/Style | Colour | Alignment | Line Spacing | Before | After | Left Indent | Right Indent | Paragraph Borders | Paragraph Shading | Border Spacing | Pagination |
|---|---|---|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| Normal | Paragraph | Base fallback | — | Body Text | Congenial | 10.5 pt | Regular | Charcoal | Left | 1.30 | 0 pt | 6 pt | 0 cm | 0 cm | None | None | — | Widow/orphan on |
| Body Text | Linked paragraph + character | Main prose | Normal | Body Text | Congenial | 10.5 pt | Regular | Charcoal | Left | 1.30 | 0 pt | 7 pt | 0 cm | 0 cm | None | None | — | Widow/orphan on |
| Body Text Compact | Linked paragraph + character | Dense procedural prose | Body Text | Body Text | Congenial | 10 pt | Regular | Charcoal | Left | 1.15 | 0 pt | 4 pt | 0 cm | 0 cm | None | None | — | Widow/orphan on |
| Heading 1 | Linked paragraph + character | Book title/front matter title | Normal | Body Text | Roboto Condensed | 24 pt | Medium | White | Left | Single | 0 pt | 16 pt | 0 cm | 0 cm | None | Dark navy-grey fill | 0 pt | Page break before; keep with next; keep lines together; single line spacing |
| Heading 2 | Linked paragraph + character | Unit title | Normal | Body Text | Roboto Condensed | 17 pt | Medium | White | Left | Single | 20 pt | 10 pt | 0 cm | 0 cm | None | Medium blue-grey fill | 0 pt | Keep with next; keep lines together; single line spacing |
| Heading 3 | Linked paragraph + character | Major section A–H | Normal | Body Text | Roboto Condensed | 14 pt | Regular | Near black | Left | Single | 18 pt | 6 pt | 0.3 cm | 0 cm | Left 4.5 pt muted blue-grey | Very light blue-grey fill | Left border space 3 pt | Keep with next; keep lines together; single line spacing |
| Heading 4 | Linked paragraph + character | Activity heading | Normal | Body Text | Roboto Condensed | 12 pt | Regular | Charcoal | Left | Single | 14 pt | 5 pt | 0 cm | 0 cm | Bottom 0.75 pt light grey-blue | None | Bottom border space 1 pt | Keep with next; keep lines together; single line spacing |
| Heading 5 | Linked paragraph + character | Theory/micro heading | Normal | Body Text | Roboto Condensed | 11 pt | Regular | Charcoal | Left | Single | 8 pt | 4 pt | 0 cm | 0 cm | Bottom 0.5 pt light grey | None | Bottom border space 1 pt | Keep with next; keep lines together; single line spacing |
| Homework Target | Linked paragraph + character | Module homework target | Body Text | Body Text | Congenial | 10 pt | Italic | Grey | Left | 1.15 | 0 pt | 12 pt | 0 cm | 0 cm | None | None | — | Widow/orphan on; keep with next |
| Reflection Text | Linked paragraph + character | Reflection prompt | Body Text | Body Text | Congenial | 10 pt | Italic | Grey | Left | 1.20 | 6 pt | 6 pt | 0.5 cm | 0 cm | None | None | — | Widow/orphan on |
| After List | Linked paragraph + character | Recovery paragraph after list | Body Text | Body Text | Congenial | 10.5 pt | Regular | Charcoal | Left | 1.30 | 8 pt | 6 pt | 0 cm | 0 cm | None | None | — | Widow/orphan on |
| Caption | Linked paragraph + character | Caption | Body Text | Body Text | Congenial | 9 pt | Italic | Grey | Left | 1.10 | 4 pt | 8 pt | 0 cm | 0 cm | None | None | — | Widow/orphan on; keep with previous |
| Page Header | Linked paragraph + character | Running header | Normal | Page Header | Congenial | 8 pt | Regular | Grey | Left | Single | 0 pt | 0 pt | 0 cm | 0 cm | None | None | — | Single line spacing |
| Page Footer | Linked paragraph + character | Running footer | Normal | Page Footer | Congenial | 8 pt | Regular | Grey | Outside page edge | Single | 0 pt | 0 pt | 0 cm | 0 cm | None | None | — | Single line spacing |

Linked-style rule:

| Rule | Value |
|---|---|
| Heading styles | Linked paragraph + character |
| Body and supporting paragraph styles | Linked paragraph + character |
| Normal | Paragraph only; left aligned; widow/orphan on |
| Pure inline emphasis styles | Character only, listed in Section 7 |
| Semantic Div styles | Linked paragraph + character, listed in Section 6 |
| Table styles | Table styles, listed in Section 8 |


---

## 5. List Styles And List Templates

Microsoft Word list formatting must be controlled through both:

1. paragraph styles, and
2. multilevel list templates.

The paragraph style controls the paragraph appearance. The list template controls the marker, numbering, indentation, restart behaviour, linked style, and follow-marker behaviour.

The reference DOCX must define stable list templates instead of relying on Word's automatic list guessing.

---

## 5.1 List Paragraph Styles

| Style Name | Purpose | Font | Size | Colour | Line Spacing | Before | After | Left Indent | Hanging Indent | Marker | Marker Colour | Restart Rule |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|
| List Bullet | Standard bullet list | Congenial | 10.5 pt | Charcoal | 1.15 | 0 pt | 3 pt | 0.8 cm | 0.45 cm | • | Charcoal | Not applicable |
| List Bullet 2 | Nested bullet list | Congenial | 10 pt | Charcoal | 1.10 | 0 pt | 2 pt | 1.3 cm | 0.45 cm | ◦ | Charcoal | Not applicable |
| List Number | Standard numbered list | Congenial | 10.5 pt | Charcoal | 1.15 | 0 pt | 3 pt | 0.9 cm | 0.5 cm | 1. | Charcoal | Restart per list |
| List Number 2 | Nested numbered list | Congenial | 10 pt | Charcoal | 1.10 | 0 pt | 2 pt | 1.4 cm | 0.5 cm | a. | Charcoal | Restart per parent list |
| Checklist | Self-edit checklist | Congenial | 10.5 pt | Charcoal | 1.15 | 0 pt | 4 pt | 0.9 cm | 0.5 cm | □ | Charcoal | Not applicable |

List block recovery:

| Setting | Value |
|---|---:|
| Space after final list item before prose | 8 pt |
| Space after final list item before heading | Heading spacing controls |
| Space after final list item before semantic block | 8 pt |

---

## 5.2 Multilevel List Template — Textbook Bullet List

| Setting | Value |
|---|---|
| Template name | Textbook Bullet List |
| Template type | Multilevel bullet list |
| Number of active levels | 2 |
| Restart behaviour | Continuous within local list block |
| Apply linked styles | Yes |
| Use Word automatic bullet formatting | No |

### Textbook Bullet List — Level Definitions

| Level | Linked Paragraph Style | Marker | Marker Font | Marker Size | Marker Colour | Number/Bullet Alignment | Aligned At | Text Indent At | Tab Stop At | Follow Marker With | Add Tab Stop | Restart After Level | Paragraph After | Line Spacing |
|---:|---|---|---|---:|---|---|---:|---:|---:|---|---|---|---:|---:|
| 1 | List Bullet | • | Congenial | 10.5 pt | Charcoal | Left | 0.35 cm | 0.80 cm | 0.80 cm | Tab character | Yes | None | 3 pt | 1.15 |
| 2 | List Bullet 2 | ◦ | Congenial | 10 pt | Charcoal | Left | 0.85 cm | 1.30 cm | 1.30 cm | Tab character | Yes | None | 2 pt | 1.10 |

---

## 5.3 Multilevel List Template — Textbook Numbered List

| Setting | Value |
|---|---|
| Template name | Textbook Numbered List |
| Template type | Multilevel numbered list |
| Number of active levels | 2 |
| Apply linked styles | Yes |
| Restart level 1 | At each independent Markdown ordered list block |
| Restart level 2 | After level 1 |
| Preserve lazy Markdown numbering | Yes; output numbering controlled by template |
| Use legal-style numbering | No |

### Textbook Numbered List — Level Definitions

| Level | Linked Paragraph Style | Number Style | Number Format | Marker Font | Marker Size | Marker Colour | Number Alignment | Aligned At | Text Indent At | Tab Stop At | Follow Number With | Add Tab Stop | Restart After Level | Paragraph After | Line Spacing |
|---:|---|---|---|---|---:|---|---|---:|---:|---:|---|---|---|---:|---:|
| 1 | List Number | Arabic | %1. | Congenial | 10.5 pt | Charcoal | Left | 0.35 cm | 0.90 cm | 0.90 cm | Tab character | Yes | None | 3 pt | 1.15 |
| 2 | List Number 2 | Lowercase letter | %2. | Congenial | 10 pt | Charcoal | Left | 0.85 cm | 1.40 cm | 1.40 cm | Tab character | Yes | Level 1 | 2 pt | 1.10 |

---

## 5.4 Single-Level List Template — Textbook Checklist

| Setting | Value |
|---|---|
| Template name | Textbook Checklist |
| Template type | Single-level bullet list |
| Linked paragraph style | Checklist |
| Marker | □ |
| Marker font | Congenial |
| Marker size | 10.5 pt |
| Marker colour | Charcoal |
| Alignment | Left |
| Aligned at | 0.35 cm |
| Text indent at | 0.90 cm |
| Tab stop at | 0.90 cm |
| Follow marker with | Tab character |
| Add tab stop | Yes |
| Paragraph after | 4 pt |
| Line spacing | 1.15 |

---

## 5.5 List Implementation Rules

| Rule | Value |
|---|---|
| Create list templates before applying list paragraph styles | Yes |
| Link each list-template level to its paragraph style | Yes |
| Use direct paragraph indent overrides | No |
| Use direct numbering overrides | No |
| Use Word automatic list guessing | No |
| Use separate templates for bullets and numbers | Yes |
| Use separate checklist template | Yes |
| Keep list marker colour same as body text | Yes |
| Maintain 8 pt recovery space after completed list blocks | Yes |
| Do not use 1.5 line spacing inside lists | Yes |
| Do not globally renumber lazy Markdown lists in source | Yes |
| Let Pandoc/Word output numbering resolve through template | Yes |

---

## 5.6 Visual Weight Review For List System

The list system is deliberately light.

| Feature | Value |
|---|---|
| Bullet marker weight | Normal |
| Number marker weight | Normal |
| Marker colour | Body charcoal, not accent colour |
| List text weight | Regular |
| List indentation | Moderate |
| Internal spacing | Compact-readable |
| External spacing | 8 pt recovery after list block |

---

## 6. Semantic Div Paragraph Styles

These paragraph styles are applied to Pandoc semantic Div content.

The reference DOCX used strong paragraph borders, including 4.5–6 pt left borders. The new design keeps that attention-drawing grammar but modernizes it with cleaner colour, lighter fills, and tighter spacing.

| Style Name | Div Class | Purpose | Font | Size | Weight/Style | Colour | Line Spacing | Before | After | Left Indent | Right Indent | Paragraph Border | Border Colour | Border Spacing | Shading | Internal Effect |
|---|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---|---|---|---|---|
| Learn Process | `learn-process` | Why a model/revision/process works | Congenial | 10 pt | Regular | Charcoal | 1.20 | 10 pt | 10 pt | 0.35 cm | 0 cm | Left 4.5 pt | Muted blue | 3 pt | Very light blue | Strong left attention rule |
| Learn Language | `learn-language` | Language, grammar, phrase, register, contrast | Congenial | 10 pt | Regular | Charcoal | 1.20 | 10 pt | 10 pt | 0.35 cm | 0 cm | Left 4.5 pt | Blue-grey | 3 pt | Very light blue-grey | Strong left attention rule |
| Learn Principle | `learn-principle` | Major conceptual principle | Congenial | 10 pt | Regular | Charcoal | 1.20 | 10 pt | 10 pt | 0.35 cm | 0 cm | Left 6 pt | Muted blue | 3 pt | Soft light blue | Highest learning emphasis |
| Learn Transfer | `learn-transfer` | Transfer/application reminder | Congenial | 10 pt | Regular | Charcoal | 1.20 | 10 pt | 10 pt | 0.35 cm | 0 cm | Left 6 pt | Muted orange | 3 pt | Very light orange | Reminder/caution emphasis |
| Learn Teaching | `learn-teaching` | Teaching-point explanation | Congenial | 10 pt | Regular | Charcoal | 1.20 | 10 pt | 10 pt | 0.35 cm | 0 cm | Left 4.5 pt | Muted blue | 3 pt | Very light blue | Teaching emphasis |
| Learn Note | `learn-note` | General explanatory note | Congenial | 10 pt | Regular | Charcoal | 1.20 | 8 pt | 8 pt | 0.35 cm | 0 cm | Left 3 pt | Soft grey | 3 pt | Very light grey | Low emphasis note |
| Model Bad | `model-bad` | Original/problematic sample | Congenial | 10 pt | Italic allowed in sample | Charcoal | 1.20 | 10 pt | 10 pt | 0.5 cm | 0.5 cm | Top 0.75 pt / Left 6 pt / Bottom 0.75 pt / Right 0.75 pt | Muted red | Left 2 pt; other 1 pt | Very light red | Red sample container |
| Model Good | `model-good` | Revised/improved sample | Congenial | 10 pt | Italic allowed in sample | Charcoal | 1.20 | 10 pt | 10 pt | 0.5 cm | 0.5 cm | Top 0.75 pt / Left 6 pt / Bottom 0.75 pt / Right 0.75 pt | Muted green | Left 2 pt; other 1 pt | Very light green | Green sample container |
| Worked Example | `worked-example` | Procedural demonstration | Congenial | 10 pt | Regular | Charcoal | 1.20 | 10 pt | 10 pt | 0.35 cm | 0 cm | Left 4.5 pt | Blue-grey | 3 pt | Very light blue-grey | Demonstration container |
| Example | `example` | Ordinary block example | Congenial | 10 pt | Regular | Charcoal | 1.20 | 8 pt | 8 pt | 0.35 cm | 0 cm | Left 3 pt | Soft grey | 3 pt | Very light grey | Low-emphasis example |
| Placeholder | `placeholder` | Student response marker | Congenial | 10 pt | Italic | Grey | 1.15 | 8 pt | 8 pt | 0 cm | 0 cm | Full 0.5 pt dotted | Soft grey | 2 pt | No fill | Quiet writable marker |
| Self Study | `self-study` | Self-study guidance | Congenial | 10 pt | Regular | Charcoal | 1.20 | 8 pt | 8 pt | 0.35 cm | 0 cm | Left 3 pt | Soft grey | 3 pt | Very light grey | Learner guidance |
| Annotation | `annotation` | Annotation explaining model feature | Congenial | 9.5 pt | Regular | Grey | 1.15 | 4 pt | 6 pt | 0.35 cm | 0 cm | Left 3 pt | Soft grey | 2 pt | No fill | Small annotation |

Semantic label character formatting:

| Label Type | Font | Size | Weight | Colour |
|---|---|---:|---|---|
| Learn label | Roboto Condensed | 10 pt | Medium | Matching semantic accent |
| Learn principle label | Roboto Condensed | 10 pt | Medium | Muted blue |
| Learn transfer label | Roboto Condensed | 10 pt | Medium | Muted orange |
| Model bad label | Roboto Condensed | 10 pt | Medium | Muted red |
| Model good label | Roboto Condensed | 10 pt | Medium | Muted green |
| Worked example label | Roboto Condensed | 10 pt | Medium | Blue-grey |
| Placeholder label | Congenial | 10 pt | Italic | Grey |
| Annotation label | Congenial | 9.5 pt | Regular Italic | Grey |

Semantic block object rules:

| Property | Value |
|---|---|
| Maximum block width | Body text width |
| Text wrapping | Inline with text flow |
| Floating | No |
| Shadow | None |
| Bevel | None |
| Glow | None |
| 3D effects | None |
| Corner radius | 0 pt |
| Consecutive semantic block separation | 6 pt minimum |
| Maximum semantic fill coverage per page | 25% |

---

## 7. Character Styles

| Style Name | Purpose | Font | Size | Weight/Style | Colour | Additional Setting |
|---|---|---|---:|---|---|---|
| Strong | Ordinary emphasis | Congenial | Inherit | Medium | Charcoal | No colour change |
| Emphasis | Italic emphasis | Congenial | Inherit | Italic | Inherit | No colour change |
| Metadata Code | Activity code `(B1)` | Roboto Condensed | 8 pt | Regular | Grey | Small caps; hidden off |
| Activity Star | Star marker `★` | Roboto Condensed | 8 pt | Regular | Muted orange | Baseline normal |
| Learn Label | Learn label | Roboto Condensed | 10 pt | Regular | Semantic colour | Used only inside learn blocks |
| Model Label Bad | Original text label | Roboto Condensed | 10 pt | Medium | Muted red | Used only inside model-bad |
| Model Label Good | Revised text label | Roboto Condensed | 10 pt | Medium | Muted green | Used only inside model-good |
| Inline Code | Code/token text | Consolas | 9 pt | Regular | Charcoal | Light grey highlight #F7F7F7 |
| Placeholder Token | `{{PH-*}}` token | Consolas | 8 pt | Regular | Grey | Hidden off |
| Small Note | Secondary note text | Congenial | 9 pt | Regular Italic | Grey | Used for quiet metadata |

---

## 8. Table Styles

## 8.1 Global Table Object Settings

| Setting | Value |
|---|---|
| Table alignment | Center |
| Table preferred width | 100% of text block |
| Table left indent | 0 cm |
| Text wrapping | None |
| Cell spacing | 0 pt |
| Allow row to break across pages | Off |
| Repeat header row | On |
| Default vertical cell alignment | Top |
| Default paragraph alignment in cells | Left |
| Table space before | 8 pt |
| Table space after | 10 pt |
| Autofit | Fixed column widths after creation |
| Table layout | Fixed |

## 8.2 Standard Table

| Property | Value |
|---|---|
| Font | Congenial |
| Font size | 9.5 pt |
| Line spacing in cells | 1.10 |
| Paragraph after in cells | 2 pt |
| Table alignment | Center |
| Preferred width | 100% |
| Left indent | 0 cm |
| Header fill | Dark navy-grey #2D4155 |
| Header text colour | White |
| Header font weight | Medium |
| Header row repeat | On |
| Outside top border | 0.75 pt #969696 |
| Outside bottom border | 0.75 pt #969696 |
| Outside left border | 0.75 pt #969696 |
| Outside right border | 0.75 pt #969696 |
| Inside horizontal borders | 0.5 pt #CDD2D6 |
| Inside vertical borders | 0.5 pt #CDD2D6 |
| Cell top margin | 4 pt |
| Cell bottom margin | 4 pt |
| Cell left margin | 5 pt |
| Cell right margin | 5 pt |
| Row shading | None |
| Table before spacing | 8 pt |
| Table after spacing | 10 pt |

## 8.3 Rubric Table

| Property | Value |
|---|---|
| Font | Congenial |
| Font size | 9 pt |
| Line spacing in cells | 1.10 |
| Paragraph after in cells | 3 pt |
| Table alignment | Center |
| Preferred width | 100% |
| Left indent | 0 cm |
| Header fill | Medium blue-grey #46647D |
| Header text colour | White |
| Header font weight | Medium |
| Header row repeat | On |
| Outside borders | 0.75 pt #969696 |
| Inside horizontal borders | 0.5 pt #CDD2D6 |
| Inside vertical borders | 0.5 pt #CDD2D6 |
| Alternating row fill | #F7F7F7 |
| Cell top margin | 5 pt |
| Cell bottom margin | 5 pt |
| Cell left margin | 6 pt |
| Cell right margin | 6 pt |
| Allow row break across pages | Off |
| Table before spacing | 10 pt |
| Table after spacing | 12 pt |

## 8.4 Phrase Bank Table

| Property | Value |
|---|---|
| Font | Congenial |
| Font size | 9.5 pt |
| Line spacing in cells | 1.10 |
| Paragraph after in cells | 2 pt |
| Table alignment | Center |
| Preferred width | 100% |
| Header fill | #F2F7FC |
| Header text colour | Near black #232323 |
| Header font weight | Medium |
| Outside borders | 0.5 pt #CDD2D6 |
| Inside borders | 0.5 pt #CDD2D6 |
| Cell top margin | 4 pt |
| Cell bottom margin | 4 pt |
| Cell left margin | 6 pt |
| Cell right margin | 6 pt |
| Table before spacing | 8 pt |
| Table after spacing | 10 pt |

## 8.5 Comparison Table

| Property | Value |
|---|---|
| Font | Congenial |
| Font size | 9.5 pt |
| Line spacing in cells | 1.10 |
| Paragraph after in cells | 3 pt |
| Table alignment | Center |
| Preferred width | 100% |
| Header fill | #F7F7F7 |
| Header text colour | Near black #232323 |
| Header font weight | Medium |
| Outside borders | 0.5 pt #CDD2D6 |
| Inside borders | 0.5 pt #CDD2D6 |
| Left comparison accent | 3 pt muted red border on original column |
| Right comparison accent | 3 pt muted green border on revised column |
| Cell top margin | 5 pt |
| Cell bottom margin | 5 pt |
| Cell left margin | 6 pt |
| Cell right margin | 6 pt |
| Table before spacing | 10 pt |
| Table after spacing | 10 pt |

---

## 9. Object Styles

## 9.1 Semantic Container Object

| Property | Value |
|---|---|
| Text wrapping | Top and bottom |
| Horizontal alignment | Align with text block left edge |
| Width | 100% of text block |
| Internal top margin | 5 pt |
| Internal bottom margin | 5 pt |
| Internal left margin | 6 pt |
| Internal right margin | 6 pt |
| Border width | 0.75 pt |
| Border colour | Matching semantic accent |
| Fill | Matching semantic light fill |
| Corner radius | 0 pt |
| Shadow | None |
| Glow | None |
| Bevel | None |
| Transparency | 0% object transparency; colour is pre-lightened |
| Object spacing before | 10 pt |
| Object spacing after | 10 pt |
| Anchor | Move with text |
| Allow overlap | Off |

## 9.2 Image Object

| Property | Value |
|---|---|
| Alignment | Center |
| Text wrapping | Top and bottom |
| Border | 0.5 pt #CDD2D6 |
| Shadow | None |
| Glow | None |
| Bevel | None |
| Aspect ratio | Locked |
| Space before | 10 pt |
| Space after | 10 pt |
| Caption spacing after | 8 pt |
| Caption alignment | Left |
| Anchor | Move with text |
| Allow overlap | Off |

## 9.3 Text Box Object

| Property | Value |
|---|---|
| Text wrapping | Top and bottom |
| Horizontal alignment | Align with text block |
| Width | 100% of text block unless explicitly sized by layout |
| Internal top margin | 5 pt |
| Internal bottom margin | 5 pt |
| Internal left margin | 6 pt |
| Internal right margin | 6 pt |
| Border | 0.75 pt #CDD2D6 |
| Fill | White |
| Shadow | None |
| Glow | None |
| Bevel | None |
| Anchor | Move with text |
| Allow overlap | Off |

## 9.4 Separator Rule

| Property | Value |
|---|---|
| Line width | 0.5 pt |
| Line colour | #CDD2D6 |
| Space before | 10 pt |
| Space after | 10 pt |
| Alignment | Text block width |
| Use | Section separators only |

---

## 10. Page Furniture

## 10.1 Global Running Page Settings

| Setting | Value |
|---|---|
| Different odd and even pages | On |
| Different first page | On |
| Header distance from edge | 1.0 cm |
| Footer distance from edge | 1.0 cm |
| Module opener header/footer | Suppressed |
| Unit opener header/footer | Footer only |
| Running header decorative line | None |
| Running footer decorative line | None |

## 10.2 Odd Page Footer

| Property | Value |
|---|---|
| Alignment | Outside/right |
| Page number position | Outside/right |
| Running text position | Inside/left |
| Running text content | Short unit title |
| Font | Congenial |
| Size | 8 pt |
| Weight | Regular |
| Colour | Grey #6E6E6E |
| Border line | None |

## 10.3 Even Page Footer

| Property | Value |
|---|---|
| Alignment | Outside/left |
| Page number position | Outside/left |
| Running text position | Inside/right |
| Running text content | Administrative Writing, Advanced |
| Font | Congenial |
| Size | 8 pt |
| Weight | Regular |
| Colour | Grey #6E6E6E |
| Border line | None |

## 10.4 Page Number Character Style

| Property | Value |
|---|---|
| Font | Congenial |
| Size | 8 pt |
| Weight | Regular |
| Colour | Grey #6E6E6E |
| Bold | Off |
| Italic | Off |

---

## 11. Pandoc Mapping Notes

| Markdown / Div Element | Word Style |
|---|---|
| `#` | Heading 1 — book title/front matter title |
| `##` | Heading 2 |
| `###` | Heading 3 |
| `####` | Heading 4 |
| `#####` | Heading 5 |
| `######` | Not used; do not define Heading 6 |
| Normal paragraph | Body Text |
| Bullet list | List Bullet |
| Ordered list | List Number |
| `::: learn-process` | Learn Process |
| `::: learn-language` | Learn Language |
| `::: learn-principle` | Learn Principle |
| `::: learn-transfer` | Learn Transfer |
| `::: learn-teaching` | Learn Teaching |
| `::: learn-note` | Learn Note |
| `::: model-bad` | Model Bad |
| `::: model-good` | Model Good |
| `::: worked-example` | Worked Example |
| `::: example` | Example |
| `::: placeholder` | Placeholder |
| `::: self-study` | Self Study |
| `::: annotation` | Annotation |
| `(B1)`, `(C2)`, `(H3)` | Metadata Code character style |
| `{{PH-*}}` | Placeholder Token character style |

---

## 12. Modern Visual Consistency Rules

### Visual Weight Control

The redesign deliberately reduces the number of bold/heavy elements. Bold is avoided except where Word/Pandoc requires it for default behaviour or where a future cover/front-matter design explicitly calls for it. Frequent elements use Regular or Medium weights so the page does not become visually busy.

| Element Type | Maximum Weight |
|---|---|
| Body text | Regular |
| Ordinary emphasis | Medium |
| Heading 1 | Medium |
| Heading 2 | Medium |
| Heading 3 | Regular |
| Heading 4 | Regular |
| Heading 5 | Regular |
| Learn labels | Regular or Medium |
| Model labels | Medium |
| Annotation labels | Regular Italic |
| Table headers | Medium |
| List markers | Regular |
| Footer/page numbers | Regular |



| Rule | Value |
|---|---|
| Body text carries reading experience | Yes |
| Roboto Condensed used only for navigation/labels | Yes |
| Semantic accent colours used consistently | Yes |
| Heavy visual effects | Not used |
| Shadows/glows/bevels | Not used |
| Black borders | Not used |
| Saturated fills | Not used |
| Border system | Strong left accent for semantic learning blocks; restrained full borders for model samples |
| Heading system | Calm, lightweight, navigational |
| List system | Compact internal rhythm with recovery space after block |
| Table system | Fixed layout, centered, generous cell margins, light borders |
| Page furniture | Quiet editorial footer system |
| Metadata | Small, grey, non-competing |
| Overall look | Modern, clean, editorial textbook |

---

## 13. PDF-Derived Visual Refinements

The following refinements were identified during direct visual review of the current PDF layout and have been incorporated into the final style direction.

### 13.1 Heading Density Control

Observed issue:

- Heading frequency remains visually high.
- Repeated Heading 4 activity titles create excessive visual interruption.
- Roboto Condensed can become visually tiring when used repeatedly at similar weights.

Final design rule:

| Setting | Value |
|---|---|
| Heading 4 font weight | Regular only |
| Heading 4 tracking | Normal |
| Heading 4 colour | #2D2D2D only |
| Heading 4 border | Bottom 0.75 pt only |
| Heading 4 fill | None |
| Heading 4 all caps | Not permitted |
| Consecutive heading spacing compression | Enabled visually via lower after-spacing |

Result:

- calmer activity rhythm
- reduced heading fatigue
- more editorial feel

---

### 13.2 Module And Unit Opening Pages

Observed issue:

- Module and unit opener pages still feel slightly Word-document-like.
- Top titles compete visually with page furniture.

Final design rule:

| Setting | Value |
|---|---|
| Module opener top whitespace | Increased |
| Module title vertical padding | 8 pt top/bottom |
| Unit title vertical padding | 5 pt top/bottom |
| Running footer on module opener | Suppressed |
| Running header on module opener | Suppressed |
| Introductory prose max width | Body text width only |

Result:

- more premium textbook feel
- stronger section transitions
- improved visual pacing

---

### 13.3 Body Text Texture

Observed issue:

- Some pages still appear slightly grey and dense.
- Long instructional passages need stronger visual breathing rhythm.

Final design rule:

| Setting | Value |
|---|---|
| Body line spacing | 1.30 fixed |
| Body paragraph after-spacing | 7 pt |
| Maximum consecutive body paragraphs without interruption | 5 preferred |
| Recovery space after dense prose | 8–10 pt |
| Left/right margins | 3.0 cm fixed |

Result:

- improved readability
- reduced fatigue
- calmer page texture

---

### 13.4 List Rhythm

Observed issue:

- Lists in the PDF visually merge into surrounding prose.
- Recovery space after lists is insufficient in some sections.

Final design rule:

| Setting | Value |
|---|---|
| List line spacing | 1.15 |
| List item after-spacing | 3 pt |
| Space after complete list block | 8 pt |
| Bullet alignment | Optical left alignment |
| List marker colour | #2D2D2D |

Result:

- cleaner scanning
- stronger instructional rhythm
- reduced crowding

---

### 13.5 Semantic Learning Blocks

Observed issue:

- Existing semantic blocks sometimes feel disconnected from surrounding prose.
- Some blocks appear visually heavier than necessary.

Final design rule:

| Setting | Value |
|---|---|
| Semantic left border emphasis | Retained |
| Left border width | 4.5–6 pt depending on semantic importance |
| Border spacing | 3 pt |
| Fill brightness | Minimum 94% |
| Fill saturation | Low |
| Full-box borders | Reserved for model-good/model-bad only |
| Rounded corners | Not used |
| Shadows | Not used |
| Consecutive semantic blocks | Minimum 6 pt separation |

Result:

- modernized semantic system
- strong educational signalling
- cleaner visual integration

---

### 13.6 Placeholder Areas

Observed issue:

- Placeholder drafting areas visually collapse into surrounding instructional prose.
- Students need stronger visual recognition of writable areas.

Final design rule:

| Setting | Value |
|---|---|
| Placeholder border | 0.5 pt dotted grey |
| Placeholder spacing before | 8 pt |
| Placeholder spacing after | 8 pt |
| Placeholder fill | None |
| Placeholder label style | Grey italic |
| Placeholder minimum height | 2 lines equivalent |

Result:

- improved usability
- clearer learner interaction zones
- less visual confusion

---

### 13.7 Model Comparison Sections

Observed issue:

- Original vs revised samples are among the strongest pedagogical elements in the PDF.
- These require stronger visual distinction than ordinary notes.

Final design rule:

| Setting | Value |
|---|---|
| Original sample border accent | 6 pt muted red |
| Revised sample border accent | 6 pt muted green |
| Comparison spacing before | 10 pt |
| Comparison spacing after | 10 pt |
| Comparison internal padding | 6 pt |
| Comparison fill intensity | Very light only |

Result:

- clearer pedagogical contrast
- stronger revision visibility
- improved learning clarity

---

### 13.8 Running Footer Visual Balance

Observed issue:

- Footer positioning in the PDF still feels slightly detached from the page architecture.

Final design rule:

| Setting | Value |
|---|---|
| Footer distance from edge | 1.0 cm |
| Footer font size | 8 pt |
| Footer colour | #6E6E6E |
| Footer alignment | Outside edge |
| Decorative footer rules | Not used |
| Footer bold | Not permitted |

Result:

- calmer navigation system
- more professional editorial appearance
- stronger long-document consistency |
