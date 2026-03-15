# Project Learning

Durable project memory for `C:\Dev\Code\book_administrative-writing`.

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
- Observation: `adv/edits & guides/aw-adv_project_todo_list.md` shows N1-N10 complete, N11 not started, and identifies book-wide QA as the next major workstream; the active edited content set is the six `adv/md/n10/aw-adv_mod*_n10.md` files
- Preferred behavior: treat the advanced N10 module set and the N11 QA step as the current highest-maturity content baseline for project planning and review work

### 2026-03-15T00:46:14.1210166+09:00 - Advanced Planning Source Of Truth

- Status: `monitor`
- Scope: project/conventions
- Context: advanced documentation hierarchy
- Observation: `adv/edits & guides/aw-adv_unit_structural_profiles_revised.md` identifies itself as the planning source of truth, and the advanced to-do list treats it and the N10 module files as the authoritative references for editing and QA
- Preferred behavior: when working on advanced content, use the revised structural profiles, the advanced to-do list, and the N10 module files ahead of older context summaries

### 2026-03-15T00:46:14.1210166+09:00 - Advanced Context Document Is Historically Useful But Stale

- Status: `monitor`
- Scope: project/conventions
- Context: comparison of advanced status documents
- Observation: `adv/edits & guides/aw-adv_project_context.md` still describes the project as being in structural planning and lists pre-N9 next steps, which no longer matches the current N10-complete state in `aw-adv_project_todo_list.md`
- Preferred behavior: treat `aw-adv_project_context.md` as historical background only unless it is refreshed; do not use it as the primary status source for current advanced work

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
- Observation: `N11` has now started; the book-wide QA checklist framework was drafted at `adv/edits & guides/aw-adv_n11_qa_checklist.md` and the advanced to-do list now marks `N11` as in progress
- Preferred behavior: use the new `N11` checklist as the authoritative QA framework for the next advanced review pass, rather than relying on the older `N9` QA controls

### 2026-03-15T01:07:00+09:00 - Advanced N11 Round 1 Findings Recorded

- Status: `monitor`
- Scope: project/state
- Context: initial `N11` execution
- Observation: a first `N11` review note now exists at `adv/edits & guides/aw-adv_n11_qa_review_round1.md`; early evidence confirms `P2`, `P6`, and Module 2 Section H ordering in the active `n10` files, while portfolio-task E-word-count handling and final book-level structural-variety confirmation remain active QA items
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
- Observation: `adv/edits & guides/aw-adv_n11_qa_checklist.md` now explicitly tests whether prompt wording remains readable for B1+/B2 aspirational learners, whether revised prompts drift upward in linguistic sophistication or processing load, and whether scenario families are distributed broadly enough across the book; each new check is tied to named source documents
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
- Preferred behavior: treat `aw-adv_n11_qa_review_round2.md` as the operative N11 record and use it to drive the next correction pass, rather than relying on the earlier partial Round 1 / selective Round 2 notes

### 2026-03-15T00:34:37.9048369+09:00 - Project Memory Scaffold Initialized

- Status: `resolved`
- Scope: project/workflow
- Context: repository-level Codex memory setup
- Decision: the standard project scaffold was created at the repository root with `AGENTS.md`, `user-learning-mirror.md`, `project-learning.md`, `project-journal.md`, and `instruction-read-log.csv`
- Preferred behavior: keep all project-memory files at the repository root and use them as the authoritative project-level memory layer

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
