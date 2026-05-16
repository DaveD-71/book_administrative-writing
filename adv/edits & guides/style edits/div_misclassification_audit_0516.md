# Div Misclassification Audit — aw-adv-all_0516.md

**File audited:** `C:\Dev\Code\book_administrative-writing\adv\md\working\aw-adv-all_0516.md`
**Audit date:** 2026-05-16
**Method:** Full file read, div by div. Every div was read and its content assessed independently of its label.

---

## 1. Misclassification List

| Line | Current class | Correct class | Label line | Reason |
|---|---|---|---|---|
| 138 | `language` | `learn` | Learn — Patterns: | Lists coordination connectors as pattern references (X *and* Y, X *but* Y, etc.) with no task. Pure teaching input — a pattern reference panel, not a practice exercise. |
| 163 | `language` | `learn` | Learn — Patterns: | Lists subordinating conjunctions (*because, although, when*, etc.) with no task. Pure teaching input — a vocabulary reference panel. |
| 180 | `language` | `learn` | 3. Clarity Patterns For Administrative Writing | A reference table of three named patterns with worked examples. No production task in this div. The learner reads and refers to it — teaching input presented as a named reference. |
| 194 | `language` | `rewrite` | Apply the Patterns | Explicitly asks the learner to rewrite each sentence using the indicated pattern. This is a sentence-transformation production task, not a language input panel. |
| 207 | `language` | `learn` | Learn — Note On Contrast: | A teaching note explaining when to use *but* vs. *however* vs. *although*. No task — the learner reads and absorbs the principle. |
| 213 | `language` | `learn` | Learn — Note On Contrast: | A teaching note explaining *although* vs. *while* as subordinate contrast markers, with an example comparison. No task. |
| 472 | `rewrite` | `learn` | 2. Neutral Clarification Language | This outer div provides a definition and explanation of neutral clarification language as a language category. No rewrite task is issued inside this div (the rewrite task is in the separate `rewrite` div at line 489). The div is teaching input about a language category. |
| 500 | `notice` | `learn` | 3. Audience-Appropriate Tone | Presents a named scale (Internal / Interagency / International), a worked example table, and an explanatory principle statement. No observation or analysis task is required from the learner — the div explains the principle. The learner reads it as teaching input. |
| 756 | `notice` | `learn` | 1. Cohesive Devices | Presents a reference classification table grouping cohesive devices by function (adding, result, contrast, clarifying), followed by explanatory prose about why cohesive devices matter. No noticing task is assigned in this outer div — it is a teaching reference panel. (The nested `notice` at line 770 contains the actual sorting task.) |
| 810 | `language` | `learn` | 3. Thematic Progression | Opens with a principle statement ("Good paragraphs start with known information…"), contains a nested pattern table with a three-step example and explanatory commentary. No practice task is in this outer div. Teaching input about a discourse principle, not a language form. |
| 828 | `language` | `rewrite` | Add Logical Connectors | Asks the learner to add appropriate connectors to four sentences with blank spaces. This is a sentence-completion/rewrite task, not a language input panel. |
| 1413 | `language` | `notice` | Phrase Bank Building | Provides a list of phrases and asks the learner to sort/organise them into a personal phrase bank under four labelled headings. This is a classification/sorting observation task — the learner analyses and categorises given material, producing no new text. |
| 2655 | `language` | `rewrite` | Expansion Task — Develop Supporting Detail | Asks the learner to expand each bare sentence into 2–3 sentences by adding specific missing elements (effective date, reason, description of change, benefit). This is a text-expansion/rewrite production task, not a language input panel. |
| 3629 | `language` | `notice` | Phrase Bank Building — Build Reusable Language | Provides twelve phrases and asks the learner to sort them into a personal phrase bank under four headings. Classification/sorting task on given material — same pattern as line 1413. |
| 4695 | `language` | `rewrite` | Expansion Task — Develop Supporting Detail | Asks the learner to expand each bare sentence into 2–3 sentences adding a policy reference, reasoning, and a benefit statement. Text-expansion/rewrite production task. |
| 5671 | `language` | `notice` | Phrase Bank Building — Build Reusable Language | Provides twelve phrases and asks the learner to sort them into a personal phrase bank under four headings (introducing themes, agreement, contrast, conclusions). Same classification/sorting pattern as lines 1413 and 3629. |
| 6039 | `language` | `rewrite` | Add a Purpose Statement | Asks the learner to add a sentence explaining purpose or likely impact to each of four given policy-change statements. Sentence-addition/rewrite task on given text. |
| 6410 | `language` | `rewrite` | Add a Benefit Statement | Asks the learner to add a sentence describing the expected benefit to each of four given policy statements. Sentence-addition/rewrite task on given text — same pattern as line 6039. |
| 6766 | `language` | `write` | Write the Opening Sentence | Asks the learner to write an appropriate opening sentence for each of four described situations. The learner produces original text from scratch given a scenario description — this is `write`, not a language input or transformation of existing text. |
| 6831 | `language` | `rewrite` | Clarify the Action | Asks the learner to rewrite each vague item as a specific, clearly documented action taken. Sentence-rewrite task on given text. |
| 6865 | `language` | `rewrite` | Add a Next-Step Statement | Asks the learner to rewrite each item to include a clear, time-bound next step. Sentence-rewrite/expansion task on given text. |

---

## 2. Summary Table

| Current class | Correctly classified | Misclassified | Total |
|---|---|---|---|
| `learn` | 113 | 1 | 114 |
| `language` | 33 | 21 | 54 |
| `notice` | 77 | 2 | 79 |
| `write` | 89 | 0 | 89 |
| `rewrite` | 56 | 1 | 57 |
| `edit` | 75 | 0 | 75 |
| `example` | 127 | 0 | 127 |
| `structure` | 0 | — | 0 |
| `revise` | 0 | — | 0 |
| **Total** | **570** | **25** | **595** |

*Note: Counts exclude nested divs that are label-only markers (e.g., `learn` divs used solely as section labels with no prose content). The total of 595 div openings matches the file grep count.*

---

## 3. Notes

### The `language` class is being used for four distinct purposes — only one is correct

The most significant systematic issue is that `language` is applied to four types of content that require different classes:

1. **Teaching input about language patterns** — reference panels of connectors, patterns, or structures with no task attached. These should be `learn`. Affected lines: 138, 163, 180, 207, 213, 810.

2. **Sentence-transformation or sentence-completion tasks** — the learner transforms, completes, or rewrites given sentences. These should be `rewrite`. Affected lines: 194, 828, 2655, 4695, 6039, 6410, 6831, 6865.

3. **Phrase-bank sorting tasks** — the learner sorts a given list of phrases into categories. These should be `notice` (no original text is produced; the learner classifies given material). Affected lines: 1413, 3629, 5671.

4. **Original sentence writing** — the learner produces original sentences from scratch given a scenario description. This should be `write`. Affected line: 6766.

The `language` class should be reserved for divs where the primary content is the language system itself — a phrase bank presented *for reference*, a grammar explanation, a vocabulary list — not for production tasks.

### The `Add a ... Statement` task type is consistently misclassified

Three divs use a parallel task structure — "Add a [X] statement" — where the learner reads four given sentences and adds one sentence to each. All three (lines 2655 expansion, 6039, 6410) are classified as `language`. Because the learner produces new text by transforming or extending existing text, these are `rewrite` tasks.

### `language` used as an explanatory wrapper for rewrite tasks

In Unit 17 (line 5314) and Unit 18 (line 5625), outer `language` divs titled "Sentence Rewriting — [topic]" wrap both teaching prose and a nested `rewrite` task. These outer divs are borderline: they deliver language input (nested `learn` + `language` panels) but their primary activity is the rewrite task. These were not flagged as definitive misclassifications because the outer div genuinely contains substantial language-input material; however, the section title "Sentence Rewriting" points to `rewrite` as the intended function.

### Two `notice` divs are teaching panels, not observation tasks

Line 500 ("3. Audience-Appropriate Tone") and line 756 ("1. Cohesive Devices") are positioned in the Language Focus sections and contain reference tables plus explanatory prose. Neither div assigns the learner an observation, analysis, or comparison task. They should be `learn` because the learner reads them as teaching input.

### The `rewrite` misclassification at line 472 is a structural labelling error

The outer div at line 472 ("2. Neutral Clarification Language") is a titled section that introduces a language category, explains its purpose, and contains a nested `language` div with example phrases. No rewrite task appears inside it. The actual rewrite task is a separate sibling div at line 489. The outer div at 472 is teaching input and should be `learn`.

### No misclassifications found in `write`, `edit`, `example`, `revise`, or `structure`

All `write` divs ask learners to produce original text. All `edit` divs ask learners to identify errors, apply checklists, or do proofreading. All `example` divs present reference or model text. No `revise` or `structure` divs appear in this file.
