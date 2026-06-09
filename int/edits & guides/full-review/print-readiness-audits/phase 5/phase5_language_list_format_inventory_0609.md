# Phase 5 Language-List Format Inventory

## Scope

This inventory covers student-facing language banks and reusable language-support lists in `int/md/working/aw-int-all_0519.md`.

Included:

- phrase banks
- vocabulary or verb banks
- openings / closings / purpose-line banks
- audience-specific or function-specific language sets

Excluded:

- general self-check checklists
- structural or proofreading lists that do not mainly teach reusable wording

## Pattern Families

### Pattern A. Simple phrase bank with no subgroup labels

- setup: div title, optional one-sentence lead-in, then one bullet list
- function-label formatting: none
- item capitalization: sentence case or normal phrase case
- item punctuation: grammatical punctuation kept, often ellipses, commas, or periods
- examples: Unit 2 `Useful Phrases for Requests`, Unit 4 `Opening Purpose Phrases`, Unit 5 `Asking for Clarification`, Unit 5 `Checking Your Understanding`, Unit 5 `Example Clarification Questions`

### Pattern B. Bold subgroup labels without colons

- setup: div title, then bold function headings as standalone lines
- function-label formatting: bold, no colon
- item capitalization: varies by subgroup; usually sentence case for model phrases, lowercase for cause fragments
- item punctuation: grammatical punctuation kept; fragments usually have no periods
- examples: Unit 2 `Useful Phrases by Function`, Unit 10 `Useful Problem-Explanation Phrases`, Unit 13 `Useful Phrases for Explanations`, Unit 14 `Useful Phrases to Clarify Information`, Unit 21 `Standardising Team Writing`, Unit 22 `Three Audiences, Three Styles`

### Pattern C. Plain-text subgroup labels ending with a colon

- setup: div title, optional lead-in sentence, then plain function labels on separate lines ending in `:`
- function-label formatting: plain text plus colon
- item capitalization: varies by grammar; sentence-style phrases use capitals, fragment lists may be lowercase
- item punctuation: sentence-style items keep punctuation; fragment lists usually have none
- examples: Unit 4 `Email Openings and Closings`, Unit 6 `Useful Phrases for Delays and Changes`, Unit 8 `Clear Instruction Verbs`, Unit 12 `Structure of an External Inquiry`

### Pattern D. Mixed structure-plus-language block

- setup: one block combines a non-language structure list with a phrase bank
- function-label formatting: plain structural lead-in plus bold or plain phrase-bank marker
- item capitalization: structure items often title case or bold noun phrases; phrase-bank items use sentence case
- item punctuation: structure items often no end punctuation; phrase-bank items follow grammar
- examples: Unit 11 `Key Elements of a Meeting Summary`, Unit 12 `Structure of an External Inquiry`, Unit 20 `Revision vs. Notice`

### Pattern E. Table-based language bank

- setup: language support is presented as a two-column table rather than bullets
- function-label formatting: row labels such as `Greeting`, `Opening`, `Purpose`
- item capitalization: sentence case or phrase case inside table cells
- item punctuation: grammatical punctuation kept inside examples
- example: Unit 15 `Standard Email Elements`

## Instance Inventory

| Unit | Block title | Setup pattern | Function-label style | List item capitalization | List item punctuation | Notes |
|---|---|---|---|---|---|---|
| 2 | Useful Phrases for Requests | single list | none | sentence case | ellipses / question marks | clean simple phrase bank |
| 2 | Useful Phrases by Function | grouped list | bold labels, no colon | sentence case | grammar-based | function labels are visually stronger than in plain-colon lists |
| 4 | Subject Lines | single list after bold sublabel | bold sublabel `**Examples of Clear Subject Lines**` | Title Case noun phrases | none | subject-line examples differ from normal sentence-style phrase banks |
| 4 | Email Openings and Closings | grouped list | plain labels with colon | sentence case | commas / periods | plain-colon function labels |
| 4 | Opening Purpose Phrases | single list | none | sentence case | ellipses | clean simple phrase bank |
| 5 | Asking for Clarification | single list | none | sentence case | ellipses / question marks | consistent with Unit 2 request list |
| 5 | Checking Your Understanding | single list | none | sentence case | question marks / comma / ellipsis | mixed punctuation because phrases are incomplete starters |
| 5 | Example Clarification Questions | single list | none | sentence case | full question marks / colon within item | example-question bank rather than phrase stem bank |
| 6 | Useful Phrases for Delays and Changes | grouped list | plain labels with colon | mixed: sentence case plus lowercase fragments | mixed: sentence punctuation for full clauses, none for fragment reasons | strongest example of grammar-based capitalization split |
| 8 | Clear Instruction Verbs | single list | plain lead-in with colon | single-word Title Case | none | visually inconsistent with lowercase fragment convention elsewhere |
| 10 | Useful Problem-Explanation Phrases | grouped list | bold labels, no colon | mixed: sentence case plus lowercase cause fragments | mixed by grammar | parallel to Unit 6 but with different function-label styling |
| 11 | Key Elements of a Meeting Summary | mixed structure + phrase bank | plain lead-in plus bold `**Useful Phrases**` | bold noun phrases in structure list; sentence case in phrase list | none in structure list; ellipses in phrase list | two different list types inside one block |
| 12 | Structure of an External Inquiry | numbered structure list + phrase list | plain lead-in plus plain `Useful phrases:` | sentence case in phrase list | ellipses / question marks / periods | mixed numbered structure and bullet language support |
| 13 | Useful Phrases for Explanations | grouped list | bold labels, no colon | mixed: sentence case plus lowercase fragments | mixed by grammar | same grammar logic as Units 6 and 10 |
| 14 | Useful Phrases to Clarify Information | grouped list | bold labels, no colon | sentence case | periods / ellipses | most internally consistent bold-group model |
| 15 | Standard Email Elements | table | row labels in table | sentence case / phrase case | commas / periods / ellipses | table outlier, not a normal list |
| 20 | Revision vs. Notice | mixed audience blocks | bold audience labels plus plain `Useful phrases:` | sentence case | periods / ellipses | repeated `Useful phrases:` label under two audience headings |
| 21 | Standardising Team Writing | grouped list | bold labels, no colon | mixed: sentence case plus Title Case fragments | mixed: some none, some periods / commas / ellipses | `Formatting Standards` list is not really a phrase bank |
| 22 | Three Audiences, Three Styles | grouped list | bold audience labels, no colon | sentence case | periods / ellipses | audience labels include parenthetical descriptors |

## Main Formatting Findings

1. Function labels currently use at least four visible styles:
   - none
   - bold without colon
   - plain text with colon
   - table row labels

2. Item capitalization follows grammar more often than one visual style:
   - full sentence or phrase starters use sentence case
   - cause fragments such as `because...` or `due to...` use lowercase
   - subject lines use Title Case
   - single-word verb banks use Title Case

3. Item punctuation is also grammar-based rather than standardized visually:
   - ellipses for open phrase stems
   - periods for complete statements
   - commas where the phrase itself requires one
   - no punctuation for fragments, noun phrases, or one-word items

4. The repo already has a grammar-based punctuation policy, but the presentation of function labels is not yet standardized across comparable language banks.

## Likely Standardization Questions

- Should function labels in phrase banks default to bold headings or plain labels with colons?
- Should one-word language items such as instruction verbs stay in Title Case, or align with fragment-list lowercase logic?
- Should mixed structure-plus-language blocks be split more consistently so structure lists and phrase banks do not share one formatting frame?
- Should subject-line example lists be treated as a separate style family because they are titles rather than sentence stems?
