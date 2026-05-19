# Intermediate Missing Placeholder Audit

Date: 2026-05-19

Source: `int/md/working/aw-int-all.md`

Revision note: this audit supersedes the earlier div-block-local scan. Placeholder matching is now structural-section based because many Intermediate activities place instruction and example divs above a single response placeholder near the bottom of the same `###` section.

Association rule: a placeholder counts as matching when it appears anywhere inside the same structural `###` section before the next `###` or higher heading. This includes placeholders below instructional/example material.

- Candidate structural sections without associated placeholders: 104
- High confidence: 37
- Medium confidence: 35
- Low confidence: 32

Confirmed cleared example: Unit 5 `E. Extended Writing Task - Clarification Summary Paragraph` has its response placeholder at the bottom of the same section, so it is not a missing-placeholder case.

## Candidate Sections

| Line | Confidence | Unit | Section | Div classes | Reason | Response cues |
|---|---|---|---|---|---|---|
| 173 | high | Unit 1 - Clear Sentence Structure | C. Language 2 - Avoiding Unnecessary Complexity | learn, rewrite | response cue/arrow in section; production div class present: rewrite | L211: Clear:; L214: Clear:; L217: Clear:; L220: Clear: |
| 456 | high | Unit 2 - Professional Tone Basics | C. Language 1 - Polite Request Phrases | language, rewrite | response cue/arrow in section; production div class present: rewrite | L482: ->; L485: ->; L488: ->; L491: -> |
| 494 | high | Unit 2 - Professional Tone Basics | C. Language 2 - Professional Tone in Explanations | learn, rewrite | response cue/arrow in section; production div class present: rewrite | L537: ->; L540: ->; L543: ->; L546: -> |
| 953 | high | Unit 3 - Paragraph Structure | C. Practice B - Reorder to Create a Clear Paragraph | write | response cue/arrow in section; production div class present: write | L984: ->; L985: -> |
| 1399 | high | Unit 4 - Email Layout and Standard Phrases | C. Language 1 - Subject Lines | language, rewrite | response cue/arrow in section; production div class present: rewrite | L1430: ->; L1433: ->; L1436: ->; L1439: -> |
| 1503 | high | Unit 4 - Email Layout and Standard Phrases | C. Language 3 - Opening Sentences (Purpose) | language, learn, write | response cue/arrow in section; production div class present: write | L1541: ->; L1544: ->; L1547: -> |
| 1791 | high | Unit 5 - Requesting Clarification | C. Practice A - Make These Questions Clearer | rewrite | response cue/arrow in section; production div class present: rewrite | L1810: ->; L1813: ->; L1816: ->; L1819: -> |
| 1860 | high | Unit 5 - Requesting Clarification | C. Practice B - Improve the Clarity | rewrite | response cue/arrow in section; production div class present: rewrite | L1868: ->; L1871: ->; L1874: ->; L1877: -> |
| 1909 | high | Unit 5 - Requesting Clarification | D. Extended Guided Practice - Rewrite and Improve | rewrite | response cue/arrow in section; production div class present: rewrite | L1917: ->; L1920: ->; L1923: ->; L1926: -> |
| 2207 | high | Unit 6 - Communicating Delays or Changes | C. Practice A - Improve the Clarity | rewrite | response cue/arrow in section; production div class present: rewrite | L2226: ->; L2229: ->; L2232: ->; L2235: -> |
| 2294 | high | Unit 6 - Communicating Delays or Changes | C. Practice C - Add Supporting Information | write | response cue/arrow in section; production div class present: write | L2302: ->; L2305: ->; L2308: -> |
| 2600 | high | Unit 7 - Making Requests Politely | C. Practice A - Rewrite the Request | rewrite | response cue/arrow in section; production div class present: rewrite | L2621: ->; L2624: ->; L2627: ->; L2630: -> |
| 2655 | high | Unit 7 - Making Requests Politely | C. Practice B - Make the Request More Specific | rewrite | response cue/arrow in section; production div class present: rewrite | L2674: ->; L2677: ->; L2680: ->; L2683: -> |
| 2725 | high | Unit 7 - Making Requests Politely | C. Practice C - Soften the Request | rewrite | response cue/arrow in section; production div class present: rewrite | L2733: ->; L2736: ->; L2739: ->; L2742: -> |
| 3318 | high | Unit 8 - Writing Simple Procedures | C. Practice A - Improve the Verb Choice | rewrite | response cue/arrow in section; production div class present: rewrite | L3326: ->; L3329: ->; L3332: ->; L3335: -> |
| 3349 | high | Unit 8 - Writing Simple Procedures | C. Practice B - Put the Steps in Order | write | response cue/arrow in section; production div class present: write | L3363: Write the correct order: |
| 3720 | high | Unit 9 - Internal Notices | C. Language 2 - Neutral Tone | learn, rewrite | response cue/arrow in section; production div class present: rewrite | L3739: ->; L3742: ->; L3745: ->; L3748: -> |
| 3751 | high | Unit 9 - Internal Notices | C. Practice B - Improve the Clarity | rewrite | response cue/arrow in section; production div class present: rewrite | L3772: ->; L3775: ->; L3778: ->; L3781: -> |
| 4132 | high | Unit 10 - Explaining Problems Clearly | C. Practice A - Improve the Explanation | rewrite | response cue/arrow in section; production div class present: rewrite | L4151: ->; L4154: ->; L4157: ->; L4160: -> |
| 4163 | high | Unit 10 - Explaining Problems Clearly | C. Practice B - Add Details | write | response cue/arrow in section; production div class present: write | L4183: ->; L4186: ->; L4189: -> |
| 4515 | high | Unit 11 - Writing Simple Meeting Summaries | C. Practice B - Improve the Clarity | rewrite | response cue/arrow in section; production div class present: rewrite | L4523: ->; L4526: ->; L4529: -> |
| 5152 | high | Unit 12 - Writing Simple External Inquiries | C. Practice A - Improve the Inquiry | rewrite | response cue/arrow in section; production div class present: rewrite | L5174: ->; L5177: ->; L5180: ->; L5183: -> |
| 5186 | high | Unit 12 - Writing Simple External Inquiries | C. Practice B - Add Background Information | write | response cue/arrow in section; production div class present: write | L5207: ->; L5210: ->; L5213: -> |
| 5523 | high | Unit 13 - Providing Simple Explanations | C. Practice A - Improve the Explanation | rewrite | response cue/arrow in section; production div class present: rewrite | L5545: ->; L5548: ->; L5551: ->; L5554: -> |
| 5557 | high | Unit 13 - Providing Simple Explanations | C. Practice B - Add a Reason or Background | write | response cue/arrow in section; production div class present: write | L5577: ->; L5580: ->; L5583: -> |
| 5886 | high | Unit 14 - Responding to Confusion | C. Practice A - Improve the Response | rewrite | response cue/arrow in section; production div class present: rewrite | L5907: ->; L5910: ->; L5913: ->; L5916: -> |
| 5919 | high | Unit 14 - Responding to Confusion | C. Practice B - Add Clarifying Information | write | response cue/arrow in section; production div class present: write | L5927: ->; L5930: ->; L5933: -> |
| 6248 | high | Unit 15 - Maintaining Consistent Email Style | C. Practice A - Improve Consistency | rewrite | response cue/arrow in section; production div class present: rewrite | L6256: ->; L6259: ->; L6262: -> |
| 6300 | high | Unit 15 - Maintaining Consistent Email Style | C. Practice B - Reformat the Email | rewrite | response cue/arrow in section; production div class present: rewrite | L6331: Rewrite here: |
| 6911 | high | Unit 16 - Editing for Accuracy | C. Practice A - Correct the Sentences | edit | response cue/arrow in section; production div class present: edit | L6931: ->; L6934: ->; L6937: ->; L6940: -> |
| 7222 | high | Unit 17 - Editing for Clarity | C. Practice A - Make the Sentences Clearer | rewrite | response cue/arrow in section; production div class present: rewrite | L7230: ->; L7233: ->; L7236: ->; L7239: -> |
| 7553 | high | Unit 18 - Editing for Tone | C. Practice A - Make the Tone Polite | rewrite | response cue/arrow in section; production div class present: rewrite | L7575: ->; L7578: ->; L7581: ->; L7584: -> |
| 7624 | high | Unit 18 - Editing for Tone | C. Practice B - Improve the Email Tone | rewrite | response cue/arrow in section; production div class present: rewrite | L7636: Rewrite:; L7643: Rewrite: |
| 8098 | high | Unit 19 - Integrated Task 1: Combined Email + Internal Explanation | C. Practice A - Rewrite for Audience & Tone | rewrite | response cue/arrow in section; production div class present: rewrite | L8108: ->; L8113: ->; L8118: ->; L8123: -> |
| 8485 | high | Unit 20 - Integrated Task 2: Revision + Notice Writing | C. Practice A - Rewrite for Audience & Tone | rewrite | response cue/arrow in section; production div class present: rewrite | L8495: ->; L8500: ->; L8505: ->; L8510: -> |
| 8875 | high | Unit 21 - Writing for Consistency Across a Team | C. Practice A - Improve Team Consistency | rewrite | response cue/arrow in section; production div class present: rewrite | L8883: ->; L8886: ->; L8889: -> |
| 9226 | high | Unit 22 - Multi-Document Communication Task | C. Practice A - Match Tone to Audience | rewrite | response cue/arrow in section; production div class present: rewrite | L9234: ->; L9237: ->; L9240: ->; L9243: -> |
| 111 | medium | Unit 1 - Clear Sentence Structure | C. Language 1 - Basic Sentence Pattern (SVO / SVC) | language, notice, write | production div class present: write |  |
| 1160 | medium | Unit 3 - Paragraph Structure | Module 1 transfer task | write | production div class present: write |  |
| 1194 | medium | Unit 3 - Paragraph Structure | Module 1 revision lab | example-good, revise | production div class present: revise |  |
| 1231 | medium | Unit 3 - Paragraph Structure | Module 1 preparation for Module 2 | edit | production div class present: edit |  |
| 1452 | medium | Unit 4 - Email Layout and Standard Phrases | C. Language 2 - Openings and Closings | language, write | production div class present: write |  |
| 1880 | medium | Unit 5 - Requesting Clarification | C. Practice C - Clarification from Context | write | production div class present: write |  |
| 2274 | medium | Unit 6 - Communicating Delays or Changes | C. Practice B - Reorder to Make a Clear Update | write | production div class present: write |  |
| 2971 | medium | Unit 7 - Making Requests Politely | Module 2 transfer task | write | production div class present: write |  |
| 3056 | medium | Unit 7 - Making Requests Politely | Module 2 revision lab | write | production div class present: write |  |
| 3370 | medium | Unit 8 - Writing Simple Procedures | C. Practice C - Add Missing Steps | write | production div class present: write |  |
| 4757 | medium | Unit 11 - Writing Simple Meeting Summaries | Module 3 transfer task | write | production div class present: write |  |
| 4817 | medium | Unit 11 - Writing Simple Meeting Summaries | Module 3 revision lab | write | production div class present: write |  |
| 4866 | medium | Unit 11 - Writing Simple Meeting Summaries | Module 3 sequencing rebuild lab | revise | production div class present: revise |  |
| 4888 | medium | Unit 11 - Writing Simple Meeting Summaries | Module 3 internal-document rebuild workshop | revise | production div class present: revise |  |
| 6534 | medium | Unit 15 - Maintaining Consistent Email Style | Module 4 transfer task | write | production div class present: write |  |
| 6597 | medium | Unit 15 - Maintaining Consistent Email Style | Module 4 revision lab | write | production div class present: write |  |
| 6644 | medium | Unit 15 - Maintaining Consistent Email Style | Module 4 external communication rebuild lab | revise | production div class present: revise |  |
| 6674 | medium | Unit 15 - Maintaining Consistent Email Style | Module 4 outward-facing rebuild workshop | revise | production div class present: revise |  |
| 6721 | medium | Unit 15 - Maintaining Consistent Email Style | Module 4 audience-shift practice set | write | production div class present: write |  |
| 6806 | medium | Unit 16 - Editing for Accuracy | A. Warm-Up: Spot the Errors | edit, learn | production div class present: edit |  |
| 6943 | medium | Unit 16 - Editing for Accuracy | C. Practice B - Edit for Accuracy | edit | production div class present: edit |  |
| 7262 | medium | Unit 17 - Editing for Clarity | C. Practice B - Reorganise for Better Flow | rewrite | production div class present: rewrite |  |
| 7835 | medium | Unit 18 - Editing for Tone | Module 5 transfer task | revise | production div class present: revise |  |
| 7872 | medium | Unit 18 - Editing for Tone | Module 5 revision clinic | edit | production div class present: edit |  |
| 7902 | medium | Unit 18 - Editing for Tone | Module 5 carry-forward task | write | production div class present: write |  |
| 7940 | medium | Unit 18 - Editing for Tone | Module 5 editing memo for later modules | write | production div class present: write |  |
| 8892 | medium | Unit 21 - Writing for Consistency Across a Team | C. Practice B - Standardise Format & Tone | rewrite | production div class present: rewrite |  |
| 9654 | medium | Unit 23 - Portfolio Writing & Final Revision | C. Practice A - Edit a Draft Email | revise | production div class present: revise |  |
| 9667 | medium | Unit 23 - Portfolio Writing & Final Revision | C. Practice B - Edit a Paragraph | revise | production div class present: revise |  |
| 9694 | medium | Unit 23 - Portfolio Writing & Final Revision | C. Practice C - Edit a Notice or Short Message | revise | production div class present: revise |  |
| 10014 | medium | Unit 23 - Portfolio Writing & Final Revision | Module 6 rebuild lab | revise | production div class present: revise |  |
| 10036 | medium | Unit 23 - Portfolio Writing & Final Revision | Module 6 transfer task | write | production div class present: write |  |
| 10077 | medium | Unit 23 - Portfolio Writing & Final Revision | Module 6 integrated revision lab | rewrite | production div class present: rewrite |  |
| 10114 | medium | Unit 23 - Portfolio Writing & Final Revision | Module 6 final course transfer task | write | production div class present: write |  |
| 10190 | medium | Unit 23 - Portfolio Writing & Final Revision | Module 6 multi-document rebuild workshop | revise | production div class present: revise |  |
| 248 | low | Unit 1 - Clear Sentence Structure | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 355 | low | Unit 1 - Clear Sentence Structure | F. Reflection | edit, write | production div class present: edit, write |  |
| 611 | low | Unit 2 - Professional Tone Basics | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 704 | low | Unit 2 - Professional Tone Basics | F. Reflection | edit | production div class present: edit |  |
| 1006 | low | Unit 3 - Paragraph Structure | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 1080 | low | Unit 3 - Paragraph Structure | F. Reflection | edit | production div class present: edit |  |
| 1146 | low | Unit 3 - Paragraph Structure | Module 1 self-edit routine | edit | production div class present: edit |  |
| 1579 | low | Unit 4 - Email Layout and Standard Phrases | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 1958 | low | Unit 5 - Requesting Clarification | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 2340 | low | Unit 6 - Communicating Delays or Changes | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 2776 | low | Unit 7 - Making Requests Politely | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 2956 | low | Unit 7 - Making Requests Politely | Module 2 email control checklist | edit | production div class present: edit |  |
| 3419 | low | Unit 8 - Writing Simple Procedures | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 3809 | low | Unit 9 - Internal Notices | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 4221 | low | Unit 10 - Explaining Problems Clearly | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 4549 | low | Unit 11 - Writing Simple Meeting Summaries | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 4743 | low | Unit 11 - Writing Simple Meeting Summaries | Module 3 self-edit routine | edit | production div class present: edit |  |
| 5233 | low | Unit 12 - Writing Simple External Inquiries | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 5615 | low | Unit 13 - Providing Simple Explanations | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 5961 | low | Unit 14 - Responding to Confusion | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 6355 | low | Unit 15 - Maintaining Consistent Email Style | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 6520 | low | Unit 15 - Maintaining Consistent Email Style | Module 4 communication checklist | edit | production div class present: edit |  |
| 6983 | low | Unit 16 - Editing for Accuracy | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 7312 | low | Unit 17 - Editing for Clarity | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 7667 | low | Unit 18 - Editing for Tone | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 7822 | low | Unit 18 - Editing for Tone | Module 5 editing routine | edit | production div class present: edit |  |
| 8195 | low | Unit 19 - Integrated Task 1: Combined Email + Internal Explanation | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 8567 | low | Unit 20 - Integrated Task 2: Revision + Notice Writing | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 8952 | low | Unit 21 - Writing for Consistency Across a Team | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 9338 | low | Unit 22 - Multi-Document Communication Task | F. Self-Check Before Freer Practice | edit | production div class present: edit |  |
| 9720 | low | Unit 23 - Portfolio Writing & Final Revision | F. Self-Check Before Final Submission | edit | production div class present: edit |  |
| 9864 | low | Unit 23 - Portfolio Writing & Final Revision | G. Capstone Rebuild Routine | revise | production div class present: revise |  |
