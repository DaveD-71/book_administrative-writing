# Phase 3 Recommendations - Remaining Module 2 Content

Date: 2026-06-03

Source reviewed: `int/md/working/aw-int-all_0519.md`

Scope: Unit 7 and Module 2 Review Workshop. Units 4-6 have already been repaired or reviewed separately.

## Summary

Unit 7 still follows the older duplicated-tail pattern and needs a full Phase 3 repair before Module 2 can be considered consistent with the Module 1 standard. The larger problem is not only the heading order. The unit repeats the same request-writing criteria in many forms: polite structure, specific detail, reason/context, and low pressure. These points are useful, but the current sequence presents them as several disconnected lists and repeated mini-checklists rather than as a clear progression from noticing, to language choice, to sentence-level practice, to email production.

The Module 2 Review Workshop is closer to the current review-workshop pattern, but it still contains some poorly placed commentary and checklist-heavy instructions that can be tightened.

## Deeper Editorial Findings

1. The unit goal is clear, but the activity path is not.
   - Focus statements identify four skills: choose a polite structure, add detail, soften without losing clarity, and write a short request email.
   - The activities repeat these same four skills several times instead of moving cleanly through them.
   - Repair target: make `C. Language` the controlled sentence-level practice area, `D` the supported email, `E` freer email production, `F` editing, `G` final check/reflection, and `H` transfer.

2. A/B/C repeat the same criteria too often.
   - `A. Warm-Up` ends with a four-item "Quick Rule for Polite Requests."
   - `B. Example Check` repeats the same explanation: cooperative tone, exact need, reason.
   - `C. Language` repeats it again in `Key Notes`, `Adding Context`, `Rewrite the Request`, `Requests with Specific Details`, `Avoiding Pressure`, and `Why This Works`.
   - Repair target: keep one short rule after the warm-up or example, then let C teach the three request controls in sequence: polite form, specific detail, reason/pressure control.

3. Several lists are explanation-only clutter.
   - Lists at `Quick Rule`, `Key Notes`, `Make each request stronger by adding`, `Mini request frame`, `A good request includes`, `Specific requests are easier...`, `Administrative English avoids`, and `Good request writing balances` mostly restate the same information.
   - Repair target: convert most of these to short prose and keep only the table, the exercise items, and a compact phrase bank where the learner needs options.

4. The C section currently has three mini-practice sets plus three extra general response boxes.
   - The item-level placeholders already give students response space for all 12 rewrite items.
   - The separate `U07-practice-a-request`, `U07-practice-b-specific`, and `U07-practice-c-soften` boxes are not connected to a clearly different output.
   - Repair target: remove those extra boxes, or redesign them as one final short request-email mini task if a synthesis step is genuinely needed.

5. The source-text/action/output order is inconsistent.
   - Some tasks give a rule, then a second rule, then a frame, then the items.
   - Some tasks use labels like `Mini contrast` and `Examples` where a direct instruction would be clearer.
   - Repair target: for each task, use source first where needed, then action, then output requirement, then response space.

6. The unit uses "request" and "email" interchangeably too early.
   - C is sentence-level request rewriting, while D/E/H are email production.
   - The current wording sometimes asks for a "request email" before students have practiced the email-level structure in the unit.
   - Repair target: explicitly distinguish "request sentence" or "request line" in C from "request email" in D/E/H.

## Unit 7 - Required Edits

1. Normalize the visible activity shell.
   - Current sequence includes `A B C D F E G H E F H`.
   - Repair to the standard sequence: `A. Warm-Up`, `B. Example Check`, `C. Language`, `D. Guided Practice`, `E. Freer Practice`, `F. Editing Practice`, `G. Self-Check and Reflection`, `H. Transfer and Homework`.
   - Merge or remove the later `E. Extended Writing Task`, `F. Reflection`, and `H. Homework` sections by function.

2. Remove generic response labels and floating placeholders.
   - Labels such as `Write Here`, `Use this box for one complete version`, `Write Your Revised Version`, `Write Your Paragraph`, and `Homework Draft` remain.
   - Move all placeholders inside the relevant semantic divs.
   - Replace generic labels with task-specific labels only where separate outputs are genuinely needed.

3. Repair the `C. Language` section.
   - The politeness-scale table has blank lines between every table row, which caused raw pipe-table rendering in the earlier Module 2 PDF review.
   - The `Key Notes` first bullet has broken bold markup: `**\`Can you...?\` is grammatically correct but **not appropriate**`.
   - Several support blocks repeat the same request criteria: polite form, specific detail, reason/context, and reduced pressure. Consolidate these into a clearer language sequence.
   - Remove the extra full-practice placeholder boxes after the item-level rewrite tasks unless the task explicitly asks students to combine the item rewrites into one final version.
   - Rebuild C around three controlled practice moves:
     1. choose or apply a polite request form;
     2. make the request specific enough to answer;
     3. soften urgency or pressure without making the action unclear.
   - Convert explanation-only lists into short prose unless the list gives phrase options or numbered exercise items.

4. Improve task information order in `C. Language`.
   - The rewrite tasks should move source text, action, output requirement, and response space into a predictable order.
   - The "Mini request frame" list is another checklist of the same criteria already stated above it; either remove it or turn it into one short reminder sentence.

5. Repair `D. Guided Practice`.
   - Keep the response placeholder inside the `write` div.
   - Remove `Write your email:`, `Use this box for one complete version`, and `Write Here` style repetition.
   - The task can retain the email-component scaffold, but the instruction should state the situation first, then the required email output.
   - Consider changing the scaffold from a list of seven email parts into a compact prompt paragraph plus a short email-frame table only if the list remains visually heavy after rendering.

6. Move self-check after editing/practice.
   - The current `F. Self-Check Before Freer Practice` appears before `E. Freer Practice`.
   - If it is only a pre-writing checklist, merge it into `E` as a brief planning check.
   - Otherwise convert it to `G. Self-Check and Reflection` after `F. Editing Practice`.

7. Repair `E. Freer Practice`.
   - Keep the two email placeholders inside the `write` div.
   - Check whether `rows=10` is still necessary for each 3-4 sentence email; it may be large, but visual output should decide.
   - Remove the repeated `Write your emails:` line if the output requirement is already clear.
   - The options are long because each includes the full reason. Keep the reason, but consider presenting each option as `request purpose + reason` in one compact sentence or table if the rendered page feels dense.
   - The `In each email, include:` checklist repeats the Focus/C criteria. It can become one concise sentence: `In each email, include a clear opening, one polite request, a short reason, and a softened closing.`

8. Repair `F. Editing Practice`.
   - Current `G. Editing Practice` should become visible `F`.
   - It asks students to rewrite four separate requests and then also write a "full corrected version" box. The full-version box appears redundant because the task is sentence-level.
   - Remove the final full-version placeholder unless the task is redesigned as a short email revision.

9. Repair `H. Transfer and Homework`.
   - Merge the current `H. Transfer Extension` and `H. Homework` because they ask nearly the same thing: rewrite one request using two polite structures.
   - Decide whether the neutral report paragraph from `E. Extended Writing Task` belongs in Unit 7. It shifts away from request emails into report background; if retained, it should be clearly framed as transfer, not a second E section.
   - Add or retain a short reflection task only if it supports transfer and has a real response space or clear self-check purpose.
   - Recommended repair: keep one H task that asks students to choose one real or practice request and write two versions for different politeness levels. Add two brief notes about which version fits which reader. Remove the separate homework task unless it adds a genuinely different home output.
   - The report paragraph task should probably be removed from Unit 7. It teaches background explanation rather than making requests politely and overlaps more naturally with later explanation/report units.

10. Update the answer key for Unit 7 in the same edit cycle.
    - The current answer key has useful C/D/G model material but does not match the repaired visible shell.
    - Add or revise guidance for `E. Freer Practice`, `F. Editing Practice`, `G. Self-Check and Reflection`, and `H. Transfer and Homework` after the student-book edits.
    - Remove stale references to any deleted extended-writing, full-version, or homework labels.

## Module 2 Review Workshop - Required Edits

1. Reduce the opening takeaways if the page feels list-heavy.
   - The four `Core Takeaways` bullets are useful, but they repeat unit goals. They can remain if visually acceptable, but a short prose paragraph may work better after the Unit 4 cleanup standard.

2. Move explanatory commentary out of the `example-good` block in `Revision Lab`.
   - The possible stronger version includes an explanatory paragraph beginning `This version is stronger because...`.
   - That commentary is not part of the model email and should be moved to a separate `learn`/teacher-facing note or removed from the student book if it repeats the task.

3. Tighten `Email Comparison Review`.
   - `Compare these two request openings` followed by a separate `Review Response` div is structurally acceptable, but the response prompt repeats `stronger` plus three criteria.
   - A clearer instruction would be: `Write 2-3 sentences explaining why Version B is easier for the reader to act on. Mention tone, reason, and action.`

4. Tighten `Revision Lab`.
   - The weak email is useful, but the task prompt asks for topic, exact problem, action, subject, opening, and polite request all in one sentence.
   - Recommended wording: introduce the weak email, then ask students to rewrite it with a clearer subject line, a professional opening, the exact problem, and one polite request.

5. Reconsider the possible stronger version placement.
   - If the model appears immediately after the student response box, it is acceptable as feedback/modeling, but it may be better in the answer key if the review workshop needs more student work and less model text.
   - If retained in the student book, keep only the model email in the example div and move explanation outside the div or remove it.

6. Tighten `Self-Edit Routine`.
   - The checklist is useful, but it combines Unit 4, Unit 5, Unit 6, and Unit 7 checks in one long list.
   - Keep it if the workshop is meant as a module-wide diagnostic; otherwise reduce to four items: subject/opening, one clear question or request, delay/change current status and next step, and closing tone.

7. Check transfer placeholder sizes.
   - `M2-transfer-internal-email` and `M2-transfer-external-email` are both `rows=4`.
   - The task asks for two short emails, so the rows may be tight depending on visual output. Increase if the regenerated DOCX/PDF shows cramped writing space.

8. Reorganize `Transfer Task` instructions.
   - It currently has three stacked lists: situation options, audience outputs, and audience notes.
   - Convert some of this into prose: `Choose one workplace situation. Write one internal email and one external email about the same situation. Then add three short notes about what changed for the audience.`
   - Keep only the situation options as bullets if needed.

9. Consider making `Audience Notes` a clearer subtask label.
   - It currently appears as plain text inside the `write` div.
   - If kept, use a short explanatory sentence such as `After writing both emails, add three short notes about audience choices.`

10. Validate answer-key alignment after Unit 7 changes.
   - The Module 2 Review Workshop answer-key block already follows the current review-workshop pattern.
   - Recheck it after Unit 7 is repaired because the transfer task asks students to name which unit helped their decision, and Unit 7 wording may change.

## Priority

1. Repair Unit 7 first. It is the only remaining unrepaired ordinary unit in Module 2.
2. Then make the small Module 2 Review Workshop cleanup.
3. Update `int/md/working/aw-int-answer-key.md`.
4. Run focused audits: Unit 7 heading sequence, div balance, placeholders inside divs, placeholder IDs, generic-label scan, and answer-key alignment.
5. Regenerate DOCX/PDF and visually check the old Module 2 risk points, especially the Unit 7 politeness-scale table and page breaks around response spaces.
