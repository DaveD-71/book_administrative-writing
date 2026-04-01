# Full Review Round 1
## *Administrative Writing, Intermediate*

---

> **Scope**
> This file records the first full-review round for the live intermediate module set in `int/md/final/modules`, using the current intermediate full-review protocol as the authority frame.
>
> **Review baseline**
> - live source set:
>   - `int/md/final/modules/aw-int_mod1.md`
>   - `int/md/final/modules/aw-int_mod2.md`
>   - `int/md/final/modules/aw-int_mod3.md`
>   - `int/md/final/modules/aw-int_mod4.md`
>   - `int/md/final/modules/aw-int_mod5.md`
>   - `int/md/final/modules/aw-int_mod6.md`
> - full-review protocol:
>   - `int/edits & guides/planning/guide-set/aw-int_full-review_protocol.md`
> - controlling planning references:
>   - `int/edits & guides/planning/guide-set/aw-int_project_todo_list.md`
>   - `int/edits & guides/planning/guide-set/aw-int_unit_structural_profiles.md`
>   - `int/edits & guides/planning/guide-set/aw-int_activity_framework.md`
>   - `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md`
>   - `int/edits & guides/planning/guide-set/aw-int_student-response-layout_plan.md`
> - QA baseline already closed in:
>   - `int/archive/edits & guides/qa/aw-int_qa_review_round1.md`
> - continuity / historical QA reference:
>   - `int/archive/edits & guides/qa/aw-int_qa_round1.md`

## Key Decisions Checked

- `INT-6` remains closed and is not being reopened without fresh live evidence.
- The six files in `int/md/final/modules` remain the only live editing source.
- `int/md/final/aw-int-all.md` remains a regenerated reference-only snapshot and should be rebuilt after any live module edit.
- The hybrid `A-H` shell remains the accepted structural model, but the book must still read as a simpler, more teachable intermediate text rather than as an advanced transplant.
- The intermediate book must keep advanced-equivalent support depth while remaining readable for A2-B1+ learners.
- `P6` is already recorded in the project-control layer as having a completed live source-layer placeholder system, with only final print-layout work deferred.

## Findings

### 1. The late Module 6 guided multi-document boxes were still out of line with the declared source-layer placeholder standard

**Severity:** `Revise`

**Finding type:** `Planning/live mismatch`

**Files:**
- `int/edits & guides/planning/guide-set/aw-int_student-response-layout_plan.md:152`
- `int/edits & guides/planning/guide-set/aw-int_student-response-layout_plan.md:221`
- `int/edits & guides/planning/guide-set/aw-int_student-response-layout_plan.md:238`
- `int/edits & guides/planning/guide-set/aw-int_project_todo_list.md:46`
- `int/md/final/modules/aw-int_mod6.md:165`
- `int/md/final/modules/aw-int_mod6.md:203`
- `int/md/final/modules/aw-int_mod6.md:495`
- `int/md/final/modules/aw-int_mod6.md:516`
- `int/md/final/modules/aw-int_mod6.md:1115`
- `int/md/final/modules/aw-int_mod6.md:1135`
- `int/md/final/modules/aw-int_mod6.md:1173`

**Controlling reference / key decision being tested:**
- The student-response layout plan says Module 6 integrated tasks must use labeled sub-boxes for audience- or purpose-split documents.
- The same plan says `Write Here` alone is not enough for paired or multi-document tasks.
- The project to-do list already described the live source-layer placeholder system as complete.

**Why this matters at book level:**
- This is not just print-layout housekeeping. The live manuscript itself is supposed to carry the source-layer label and marker logic that later stages will build on.
- Generic `Write Here` labels weaken the learner-facing distinction between paired guided outputs in the most complex module of the book.
- Duplicate placeholder IDs in the same live file create ambiguity for later print-layer work and for any support-material workflow that relies on the marker names.
- Because this issue sits in Units 19, 20, and 22, it affects the book's culminating audience-control and multi-document architecture rather than a local early-unit detail.

**Evidence:**
- Round-start scan of `int/md/final/modules/aw-int_mod6.md` found that the paired guided boxes in Units 19 and 20, and two of the three guided boxes in Unit 22, still used generic `Write Here` labels.
- The same round-start scan found duplicate live placeholder IDs in those guided sets:
  - `U19-guided-document`
  - `U20-guided-document`
  - `U22-guided-document`
- Those repeated IDs and generic labels contradicted the live-source-layer completion claim in the project to-do file and the audience-specific label requirement in the layout plan.

**Recommended action:**
- Replace the generic guided labels in Units 19, 20, and 22 with audience-specific labels.
- Replace the duplicate guided placeholder IDs with unique task-specific IDs.
- Regenerate `int/md/final/aw-int-all.md` from the corrected live module set.

**Resolution note (2026-04-01):**
- The live source was corrected in `int/md/final/modules/aw-int_mod6.md`:
  - Unit 19 now uses:
    - `External Email`
    - `Internal Explanation`
  - Unit 20 now uses:
    - `Revision Message`
    - `Internal Notice`
  - Unit 22 now uses:
    - `Applicant Reply`
    - `Colleague Explanation`
    - `Internal Notice`
- The duplicate guided placeholder IDs were replaced with unique task-specific IDs:
  - `U19-guided-external-email`
  - `U19-guided-internal-explanation`
  - `U20-guided-revision-message`
  - `U20-guided-internal-notice`
  - `U22-guided-applicant-reply`
  - `U22-guided-colleague-explanation`
  - `U22-guided-internal-notice`
- `int/md/final/aw-int-all.md` was regenerated directly from the six canonical module files after the fix.

---

## Section 4 Assessment

### Whole-book coherence

**Judgment:** sufficiently evidenced, clear after targeted source correction

- All 23 live units now carry the hybrid `A-H` shell, and the shell is present in every unit from Unit 1 to Unit 23.
- The live sequence still reads as one book:
  - sentence and tone control in Module 1
  - routine email control in Module 2
  - internal explanation / procedure / summary work in Module 3
  - outward-facing and consistency-focused communication in Module 4
  - revision-focused work in Module 5
  - integrated multi-document and portfolio work in Module 6
- The one whole-book coherence defect surfaced in this round was the late Module 6 guided placeholder-label drift recorded in Finding 1, and it has now been corrected in source.

### Progression

**Judgment:** sufficiently evidenced, passes

- The book still rises in a controlled way from:
  - `3-4` sentence early emails and messages
  - `5-6` sentence paragraphs and report-style units
  - paired texts in Modules 2 to 5
  - integrated two-document and three-document sets in Module 6
  - a final four-item portfolio in Unit 23
- Module 6 still reads as a culmination rather than a separate book:
  - audience split
  - revision / notice contrast
  - team consistency
  - multi-document control
  - final portfolio assembly
- No new progression dip or spike significant enough to distort the book-level learning path was confirmed in this round.

### Live/planning alignment

**Judgment:** sufficiently evidenced, passes after targeted source correction

- The live module set remains aligned with the hybrid `A-H` structural model and the broader intermediate framework.
- The full-review round found one real planning/live mismatch:
  - the late Module 6 guided placeholder layer had not fully caught up with the declared source-layer layout standard
- That mismatch has now been corrected, so the live source, project to-do file, and student-response layout plan once again describe the same intermediate book.

### Learner usability

**Judgment:** sufficiently evidenced, passes

- The book remains usable in self-study and interrupted-use terms:
  - fallback options remain visible where real workplace material is invited
  - carry-forward tasks and later integrated tasks still name their internal logic clearly enough to follow
  - late Module 6 guided tasks now name the audience or document purpose directly at the box level instead of leaving paired outputs under generic `Write Here` labels
- The fixed Module 6 guided labels improve reader control in exactly the part of the book where learners are most likely to confuse document roles.

### Editorial readiness for support materials

**Judgment:** sufficiently evidenced, ready

- The live module set is now stable enough for later support-material work because:
  - the late Module 6 source-layer placeholder drift has been corrected
  - placeholder IDs are unique across the live module set
  - `int/md/final/aw-int-all.md` has been regenerated from the corrected canonical source set
- No unresolved source-of-truth conflict remains severe enough to force later answer-key or print-layer work to be written against moving targets.

## Targeted Recheck After Live Corrections

- Corrected live file:
  - `int/md/final/modules/aw-int_mod6.md`
- Derived combined file regenerated from the canonical source set:
  - `int/md/final/aw-int-all.md`
- Recheck results:
  - all 23 units still carry the hybrid `A-H` shell
  - the late Module 6 guided paired / multi-document boxes now use audience-specific labels
  - duplicate placeholder IDs are no longer present anywhere in the live intermediate module set
  - the regenerated combined file exactly matches a UTF-8 direct append of the six live modules
  - the intermediate tree passes `python scripts/check_mojibake.py int`

## Review Summary

This Round 1 pass was a real post-QA full review rather than a recycled QA note.

What the review established:

- the live Intermediate book is structurally coherent and still clearly reads as one scaffolded series-level manuscript
- the progression from Module 1 foundations to Module 6 integrated portfolio work remains credible and teachable
- the control layer and live source were broadly aligned, but one real late-book source-layer mismatch remained in the Module 6 guided placeholder labels and IDs
- that mismatch was local, concrete, and repairable without reopening the planning architecture
- the corrected live source is now stable enough for later support-material work

Current judgment:

- Intermediate full review is **complete**
- the live Intermediate source is **stable enough for later support-material work**
- the next active stage is **`P6`**

## Next Suggested Actions

1. Treat the six files in `int/md/final/modules` as the stable post-full-review intermediate source baseline.
2. Use the regenerated `int/md/final/aw-int-all.md` as the derived combined reference snapshot for later production work.
3. Move the active intermediate workstream to `P6`, then continue to `P3` once the remaining production-order dependencies are satisfied.

---

*Working status: Round 1 has now been completed as a protocol-based whole-book pass and closed through one targeted live-source correction and recheck. The intermediate book is now ready to leave `INT-7` and proceed to `P6`.*
