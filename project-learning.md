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



