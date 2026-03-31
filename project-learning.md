# Project Learning

Durable project memory for the active repository root.

Historical note:

- older entries may contain absolute paths from earlier machines or clone locations
- treat those path values as historical snapshots unless an entry explicitly states it is defining the current workspace root

## Entries

### 2026-03-15T00:46:14.1210166+09:00 - Project Scope And Deliverables

- Status: `monitor`
- Scope: project/scope
- Context: repository content audit
- Observation: the repository contains two textbook tracks prepared for the 2026 Japan Patent Office administrative writing proposal: an advanced book under `adv` and an intermediate book under `int`; `about.txt` says the text exists primarily in Markdown and only the first unit of each book has been formatted in Word
- Preferred behavior: treat the repo as a dual-book content workspace with Markdown as the primary working format and Word formatting as a downstream task


### 2026-03-15T00:46:14.1210166+09:00 - Advanced Track Is The Mature Active Workstream

- Status: `monitor`
- Scope: project/state
- Context: advanced planning and status audit
- Observation: `adv/edits & guides/planning/guide-set/aw-adv_project_todo_list.md` shows N1-N10 complete, N11 not started, and identifies book-wide QA as the next major workstream; the active edited content set is the six `adv/md/n10/aw-adv_mod*_n10.md` files
- Preferred behavior: treat the advanced N10 module set and the N11 QA step as the current highest-maturity content baseline for project planning and review work


### 2026-03-15T00:46:14.1210166+09:00 - Advanced Planning Source Of Truth

- Status: `monitor`
- Scope: project/conventions
- Context: advanced documentation hierarchy
- Observation: `adv/edits & guides/planning/guide-set/aw-adv_unit_structural_profiles_revised.md` identifies itself as the planning source of truth, and the advanced to-do list treats it and the N10 module files as the authoritative references for editing and QA
- Preferred behavior: when working on advanced content, use the revised structural profiles, the advanced to-do list, and the N10 module files ahead of older context summaries


### 2026-03-15T00:46:14.1210166+09:00 - Advanced Context Document Is Historically Useful But Stale

- Status: `monitor`
- Scope: project/conventions
- Context: comparison of advanced status documents
- Observation: `adv/edits & guides/planning/supporting/aw-adv_project_context.md` still describes the project as being in structural planning and lists pre-N9 next steps, which no longer matches the current N10-complete state in `adv/edits & guides/planning/guide-set/aw-adv_project_todo_list.md`
- Preferred behavior: treat `adv/edits & guides/planning/supporting/aw-adv_project_context.md` as historical background only unless it is refreshed; do not use it as the primary status source for current advanced work


### 2026-03-15T00:46:14.1210166+09:00 - Intermediate Track Appears Earlier-Stage Than Advanced

- Status: `monitor`
- Scope: project/state
- Context: intermediate content audit
- Observation: the intermediate track contains `int/aw-int-all.md`, `int/int_writing_text_intro.md`, and 23 split unit files under `int/md`; the introduction presents an A2-B1+ book and the combined file is about 14,978 words, which is materially lighter than the advanced N10 set
- Preferred behavior: assume the intermediate book is a substantial draft set but not yet pushed through the same editorial pass structure or QA framework as the advanced track unless newer intermediate planning documents are added


### 2026-03-15T00:46:14.1210166+09:00 - Local Module Tool Supports Editorial Pass Work

- Status: `monitor`
- Scope: project/tooling
- Context: scripts audit
- Observation: `scripts/module_tool.py` is the repo-local utility for scaffolding new module files, scaffolding pass-to-pass copies, validating N9 structural conventions, summarising module structure, and making exact-match content edits
- Preferred behavior: prefer `scripts/module_tool.py` when doing repetitive module-pass operations or literal Markdown edits related to advanced module workflow


### 2026-03-15T00:59:14.7432774+09:00 - Advanced N11 QA Framework Started

- Status: `monitor`
- Scope: project/state
- Context: advanced quality-assurance stage
- Observation: `N11` has now started; the book-wide QA checklist framework was drafted at `adv/edits & guides/planning/guide-set/aw-adv_n11_qa_checklist.md` and the advanced to-do list now marks `N11` as in progress
- Preferred behavior: use the new `N11` checklist as the authoritative QA framework for the next advanced review pass, rather than relying on the older `N9` QA controls


### 2026-03-15T01:07:00+09:00 - Advanced N11 Round 1 Findings Recorded

- Status: `monitor`
- Scope: project/state
- Context: initial `N11` execution
- Observation: a first `N11` review note now exists at `adv/edits & guides/n11/aw-adv_n11_qa_review_round1.md`; early evidence confirms `P2`, `P6`, and Module 2 Section H ordering in the active `n10` files, while portfolio-task E-word-count handling and final book-level structural-variety confirmation remain active QA items
- Preferred behavior: continue `N11` from the recorded Round 1 findings rather than restarting book-wide checks from scratch


### 2026-03-15T01:12:00+09:00 - Portfolio-Task Units Cleared In N11 Manual Pass

- Status: `monitor`
- Scope: project/state
- Context: follow-up `N11` review on non-standard structures
- Observation: manual review confirmed that Units 14 and 22 state clear `E4` portfolio-task lengths and that Unit 22's non-standard integrated-writing structure is well supported; the earlier uncertainty came from summary-tool limitations rather than from an actual content failure
- Preferred behavior: treat portfolio-task units as manual-review cases in future QA rather than relying on automated summary output alone


### 2026-03-15T01:18:00+09:00 - N10 Support Layer And Structural Variety Confirmed At Book Level

- Status: `monitor`
- Scope: project/state
- Context: broader `N11` review
- Observation: the active `n10` module files now visibly contain a strong spread of explicit teaching markers and a wide activity-type range beyond the original baseline pattern; the remaining open book-level risk is not structural monotony but residual scenario/JPO-option overlap in some interoffice coordination contexts
- Preferred behavior: continue `N11` with a targeted sameness review on scenario families and JPO-option differentiation rather than re-checking whether structural variety exists at all


### 2026-03-15T15:16:24.7226107+09:00 - Key JPO Option Overlaps Repaired In Active N10 Files

- Status: `monitor`
- Scope: project/state
- Context: targeted `N11` sameness pass
- Observation: four genuine JPO homework-option overlaps were confirmed and repaired in Units 4, 6, 13, and 15 of the active `n10` files; the revised prompts now remain skill-parallel while using more distinct professional contexts
- Preferred behavior: treat the remaining sameness risk as a lighter book-level monitoring task rather than as a known unresolved defect in those four units


### 2026-03-15T19:32:00+09:00 - N11 Now Explicitly Tests Prompt Readability And Scenario-Family Distribution

- Status: `monitor`
- Scope: project/conventions
- Context: checklist tightening during `N11`
- Observation: `adv/edits & guides/planning/guide-set/aw-adv_n11_qa_checklist.md` now explicitly tests whether prompt wording remains readable for B1+/B2 aspirational learners, whether revised prompts drift upward in linguistic sophistication or processing load, and whether scenario families are distributed broadly enough across the book; each new check is tied to named source documents
- Preferred behavior: treat learner-level prompt readability and book-level scenario-family spread as explicit `N11` sign-off criteria, not as optional style preferences


### 2026-03-15T19:32:00+09:00 - Modules 2 And 4 Still Carry A Narrow JPO Scenario Band

- Status: `workaround`
- Scope: project/state
- Context: `N11` Round 2 focused pass
- Observation: even after the earlier overlap repairs, some active JPO prompts in Modules 2 and 4 remain too dense and too clustered around trilateral or counterpart-office coordination, especially in Units 4, 6, 13, and 15
- Preferred behavior: before treating those modules as clear under `N11`, run one more targeted prompt pass that shortens the affected JPO options and broadens their professional context range


### 2026-03-15T19:32:00+09:00 - Full N11 Round 2 Pass Reframed The Remaining Blockers

- Status: `monitor`
- Scope: project/state
- Context: full-book pass against the revised `N11` checklist
- Observation: the full Round 2 pass confirmed that the main live blockers are now limited to two areas: structural / activity-labelling inconsistency in Modules 1 and 3, and over-dense / over-clustered JPO scenario families in Modules 2 and 4; Modules 5 and 6 are broadly clear under the revised QA standard
- Preferred behavior: treat `adv/edits & guides/n11/aw-adv_n11_qa_review_round2.md` as the operative N11 record and use it to drive the next correction pass, rather than relying on the earlier partial Round 1 / selective Round 2 notes


### 2026-03-15T20:05:00+09:00 - Round 3 Replaces Round 2 As The Operative N11 Record

- Status: `monitor`
- Scope: project/state
- Context: external checklist verification and Round 3 QA pass
- Observation: `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md` is now the operative `N11` record. It corrects two Round 2 distortions: Module 3 was overstated as a wider structural blocker, and Module 6 was understated because Unit 20 structural defects were not carried into the operative summary. The live blocker set is now: H1/profile decision in Units 2, 3, 4, 6, and 11; Module 1 structural cleanup; Modules 2 and 4 JPO prompt simplification and de-clustering; and Unit 20 structural cleanup.
- Preferred behavior: use Round 3, not Round 2, as the current sign-off baseline for `N11`, and treat earlier round files as historical supporting records


### 2026-03-15T20:05:00+09:00 - Claude v2 Checklist Upgrades Are Now Part Of The Main N11 Standard

- Status: `monitor`
- Scope: project/conventions
- Context: checklist verification against external feedback
- Observation: `adv/edits & guides/planning/guide-set/aw-adv_n11_qa_checklist.md` now includes the stronger v2 controls validated through Claude feedback: preliminary cross-check against earlier review files, explicit H1 structural compliance, explicit word-count progression, activity-heading / sub-labelling checks, requirement sources for workplace relevance, and named deferral of the learning-goals mapping issues
- Preferred behavior: treat the main `adv/edits & guides/planning/guide-set/aw-adv_n11_qa_checklist.md` file as the single operative checklist and do not rely on the looser earlier Round 2 standard


### 2026-03-16T02:05:00+09:00 - Round 3 Source Fixes Preserve The Existing Section-H House Standard

- Status: `monitor`
- Scope: project/conventions
- Context: implementation of the Round 3 correction set
- Observation: the H1 decision was applied to the affected units, but the implementation deliberately preserved the repo's established Section H order (`H2 -> H3 -> H1` where relevant) rather than importing the alternate ordering proposed in Claude's Step 19 note; Module 1 structural cleanup, Module 2/4 JPO prompt diversification, and Unit 20 structural cleanup were applied in the same correction pass
- Preferred behavior: treat the repo's existing H-ordering convention as authoritative unless a future project decision explicitly replaces it


### 2026-03-16T09:28:49.3778502+09:00 - H1 Is Now A Book-Wide Feature In The Active Advanced Baseline

- Status: `monitor`
- Scope: project/decision
- Context: post-Round-3 follow-through on the accepted H1 policy
- Observation: the active advanced baseline now treats H1 Extension Task as a consistent book-wide feature, including Unit 18 and Units 20-23, while preserving the established Section H order (`H2 -> H3 -> H1` where H2 is present, otherwise `H3 -> H1`)
- Preferred behavior: future QA and editing passes should assess H1 as a book-wide requirement and should not treat the old six-unit mismatch set as the governing scope any longer


### 2026-03-15T00:34:37.9048369+09:00 - Repository Root And Sync Baseline

- Status: `monitor`
- Scope: project/state
- Context: initial scaffold seeding
- Observation: repository root is `C:\Dev\Code\book_administrative-writing`; branch state was `main...origin/main`; `git fetch --dry-run origin` showed no pending remote update at setup time
- Preferred behavior: check repo sync status before substantive work that depends on project instructions or recent remote changes


### 2026-03-15T00:34:37.9048369+09:00 - Initial Visible Repo Structure

- Status: `monitor`
- Scope: project/context
- Context: initial scaffold seeding
- Observation: top-level visible entries included `.vscode`, `adv`, `int`, `scripts`, `about.txt`, `ai_prompt.txt`, `aw-master_activity_menu.md`, and `image_translation_en.txt`
- Preferred behavior: treat `adv`, `int`, and `scripts` as the main high-level areas until more specific project structure decisions are recorded


### 2026-03-17T19:48:30.4465385+09:00 - P7 Now Uses A Dual-Use Unit 23 Rubric Pair

- Status: `monitor`
- Scope: project/decision
- Context: completion of the remaining pre-full-review content item for the advanced book
- Observation: `P7` is now implemented as a dual-use rubric pair for Unit 23: a learner-facing self-assessment rubric embedded in the live `adv/md/n10/aw-adv_mod6_n10.md` file and a companion rubric at `adv/md/n10/aw-adv_unit23_capstone_rubric.md`, both aligned to the same eight analytic criteria and using the same three performance bands (`Strong`, `Developing`, `Needs work`)
- Preferred behavior: treat the teacher rubric as the authoritative marking reference, keep the learner rubric aligned to the same criterion architecture, and begin the advanced full review from this completed `P7` baseline rather than treating the Unit 23 self-edit table alone as sufficient


### 2026-03-17T21:20:00+09:00 - N11 Needs A Dedicated Grouped-Option Parallelism Pass Before Sign-Off

- Status: `monitor`
- Scope: project/state
- Context: broader post-`P7` audit of the live advanced `n10` files before entering full review
- Observation: the earlier `N11` targeted recheck was too narrow to close the prompt-calibration and choice-list-quality criteria fully. The new issue list at `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md` carries forward unresolved Round 2 / Round 3 grouped-option findings and adds new live-file outliers in Module 6.
- Preferred behavior: do not treat `N11` as complete until the grouped-option issue list has been worked through and the affected choice sets have been rechecked explicitly against level appropriacy, calibration, choice-list quality, and variety


### 2026-03-17T21:35:00+09:00 - Reopened N11 Files Now Define The Next Restart Point Explicitly

- Status: `monitor`
- Scope: project/workflow
- Context: end-of-day handoff preparation after reopening the grouped-option portion of `N11`
- Observation: the live restart path is now explicitly defined in `adv/edits & guides/planning/guide-set/aw-adv_project_todo_list.md`, `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md`, and `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md`
- Preferred behavior: when work resumes, start from the grouped-option issue list, edit the live `adv/md/n10` files, and use the Round 3 note plus the main `N11` checklist as the recheck reference set


### 2026-03-18T00:00:00+09:00 - Advanced Edit Guides Now Use Functional Subfolders

- Status: `monitor`
- Scope: project/structure
- Context: repo cleanup before resuming the reopened `N11` pass
- Observation: `adv/edits & guides` is now organized into `planning`, `n10`, `n11`, `steps`, and `references` subfolders, and internal repo references have been updated to the new locations
- Preferred behavior: place new advanced planning docs in `adv/edits & guides/planning`, `N10` framework or feedback docs in `adv/edits & guides/n10`, `N11` QA and review docs in `adv/edits & guides/n11`, step-by-step working notes in `adv/edits & guides/steps`, and excerpt/reference material in `adv/edits & guides/references`


### 2026-03-18T00:55:00+09:00 - N11 Is Now Clear And The Next Stage Is Full Review

- Status: `monitor`
- Scope: project/state
- Context: completion of the reopened grouped-option / JPO-calibration QA work
- Observation: the known `GO-01` to `GO-10` issue set was revised and explicitly rechecked, two additional book-level outliers were tightened during the broader six-module scan, and the book now clears the relevant `N11` criteria for level appropriacy, calibration, choice-list quality, and variety
- Preferred behavior: treat `adv/edits & guides/n11/aw-adv_n11_qa_review_round3.md` as the final operative `N11` record, keep `adv/edits & guides/n11/aw-adv_n11_grouped-option_issue_list_2026-03-17.md` as historical QA support, and move next to full review rather than reopening `N11` unless new evidence appears


### 2026-03-18T02:05:00+09:00 - Round 4 Replaced Round 3 As The Authoritative N11 Record

- Status: `monitor`
- Scope: project/state
- Context: clean-sheet Round 4 full-book QA pass after the earlier Round 1 -> Round 3 scope drift was explicitly identified
- Observation: Round 4 did not inherit sign-off from the earlier review files. It re-ran the full `N11` checklist across all six live `adv/md/n10` module files, found one remaining cross-module formatting/structural-consistency family in the active files, corrected it in the same pass, and then cleared the book through the final sign-off gate. The authoritative record is now `adv/edits & guides/n11/aw-adv_n11_qa_review_round4.md`.
- Preferred behavior: treat Round 4 as the final `N11` control document, keep Round 1 to Round 3 plus the grouped-option issue list as historical support only, and begin the next stage from the Round 4 verdict rather than from earlier closure language


### 2026-03-18T18:04:43+09:00 - Intermediate Book Now Has A Saved Development Plan Baseline

- Status: `monitor`
- Scope: project/decision
- Context: preparation for repeating the advanced-book development process on the intermediate draft set
- Observation: the original saved intermediate development plan now lives at `int/edits & guides/planning/supporting/aw-int_development_plan.md`, while the authoritative intermediate control layer now lives in `int/edits & guides/planning/guide-set`. The governing model remains a rigorous adaptation of the advanced workflow rather than a one-to-one clone: keep the simpler intermediate identity, use limited JPO contextualization, treat `int/md` plus the intro as the live source set, and build planning, language-instruction, QA, and full-review layers before major content rewriting.
- Preferred behavior: use the supporting development plan as historical setup context only, and use the intermediate guide-set documents as the current planning source of truth for future execution


### 2026-03-22T18:04:57.9320799+09:00 - E3 Role Definition Standard Is Now Encoded In Series Source Documents

- Status: `monitor`
- Scope: project/decision
- Context: follow-through after the advanced-book E3 role-clarity corrections
- Observation: the series source-of-truth documents now encode an explicit E3 role-definition standard in `adv/edits & guides/planning/guide-set/aw-master_activity_menu.md` and `adv/edits & guides/planning/guide-set/aw-adv_prompt-writing-policy.md`. The standard requires E3 roles to be written as functional descriptions of what the writer does, who they write to, and why they are the appropriate writer, rather than as unexplained job titles.
- Preferred behavior: when drafting, revising, or QA-checking any E3 task in this repo, evaluate role wording against the encoded functional-description standard rather than relying on local prompt fixes or memory alone


### 2026-03-22T18:16:20.9526981+09:00 - Full Review Has Now Started On The Advanced N10 Baseline

- Status: `monitor`
- Scope: project/state
- Context: first post-`N11` editorial review pass on the completed advanced book
- Observation: the advanced full review has now started, with the first findings recorded at `adv/edits & guides/full-review/aw-adv_full-review_round1.md`. Round 1 did not reopen `N11`, but it did surface three follow-up points: a Unit 23 planning/live mismatch around the capstone rubric description, a Unit 18 usability gap in the `B6 -> D2` revision chain, and a Unit 12 output-length calibration question.
- Preferred behavior: treat the new `full-review` folder as the active location for post-`N11` editorial review findings, work through the Round 1 cleanup items there, and keep `P4` deferred until the full-review findings are resolved or explicitly accepted


### 2026-03-22T18:16:20.9526981+09:00 - Full Review Protocol Now Defines The Post-N11 Editorial Stage

- Status: `monitor`
- Scope: project/conventions
- Context: formalizing the full-review stage after its first findings round
- Observation: `adv/edits & guides/planning/guide-set/aw-adv_full-review_protocol.md` now defines the full-review stage as a post-`N11` whole-book editorial pass on the live `adv/md/n10` baseline, distinct from QA reruns and distinct from drafting. It also defines the source hierarchy, finding types, severity labels, recording rules, and done criteria for moving on to `P4`.
- Preferred behavior: use the new full-review protocol as the source-of-truth definition for this stage, record each review pass in the `full-review` folder, and update the project control files whenever full review materially changes state


### 2026-03-22T18:16:20.9526981+09:00 - Master Activity Menu Now Lives Under Planning

- Status: `monitor`
- Scope: project/structure
- Context: repo organization change during the new full-review stage
- Observation: the active Master Activity Menu file has been moved from the repo root to `adv/edits & guides/planning/guide-set/aw-master_activity_menu.md`. The planning area now separates into a current `guide-set` subfolder for authoritative planning/control documents and a `supporting` subfolder for background material that should not drive current project-state decisions.
- Preferred behavior: use the planning-path copy as the authoritative activity-menu reference in current project work, and update active control documents to reference the planning location rather than the old repo-root path


### 2026-03-22T18:16:20.9526981+09:00 - Planning Guide Set Now Defines The Current Development Reference Bundle

- Status: `monitor`
- Scope: project/conventions
- Context: planning-folder consolidation after the start of full review
- Observation: `adv/edits & guides/planning/guide-set/aw-adv_development_guide.md` now defines the authoritative current planning-and-cross-check bundle for advanced-book work. The guide set contains the to-do list, activity menu, prompt-writing policy, structural profiles, `N11` checklist, and full-review protocol; `planning/supporting` now holds background documents that are informative but not authoritative.
- Preferred behavior: start future development and cross-checking from `adv/edits & guides/planning/guide-set/aw-adv_development_guide.md`, and treat files outside the guide set as supporting or historical unless a guide-set document explicitly points to them


### 2026-03-22T19:05:00+09:00 - Advanced Planning System Is Transfer-Shaped But Not Template-Equivalent

- Status: `monitor`
- Scope: project/conventions
- Context: audit of the planning-folder consolidation for reuse in the intermediate track
- Observation: `adv/edits & guides/planning/guide-set/aw-adv_transfer-readiness_audit.md` now classifies the advanced planning set by role and transferability. The audit conclusion is that the `guide-set` plus `supporting` architecture is the right reusable system shape, but the advanced project to-do list and structural profiles remain advanced-specific instances rather than direct intermediate templates.
- Preferred behavior: reuse the document-role system for `int`, but adapt the project-state and structural-planning content as intermediate-specific files rather than cloning advanced-book control content verbatim


### 2026-03-22T19:25:00+09:00 - Intermediate Planning Now Uses The Same Guide-Set / Supporting Control Pattern

- Status: `monitor`
- Scope: project/conventions
- Context: transferring the cleaned planning architecture from the advanced track to the intermediate track
- Observation: the intermediate planning layer now uses `int/edits & guides/planning/guide-set` for current control documents and `int/edits & guides/planning/supporting` for background documents. The intermediate guide set now includes an index, project to-do list, activity framework, prompt-writing policy, structural-profile scaffold, QA checklist scaffold, and full-review protocol scaffold.
- Preferred behavior: treat the new intermediate guide set as the authoritative planning/control layer for future intermediate work, and use the supporting folder only for background/setup context


### 2026-03-22T19:35:00+09:00 - Planning-System Reorganization Is Now Locked On Main

- Status: `monitor`
- Scope: project/state
- Context: finalization of the advanced planning cleanup and the intermediate planning-stack build
- Observation: the advanced planning reorganization, transfer-readiness audit, intermediate guide-set creation, and related project-memory updates were committed and pushed on `main` in commit `2e2b2e1`.
- Preferred behavior: treat the committed planning structure as the live baseline for future advanced and intermediate planning work, and use follow-up commits only for concrete new findings or intentional template refinements


### 2026-03-22T20:05:00+09:00 - Unit 23 Capstone Rubric Now Points Students Back To Taught Units

- Status: `monitor`
- Scope: project/decision
- Context: resolving the first recorded full-review issue in the advanced book
- Observation: Unit 23 now keeps the eight-criterion capstone rubric, but each criterion is explicitly linked back to earlier units that teach the relevant skill. The learner-facing rubric in `adv/md/n10/aw-adv_mod6_n10.md` and the companion rubric in `adv/md/n10/aw-adv_unit23_capstone_rubric.md` now both include the same criterion-to-unit teaching map. Word count remains a submission requirement, not a standalone analytic criterion.
- Preferred behavior: treat the eight-criterion rubric pair as the authoritative Unit 23 assessment model, and use the linked units as the required retrieval path when students or teachers diagnose a weak capstone criterion


### 2026-03-22T20:20:00+09:00 - Full Review Round 1 Cleanup Is Now Closed

- Status: `monitor`
- Scope: project/state
- Context: follow-through after the first advanced full-review pass
- Observation: the remaining Round 1 issues have now been addressed. Unit 18 now explicitly tells learners to keep the `B6` paragraph for reuse in `D2`, and Unit 12's shorter `E3` output range is now recorded in the planning layer as an intentional bounded exception rather than unexplained drift.
- Preferred behavior: treat the Round 1 findings as resolved, use the updated live advanced baseline for the next full-review pass, and record any further issues as a new round rather than reopening the completed Round 1 items


### 2026-03-22T21:10:00+09:00 - Intermediate Baseline Audit Confirmed A Stable Live Draft Shape

- Status: `monitor`
- Scope: project/state
- Context: start of `INT-2` against the live intermediate source set
- Observation: the live intermediate baseline is structurally intact at `int/edits & guides/planning/supporting/int_writing_text_intro.md` plus `int/md/units/aw-int-01.md` to `aw-int-23.md`, with `int/md/aw-int-all.md` retained as a reference-only combined snapshot. The draft already shows a strong repeated lower-intermediate progression from focus and explanation into guided and freer writing, then shifts into integrated multi-audience work in Units 19-23.
- Preferred behavior: treat the live draft as a usable structured baseline to be formalised and controlled, not as an unstructured rough draft that needs its architecture invented from scratch


### 2026-03-22T21:10:00+09:00 - Intermediate Profiles Should Preserve Sentence-Band Scaffolding Before Any Later Output Normalisation

- Status: `monitor`
- Scope: project/decision
- Context: Round 1 baseline audit findings on output control
- Observation: the live intermediate book currently controls output mainly through sentence-count bands such as `3-4`, `3-5`, `4-6`, `5-7`, and `6-8` sentences rather than through a stable word-range framework. That scaffolding is currently functional for the book's A2-B1+ level and should be recorded accurately in the structural profiles before any later normalisation decisions are made.
- Preferred behavior: build the profile layer from the existing sentence-band model first, especially for the integrated late-book units, instead of prematurely forcing advanced-style word-count logic onto the intermediate draft


### 2026-03-22T21:35:00+09:00 - Intermediate Module Scaffolds Now Exist Alongside The Split-Unit Baseline

- Status: `monitor`
- Scope: project/structure
- Context: preparing the intermediate track for module-by-module execution patterned after the advanced workflow
- Observation: a combined module-file layer now exists at `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md`, built directly from the current split unit files. The split unit files under `int/md/units` remain the canonical baseline for now, while the module files provide the module-level working layer needed for later module-by-module revision.
- Preferred behavior: keep the split unit set as the canonical source baseline until an explicit source switch is recorded, but use the new module scaffolds when the intermediate revision pass moves from planning into module-level editing


### 2026-03-22T21:45:00+09:00 - Intermediate Split Unit Files Now Live Under int/md/units

- Status: `monitor`
- Scope: project/structure
- Context: tightening the intermediate source layout after the first module-file layer was created
- Observation: the 23 split intermediate unit files now live under `int/md/units`, while `int/md/aw-int-all.md` remains the combined reference snapshot and `int/md/first_draft_modules` holds the first module-file layer. This separates unit sources, module scaffolds, and the combined draft more clearly inside `int/md`.
- Preferred behavior: use `int/md/units` as the canonical split-unit source location in all current intermediate control documents, and avoid leaving active references pointed at the older flat `int/md` unit paths


### 2026-03-22T22:20:00+09:00 - Intermediate Editing Now Uses Module Files Only

- Status: `monitor`
- Scope: project/decision
- Context: explicit source-of-truth switch for active intermediate drafting
- Observation: the active intermediate editing layer is now `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md` together with `int/edits & guides/planning/supporting/int_writing_text_intro.md`. The split unit files in `int/md/units` and the combined draft in `int/md/aw-int-all.md` are now reference-only unless a later control decision explicitly restores them as active source files.
- Preferred behavior: perform all future intermediate editing in the module files only, and update QA/full-review/control references to treat the module layer as the live book


### 2026-03-22T22:35:00+09:00 - Intermediate To-Do List Now Functions As An Operational Control File

- Status: `monitor`
- Scope: project/conventions
- Context: tightening the intermediate planning stack so it is as useful as the mature advanced control layer
- Observation: `int/edits & guides/planning/guide-set/aw-int_project_todo_list.md` now defines the intermediate project stages with explicit scope, outputs, controlling files, current decisions, and stage-specific expectations rather than acting only as a lightweight roadmap. It now serves as the operational control file for the intermediate track.
- Preferred behavior: use the expanded intermediate to-do list the way the advanced track uses its mature control file: as the first stop for current stage status, agreed sequence, controlling references, and non-negotiable project decisions


### 2026-03-22T22:55:00+09:00 - Intermediate Guide-Set Stage Documents Now Match The Mature Control Standard

- Status: `monitor`
- Scope: project/conventions
- Context: checking the rest of the intermediate planning layer for scaffold-level gaps after the to-do list was strengthened
- Observation: the intermediate guide-set documents for development guidance, activity control, prompt policy, QA, and full review have now been upgraded from light scaffolds into operational stage-definition files. The current authoritative set is:
  - `int/edits & guides/planning/guide-set/aw-int_development_guide.md`
  - `int/edits & guides/planning/guide-set/aw-int_activity_framework.md`
  - `int/edits & guides/planning/guide-set/aw-int_prompt-writing-policy.md`
  - `int/edits & guides/planning/guide-set/aw-int_qa_checklist.md`
  - `int/edits & guides/planning/guide-set/aw-int_full-review_protocol.md`
- Preferred behavior: treat these files as the intermediate equivalents of the mature advanced control documents, use the module files as the live source they govern, and keep future planning refinements aligned to the intermediate book's A2-B1+ identity rather than importing advanced-only architecture


### 2026-03-22T23:25:00+09:00 - Intermediate Structural-Profile File Now Uses The Stable Non-Suffixed Name

- Status: `monitor`
- Scope: project/conventions
- Context: tightening the intermediate planning naming layer after the profile file became the live source-of-truth for `INT-3`
- Observation: the intermediate structural-profile control file now uses `int/edits & guides/planning/guide-set/aw-int_unit_structural_profiles.md` as its stable name, replacing the earlier suffixed filename, and the active planning references now point to the non-suffixed name.
- Preferred behavior: treat `aw-int_unit_structural_profiles.md` as the sole current structural-profile source-of-truth and do not recreate the `_revised` suffix in later control documents unless a genuinely separate revision artifact is intended


### 2026-03-22T23:55:00+09:00 - Intermediate Structural-Profile Layer Is Now Complete And Governs INT-4

- Status: `monitor`
- Scope: project/state
- Context: completion of `INT-3` across Modules 1 to 6
- Observation: `int/edits & guides/planning/guide-set/aw-int_unit_structural_profiles.md` now contains profile coverage for all 23 units. The file now functions as the complete planning source-of-truth for module purpose, unit goals, Can-Do architecture, activity-purpose maps, output expectations, revision flags, and approved exceptions across the whole intermediate book.
- Preferred behavior: treat `INT-3` as complete, use the finished structural-profile layer as the governing baseline for `INT-4`, and record any later revision tensions as planning/live issues rather than silently bypassing the profile decisions


### 2026-03-23T00:10:00+09:00 - INT-4 Has Started With A Prompt-Control Revision Pass On Module 1

- Status: `monitor`
- Scope: project/stage
- Context: start of the whole-book draft revision pass after the profile layer was completed
- Observation: `INT-4` is now in progress. The first live revision pass has started in `int/md/first_draft_modules/aw-int_mod1.md`, focusing on prompt control and task framing so the early units match the completed prompt-writing policy and structural-profile expectations more closely.
- Preferred behavior: continue `INT-4` module by module from Module 1 onward, using the structural profiles, activity framework, and prompt-writing policy together rather than treating any one control file in isolation


### 2026-03-23T01:35:00+09:00 - The Initial INT-4 Prompt-And-Structure Pass Now Covers All Six Intermediate Modules

- Status: `monitor`
- Scope: project/stage
- Context: whole-book draft revision pass after the structural-profile layer was completed
- Observation: the first `INT-4` revision pass has now been applied across `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md`. The main work so far has been tightening prompt control, audience framing, editing-role clarity, and integrated-task reader contrast without redesigning the unit architecture.
- Preferred behavior: before closing `INT-4`, run a whole-book consistency sweep across the six revised module files and record any remaining planning/live tensions or cleanup needs rather than assuming the first pass is sufficient


### 2026-03-23T02:05:00+09:00 - INT-4 Closed Cleanly After The Whole-Book Prompt-And-Structure Sweep

- Status: `monitor`
- Scope: project/stage
- Context: follow-through sweep after the initial Module 1 to Module 6 revision cycle
- Observation: the whole-book `INT-4` follow-through sweep found no remaining cross-module prompt-structure problem that required a second targeted cleanup pass. The only residual live-text issue was a minor Unit 21 focus-line wording defect in `int/md/first_draft_modules/aw-int_mod6.md`, and it was corrected in the same pass.
- Preferred behavior: treat `INT-4` as complete, preserve the prompt-and-structure gains already made in the six module files, and move the next editorial effort into `INT-5` teaching-layer strengthening rather than reopening prompt control without cause


### 2026-03-23T02:15:00+09:00 - INT-5 Has Started With A Module 1 Teaching-Explicitness Pass

- Status: `monitor`
- Scope: project/stage
- Context: start of the language-instruction strengthening stage after the structural revision pass closed
- Observation: `INT-5` is now in progress. The first strengthening work begins in `int/md/first_draft_modules/aw-int_mod1.md`, focusing on short explicit teaching supports such as clear-sentence checks, simplification guidance, tone checks, and paragraph-planning guidance where the draft previously relied too heavily on examples alone.
- Preferred behavior: continue `INT-5` module by module, adding concise concept support and guided transfer help without importing advanced-level theory density into the intermediate book


### 2026-03-23T02:30:00+09:00 - The Initial INT-5 Teaching-Strengthening Pass Now Covers Modules 1 And 2

- Status: `monitor`
- Scope: project/stage
- Context: early movement through the language-instruction strengthening stage
- Observation: the first `INT-5` teaching-explicitness pass now covers `int/md/first_draft_modules/aw-int_mod1.md` and `aw-int_mod2.md`. The main work so far has been adding short, reusable instructional supports such as checklists, question frames, and writing-move rules without changing the task architecture created during `INT-4`.
- Preferred behavior: continue `INT-5` through Modules 3 to 6 using the same principle: make the teaching more visible where needed, but keep the overall prose load and structure at an intermediate level


### 2026-03-23T02:45:00+09:00 - The Initial INT-5 Teaching-Strengthening Pass Now Covers Modules 1 To 3

- Status: `monitor`
- Scope: project/stage
- Context: continued language-instruction strengthening after the early-module teaching pass began
- Observation: the first `INT-5` pass now covers `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod3.md`. The stage pattern is stable: add short explanatory frames and self-check routines where the learner needs transfer help, but do not redesign the section spine or increase theory load.
- Preferred behavior: continue through Modules 4 to 6 using the same restrained strengthening model so the intermediate book becomes more teachable without drifting toward advanced-style instructional density


### 2026-03-23T03:00:00+09:00 - The Initial INT-5 Teaching-Strengthening Pass Now Covers Modules 1 To 4

- Status: `monitor`
- Scope: project/stage
- Context: continuing the language-instruction strengthening pass into the outward-facing communication band
- Observation: the first `INT-5` pass now covers `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod4.md`. The pass remains consistent: brief instructional rules and checklists are being added where they support transfer, while the lighter intermediate prose standard and the existing task architecture remain intact.
- Preferred behavior: continue through Modules 5 and 6 using the same low-load strengthening model before deciding whether a second deeper teaching pass is needed


### 2026-03-23T03:15:00+09:00 - The Initial INT-5 Teaching-Strengthening Pass Now Covers Modules 1 To 5

- Status: `monitor`
- Scope: project/stage
- Context: extending the language-instruction pass into the editing-and-revision band
- Observation: the first `INT-5` pass now covers `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod5.md`. The editing units now also use short learner-facing revision checks, so the teaching support remains visible even when the task is based on correcting a draft rather than producing new writing.
- Preferred behavior: complete the same restrained teaching-strengthening pass in Module 6, then review whether the whole-book language-instruction layer is coherent enough to keep moving forward without another early-stage rewrite


### 2026-03-23T03:30:00+09:00 - The Initial INT-5 Teaching-Strengthening Pass Now Covers All Six Intermediate Modules

- Status: `monitor`
- Scope: project/stage
- Context: completion of the first module-by-module language-instruction strengthening cycle
- Observation: the first `INT-5` pass now covers `int/md/first_draft_modules/aw-int_mod1.md` to `aw-int_mod6.md`. The pass added brief teaching supports such as checklists, question frames, and revision routines across the whole book while preserving the existing prompt structure and the lower-intermediate load.
- Preferred behavior: before closing `INT-5`, run a whole-book teaching-layer sweep to catch any remaining places where key writing moves are still too implicit or where the new support has become heavier than intended


### 2026-03-23T03:45:00+09:00 - INT-5 Closed And INT-6 QA Has Begun

- Status: `monitor`
- Scope: project/stage
- Context: transition from language-instruction strengthening into formal QA
- Observation: the whole-book teaching-layer sweep found no obvious prompt-policy relapse or overcorrection severe enough to justify another immediate `INT-5` rewrite pass. `INT-5` is now treated as complete, `INT-6` is active, and the first live QA record now exists at `int/edits & guides/qa/aw-int_qa_round1.md`.
- Preferred behavior: continue QA through the live module files, record concrete evidence for each `Revise` or `Monitor` finding, and keep deferred Unit 23 rubric support visible as deferred rather than silently treating it as finished


### 2026-03-23T04:05:00+09:00 - The Intermediate QA Checklist Now Operates At The Mature Hard-Gate Standard

- Status: `monitor`
- Scope: project/control
- Context: strengthening the live QA stage definition after checking it against the mature advanced QA checklist
- Observation: `int/edits & guides/planning/guide-set/aw-int_qa_checklist.md` now includes the same level of operational rigor as the advanced QA control file: a preliminary cross-check, blocker-aware workflow, stronger category coverage, requirement-source notes where needed, explicit pinned-item handling, book-level sign-off questions, and a standard recording template for findings.
- Preferred behavior: use the revised intermediate QA checklist as the authoritative review standard for the rest of `INT-6`, and do not fall back to the earlier lighter interpretation of intermediate QA


### 2026-03-23T04:20:00+09:00 - Round 1 QA Now Includes The Hard-Gate Cross-Check And A New Unit 5 Planning-Live Monitor Item

- Status: `monitor`
- Scope: project/stage
- Context: re-evaluation of the live Round 1 QA record after the intermediate checklist was tightened
- Observation: `int/edits & guides/qa/aw-int_qa_round1.md` has now been re-evaluated against the revised checklist rather than the earlier lighter standard. That re-evaluation preserved the existing Unit 5 workload `Revise` item, kept the Unit 8 format ambiguity as `Monitor`, preserved the Unit 23 rubric requirement as `Deferred`, and added a new Unit 5 planning/live `Monitor` item because the structural profile still mentions a Reflection-layer mini email task that the live source no longer contains.
- Preferred behavior: treat the current Round 1 file as the authoritative QA record, resolve the Unit 5 live workload issue and the Unit 5 profile drift before attempting to close intermediate QA


### 2026-03-23T04:45:00+09:00 - The Recorded Round 1 Intermediate QA Issue Set Has Been Cleared

- Status: `monitor`
- Scope: project/stage
- Context: same-pass correction of the four issues named in the re-evaluated Round 1 QA record
- Observation: the recorded Round 1 issue set has now been addressed in both the live source and the control layer. Unit 5 now uses a lighter freer-writing load, the Unit 5 structural profile now matches the live source again, Unit 8 now defines its manual-section format explicitly, and Unit 23 now has both a learner-facing rubric and a companion teacher / QA marking note. `P1` and `P2` in the project to-do list are now recorded as done.
- Preferred behavior: continue `INT-6` using the corrected Round 1 record as the active baseline, and focus the next QA work on whether any additional whole-book findings remain before full review


### 2026-03-23T10:00:00+09:00 - Intermediate Support-Parity Intervention Stage Now Blocks QA

- Status: `monitor`
- Scope: project/control
- Context: control-layer correction after confirming that the intermediate book remained materially thinner than the advanced book in support depth and developed volume
- Observation: the project now treats the saved intervention file `int/edits & guides/planning/guide-set/aw-int_Support-Parity Intervention Plan.md` as the authoritative blocking control document. A new stage, `INT-5A | Support-Parity Intervention Stage`, is now active, and `INT-6` is blocked until the intervention rebuild is complete.
- Preferred behavior: do not treat the first `INT-5` pass as sufficient by default; use `INT-5A` to rebuild the planning stack and the live module files to advanced-equivalent pedagogical completeness before QA resumes


### 2026-03-23T11:15:00+09:00 - The First INT-5A Rebuild Wave Now Covers All Six Intermediate Modules But QA Remains Blocked

- Status: `monitor`
- Scope: project/stage
- Context: first whole-book live rebuild after activating the support-parity intervention stage
- Observation: all six live intermediate module files now include the required missing support functions at both the unit and module levels. The new support layer includes model checks, explicit why-this-works explanations, self-check routines, editing-practice tasks, transfer extensions, module guides, and module review workshops. This materially strengthens the book's pedagogical support, but current module counts still remain below the required `80-90%` parity band, especially in Modules 4 and 6.
- Preferred behavior: keep `INT-5A` active, continue deepening the live modules rather than resuming QA, and use the current rebuild wave as the new floor rather than as a final intervention endpoint


### 2026-03-23T12:10:00+09:00 - The Second INT-5A Rebuild Wave Added Module-Level Strategy And Revision Support Across All Six Modules

- Status: `monitor`
- Scope: project/stage
- Context: second whole-book live rebuild under the support-parity intervention
- Observation: the live module files now include a stronger module-level support spine beyond the first-wave unit additions. Across Modules 1 to 6, the book now includes strategy maps, revision labs, and stronger module-level transfer tasks. This moved all six modules upward again, but the book still remains below the required parity band, with the largest remaining shortfalls in Modules 4 and 6.
- Preferred behavior: keep `INT-5A` active, use the current two-wave rebuild as the new baseline, and focus the next deepening work on the still-thin outward-facing and capstone modules before attempting QA restart


### 2026-03-23T12:25:00+09:00 - Advanced Activity Wordcount Averages Are Now Saved As An Intermediate Parity Reference

- Status: `monitor`
- Scope: project/control
- Context: support-parity calibration for the intermediate intervention stage
- Observation: a new reference file now exists at `int/edits & guides/planning/guide-set/aw-int_advanced_activity_wordcount_reference.md`. It records the activity-level wordcount averages from the live advanced `n10` files, including the overall coded-activity average of `118.72` words and the per-activity-type averages from `A1` to `H3`.
- Preferred behavior: use this file as a calibration benchmark during `INT-5A` when judging whether intermediate activity support remains materially thinner than the advanced book, but do not treat it as a direct copying template


### 2026-03-23T12:40:00+09:00 - The Intermediate Intervention Now Has A Saved Activity-Level Gap Worklist

- Status: `monitor`
- Scope: project/control
- Context: translating the advanced activity reference into a live intermediate execution aid
- Observation: a new file now exists at `int/edits & guides/planning/guide-set/aw-int_activity_gap_worklist.md`. It turns the advanced-reference comparison into a prioritized intermediate activity-level worklist and confirms that the heaviest remaining underdevelopment is concentrated in Modules 4 and 6, then Modules 3 and 5.
- Preferred behavior: use this worklist during the next `INT-5A` passes so activity-level deepening follows an explicit diagnosis rather than scattered judgment


### 2026-03-23T12:55:00+09:00 - Intermediate Module Files Now Use The Same Unit-Heading Format As The Advanced Book

- Status: `monitor`
- Scope: project/control
- Context: cross-book formatting normalization during the intermediate intervention stage
- Observation: the live intermediate module files now use the advanced-style unit heading format `## Unit X - Title` instead of the earlier draft-style `## X. Title`. The intermediate wording remains simpler and level-appropriate, but the structural heading format is now aligned across both books.
- Preferred behavior: keep the normalized `Unit X - Title` heading format in future intermediate module edits unless a later project-level formatting decision intentionally replaces it





### 2026-03-31T12:00:00+09:00 - Student-Response Placeholder And Print-Layout Stage Added For Both Books

- Status: `monitor`
- Scope: project/finish-sequence
- Context: late-stage student-book production planning
- Observation: both textbook tracks now explicitly include a post-text-sign-off student-response placeholder and print-layout stage. New source-of-truth planning files define a shared five-type placeholder system (`PH-1` to `PH-5`), placement rules, and standardized box labels for handwritten student responses:
- adv/edits & guides/planning/guide-set/aw-adv_student-response-layout_plan.md
- int/edits & guides/planning/guide-set/aw-int_student-response-layout_plan.md
- Preferred behavior: treat placeholder planning and insertion as a formal late-stage production task rather than an ad hoc formatting step; apply it after the content review stage and before final print production


### 2026-03-31T12:35:00+09:00 - Intermediate Module 6 Now Clears The INT-5A Parity Floor With A Stronger Integrated-Task Support Layer

- Status: `monitor`
- Scope: project/stage
- Context: continuing `INT-5A` Wave 4 with `Module 6` as the first priority target
- Observation: `int/md/first_draft_modules/aw-int_mod6.md` was expanded from about `7,249` words to about `8,233` words through targeted support additions rather than new task proliferation. The pass added explicit planning/control scaffolds for audience split, correction consistency, and cross-document consistency in Units 19, 20, and 22, plus stronger portfolio assembly, portfolio balance, and capstone rebuild support in Unit 23 and a module-level rebuild lab. This now clears the `INT-5A` Module 6 parity floor of `8,126` words.
- Preferred behavior: treat Module 6 as having reached the floor with a stronger integrated-writing support layer, and move the next `INT-5A` priority pass to Module 3 unless a later quality review reveals a specific remaining Module 6 weakness


### 2026-03-31T13:05:00+09:00 - Intermediate Module 3 Now Clears The INT-5A Parity Floor With Stronger Internal-Document Support

- Status: `monitor`
- Scope: project/stage
- Context: continuing `INT-5A` Wave 4 with `Module 3` as the second priority target after Module 6
- Observation: `int/md/first_draft_modules/aw-int_mod3.md` was expanded from about `5,779` words to about `6,031` words through targeted support additions in Units 9, 10, and 11. The pass added a `Notice Control Board`, a `Problem-Logic Planning Grid`, and a `Summary Action Check` so students get clearer support for internal-notice purpose, problem-explanation logic, and action-oriented meeting summaries. This now clears the `INT-5A` Module 3 parity floor of `5,962` words.
- Preferred behavior: treat Module 3 as having reached the floor with stronger internal-document planning and rebuild support, and move the next `INT-5A` priority pass to Module 4 unless a later quality review reveals a specific remaining Module 3 weakness


### 2026-03-31T14:05:00+09:00 - Repo-Wide Mojibake Cleanup Now Uses A Dedicated UTF-8 Checker And A Clean Combined-Draft Rebuild

- Status: `monitor`
- Scope: project/tooling
- Context: project-wide mojibake review after corruption was found outside the live module files
- Observation: the repo-wide scan found remaining mojibake in planning files, project memory notes, and `int/md/aw-int-all.md`. The affected small files were normalized directly, and the combined intermediate draft was rebuilt from the clean intro plus the six live module files under explicit UTF-8 handling. A new repo utility, `scripts/check_mojibake.py`, now provides an explicit mojibake scan for common corruption patterns without depending on Windows console rendering.
- Preferred behavior: run `python scripts/check_mojibake.py` before large regeneration steps and before commit whenever encoding drift is suspected; if the combined intermediate draft needs regeneration, rebuild it from the live UTF-8 source files rather than editing the combined file directly
