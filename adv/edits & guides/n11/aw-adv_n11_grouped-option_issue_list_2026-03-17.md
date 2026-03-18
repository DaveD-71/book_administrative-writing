# N11 Grouped-Option Issue List - 2026-03-17
## Administrative Writing, Advanced

Purpose:

- record the grouped-option parallelism issues that remain relevant before `N11` can be signed off
- combine the earlier Round 1 / Round 2 / Round 3 findings with the broader live-file scan run on 2026-03-17
- separate issues that were already identified in earlier QA from additional current outliers found in the wider scan

Scope:

- live files under `adv/md/n10`
- grouped scenario sets in writing tasks, especially `E` and `H3`
- option parallelism, JPO-option calibration, prompt load, and within-set scenario fit

Important note:

- some historical Round 2 / Round 3 wording no longer matches the live option text exactly
- however, the same issue families remain relevant where the live file still shows over-specialisation, prompt-load inflation, weak option parallelism, or residual within-set sameness

---

## 1. Earlier QA Findings That Still Matter

| Historical item | Earlier QA reference | Earlier finding | Current status |
|---|---|---|---|
| H-01 | `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md:219-236` | Scenario and JPO-option variety still needed a tighter sameness check before final `N11` sign-off. | Still relevant. The broader 2026-03-17 scan confirms that grouped-option parallelism was not fully rechecked before `N11` was treated as complete. |
| H-02 | `adv/edits & guides/n11/aw-adv_n11_qa_review_round2.md:151-186` | Module 2 remained over-clustered around trilateral and counterpart-office coordination scenarios; some options were longer and more processing-heavy than the parallel non-JPO choices. | Still relevant. Multiple Module 2 choice sets still show residual parallelism and calibration issues. |
| H-03 | `adv/edits & guides/n11/aw-adv_n11_qa_review_round2.md:190-219` | Module 4 still contained JPO prompts that were too dense, too close to paired tasks, or too specialised relative to the non-JPO options. | Still relevant. Unit 12, Unit 13, and Unit 15 still need explicit re-evaluation. |
| H-04 | `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md:176-202` | Round 3 still treated Modules 2 and 4 as `Revise` for learner suitability, calibration, choice-list quality, and variety. | Still relevant. The later targeted recheck did not close these issues rigorously enough. |

---

## 2. Current Live Issue List

Legend:

- `Carried forward` = already identifiable in earlier `N11` review rounds and still not cleanly closed
- `Newly surfaced` = not stated with enough specificity in the earlier rounds but visible in the broader live-file scan

| ID | Status | Live location | Issue type | Current live evidence | Earlier QA reference | Recommended action | Priority |
|---|---|---|---|---|---|---|---|
| GO-01 | Carried forward | `adv/md/n10/aw-adv_mod2_n10.md` Unit 4 `E1` (`201-216`) | Weak option parallelism / under-specified JPO option | Options 1-3 clearly state both the problem and the downstream consequence. The JPO option only says two sections may contain conflicting guidance, which makes the task pressure less explicit and less parallel. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:176-202` | Tighten the JPO option so it names the consequence and required action as clearly as the other three options. | Should revise |
| GO-02 | Carried forward | `adv/md/n10/aw-adv_mod2_n10.md` Unit 4 `H3` (`259-274`) | JPO option remains more specialised and more loaded than peers | Options 1-3 are bounded administrative clarification tasks. The JPO option bundles processing stage, reply deadline, and further-materials uncertainty around an international filing. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:176-202` | Simplify the JPO option so it carries one main uncertainty family rather than three. | Should revise |
| GO-03 | Carried forward | `adv/md/n10/aw-adv_mod2_n10.md` Unit 5 `E1` (`465-482`) | Over-specialised JPO option | The JPO option shifts into EPO search-report citation classification. The other three options stay in document-consistency and deadline / attachment inconsistency territory. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:176-202` | Replace or simplify the JPO option so it remains in the same document-consistency skill frame as the other options. | Should revise |
| GO-04 | Carried forward | `adv/md/n10/aw-adv_mod2_n10.md` Unit 7 `E1` (`990-1005`) | Choice-list mismatch on dependency structure | Options 1-3 explicitly encode sequential dependency. The JPO option lists three requests, but the dependency logic is weaker and flatter. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:143-146` and `:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:194-202` | Recast the JPO option so each requested item clearly depends on the previous one. | Should revise |
| GO-05 | Carried forward | `adv/md/n10/aw-adv_mod2_n10.md` Unit 7 `H3` (`1048-1060`) | Choice-list mismatch on dependency structure | Same issue as `GO-04`: the first three options build clear staged dependency; the JPO option reads more like a standard multi-part clarification request. | Round 2 Module 2 block at `aw-adv_n11_qa_review_round2.md:143-146` and `:151-186`; Round 3 Module 2/4 block at `aw-adv_n11_qa_review_round3.md:194-202` | Rewrite the JPO option so the steps are genuinely sequential rather than merely grouped. | Should revise |
| GO-06 | Carried forward | `adv/md/n10/aw-adv_mod4_n10.md` Unit 12 pairing: `E3` (`214-229`) and `H3` (`283-298`) | Residual within-unit sameness | Both JPO options are still external-inquiry scenarios built around incomplete or unconfirmed updates from a counterpart office. The surface details differ, but the communicative pressure remains close. | Round 2 Unit 12 note at `aw-adv_n11_qa_review_round2.md:198-199`; Round 3 Unit 12 note at `aw-adv_n11_qa_review_round3.md:188` | Re-separate the pair more decisively so one option does not feel like a narrowed variant of the other. | Should revise |
| GO-07 | Carried forward | `adv/md/n10/aw-adv_mod4_n10.md` Unit 13 `H3` (`554-568`) | Prompt-load inflation | Options 1-3 are cleanly bounded implementation-risk scenarios. The JPO option adds checklist revision, training gaps, and a pending support tool in one compressed option. | Round 2 Unit 13 note at `aw-adv_n11_qa_review_round2.md:200-201`; Round 3 Unit 13 note at `aw-adv_n11_qa_review_round3.md:189` | Shorten the option and reduce it to one main operational risk frame. | Should revise |
| GO-08 | Carried forward | `adv/md/n10/aw-adv_mod4_n10.md` Unit 15 pairing: `E1` (`992-1007`) and `H3` (`1060-1075`) | Residual within-unit sameness / over-specialisation | Both JPO options are policy-aligned rationales for adopting shared coordination artefacts. The pair remains closer to itself than the non-JPO options are, and both are more specialised than the surrounding choices. | Round 2 Unit 15 note at `aw-adv_n11_qa_review_round2.md:202-219`; Round 3 Unit 15 note at `aw-adv_n11_qa_review_round3.md:190` | Broaden one of the two JPO options so the pair no longer sits in the same narrow rationale family. | Should revise |
| GO-09 | Newly surfaced | `adv/md/n10/aw-adv_mod6_n10.md` Unit 21 `E4` (`863-872`) | JPO option denser than peer options | Options 1-3 are short report-source descriptions. The JPO option adds more detail, more implied variability, and a fuller mini-brief than the other three. | Earlier broader variety warning at `aw-adv_n11_qa_review_round1.md:219-236`; Modules 1/3/5/6 were not specifically reopened in Round 2 | Trim the JPO option to the same descriptive load as the other three options. | Should revise |
| GO-10 | Newly surfaced | `adv/md/n10/aw-adv_mod6_n10.md` Unit 21 `H3` (`936-943`) | Mixed source-set logic / weaker within-set parallelism | Options 1-3 each define one clear input set. The JPO option mixes "multiple JPO teams or partner offices," making the source base less parallel than the other choices. | Earlier broader variety warning at `aw-adv_n11_qa_review_round1.md:219-236`; Modules 1/3/5/6 were not specifically reopened in Round 2 | Decide whether this option is about internal JPO teams or external partner offices, not both. | Should revise |

---

## 3. Follow-Up Recommendation

Before `N11` can be signed off, the next pass should:

1. work through `GO-01` to `GO-10` in the live `n10` files
2. recheck each edited choice set against:
   - `5B.1 Level appropriacy`
   - `5D.3 Calibration`
   - `5D.4 Choice-list quality`
   - `5E.3 Variety without chaos`
3. explicitly record, for each issue:
   - whether it was revised
   - what changed
   - why the revised option is now parallel to its peers
4. avoid broad closure language such as "Modules 2 and 4 are now sufficiently differentiated" unless every carried-forward issue has been rechecked at unit level

Current conclusion:

- this issue list is sufficient to block final `N11` sign-off
- `P7` may remain complete
- full review should not begin until these grouped-option issues have been addressed and rechecked

---

## 4. Start Here Tomorrow

Primary working files:

- live source files:
  - `adv/md/n10/aw-adv_mod2_n10.md`
  - `adv/md/n10/aw-adv_mod4_n10.md`
  - `adv/md/n10/aw-adv_mod6_n10.md`
- issue tracker for this pass:
  - `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
- operative QA record:
  - `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md`
- checklist to recheck against:
  - `adv/edits & guides/n11/aw-adv_n11_qa_checklist.md`

Historical reference files:

- `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md`
- `adv/edits & guides/n11/aw-adv_n11_qa_review_round2.md`

Most relevant checklist criteria:

- `5B.1 Level appropriacy`
- `5D.3 Calibration`
- `5D.4 Choice-list quality`
- `5E.3 Variety without chaos`

Definition of done for the next pass:

- each `GO-*` item in this file has been reviewed against the live source
- each affected option set has either been revised or explicitly retained with a stated reason
- the recheck note explains why the final option set is now parallel in:
  - scope
  - detail level
  - difficulty
  - professional framing
