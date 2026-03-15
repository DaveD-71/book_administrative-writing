# N11 QA Checklist

## *Administrative Writing, Advanced*

---

> **Purpose of this document**
> This file defines the `N11` book-wide quality assurance framework for the advanced book after completion of `N9` and `N10`.
>
> `N11` is not a prompt-repair pass, not a language-instruction pass, and not a structural redesign pass. It is the final hierarchical quality check that tests whether the completed `N10` book now meets the agreed project standards at unit, module, and whole-book level before the full review stage.
>
> **Version note (v2):** This version corrects gaps identified after cross-checking the Round 2 review against the checklist. Additions include: a preliminary cross-check step against known open issues (Section 4.0); an explicit H1 Extension Task compliance check (5G.1); N10 minimum deliverables as the concrete standard for 5C; an activity heading format check (5L.1); explicit word-count targets in 5I.2 and 5D.3; a requirement source for 5B.2; and a named entry in 5M.2 for the deferred learning goals mapping issues.

---

## 1. Scope Of N11

`N11` checks the completed advanced book against the agreed standards for:

- design for purpose and learning-goal alignment
- learner suitability
- language and learning
- prompt and task design
- consistency and cohesion
- model-text quality
- structural profile compliance
- activity-type fidelity
- progression across units and modules
- self-study accessibility
- answer-key supportability
- formatting and production readiness
- remaining pinned-item checks that are meant to be confirmed at QA stage

`N11` should identify:

- what already meets the standard
- what needs correction before full review
- what can remain as a later deferred item because it belongs to a post-content stage such as answer-key production

---

## 2. Source Hierarchy For N11

Use the following source order:

1. `adv/edits & guides/aw-adv_project_todo_list.md`
2. `adv/edits & guides/aw-adv_unit_structural_profiles_revised.md`
3. `aw-master_activity_menu.md`
4. `adv/edits & guides/aw-adv_prompt-writing-policy.md`
5. `adv/edits & guides/aw-adv_n10_language_instruction_framework.md`
6. active module files in `adv/md/n10/aw-adv_mod1_n10.md` to `aw-adv_mod6_n10.md`
7. relevant implementation or review guides in `adv/edits & guides`
8. earlier `N9` QA files only as narrow precedent, not as the final QA standard

If sources disagree, prefer the higher source in this list unless the project owner has made a later explicit decision.

---

## 3. Output Model For N11

Use three levels of QA structure:

### Level 1 — QA Category

The major review area, such as:

- Design for Purpose
- Learner Suitability
- Language and Learning
- Prompt and Task Design
- Consistency and Cohesion
- Model Text Quality

### Level 2 — Criterion

The specific aspect within the category, such as:

- unit-level goal alignment
- activity-type fidelity
- self-study accessibility
- prompt calibration

### Level 3 — Check Item

The concrete test that can be answered during review.

Use status values:

- `Pass`
- `Revise`
- `Monitor`
- `Deferred`

Use `Deferred` only for items explicitly scheduled for a later stage, such as `P4` answer-key production or `P7` rubric writing if they are not meant to block QA sign-off yet.

---

## 4. Review Workflow

### 4.0 Preliminary cross-check (before module review begins)

Before beginning the module-by-module pass, complete the following:

1. Read the current `N10` feedback reports (`aw-adv_n10_feedback_mod1-3_v2.md` and `aw-adv_n10_feedback_mod4-6_v2.md`) and list all findings that were identified but not yet actioned — including structural issues, content placement errors, missing activity codes, and word count inconsistencies.
2. Confirm the status of the H1 Extension Task structural decision for Units 2, 3, 4, 6, and 11. The structural profiles specify these units should not have H1; if the N10 files contain H1 Extension Tasks for these units, record as `Revise` pending the project owner's decision. Do not proceed past this point without a decision on record.
3. Note any other open decisions logged in the project to-do list that affect content currently under review.

These preliminary items must be recorded before module findings are captured. A `Revise` at this stage blocks sign-off regardless of module-level results.

### 4.1 Review order

Run `N11` in this sequence:

1. complete preliminary cross-check (Section 4.0)
2. confirm book-level source documents and standards
3. review module by module using the active `n10` files
4. capture unit-level findings
5. summarise module-level findings
6. consolidate book-level findings
7. determine whether the book is ready for full review

### 4.2 Review scale

`N11` is hierarchical:

- some checks are **unit-level**
- some checks are **module-level**
- some checks are **book-level**

Do not force every check down to the unit if it is really about the whole book.

### 4.3 Evidence rule

Every `Revise` judgment should state:

- the file and unit/module affected
- the failed criterion
- the specific reason it fails
- the minimum corrective action needed

### 4.4 Non-overwrite rule

`N11` should not silently reopen the planning architecture.

If the failure is:

- a local content issue, mark `Revise`
- a structural mismatch that suggests the planning source itself is wrong, mark `Monitor` and note that the issue is architectural

---

## 5. Level 1 Categories, Criteria, And Checks

## 5A. Design For Purpose

### 5A.1 Module-purpose alignment

- [ ] Each unit clearly supports the stated purpose of its module
- [ ] The module introduction in the structural profiles matches what the module file actually delivers
- [ ] The module’s set of units forms a coherent skill cluster rather than a loose topic grouping

### 5A.2 Unit-goal alignment

- [ ] The active unit content clearly supports the unit-level Can-Do statements
- [ ] The main writing outcome of the unit matches the stated learning goal
- [ ] The unit does not drift into a different dominant skill than the one named in the profiles

### 5A.3 Activity-goal alignment

- [ ] The activity sequence visibly develops the unit goals rather than merely repeating them
- [ ] Early activities introduce or frame the skill appropriately
- [ ] Later activities require learners to apply the intended skill independently
- [ ] The unit shows pedagogical progression rather than eight disconnected exercises

### 5A.4 Internal unit coherence

- [ ] The model text, Language Focus, guided writing, freer writing, and homework all target the same core skill family
- [ ] Examples, prompts, and editing tasks do not pull the learner away from the unit’s main purpose
- [ ] Section-to-section transitions feel intentional rather than stitched together

## 5B. Learner Suitability

### 5B.1 Level appropriacy

- [ ] Input texts are appropriate for B1+/B2 aspirational learners
- [ ] Required output is demanding but still supportable for the target learner
- [ ] Tasks do not assume expert content knowledge beyond what the scenario provides
- [ ] Prompt and instruction wording remain readable for B1+/B2 aspirational learners and do not create avoidable extra difficulty through dense phrasing, abstract framing, or unnecessarily long scenario wording

**Requirement sources:**

- `adv/edits & guides/aw-adv_project_context.md` — target learners are B1+/B2 workplace learners in an aspirational, scaffolded context
- `adv/edits & guides/aw-adv_project_context.md` — instructions should remain direct and professional
- `adv/edits & guides/aw-adv_prompt-writing-policy.md` — prompts must be calibrated, concrete, and parallel in length/detail

### 5B.2 Workplace relevance

- [ ] Scenarios reflect recognisable administrative and interagency workplace situations
- [ ] Documents asked for are plausible outputs in that professional world
- [ ] The professional stakes feel real enough to motivate adult learners

**Requirement sources:**

- `adv/edits & guides/aw-adv_project_context.md` — the book targets interagency and international administrative contexts; scenarios must be drawn from recognisable situations in those environments
- `adv/edits & guides/aw-adv_prompt-writing-policy.md` — prompts must be situation-anchored and professionally verisimilitudinous; the scenario is the vehicle, not the point

### 5B.3 Delivery-mode suitability

- [ ] The unit can function in classroom use
- [ ] The unit can function in self-study with the established dual-framing convention
- [ ] Partner/group-dependent activities are supportable for self-study learners
- [ ] Tasks are not over-dependent on a specific class size or teaching mode unless clearly signalled

## 5C. Language And Learning

### 5C.1 Explicit teaching

A unit meets this criterion only if all six N10 minimum deliverables are present in some form. Check each one:

- [ ] Clear alignment between module purpose, unit goals, and activity goals is reflected in the teaching sequence
- [ ] A clear conceptual explanation of the target feature is present in the main Language Focus area (not just a phrase bank or model text)
- [ ] At least one explicit "why this works" element appears in model-text comparison work or Language Focus commentary
- [ ] Any key contrast or choice central to the unit is explained, not just illustrated
- [ ] At least one worked example demonstrates the target concept in a way that would otherwise remain implicit
- [ ] A visible bridge from explanation to later writing use is present before the main production task

**Requirement source:** `adv/edits & guides/aw-adv_n10_language_instruction_framework.md` Section 9 — these six items are the agreed minimum deliverables for a unit to be treated as N10-complete. Presence of explanation layer labels (`Why this works`, `Teaching point`, etc.) is necessary but not sufficient evidence of compliance; all six items must be confirmed.

### 5C.2 Conceptual clarity

- [ ] Labels are accurate and useful
- [ ] Key distinctions are explained where needed
- [ ] Worked examples support the explanation where the concept is not self-evident
- [ ] The wording does not create conceptual confusion or misleading simplifications

### 5C.3 Language support sufficiency

- [ ] Enough vocabulary, phrasing, structure, or rhetorical support is given for learners to complete the task
- [ ] Phrase banks and useful-language sections are explained rather than presented as bare inventories
- [ ] Controlled practice is sufficient to prepare later writing tasks

### 5C.4 Practice and transfer

- [ ] Section C meaningfully prepares learners for D/E/H tasks
- [ ] The bridge from explanation to production is visible
- [ ] The learner can transfer the principle to a new situation rather than only mimic the model

## 5D. Prompt And Task Design

### 5D.1 Learning-goal pressure

- [ ] Completing the task requires practising the target skill
- [ ] The scenario is a vehicle for the skill, not a distraction from it
- [ ] The task cannot be completed successfully by bypassing the intended learning behavior

### 5D.2 Professional verisimilitude

- [ ] Prompts are situation-anchored, not topic-anchored
- [ ] Purpose, audience, subject, type, and role are recoverable at the right level for the task type
- [ ] The scenario does not read like an academic exercise

### 5D.3 Calibration

- [ ] Guided tasks provide enough support without pre-solving the work
- [ ] Freer writing tasks leave meaningful analysis and organisation to the learner
- [ ] Homework tasks are appropriately independent
- [ ] Word counts align with the agreed progression: ~150w (Module 1) → ~200w (Modules 2–3) → ~250w (Modules 4–5) → ~300–350w (Module 6 / Units 22–23)
- [ ] Revised prompts do not drift upward in linguistic sophistication or processing load beyond what the target learner can reasonably handle

**Requirement sources:**

- `adv/edits & guides/aw-adv_project_context.md` — internal framing targets B1+/B2 learners in an aspirational, scaffolded context
- `adv/edits & guides/aw-adv_prompt-writing-policy.md` — the scenario is the vehicle, not the point; prompts must be calibrated so the writing work stays with the learner
- `adv/edits & guides/aw-adv_unit_structural_profiles_revised.md` — learner-facing Can-Do architecture and module-by-module workload progression govern what the learner is being asked to process and produce

### 5D.4 Choice-list quality

- [ ] Options are parallel in length, detail level, and difficulty
- [ ] Options represent genuinely different professional situations
- [ ] JPO options, where present, function as one option among equals and do not overlap with the general options

## 5E. Consistency And Cohesion

### 5E.1 Structural consistency

- [ ] Headings, numbering, and section ordering are consistent across the book
- [ ] Activity codes match the intended structure
- [ ] Section H ordering is correct

### 5E.2 Instructional consistency

- [ ] Student-facing instructions are written in a consistent professional style
- [ ] Terminology is stable across units
- [ ] Repeated features such as checklists and review sections behave consistently enough to be learnable

### 5E.3 Variety without chaos

- [ ] Activity variety exists across the book
- [ ] Scenario variety exists across the book
- [ ] Variety does not make the textbook feel structurally random or inconsistent
- [ ] The book retains a coherent identity and predictable instructional rhythm
- [ ] Scenario families are distributed broadly enough across the book that one context pattern does not dominate a module or cluster of adjacent units
- [ ] JPO variants expand the book's contextual range rather than recycling the same interoffice or trilateral coordination pattern under slightly different surface details

**Requirement sources:**

- `adv/edits & guides/aw-adv_project_context.md` — scenarios were already identified as over-reliant on a narrow set of recurring situation types and were meant to be diversified across modules
- `adv/edits & guides/aw-adv_prompt-writing-policy.md` — options should represent meaningfully different professional situations and avoid contextual overlap
- `adv/edits & guides/aw-adv_project_todo_list.md` — scenario variety and prompt-policy compliance remain explicit QA concerns in the active workstream

## 5F. Model Text Quality

### 5F.1 Weak-original quality

- [ ] The weak original is weak in the right way for the target skill
- [ ] The weak version is not broken for irrelevant reasons only
- [ ] The weakness is teachable rather than arbitrary

### 5F.2 Improved-model quality

- [ ] The improved version clearly demonstrates the target skill
- [ ] The improved version is strong enough to serve as a benchmark
- [ ] The improved version remains realistic and not over-polished to the point of inauthenticity

### 5F.3 Comparison productivity

- [ ] The contrast between weak and improved texts is teachable
- [ ] The comparison prompts actually guide useful noticing
- [ ] The model-text work helps learners understand how to improve their own writing

## 5G. Structural Profile Compliance

### 5G.1 Activity-profile compliance

- [ ] The active unit matches the assigned activity codes and sequence in the structural profiles
- [ ] First-use and special-profile exceptions are handled correctly where relevant
- [ ] Any deliberate deviation from the profile is documented and justified
- [ ] H1 Extension Tasks are present only in units where the structural profiles assign H1; units not assigned H1 (currently Units 2, 3, 4, 6, and 11) must not contain an H1 Extension Task unless the project owner has explicitly approved a profile change
- [ ] Where H1 is correctly assigned, the Extension Task contains three genuinely varied options drawn from different activity types in the Master Activity Menu

### 5G.2 Can-Do architecture compliance

- [ ] The teaching sequence visibly supports the unit and activity Can-Do statements in the structural profiles
- [ ] The module file does not undermine the planning commitments made in the profiles

## 5H. Activity-Type Fidelity

### 5H.1 Menu fidelity

- [ ] Each activity does what its code says it should do in the Master Activity Menu
- [ ] Guided, freer, review, and extension tasks are not collapsed into one another
- [ ] Optional and extensional tasks remain genuinely extensional

### 5H.2 Student experience fidelity

- [ ] The activity feels like the right kind of task to the learner
- [ ] The amount of support or independence matches the activity type
- [ ] The book does not use an activity code as a label for something pedagogically different

## 5I. Progression

### 5I.1 Within-module progression

- [ ] Units within each module show a sensible increase in complexity or integration
- [ ] Earlier units prepare for later units
- [ ] The sequence of document types and rhetorical demands is sensible

### 5I.2 Book-level progression

- [ ] Word-count progression is correct: ~150w (Module 1) → ~200w (Modules 2–3) → ~250w (Modules 4–5) → ~300–350w (Module 6 / Units 22–23)
- [ ] The book moves from foundation to more complex applied writing in a believable arc
- [ ] Module 6 functions as a capstone phase rather than just another content block

## 5J. Self-Study Accessibility

### 5J.1 Independent usability

- [ ] A self-study learner can understand what to do in each activity
- [ ] Peer or discussion tasks remain usable through the established self-study framing
- [ ] Units do not depend on invisible teacher explanation to become understandable

### 5J.2 Resource independence

- [ ] Where workplace material is invited, accessible alternatives exist where needed
- [ ] The learner can complete the unit without impossible external resources

## 5K. Answer-Key Supportability

### 5K.1 Controlled-practice answerability

- [ ] Controlled exercises have determinable or supportable answers
- [ ] Matching, classification, sequencing, and correction tasks are supportable in an answer key
- [ ] Model-text and editing tasks can be annotated clearly for teacher or self-study support

### 5K.2 Sample-response supportability

- [ ] Guided and freer writing tasks are specific enough that sample responses or marking notes can later be produced
- [ ] Current wording does not make post hoc answer-key development needlessly ambiguous

## 5L. Formatting And Production Readiness

### 5L.1 Markdown and structural hygiene

- [ ] Heading hierarchy is correct
- [ ] Numbering and separators are clean
- [ ] There are no obvious formatting artifacts or broken structure blocks
- [ ] Activity headings follow the correct format throughout: `#### Activity Name (Code)` — name first, code in parentheses; code-first formats such as `#### (C3) Activity Name` are errors
- [ ] Activity sub-labelling under F and H sections is explicit and consistent: H3, H1, F1 etc. appear as `####`-level subheadings rather than being embedded in running text or omitted

### 5L.2 Production readiness

- [ ] The text is ready for the later formatting stage without major content-structure repair
- [ ] There are no obvious copy-paste artifacts, encoding problems, or broken references

## 5M. Remaining Pinned-Item Checks

### 5M.1 Confirm-at-QA pinned items

- [ ] `P1` structural variety is visible in the final book, not just in the profiles
- [ ] `P2` data interpretation tasks are present in the intended units
- [ ] `P3` practice-item minimum is sustained across the book
- [ ] `P5` word-count targets are correct where required
- [ ] `P6` reading-to-write tasks are present in the intended units

### 5M.2 Deferred pinned items

- [ ] `P4` answer key / sample responses is recorded as a later stage, not mistaken for a current failure
- [ ] `P7` Unit 23 rubric requirement is explicitly tracked and not forgotten before sign-off
- [ ] Learning goals mapping issues (14 improvement recommendations identified in `admin-writing-adv_learning-goals-mapping.md` across five categories) are recorded as a named deferred item; confirm they are tracked in the to-do list and will not be lost before book sign-off

---

## 6. Book-Level Sign-Off Questions

Before treating `N11` as complete, answer:

- [ ] Does the advanced book now meet the agreed quality standard for a full review pass?
- [ ] Are all `Revise` findings concrete, local, and fixable without reopening the planning architecture?
- [ ] Have all `Deferred` items been explicitly named so they do not disappear between stages?
- [ ] Is there any structural or pedagogical issue significant enough to block full review?

If the answer to the last question is `Yes`, `N11` is not complete.

---

## 7. Suggested Recording Template For Findings

Use the following structure when recording module or unit findings:

- File under review:
- Unit or module:
- Category:
- Criterion:
- Check item:
- Result: `Pass` / `Revise` / `Monitor` / `Deferred`
- Evidence:
- Required action:

---

## 8. Immediate N11 Priorities

Prioritise the first book-wide pass on:

1. confirming that `N10` explanations are sufficient rather than merely present
2. confirming that the active `n10` module files still match the structural profiles
3. confirming that prompt and task design quality survived the later pedagogical strengthening pass
4. confirming final book-level progression and pinned-item completion status
5. identifying any blockers before full review

---

*Working status: v2 — revised after cross-checking the Round 2 review against the original checklist. Gaps addressed: preliminary cross-check step added (Section 4.0); H1 Extension Task compliance check added (5G.1); N10 minimum deliverables made the concrete standard for 5C.1; activity heading format check added (5L.1); explicit word-count targets added to 5D.3 and 5I.2; requirement source added to 5B.2; learning goals mapping deferred item added to 5M.2.*
