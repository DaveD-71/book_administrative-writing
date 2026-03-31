# Intermediate QA Checklist
## *Administrative Writing, Intermediate*

---

> **Purpose of this document**
> This file defines the whole-book quality assurance framework for the intermediate book after completion of the main revision stages.
>
> Intermediate QA is not a drafting pass, not a language-instruction pass, and not a structural redesign pass by default. It is the formal quality gate that tests whether the completed module-file source set meets the agreed project standards before full review begins.

---

## 1. Scope Of Intermediate QA

The QA gate checks the completed intermediate book against the agreed standards for:

- design for purpose and unit-goal alignment
- learner suitability
- language and learning
- prompt and task design
- consistency and cohesion
- model text and example quality
- support-depth parity against the advanced book
- structural-profile compliance
- activity and section fidelity
- progression across units and modules
- module-volume parity
- self-study accessibility
- answer-key supportability
- formatting and production readiness
- remaining pinned-item checks that are meant to be confirmed at QA stage

QA should identify:

- what already meets the standard
- what needs correction before full review
- what can remain as a later deferred item because it belongs to a post-content stage such as rubric or answer-key development

---

## 2. Source Hierarchy For QA

Use the following source order:

1. `int/edits & guides/planning/guide-set/aw-int_project_todo_list.md`
2. `int/edits & guides/planning/guide-set/aw-int_Support-Parity Intervention Plan.md`
3. `int/edits & guides/planning/guide-set/aw-int_unit_structural_profiles.md`
4. `int/edits & guides/planning/guide-set/aw-int_activity_framework.md`
5. `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md`
6. `int/edits & guides/qa/aw-int_qa_round1.md`
7. `int/edits & guides/planning/supporting/aw-int_project_context.md`
8. active module files in `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md`
9. baseline-audit or earlier development records only as narrow historical support

If sources disagree, prefer the higher source in this list unless a later explicit project decision says otherwise.

---

## 3. Output Model For QA

Use three levels of QA structure:

### Level 1 - QA Category

The major review area, such as:

- Design for Purpose
- Learner Suitability
- Language and Learning
- Prompt and Task Design
- Consistency and Cohesion
- Model Text and Example Quality

### Level 2 - Criterion

The specific aspect within the category, such as:

- unit-goal alignment
- support sufficiency
- prompt calibration
- structural-profile compliance

### Level 3 - Check Item

The concrete test that can be answered during review.

Use status values:

- `Pass`
- `Fail`

Later-stage items are not given a separate status.  
Instead, judge whether they are being controlled correctly now:

- `Pass` if the deferred item is explicitly tracked and is not being mistaken for completed work
- `Fail` if the deferred item has disappeared, is being misclassified, or is currently blocking sign-off without being recorded correctly

---

## 4. Review Workflow

### 4.0 Preliminary cross-check (before module review begins)

Before beginning the module-by-module pass, complete the following:

1. Confirm the current project-control files and active source-of-truth decisions now in force:
   - the six live module files in `int/md/first_draft_modules`
   - the completed structural-profile layer
   - the current intermediate prompt and activity standards
2. Confirm that the completed `INT-4` and `INT-5` passes did not leave an unresolved planning/live mismatch in the active control layer.
   - this includes profile-to-live `### Focus` sync
   - and transfer of profile output expectations where the live task wording had previously left them only implied
3. Note any pinned items that still affect QA judgment:
   - Unit 23 rubric support
   - later answer-key work
   - regeneration of the combined draft
4. Note any approved structural exceptions already recorded in the structural profiles so they are not misread as accidental drift during QA.
   - and note any active whole-book control notes for scenario-family distribution or reflection progression
5. Read the active continuity QA record and any Round 1 addendum before capturing new findings.
   - confirm whether an earlier book-level blocker is still active, has been cleared, or has been replaced by a new blocker
   - list any earlier `Fail` findings that remain unactioned, partially actioned, or superseded
   - do not silently continue QA from stale pre-intervention assumptions
6. Confirm whether project control still allows active QA or whether a blocking intervention stage is now in force.
7. Confirm that the review is being run against the mature advanced-style QA standard rather than a softer rebuild-confirmation standard.
   - if a module only appears "serviceable" or "structurally present" but has not been stress-tested for subtle weakness, do not record `Pass`
   - if the current evidence only shows that a blocker is absent, do not record `Pass`; record `Fail` until the category has been verified strongly enough to clear

These preliminary items must be recorded before module findings are captured. A `Fail` at this stage blocks sign-off regardless of module-level results.

### 4.1 Review order

Run QA in this sequence:

1. complete preliminary cross-check (Section 4.0)
2. confirm book-level source documents and standards
3. review the six live module files in order
4. capture unit-level findings
5. summarize module-level findings
6. consolidate book-level findings
7. determine whether the book is ready for full review

### 4.2 Review scale

QA is hierarchical:

- some checks are unit-level
- some checks are module-level
- some checks are book-level

Do not force every concern into a unit-local finding if it is really a whole-book issue.

### 4.3 Evidence rule

Every `Fail` judgment should state:

- the file and unit/module affected
- the failed criterion
- the specific reason it fails
- the minimum corrective action needed

### 4.4 Non-overwrite rule

QA should not silently rewrite the planning architecture.

If the failure is:

- a local content problem, mark `Fail`
- a likely planning/live mismatch, mark `Fail` and identify the architectural issue clearly

---

## 5. Level 1 Categories, Criteria, And Checks

## 5A. Design For Purpose

### 5A.1 Module-purpose alignment

- [ ] Each unit clearly supports the stated purpose of its module
- [ ] The module's cluster of units forms a coherent skill band rather than a loose topic grouping

### 5A.2 Unit-goal alignment

- [ ] The live unit content supports the stated learning goal and Can-Do statements
- [ ] The main writing outcome of the unit matches the unit's declared purpose
- [ ] The unit does not drift into a different dominant skill than the one named in the profiles

### 5A.3 Activity-goal alignment

- [ ] The activity sequence develops the target skill rather than repeating disconnected exercises
- [ ] Later tasks require the learner to apply the intended skill, not a different dominant skill
- [ ] The unit shows visible pedagogical progression rather than a stack of unrelated exercises

### 5A.4 Internal unit coherence

- [ ] Examples, language work, guided tasks, freer tasks, and extension tasks all support the same core skill family
- [ ] Section-to-section movement feels intentional rather than stitched together
- [ ] Added teaching support does not redirect the unit toward a different main purpose

## 5B. Learner Suitability

### 5B.1 Level appropriacy

- [ ] Input and instruction wording are appropriate for A2-B1+ workplace learners
- [ ] Task demands are challenging but still supportable for the target learner
- [ ] Prompts do not create avoidable difficulty through dense phrasing or unexplained background
- [ ] Revised teaching support does not increase processing load beyond the intended intermediate level

**Requirement sources:**

- `int/edits & guides/planning/supporting/aw-int_project_context.md` - target learners are A2-B1+ workplace learners and the book should remain readable, scaffolded, and teachable
- `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md` - prompts must remain short, concrete, and professionally readable

### 5B.2 Workplace relevance

- [ ] Scenarios reflect recognisable workplace communication needs
- [ ] Document types and writing purposes feel plausible in a routine professional environment
- [ ] The book's workplace realism remains useful without becoming over-specialised or institution-heavy

**Requirement sources:**

- `int/edits & guides/planning/supporting/aw-int_project_context.md` - workplace realism should remain broad and readable rather than niche or over-specialised
- `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md` - the learner should be challenged by the writing task, not by decoding the prompt

### 5B.3 Delivery-mode suitability

- [ ] The unit can function in both classroom use and self-study use
- [ ] Tasks do not depend on teacher mediation unless the text clearly supports the learner without it
- [ ] Homework and reflection layers remain usable without hidden classroom assumptions

## 5C. Language And Learning

### 5C.1 Explicit teaching

- [ ] The unit teaches the principle behind the target pattern, not just a phrase list
- [ ] Key language points are explained enough for transfer
- [ ] Added teaching supports make the writing move clearer rather than merely longer

### 5C.2 Conceptual clarity

- [ ] Labels are accurate and useful
- [ ] Key distinctions are explained where needed
- [ ] Short teaching frames do not create conceptual confusion or misleading simplifications

### 5C.3 Language support sufficiency

- [ ] The learner receives enough vocabulary, language, structure, or rhetorical support to complete later tasks
- [ ] Guided layers visibly prepare freer layers
- [ ] Phrase banks or checklist-style supports are explained enough to be usable, not just displayed
- [ ] Units with phrase-bank-heavy sections include worked mini-examples where the learner needs to see the phrases operating inside a full message
- [ ] Support is visible in the live unit, not merely inferable from surrounding sections or from what the teacher could explain orally

### 5C.4 Practice and transfer

- [ ] Controlled practice builds toward real writing behavior
- [ ] The learner can reasonably move from explanation to production without a hidden gap
- [ ] Reflection and homework layers extend the same skill family rather than introducing a new dominant demand
- [ ] Reflection prompts become more metacognitive in later modules instead of staying at a flat recall-only pattern

### 5C.5 Support-depth parity

- [ ] The unit does not stop at phrase exposure or short procedural advice where advanced-equivalent support would require transferable explanation
- [ ] The unit includes visible support equivalents for model/example work, explicit rationale, review/self-edit, editing/revision, and transfer/extension
- [ ] Lower level is achieved through readability and scaffolding, not through thinner pedagogy
- [ ] "Functional equivalence" is not enough if the support move is too implicit, too compressed, or too easy to miss for a self-study learner

## 5D. Prompt And Task Design

### 5D.1 Learning-goal pressure

- [ ] Completing the task requires practising the intended skill
- [ ] The scenario is a vehicle for the skill, not a distraction from it
- [ ] The task cannot be completed successfully by bypassing the intended writing behavior
- [ ] The learner cannot satisfy the task mainly by copying surface language, choosing any plausible content, or relying on a generic message that ignores the target move

### 5D.2 Professional verisimilitude

- [ ] Purpose, audience, situation, type, and role are recoverable at the right level for the task
- [ ] Prompts are workplace-like without becoming dense or overly bureaucratic
- [ ] Reader relationship is clear where it affects tone, content, or document type
- [ ] The prompt does not hide a key requirement that the learner must infer from scattered clues or from unstated workplace assumptions

### 5D.3 Calibration

- [ ] Guided tasks provide enough support without pre-solving the work
- [ ] Freer tasks are independent but still intermediate-appropriate
- [ ] Later integrated tasks do not overload the learner with too many simultaneous demands
- [ ] Output load remains believable for the unit's position in the book
- [ ] The task does not quietly exceed its stated scope by asking for extra comparison, diagnosis, audience-shift, or document-management work that the prompt has not prepared clearly

**Requirement sources:**

- `int/edits & guides/planning/supporting/aw-int_project_context.md` - the book should remain simpler, more scaffolded, and more teachable than the advanced book
- `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md` - guided tasks should remain supported and freer tasks should remain achievable for A2-B1+ learners
- `int/edits & guides/planning/guide-set/aw-int_unit_structural_profiles.md` - output expectations and approved exceptions govern workload and progression

### 5D.4 Option quality

- [ ] Scenario options, where used, are parallel in length, detail level, and difficulty
- [ ] Options represent genuinely different situations rather than cosmetic rewrites
- [ ] Shared requirements are stated once at task level rather than scattered or repeated inconsistently
- [ ] Freer-practice options are situation-anchored rather than reduced to topic labels or error-type shorthand
- [ ] Option sets do not contain one obviously easier, more familiar, or more fully specified option that distorts task calibration

## 5E. Consistency And Cohesion

### 5E.1 Structural consistency

- [ ] Section patterns remain readable and consistent enough across the book
- [ ] Headings and instructional labels behave predictably
- [ ] Later integrated units remain recognisably part of the same book
- [ ] Section order and visible section function are stable enough that a learner can transfer expectations from one unit to the next without re-learning the book each time

### 5E.2 Instructional consistency

- [ ] Student-facing instructions use a stable professional tone
- [ ] Terminology is consistent across units and modules
- [ ] Added teaching supports behave consistently enough to be learnable
- [ ] The same label is not used for materially different pedagogical jobs unless that variation is explicit and justified

### 5E.3 Variety without chaos

- [ ] Variation exists without making the book feel random
- [ ] Scenario spread, output types, and support layers feel intentionally distributed
- [ ] The book retains a coherent identity and predictable instructional rhythm
- [ ] Adjacent units do not over-cluster around the same missing/incorrect-document scenario family without a deliberate reason

## 5F. Model Text And Example Quality

### 5F.1 Weak-original or weak-example quality

- [ ] Weak examples are weak in the right way for the unit skill
- [ ] The weakness is teachable rather than arbitrary
- [ ] Comparisons focus attention on the target skill rather than irrelevant errors

### 5F.2 Improved-model quality

- [ ] Improved models demonstrate the target skill clearly
- [ ] Models remain realistic and not over-polished beyond the intermediate level
- [ ] Model improvements are visible enough to support transfer

### 5F.3 Comparison productivity

- [ ] Comparisons teach something visible and usable
- [ ] Before/after contrasts guide productive noticing
- [ ] Model work helps learners understand how to improve their own writing

## 5G. Structural-Profile Compliance

### 5G.1 Unit-profile compliance

- [ ] The live unit matches its structural profile in learning goal, Can-Do logic, and output expectation
- [ ] Any deliberate structural exception is recorded in the profiles
- [ ] The live unit does not silently erase an approved exception or add an unrecorded new one
- [ ] The live `### Focus` section reflects the current profile Can-Do statements rather than an older pre-profile wording layer
- [ ] Output expectations, audience framing, and task type remain aligned with the active profile wording rather than being only broadly similar in spirit

### 5G.2 Can-Do and framework compliance

- [ ] The teaching sequence visibly supports the unit-level Can-Do statements in the structural profiles
- [ ] The live unit behaves consistently with the intermediate activity framework
- [ ] The live unit does not drift toward advanced-style architecture without an explicit decision
- [ ] A unit is not counted compliant merely because all expected sections exist; the sections must perform the profile-assigned pedagogical job

## 5H. Activity And Section Fidelity

### 5H.1 Section-function fidelity

- [ ] Focus, Language, Practice, Guided Practice, Freer Practice, Reflection, and Homework perform the jobs assigned to them
- [ ] No section label is doing the wrong pedagogical job
- [ ] Extended Writing Task, where used, extends rather than duplicates the freer layer
- [ ] Reflection and Homework do not carry hidden core teaching load that should have appeared earlier in the unit

### 5H.2 Student experience fidelity

- [ ] The amount of support or independence matches the visible section label
- [ ] Guided Practice meaningfully prepares Freer Practice
- [ ] Revision-focused units still feel like editing/revision units rather than hidden new-drafting units
- [ ] A learner experiencing the unit cold would describe the task type the same way the checklist labels it

## 5I. Progression

### 5I.1 Within-module progression

- [ ] Units in the same module rise or shift in demand intentionally
- [ ] Output expectations remain believable for their position in the module
- [ ] Earlier units prepare for later units in the same module

### 5I.2 Book-level progression

- [ ] Later integrated tasks are prepared by earlier units
- [ ] Module 6 complexity is earned by the earlier book, not imported suddenly
- [ ] Sentence-band, paragraph-band, email-task, and integrated-task progression still matches the structural-profile logic

### 5I.3 Module-volume parity

- [ ] Module development depth is no longer severely below the advanced benchmark
- [ ] Module length is consistent with the current parity band recorded in the intervention plan unless an approved exception is recorded
- [ ] Added volume comes from real support architecture rather than filler explanation

## 5J. Self-Study Accessibility

### 5J.1 Independent usability

- [ ] Instructions, examples, and task flow are usable without hidden teacher explanation
- [ ] Carry-forward or revision-chain tasks are signposted clearly enough for interrupted use
- [ ] A self-study learner can tell what kind of output each task expects

### 5J.2 Resource independence

- [ ] Reflection and Homework layers help learners consolidate and transfer the unit skill
- [ ] The learner can complete the unit without impossible outside resources
- [ ] Any invitation to use real workplace material remains supportable for independent learners

## 5K. Answer-Key Supportability

### 5K.1 Controlled-practice answerability

- [ ] Controlled exercises have determinable or supportable answers
- [ ] Matching, classification, sequencing, correction, and rewrite tasks can be supported clearly in a later answer key
- [ ] Model-text and editing tasks can later be annotated coherently

### 5K.2 Sample-response supportability

- [ ] Guided and freer writing tasks are specific enough that later sample responses or marking notes can be produced
- [ ] Open-endedness remains manageable rather than uncontrolled
- [ ] Current wording does not make later support writing needlessly ambiguous

## 5L. Formatting And Production Readiness

### 5L.1 Markdown and structural hygiene

- [ ] Heading levels, numbering, and list behavior are stable enough for later production work
- [ ] No obvious formatting issue would distort later compilation or export
- [ ] There are no obvious copy-paste artifacts, broken blocks, or structural glitches in the live source

### 5L.2 Production readiness

- [ ] The text is ready for later formatting work without major content-structure repair
- [ ] The live module files are usable as the stable source set for later support layers
- [ ] There are no obvious copy-paste artifacts, encoding problems, or broken references in the live source set

## 5M. Remaining Pinned-Item Checks

### 5M.1 Confirm-at-QA pinned items

- [ ] The live source of truth remains the six module files, not the older split-unit baseline or combined draft
- [ ] Deferred support items that affect later sign-off are still visible in the current project-control layer
- [ ] The current QA round explicitly records any pinned item that is not meant to block QA yet
- [ ] Any pinned item that affects current judgment is tested for visible live-file evidence, not treated as satisfied merely because it is still named in planning

### 5M.2 Deferred pinned items

- [ ] `P1` Unit 23 learner-facing rubric requirement is explicitly tracked and not forgotten before sign-off
- [ ] `P2` Unit 23 teacher-facing rubric or marking-support requirement is explicitly tracked and not forgotten before sign-off
- [ ] `P3` answer key / sample responses is recorded as a later stage, not mistaken for a current QA failure
- [ ] `P4` combined-draft regeneration is recorded as a later stage, not mistaken for a missing live source file
- [ ] `P5` Word-formatting work remains clearly deferred until Markdown sign-off
- [ ] Deferred status is not used to hide a current content weakness that should already be judged in the live modules

---

## 6. Book-Level Sign-Off Questions

Before treating intermediate QA as complete, answer:

- [ ] Does the intermediate book now meet the agreed quality standard for a full review pass?
- [ ] Are all `Fail` findings concrete, local, and fixable without reopening the planning architecture?
- [ ] Have all later-stage items been explicitly named so they do not disappear between stages?
- [ ] Is there any structural, pedagogical, or learner-suitability issue significant enough to block full review?
- [ ] Is the book still materially thinner than the advanced book in support depth or development volume?

If the answer to the last question is `Yes`, QA is not complete.

Book-level support-parity failure is a blocker even when local unit-level issues also exist.  
Do not reduce a systemic parity problem to only a list of local `Fail` items.

---

## 7. Suggested Recording Template For Findings

Use the following structure when recording module or unit findings:

- File under review:
- Unit or module:
- Category:
- Criterion:
- Check item:
- Result: `Pass` / `Fail`
- Evidence:
- Required action:

---

## 8. QA Re-entry Priorities After INT-5A

When QA restarts or resumes after `INT-5A`, prioritise the first book-wide pass on:

1. confirming that the completed intervention rebuild did not create planning/live drift
2. confirming that support-depth parity and module-volume parity now meet the corrected standard
3. confirming that the live module files still match the structural profiles, activity framework, and prompt policy after intervention-stage revision
4. confirming that live `### Focus` sections, prompt-option design, and profile flags now reflect the corrected control decisions
5. checking phrase-bank worked examples, scenario-family spread, and later-module reflection progression before full review
6. identifying any remaining workload, self-study, or answer-key-supportability issues before full review
7. keeping deferred later-stage items visible rather than letting them disappear between stages

---

*Working status: source-of-truth QA-stage definition for the intermediate book, tightened to function as the operational equivalent of the mature advanced QA checklist while remaining specific to the intermediate architecture.*
