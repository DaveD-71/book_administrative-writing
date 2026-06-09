# Phase 5 Example Div `No Title` Candidate Audit

Date: 2026-06-09

## Scope

This audit checks `example`, `example-good`, and `example-bad` divs in:

- `int/md/working/aw-int-all_0519.md`

The goal is to identify example div titles that are redundant and can be safely replaced with:

```md
No Title
```

so the example formatting remains in the DOCX/PDF output while the visible example title is suppressed by the updated `textmaker` postprocessor.

## Decision Rule

A title is treated as a safe `No Title` candidate when all of the following are true:

1. the example is a single standalone model, weak draft, original text, or reminder block rather than one member of a visible comparison pair
2. the surrounding instruction already tells the reader what the text is or what to do with it
3. the later task wording does not depend on the visible title to distinguish it from another nearby example

## Not Included

The following title families are not included in this list because they still serve a visible comparison or identification function:

- paired neutral comparison labels such as `Version A / Version B`, `Paragraph A / Paragraph B`, `Email A / Email B`, `Question A / Question B`, `Update A / Update B`, `Request A / Request B`, `Notice A / Notice B`, `Summary A / Summary B`, `Sentence A / Sentence B`, and `Message A / Message B`
- the Unit 1 paired labels `Weak` / `Stronger`, which are not redundant in the current local presentation even though they may be pedagogically debatable in a separate review

## Safe `No Title` Candidates

| Line | Class | Unit / Section | Current title | Why `No Title` is safe |
|---:|---|---|---|---|
| 505 | `example-bad` | Unit 2 `D. Guided Practice` | `Original Email` | The lead-in already says `Read the email below. Why is it weak?` and the rewrite task immediately follows. |
| 685 | `example-good` | Unit 3 `C. Language` | `Example of Paragraph Structure` | The surrounding structure explanation already defines the function of the paragraph. |
| 722 | `example` | Unit 3 `C. Language` | `Review Summary Example` | The preceding teaching note already introduces this as a review-summary model. |
| 797 | `example-bad` | Unit 3 `F. Editing Practice` | `Original` | The editing instruction directly below already tells the reader to repair the paragraph. |
| 896 | `example-bad` | Module 1 Review `Revision Lab` | `Weak Draft` | The following task explicitly says `Read the weak draft`, so the visible title is redundant. |
| 1270 | `example-bad` | Unit 4 `F. Editing Practice` | `Original Email` | The lead-in already says `Read the email below. Rewrite it...`. |
| 1792 | `example-good` | Unit 6 `C. Language` | `Example Paragraph (Part of a Report or Update)` | The surrounding bullets already explain the paragraph order and function. |
| 2285 | `example-bad` | Module 2 Review `Revision Lab` | `Weak Email` | The next task title and instruction already identify it as the weak email to improve. |
| 2435 | `example-good` | Unit 8 `B. Example Check` | `Procedure Example` | The procedure content is self-identifying and the section shell already frames it as the model. |
| 2585 | `example-bad` | Unit 8 `F. Editing Practice` | `Original Procedure` | The instruction above already says `Rewrite the procedure...`. |
| 2719 | `example-good` | Unit 9 `C. Language` | `Example Notice` | The notice text itself begins with a visible heading and the next task uses the notice structurally, not by title. |
| 2843 | `example-bad` | Unit 9 `F. Editing Practice` | `Original` | The rewrite task below already identifies it as the weak notice to strengthen. |
| 3110 | `example-bad` | Unit 10 `F. Editing Practice` | `Original` | The repair task below already defines the text as the explanation to reorganise. |
| 3214 | `example` | Unit 11 `B. Example Check` | `Meeting Summary Example` | The content heading `Meeting Summary - ...` already identifies the text. |
| 3337 | `example-bad` | Unit 11 `F. Editing Practice` | `Original Summary` | The instruction above already tells the learner to rewrite the summary. |
| 3434 | `example-bad` | Module 3 Review `Revision Lab` | `Weak Notice` | The following task title already says `Improve the Internal Notice`, making the visible title unnecessary. |
| 3591 | `example` | Unit 12 `B. Example Check` | `Inquiry Email Example` | The email content is self-identifying and the surrounding explanation already frames it. |
| 3721 | `example-bad` | Unit 12 `F. Editing Practice` | `Original` | The edit task directly below already defines the text as the inquiry to repair. |
| 3962 | `example-bad` | Unit 13 `F. Editing Practice` | `Original` | The task below already identifies it as the explanation to revise. |
| 4070 | `example-good` | Unit 14 `B. Example Check` | `Clarification Response Example` | The model response is self-contained and the `Why This Works` note already anchors its role. |
| 4198 | `example-bad` | Unit 14 `F. Editing Practice` | `Original Response` | The instruction above already says `Rewrite the response...`. |
| 4364 | `example-bad` | Unit 15 `C. Language` | `Original` | The adjacent rewrite task `Reformat the Email` already defines the function of the example. |
| 4392 | `example-bad` | Unit 15 `D. Guided Practice` | `Original Draft Email` | The lead-in already tells the learner to rewrite the draft email into a consistent style. |
| 4541 | `example-bad` | Module 4 Review `Revision Lab` | `Weak Response` | The revision task below already tells the learner to rewrite the weak response. |
| 4840 | `example-bad` | Unit 16 `D. Guided Practice` | `Original Email` | The lead-in already tells the learner to rewrite the corrected professional version. |
| 4907 | `example-bad` | Unit 16 `F. Editing Practice` | `Original` | The next div title `Edit a Paragraph` already gives the functional cue. |
| 5137 | `example-bad` | Unit 17 `D. Guided Practice` | `Original Paragraph` | The instruction above already says to rewrite the paragraph in clear sentences. |
| 5186 | `example-bad` | Unit 17 `F. Editing Practice` | `Original Draft` | The instruction above already says `Rewrite the draft...`. |
| 5205 | `example-bad` | Unit 17 `F. Editing Practice` | `Original Paragraph` | The lead-in already identifies it as the paragraph to revise. |
| 5458 | `example-bad` | Unit 18 `D. Guided Practice` | `Original Email` | The instruction above already frames it as the draft email to make more professional. |
| 5509 | `example-bad` | Unit 18 `F. Editing Practice` | `Original Draft` | The prompt above already identifies it as the draft to revise. |
| 5528 | `example-bad` | Unit 18 `F. Editing Practice` | `Original Paragraph` | The tone-revision instruction already defines the paragraph’s role. |
| 5629 | `example-bad` | Module 5 Review `Revision Lab` | `Weak Draft` | The next instruction already says `Revise the weak draft in three passes`. |
| 5891 | `example` | Unit 19 `D. Guided Practice` | `Reader-purpose reminder:` | The bullet content itself functions as the reminder; the visible title only repeats that role. |
| 6454 | `example-bad` | Unit 21 `D. Guided Practice` | `Original Draft` | The surrounding bullets and `Revised Email` task already establish the transformation clearly. |
| 7276 | `example-bad` | Module 6 Review `Revision Lab` | `Single Weak Response` | The next task already says `Rebuild the weak response as a stronger set`. |

## Count

- Safe `No Title` candidates found: **36**

## Implementation Note

These candidates can be changed in source by replacing the visible example title line with:

```md
No Title
```

The updated `textmaker` postprocessor will remove that label paragraph from output while preserving the example block styling.
