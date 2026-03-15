# N11 QA Review - Round 3
## *Administrative Writing, Advanced*

---

> **Purpose of this document**
> This file records the Round 3 `N11` pass completed after external verification of the checklist design.
>
> Round 3 does two things:
>
> - adopts the stronger checklist standard confirmed in `aw-adv_n11_claude-fb_qa_checklist.md` and `aw-adv_n11_qa_checklist_v2_claude.md`
> - re-checks the live `n10` files against the newly explicit preliminary cross-check items and the Round 2 blocker list
>
> This is now the operative `N11` review record.

---

## Overall Status

Does the advanced book pass `N11` at this stage? `No - further revision required before full review`

Current position:

- the checklist standard is now materially stronger and fit for final QA use
- the book remains strong at pedagogical support, explicit teaching, and broad activity-type variety
- the live blockers are now more accurately defined than they were in Round 2
- some Round 2 findings still stand unchanged
- some older review flags do **not** stand as current defects in the active files and are withdrawn here

---

## Round 3 Findings

### 1. The operative checklist is now the stronger v2 standard

**Category:** QA Framework Alignment  
**Result:** `Pass`

Evidence:

- `adv/edits & guides/aw-adv_n11_claude-fb_qa_checklist.md` correctly identified missing checklist coverage around:
  - preliminary cross-check against open issues
  - H1 structural compliance
  - explicit N10 six-deliverable checking
  - activity-heading format
  - explicit word-count targets
  - learning-goals mapping as a named deferred item
- `adv/edits & guides/aw-adv_n11_qa_checklist_v2_claude.md` provides a stronger corrected version
- `adv/edits & guides/aw-adv_n11_qa_checklist.md` has now been updated to include those operative additions

Interpretation:

- Round 3 is the first pass using a checklist that adequately covers the live known-issue trail as well as the book-wide quality criteria

---

### 2. The H1 Extension Task decision is still unresolved and is a real sign-off blocker

**Category:** Structural Profile Compliance / Preliminary Cross-Check  
**Criteria:** `4.0 Preliminary cross-check` / `5G.1 Activity-profile compliance`  
**Result:** `Revise`

Evidence:

- `adv/edits & guides/aw-adv_n10_claude-fb_mod1-3_v2.md` identifies H1/profile mismatches in Units 2, 3, 4, 6, and 11
- live active files confirm those H1 tasks are still present:
  - `adv/md/n10/aw-adv_mod1_n10.md` — Units 2 and 3 contain H1 alongside profile-exempt H sections
  - `adv/md/n10/aw-adv_mod2_n10.md` — Units 4 and 6 contain `#### H1. Extension Task`
  - `adv/md/n10/aw-adv_mod3_n10.md` — Unit 11 contains `#### Extension Task (H1)`
- the structural profiles remain the higher source and still treat these units as non-H1 cases

Interpretation:

- this is not just a formatting inconsistency
- it is an unresolved planning-vs-implementation conflict
- `N11` cannot be signed off until the project owner decides whether these H1 tasks stay and the profiles are updated, or the tasks are removed to match the profiles

Required action:

- record an explicit decision on H1 for Units 2, 3, 4, 6, and 11 before final QA sign-off

---

### 3. Module 1 still has genuine structural cleanup work

**Category:** Structural Profile Compliance / Formatting And Production Readiness  
**Criteria:** `5G.1 Activity-profile compliance` / `5L.1 Markdown and structural hygiene`  
**Result:** `Revise`

Evidence:

- `adv/md/n10/aw-adv_mod1_n10.md`
  - Units 2 and 3 still contain both `#### Peer Review (F1)` and `#### Guided Peer Review (F1)`
  - Units 1-3 still use `### H. Homework & Extension` without explicit `####`-level H sub-labelling
- this matches the earlier structural concerns in `aw-adv_n10_claude-fb_mod1-3_v2.md`

Interpretation:

- these are real `N11` structural defects
- they are local and fixable
- they do not reopen the architecture, but they do block clean sign-off under the stronger checklist

Required action:

- remove the duplicate loose F1 openers in Units 2 and 3
- normalise H sub-labelling in Module 1 so H3/H1 are explicit and consistent with the rest of the book

---

### 4. Round 2 overstated the structural problem in Module 3

**Category:** Review Correction  
**Result:** `Pass` with correction

Evidence:

- live file check of `adv/md/n10/aw-adv_mod3_n10.md` shows:
  - Units 8-11 do contain explicit `#### Homework Writing Task (H3)` labels
  - only Unit 11 has the H1/profile mismatch problem flagged above
- the broader Round 2 wording that suggested missing explicit H3 labelling across Units 8-11 does not hold against the active file

Interpretation:

- Module 3 is not a broad structural blocker in the way Round 2 implied
- the real live issue here is narrower:
  - Unit 11 H1/profile mismatch

Required action:

- treat the earlier wider Module 3 H-labelling concern as withdrawn
- retain only the Unit 11 H1 decision issue as active

---

### 5. Modules 2 and 4 still carry the main prompt-design blockers

**Category:** Learner Suitability / Prompt And Task Design / Variety  
**Criteria:** `5B.1 Level appropriacy` / `5D.3 Calibration` / `5D.4 Choice-list quality` / `5E.3 Variety without chaos`  
**Result:** `Revise`

Evidence:

- `adv/md/n10/aw-adv_mod2_n10.md`
  - Unit 4 H3 JPO option still uses trilateral examiner-exchange planning
  - Unit 5 H3 JPO option still uses terminology mismatch in a shared examination document
  - Unit 6 E1 and H3 still sit in the same terminology / trilateral coordination family
  - Unit 7 E1 and H3 still rely on counterpart-office / trilateral clarification frames
- `adv/md/n10/aw-adv_mod4_n10.md`
  - Unit 12 E3 and H3 are still too close in external-inquiry / counterpart-office update pressure
  - Unit 13 H3 remains professionally valid but too dense for a choice-list role
  - Unit 15 E1 and H3 remain too close in trilateral terminology / template-rationale territory

Interpretation:

- the earlier local repairs improved some prompt distinctness
- they did not sufficiently broaden the scenario family range
- Modules 2 and 4 remain the main content-level blockers under the revised learner-suitability standard

Required action:

- shorten and simplify the densest JPO options
- diversify Module 2 away from trilateral / counterpart-office coordination as the default JPO frame
- re-separate the within-unit JPO pairings in Unit 12 and Unit 15

---

### 6. Module 6 is not blocker-free: Unit 20 still has live structural issues

**Category:** Structural Profile Compliance / Formatting And Production Readiness  
**Criteria:** `4.0 Preliminary cross-check` / `5G.1 Activity-profile compliance` / `5L.1 Markdown and structural hygiene`  
**Result:** `Revise`

Evidence:

- `adv/edits & guides/aw-adv_n10_claude-fb_mod4-6_v2.md` flagged:
  - duplicated `B1` heading in Unit 20
  - possible missing `D3`
- live file check of `adv/md/n10/aw-adv_mod6_n10.md` confirms:
  - Unit 20 contains two consecutive `#### Compare the Versions (B1)` headings
  - no `#### Template-Guided Writing (D3)` is present in Unit 20

Interpretation:

- Round 2 understated Module 6 by treating it as broadly clear without carrying these specific structural defects into the operative record
- these are local structural issues, but they are real and should be fixed before sign-off

Required action:

- remove or consolidate the duplicate `B1` heading in Unit 20
- decide whether `D3` should be reinstated to match the profile or whether the profile should be updated to reflect the current design

---

### 7. Two older flagged issues do not stand as live blockers in the active file set

**Category:** Preliminary Cross-Check Calibration  
**Result:** `Pass` with withdrawals

Evidence:

- `adv/md/n10/aw-adv_mod6_n10.md`
  - Unit 21 currently states:
    - Part A `90-100` words
    - Part B `90-110` words
    - Part C `70-90` words
    - total `250-300` words
  - this is internally coherent in the active file
- the earlier Unit 19/20 Practice D duplication / placement problem does not appear as a live duplicated task in the current active file set; the visible `Practice D — Organise the Justification` instance is in Unit 20, where the profile says it belongs

Interpretation:

- these earlier flags are useful historical evidence, but they should not currently be carried as live blockers without fresher contradictory evidence

Required action:

- treat Unit 21 word-count inconsistency as not currently active in the live file
- treat the Unit 19 Practice D placement problem as not currently evidenced in the active file

---

### 8. Deferred items are now named clearly enough not to disappear

**Category:** Remaining Pinned-Item Checks / Deferred Items  
**Criteria:** `5M.2 Deferred pinned items`  
**Result:** `Pass`

Evidence:

- `P4` and `P7` remain explicitly tracked in the to-do list
- `Learning goals mapping` is explicitly recorded in `adv/edits & guides/aw-adv_project_todo_list.md` as 14 deferred recommendations
- the operative checklist now names the learning-goals mapping issue explicitly under deferred pinned items

Interpretation:

- this is no longer an implicit or easy-to-lose background note
- the deferred queue is now visible enough for later sign-off work

---

## Consolidated Round 3 Conclusion

The advanced book still does not pass `N11`, but the failure state is now more accurately defined than it was in Round 2.

What now looks secure:

- the checklist standard itself
- pedagogical explanation layer
- learner-support structure
- broad activity-type variety
- progression
- most pinned-item completion

What still blocks `N11` completion:

- unresolved H1/profile decision in Units 2, 3, 4, 6, and 11
- Module 1 structural cleanup:
  - duplicate F1 headings in Units 2 and 3
  - missing explicit H sub-labelling in Units 1-3
- Modules 2 and 4 JPO prompt simplification and de-clustering
- Unit 20 structural cleanup:
  - duplicated B1 heading
  - D3/profile mismatch check and resolution

What is withdrawn from the live blocker list:

- broad missing-H3 concern across Module 3
- Unit 21 word-count inconsistency as a current active-file defect
- Unit 19 Practice D placement problem as a current active-file defect

---

## Immediate Next Steps

1. Resolve the H1 decision for Units 2, 3, 4, 6, and 11.
2. Repair Module 1 structural labelling and duplicate F1 headings.
3. Simplify and diversify the remaining JPO prompts in Modules 2 and 4.
4. Repair Unit 20 structural defects and align the file/profile on D3.
5. Re-run only the affected `N11` items after those corrections are made.

---

*Working status: Round 3 complete. This is now the operative `N11` review record, replacing Round 2 as the best current summary of live blockers and withdrawals.*
