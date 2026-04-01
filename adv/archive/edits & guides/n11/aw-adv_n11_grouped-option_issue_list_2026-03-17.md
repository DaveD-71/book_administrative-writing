# N11 Grouped-Option Issue List - 2026-03-17
## Administrative Writing, Advanced

Purpose:

- record the grouped-option parallelism issues that remain relevant before `N11` can be signed off
- combine the earlier Round 1 / Round 2 / Round 3 findings with the broader live-file scan run on 2026-03-17
- separate issues that were already identified in earlier QA from additional current outliers found in the wider scan

Scope:

- live files under `adv/md/final/modules`
- grouped scenario sets in writing tasks, especially `E` and `H3`
- option parallelism, JPO-option calibration, prompt load, and within-set scenario fit

Important note:

- some historical Round 2 / Round 3 wording no longer matches the live option text exactly
- however, the same issue families remain relevant where the live file still shows over-specialisation, prompt-load inflation, weak option parallelism, or residual within-set sameness

---

## 1. Earlier QA Findings That Still Matter

| Historical item | Earlier QA reference | Earlier finding | Current status |
|---|---|---|---|
| H-01 | `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round1.md:219-236` | Scenario and JPO-option variety still needed a tighter sameness check before final `N11` sign-off. | Still relevant. The broader 2026-03-17 scan confirms that grouped-option parallelism was not fully rechecked before `N11` was treated as complete. |
| H-02 | `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round2.md:151-186` | Module 2 remained over-clustered around trilateral and counterpart-office coordination scenarios; some options were longer and more processing-heavy than the parallel non-JPO choices. | Still relevant. Multiple Module 2 choice sets still show residual parallelism and calibration issues. |
| H-03 | `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round2.md:190-219` | Module 4 still contained JPO prompts that were too dense, too close to paired tasks, or too specialised relative to the non-JPO options. | Still relevant. Unit 12, Unit 13, and Unit 15 still need explicit re-evaluation. |
| H-04 | `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round3.md:176-202` | Round 3 still treated Modules 2 and 4 as `Revise` for learner suitability, calibration, choice-list quality, and variety. | Still relevant. The later targeted recheck did not close these issues rigorously enough. |

---

## 2. Current Live Issue List

Legend:

- `Carried forward` = already identifiable in earlier `N11` review rounds and still not cleanly closed
- `Newly surfaced` = not stated with enough specificity in the earlier rounds but visible in the broader live-file scan

| ID | Status | Live location | Issue type | Current live evidence | Earlier QA reference | Recommended action | Priority |
|---|---|---|---|---|---|---|---|
| GO-01 | Carried forward | `adv/md/final/modules/aw-adv_mod2_n10.md` Unit 4 `E1` (`201-216`) | Weak option parallelism / under-specified JPO option | Options 1-3 clearly state both the problem and the downstream consequence. The JPO option only says two sections may contain conflicting guidance, which makes the task pressure less explicit and less parallel. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:176-202` | Tighten the JPO option so it names the consequence and required action as clearly as the other three options. | Should revise |
| GO-02 | Carried forward | `adv/md/final/modules/aw-adv_mod2_n10.md` Unit 4 `H3` (`259-274`) | JPO option remains more specialised and more loaded than peers | Options 1-3 are bounded administrative clarification tasks. The JPO option bundles processing stage, reply deadline, and further-materials uncertainty around an international filing. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:176-202` | Simplify the JPO option so it carries one main uncertainty family rather than three. | Should revise |
| GO-03 | Carried forward | `adv/md/final/modules/aw-adv_mod2_n10.md` Unit 5 freer-writing task (`465-482`; later corrected from `E1` to `E3`) | Over-specialised JPO option | The JPO option shifts into EPO search-report citation classification. The other three options stay in document-consistency and deadline / attachment inconsistency territory. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:176-202` | Replace or simplify the JPO option so it remains in the same document-consistency skill frame as the other options. | Should revise |
| GO-04 | Carried forward | `adv/md/final/modules/aw-adv_mod2_n10.md` Unit 7 `E1` (`990-1005`) | Choice-list mismatch on dependency structure | Options 1-3 explicitly encode sequential dependency. The JPO option lists three requests, but the dependency logic is weaker and flatter. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:143-146` and `:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:194-202` | Recast the JPO option so each requested item clearly depends on the previous one. | Should revise |
| GO-05 | Carried forward | `adv/md/final/modules/aw-adv_mod2_n10.md` Unit 7 `H3` (`1048-1060`) | Choice-list mismatch on dependency structure | Same issue as `GO-04`: the first three options build clear staged dependency; the JPO option reads more like a standard multi-part clarification request. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:143-146` and `:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:194-202` | Rewrite the JPO option so the steps are genuinely sequential rather than merely grouped. | Should revise |
| GO-06 | Carried forward | `adv/md/final/modules/aw-adv_mod4_n10.md` Unit 12 pairing: `E3` (`214-229`) and `H3` (`283-298`) | Residual within-unit sameness | Both JPO options are still external-inquiry scenarios built around incomplete or unconfirmed updates from a counterpart office. The surface details differ, but the communicative pressure remains close. | Round 2 Unit 12 note at `aw-adv_n11_qa_review_round2.md:198-199`; Round 3 Unit 12 note at `aw-adv_n11_qa_review_round3.md:188` | Re-separate the pair more decisively so one option does not feel like a narrowed variant of the other. | Should revise |
| GO-07 | Carried forward | `adv/md/final/modules/aw-adv_mod4_n10.md` Unit 13 `H3` (`554-568`) | Prompt-load inflation | Options 1-3 are cleanly bounded implementation-risk scenarios. The JPO option adds checklist revision, training gaps, and a pending support tool in one compressed option. | Round 2 Unit 13 note at `aw-adv_n11_qa_review_round2.md:200-201`; Round 3 Unit 13 note at `aw-adv_n11_qa_review_round3.md:189` | Shorten the option and reduce it to one main operational risk frame. | Should revise |
| GO-08 | Carried forward | `adv/md/final/modules/aw-adv_mod4_n10.md` Unit 15 pairing: `E1` (`992-1007`) and `H3` (`1060-1075`) | Residual within-unit sameness / over-specialisation | Both JPO options are policy-aligned rationales for adopting shared coordination artefacts. The pair remains closer to itself than the non-JPO options are, and both are more specialised than the surrounding choices. | Round 2 Unit 15 note at `aw-adv_n11_qa_review_round2.md:202-219`; Round 3 Unit 15 note at `aw-adv_n11_qa_review_round3.md:190` | Broaden one of the two JPO options so the pair no longer sits in the same narrow rationale family. | Should revise |
| GO-09 | Newly surfaced | `adv/md/final/modules/aw-adv_mod6_n10.md` Unit 21 `E4` (`863-872`) | JPO option denser than peer options | Options 1-3 are short report-source descriptions. The JPO option adds more detail, more implied variability, and a fuller mini-brief than the other three. | Earlier broader variety warning at `aw-adv_n11_qa_review_round1.md:219-236`; Modules 1/3/5/6 were not specifically reopened in Round 2 | Trim the JPO option to the same descriptive load as the other three options. | Should revise |
| GO-10 | Newly surfaced | `adv/md/final/modules/aw-adv_mod6_n10.md` Unit 21 `H3` (`936-943`) | Mixed source-set logic / weaker within-set parallelism | Options 1-3 each define one clear input set. The JPO option mixes "multiple JPO teams or partner offices," making the source base less parallel than the other choices. | Earlier broader variety warning at `aw-adv_n11_qa_review_round1.md:219-236`; Modules 1/3/5/6 were not specifically reopened in Round 2 | Decide whether this option is about internal JPO teams or external partner offices, not both. | Should revise |

---

## 3. 2026-03-18 Source-Edit Pass

The live `n10` files have now been revised for the known grouped-option issue set.

| ID | Live action taken on 2026-03-18 | Recheck status |
|---|---|---|
| GO-01 | JPO option tightened so the consequence and required follow-up action are explicit. | Recheck against `5D.4` and `5D.3` still required |
| GO-02 | JPO option simplified to one main uncertainty family: whether further materials are needed before the next stage. | Recheck against `5B.1` and `5D.4` still required |
| GO-03 | JPO option replaced with a document-consistency scenario involving a date mismatch and a missing attachment. | Recheck against `5D.4` and `5E.3` still required |
| GO-04 | JPO option rewritten so the requests now follow a clearer step-by-step dependency chain. | Recheck against `5D.3` still required |
| GO-05 | JPO option rewritten so the actions now proceed in a genuinely sequential order. | Recheck against `5D.3` still required |
| GO-06 | Unit 12 `E3` JPO option separated more clearly from `H3` by shifting it toward file-status confirmation rather than agenda logistics. | Pair-level recheck against `5D.4` and `5E.3` still required |
| GO-07 | Unit 13 `H3` JPO option reduced to one main operational-risk frame. | Recheck against `5B.1` and `5D.3` still required |
| GO-08 | Unit 15 `H3` JPO option broadened from a narrow shared artefact rationale to a wider progress-reporting rationale. | Pair-level recheck against `5D.4` and `5E.3` still required |
| GO-09 | Unit 21 `E4` JPO option trimmed to the same descriptive load as the peer options. | Recheck against `5D.4` still required |
| GO-10 | Unit 21 `H3` JPO option narrowed to a single source-set logic (`JPO teams` only). | Recheck against `5D.4` still required |

Current status after the source-edit pass:

- all `GO-01` to `GO-10` items have now been revised in the live source files
- the issue list still blocks final `N11` sign-off until the revised sets are explicitly rechecked against the operative criteria

---

## 4. 2026-03-18 Explicit Recheck Result

The revised grouped-option set has now been rechecked against:

- `5B.1 Level appropriacy`
- `5D.3 Calibration`
- `5D.4 Choice-list quality`
- `5E.3 Variety without chaos`

Result:

- the known `GO-01` to `GO-10` issue set is now clear at the unit level
- the revised JPO options now function as peer options rather than as over-specialised or over-expanded special cases
- the carried-forward Module 2 and Module 4 problems no longer remain active blockers in their previously flagged locations

Item-by-item recheck note:

| ID | Recheck result | Why this is now clear |
|---|---|---|
| GO-01 | Clear | The JPO option now states both the consequence and the required follow-up action, making it parallel in task pressure and detail level with the other three options. |
| GO-02 | Clear | The JPO option has been reduced to one main uncertainty family, which brings it back into line with the bounded administrative clarification frame used by the peer options. |
| GO-03 | Clear | The JPO option now uses the same document-consistency / missing-information skill frame as the other choices and no longer depends on specialist citation knowledge. |
| GO-04 | Clear | The JPO option now encodes an explicit step-by-step dependency chain rather than a flat grouped request list. |
| GO-05 | Clear | The JPO option now builds genuine sequence and dependency, matching the structural demand of the other options in the set. |
| GO-06 | Clear | The Unit 12 JPO pair is now more clearly separated: `E3` is a file-status / comment-reflection inquiry, while `H3` is an agenda-status inquiry with different communicative pressure. |
| GO-07 | Clear | The Unit 13 `H3` JPO option now centres on one implementation risk rather than compressing multiple operational variables into a single option. |
| GO-08 | Clear | The Unit 15 JPO pair no longer sits in the same narrow rationale family: `E1` remains terminology-framework adoption, while `H3` now addresses progress-reporting coordination. |
| GO-09 | Clear | The Unit 21 `E4` JPO option now matches the short descriptive load of the peer report-source options. |
| GO-10 | Clear | The Unit 21 `H3` JPO option now uses one clear source-set logic (`JPO teams`), making it parallel with the other source-defined options. |

Current conclusion after the explicit recheck:

- the grouped-option issue list no longer blocks `N11` at the known-item level
- `N11` still remains open because a full-book recheck across all six `n10` modules has not yet been completed
- the next stage is the broader book-level recheck, not full review

---

## 5. 2026-03-18 Broader Book-Level Recheck Result

The broader recheck has now been run across all six live `adv/md/final/modules/aw-adv_mod*_n10.md` files.

Book-level recheck result:

- no additional active blockers remain outside the revised `GO-01` to `GO-10` set
- two further book-level outliers were identified during the wider scan and tightened during the same pass:
  - `adv/md/final/modules/aw-adv_mod2_n10.md` Unit 6 `E1`
  - `adv/md/final/modules/aw-adv_mod4_n10.md` Unit 13 `E1`
- the remaining reviewed JPO option sets in Modules 3 and 5 were retained as acceptable and do not currently block `N11`

Current conclusion:

- the grouped-option / JPO-calibration issue family is now clear at book level
- this issue list is now historical QA support rather than an active blocker file
- `N11` can now be closed at the QA-record level, subject to the main project records being updated accordingly

---

## 6. Historical Working References

Primary working files:

- live source files:
  - `adv/md/final/modules/aw-adv_mod2_n10.md`
  - `adv/md/final/modules/aw-adv_mod4_n10.md`
  - `adv/md/final/modules/aw-adv_mod6_n10.md`
- issue tracker for this pass:
  - `adv/archive/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
- operative QA record:
  - `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round3.md`
- checklist to recheck against:
  - `adv/archive/edits & guides/n11/aw-adv_n11_qa_checklist.md`

Historical reference files:

- `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round1.md`
- `adv/archive/edits & guides/n11/aw-adv_n11_qa_review_round2.md`

Most relevant checklist criteria:

- `5B.1 Level appropriacy`
- `5D.3 Calibration`
- `5D.4 Choice-list quality`
- `5E.3 Variety without chaos`

Definition of done for the broader recheck:

- all six live `n10` module files were checked against the operative criteria
- any remaining outliers beyond `GO-01` to `GO-10` were either revised or explicitly retained with a stated reason
- the final `N11` note now records that the book clears the grouped-option, calibration, and scenario-variety criteria at full-book level
