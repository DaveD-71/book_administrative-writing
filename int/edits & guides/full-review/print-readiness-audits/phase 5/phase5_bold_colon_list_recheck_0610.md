# Phase 5 Bold-Colon List Recheck

Date: 2026-06-10

## Trigger

Dave reported that the PDF still shows list patterns with bold items ending in colons. This recheck verifies whether the Phase 5 language-list review fully addressed those patterns.

## Finding

Phase 5 did **not** fully close this issue.

The earlier file:

- `phase5_language_list_format_inventory_0609.md`

correctly identified the language-bank formatting policy problem, but its stated scope excluded:

- general structural lists
- non-language support lists

As a result, several bold-colon list patterns remain in the live manuscript even after the language-list standardization pass.

## Confirmed Remaining Cases

### A. Structural slot lists with bold labels ending in colons

These are the clearest unresolved cases because the list items themselves are just bold labels with trailing colons.

| Line | Unit / Section | Source text |
|---:|---|---|
| 1234 | Unit 4 `D. Guided Practice` | `1. **Subject line:**` |
| 1235 | Unit 4 `D. Guided Practice` | `2. **Greeting:**` |
| 1236 | Unit 4 `D. Guided Practice` | `3. **Opening sentence:**` |
| 1237 | Unit 4 `D. Guided Practice` | `4. **Body (2-3 sentences):**` |
| 1238 | Unit 4 `D. Guided Practice` | `5. **Closing sentence:**` |
| 1239 | Unit 4 `D. Guided Practice` | `6. **Sign-off:**` |
| 2807 | Unit 9 `E. Freer Practice` | `- **Heading:**` |
| 2808 | Unit 9 `E. Freer Practice` | `- **Background:**` |
| 2809 | Unit 9 `E. Freer Practice` | `- **Essential information:**` |
| 2810 | Unit 9 `E. Freer Practice` | `- **Next step:**` |

### B. Bold label-plus-explanation list items

These are related, but slightly different. The bold item label ends in a colon and is immediately followed by explanatory text on the same line.

| Line | Unit / Section | Source text |
|---:|---|---|
| 781 | Unit 3 `D. Guided Practice` | `1. **Review delay:** ...` |
| 783 | Unit 3 `D. Guided Practice` | `2. **System problem:** ...` |
| 785 | Unit 3 `D. Guided Practice` | `3. **Rule change:** ...` |
| 1786 | Unit 6 `C. Language` | `1. **Topic:** What is delayed or changed` |
| 1787 | Unit 6 `C. Language` | `2. **Reason:** Why (optional)` |
| 1788 | Unit 6 `C. Language` | `3. **Effect:** What this means for the reader` |
| 1789 | Unit 6 `C. Language` | `4. **Next step / What will happen later:** Neutral, not a request` |

## Interpretation

The manuscript no longer appears to contain standalone **bold subgroup heading lines** that end in colons. That part of the issue seems to have been cleaned up.

What remains is a different but related problem:

1. list items that use **bold label + colon** as the whole item
2. list items that use **bold label + colon + inline explanation**

These were not fully covered by the Phase 5 language-list inventory because they fall outside its narrower phrase-bank scope.

## Suggested Next Step

Review the remaining cases in two passes:

1. structural slot lists
   - likely revise to bold labels **without** colons for consistency
2. bold label-plus-explanation lists
   - decide whether they should become:
     - bold labels without colons plus normal continuation text, or
     - plain sentence-style list items without the bold label treatment

This should be treated as a Phase 5 follow-up style cleanup rather than as a new structural-phase issue.

## Follow-Up Decision And Action

- Dave confirmed that the bold label-plus-explanation items in Category B should remain as they are.
- The manuscript was corrected for Category A only.

Applied source cleanup:

- Unit 4 `D. Guided Practice`
  - `**Subject line:**` -> `**Subject line**`
  - `**Greeting:**` -> `**Greeting**`
  - `**Opening sentence:**` -> `**Opening sentence**`
  - `**Body (2-3 sentences):**` -> `**Body (2-3 sentences)**`
  - `**Closing sentence:**` -> `**Closing sentence**`
  - `**Sign-off:**` -> `**Sign-off**`
- Unit 9 `E. Freer Practice`
  - `**Heading:**` -> `**Heading**`
  - `**Background:**` -> `**Background**`
  - `**Essential information:**` -> `**Essential information**`
  - `**Next step:**` -> `**Next step**`

Retained intentionally:

- Unit 3 and Unit 6 bold label-plus-explanation list items such as `**Review delay:** ...` and `**Topic:** ...`
