# N11 QA Review — Round 1
## *Administrative Writing, Advanced*

---

> **Purpose of this document**
> This file records the first working findings from `N11` after the checklist framework was drafted. It is not the final sign-off review. It captures the initial book-wide controls that could be verified quickly and reliably from the active `n10` files and related project documents.

---

## Overall Status

Does the advanced book pass `N11` at this stage? `No — review in progress`

Current position:

- the `N11` framework now exists
- several book-wide controls already pass
- some book-wide checks still need manual review across the active `n10` modules
- `P7` remains deferred as a distinct deliverable even though Unit 23 now contains a rubric-based self-edit table

---

## Findings

### 1. Structural baseline from earlier passes remains intact

**Category:** Structural Profile Compliance / Formatting And Production Readiness  
**Result:** `Pass`

Evidence:

- `python scripts/module_tool.py validate --path adv/md/revised_modules_n9/aw-adv_mod1_n9.md`
- `python scripts/module_tool.py validate --path adv/md/revised_modules_n9/aw-adv_mod6_n9.md`

Both sampled `N9` modules passed structural validation. This does not prove full `N10` book-wide compliance by itself, but it supports the inherited structural baseline.

---

### 2. `P2` data-interpretation tasks are present in the intended units

**Category:** Remaining Pinned-Item Checks  
**Result:** `Pass`

Evidence from active `n10` files:

- Unit 11: `adv/md/n10/aw-adv_mod3_n10.md` contains `#### Data Interpretation Input (B7)`
- Unit 13: `adv/md/n10/aw-adv_mod4_n10.md` contains `#### Data Interpretation Input (B7)`
- Unit 17: `adv/md/n10/aw-adv_mod5_n10.md` contains `#### Data Interpretation Input (B7)`
- Unit 21: `adv/md/n10/aw-adv_mod6_n10.md` contains `#### Data Interpretation Input (B7)`

This matches the project to-do record for `P2`.

---

### 3. `P6` reading-to-write tasks are present in the intended units

**Category:** Remaining Pinned-Item Checks  
**Result:** `Pass`

Evidence from active `n10` files:

- Unit 15: `adv/md/n10/aw-adv_mod4_n10.md` contains `#### Reading-to-Write Input (B6)`
- Unit 18: `adv/md/n10/aw-adv_mod5_n10.md` contains `#### Reading-to-Write Input (B6)`
- Unit 19: `adv/md/n10/aw-adv_mod6_n10.md` contains `#### Reading-to-Write Input (B6)`
- Unit 22: `adv/md/n10/aw-adv_mod6_n10.md` contains `#### Reading-to-Write Input (B6)`

This matches the project to-do record for `P6`.

---

### 4. Module 2 Section H ordering remains correct in the active files

**Category:** Consistency And Cohesion / Prompt And Task Design  
**Result:** `Pass`

Evidence:

- Unit 4 in `adv/md/n10/aw-adv_mod2_n10.md`: `H3`, then `H1`
- Unit 5 in `adv/md/n10/aw-adv_mod2_n10.md`: `H3`, then `H1`
- Unit 6 in `adv/md/n10/aw-adv_mod2_n10.md`: `H2`, then `H3`, then `H1`
- Unit 7 in `adv/md/n10/aw-adv_mod2_n10.md`: `H3`, then `H1`

The active file keeps the expected `H2 -> H3 -> H1` order where `H2` exists.

---

### 5. Portfolio-task word-count handling required manual confirmation and now passes

**Category:** Progression / Prompt And Task Design  
**Result:** `Pass`

Evidence:

- `python scripts/module_tool.py summary` did not surface an `E` word count for Unit 14 or Unit 22 because both use portfolio-style `E4` structures
- Manual inspection shows:
  - Unit 14 `E4` in `adv/md/n10/aw-adv_mod4_n10.md` clearly separates:
    - `Task 1 — Internal notice (80–100 words)`
    - `Task 2 — External notice (160–200 words)`
  - Unit 22 `E4` in `adv/md/n10/aw-adv_mod6_n10.md` clearly separates:
    - `Part A — Analysis (NOT SUBMITTED; approximately 60 words)`
    - `Part B — Full Administrative Document (approximately 200–240 words)`

Interpretation:

- the missing summary output is a tooling limitation, not a content failure
- the active files do state usable E-task lengths and calibrate the portfolio tasks clearly enough for learners

Follow-up:

- continue treating portfolio-style units as manual-review items in `N11`, because the summary script is not the authoritative check for them

---

### 6. `P7` is partially supported in Unit 23 but still not complete as a project deliverable

**Category:** Remaining Pinned-Item Checks / Answer-Key Supportability  
**Result:** `Deferred`

Evidence:

- Unit 23 in `adv/md/n10/aw-adv_mod6_n10.md` contains `#### Self-Editing Checklist — Rubric-Based (F3)` with a ten-criterion table and a three-point scale
- However, the to-do list still defines `P7` as a separate capstone assessment rubric needed for self-assessment **and teacher use**

Interpretation:

- the current capstone unit now contains a meaningful self-evaluation instrument
- this is not yet the same as a dedicated final rubric deliverable for teacher-facing assessment use

Required action:

- keep `P7` explicitly deferred and do not treat it as complete until the separate rubric requirement is satisfied

---

### 7. `P1` book-level structural variety still needs final confirmation

**Category:** Variety / Remaining Pinned-Item Checks  
**Result:** `Monitor`

Evidence:

- the to-do list already records that structural variety was built into the profiles and checked during `N9` and `N10`
- the final book-wide confirmation is still explicitly assigned to `N11`

Required action:

- run a deliberate whole-book pass on activity distribution, scenario repetition, and unit-to-unit structural rhythm before final `N11` sign-off

---

### 8. Unit 22 non-standard support structure is robust rather than problematic

**Category:** Learner Suitability / Self-Study Accessibility / Language And Learning  
**Result:** `Pass`

Evidence:

- Unit 22 includes a clear `B6` reading-to-write bridge, a worked integrated paragraph in `C5`, an explicit transfer reminder in `D6`, a fallback paragraph if learners do not have their Unit 18 writing, and a clear split between planning note and full document in `E4`

Interpretation:

- the unit’s non-standard portfolio structure is supported by visible scaffolding rather than simply assuming learners can perform integration unaided
- this is a strong example of `N10` support surviving into the active `N11` review stage

---

## Immediate Next Steps

1. Run a manual `N11` pass on portfolio-task units and other non-standard structures where summary tooling is insufficient.
2. Review unit-to-unit variety and progression across all six active `n10` module files.
3. Check whether `N10` explanations are sufficient in practice, not merely present.
4. Confirm book-level consistency and learner suitability across the active module set.

---

*Working status: Round 1 initial findings recorded. `N11` remains in progress.*
