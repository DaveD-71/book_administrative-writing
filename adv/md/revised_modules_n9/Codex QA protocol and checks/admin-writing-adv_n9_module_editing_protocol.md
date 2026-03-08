# N9 Module Editing Protocol
## *Administrative Writing, Advanced*

---

> **Purpose of this document**
> This file records the working protocol for future `N9` module editing. It exists to prevent over-simplified prompt rewrites, preserve activity-type fidelity, and ensure that edits are guided by the full project framework rather than by content flags alone.

---

## Primary Principle

`N9` editing is not just a prompt-cleanup pass. Each edit must satisfy all of the following at the same time:

- the unit's learning goal
- the assigned activity type and its pedagogical function
- the unit-specific content flags
- the prompt-writing policy
- the expected student-facing quality of the textbook

If a revision is structurally tidy but weak as a learner-facing prompt, it is not a successful `N9` edit.

---

## Source Order for Every Module

Before editing a module, use the following source hierarchy:

1. `adv/claudeai/admin-writing-adv_unit_structural_profiles_revised.md`
2. `admin-writing_master_activity_menu.md`
3. `adv/claudeai/admin-writing-adv_prompt-writing-policy.md`
4. Relevant files in `adv/claudeai/edits & guides`
5. Strong benchmark wording already present in `adv/md/revised_modules_n9/admin-writing-adv_mod1_n9.md`

This order matters.

- The structural profiles define the unit/activity goals and the content flags.
- The activity menu defines what each activity type is supposed to do.
- The prompt-writing policy defines quality standards for prompt design.
- The guides folder contains implementation constraints and editorial judgment.
- Existing strong N9 output provides a benchmark for student-facing phrasing quality.

---

## Required Workflow for Each Unit

### 0. Complete the written checklist before and after editing

Before editing any E or H prompt, and again before accepting it, complete the current `N9` QA checklist.

This is mandatory.

- Do not rely on memory for prompt-policy compliance.
- Do not treat "validator passed" as evidence that the prompt is acceptable.
- If a prompt has not been checked in writing against the checklist, it is not ready to return.

---

### 1. Start from the structural profile

Identify:

- the unit goal
- the assigned activity types
- the Can-Do focus for each activity
- the listed content flags for Task B

Do not begin rewriting from the source module file alone.

---

### 2. Check the activity type before changing wording

Use `admin-writing_master_activity_menu.md` to confirm what the activity is meant to do pedagogically.

This is required especially for:

- distinguishing `E1` from `E3`
- distinguishing guided vs freer vs homework task calibration
- preserving the intended role of B, C, D, E, and H activity types

Do not rewrite a prompt until the activity type is clear.

---

### 3. Use the prompt-writing policy as a filter, not a template

Check prompts for:

- learning-goal alignment
- professional verisimilitude
- recoverable PAST-R
- appropriate calibration
- scenario-list parallelism
- correct JPO option handling
- correct H ordering

Do not flatten prompts into generic formulae just to satisfy the policy.

For any task with a scenario list, the following are non-optional checks:

- options are genuinely distinct in professional situation
- options are not just branded variants of the same follow-up/problem/request
- the JPO option is one option among equals, not a near-duplicate of another option
- the JPO option uses the same target skill but a distinct context, role, or relationship
- the JPO option does not reduce the total range of choice

If any one of these fails, the prompt is not finished.

---

### 4. Read relevant guide files before editing

If a unit or module is covered by a file in `adv/claudeai/edits & guides`, read that guide before editing.

These guides often indicate the intended edit scope:

- insertion only
- structural correction
- targeted calibration
- narrow content fix

Do not turn a narrow edit into a full rewrite unless the source documents clearly require it.

---

### 5. Benchmark against strong existing prompts

Use `adv/md/revised_modules_n9/admin-writing-adv_mod1_n9.md` as a quality benchmark for student-facing prompts.

Strong prompts in this project should be:

- specific enough to feel real
- broad enough to remain transferable
- clear enough for a learner to act on immediately
- free of vague placeholders such as "administrative context" or generic institutional labels

---

### 6. Classify the edit before making it

For each flagged item, decide which of these it is:

- structural correction
- prompt calibration
- true rewrite

If the issue is structural, do not rewrite the full prompt unnecessarily.

---

### 7. Write from the learner's task experience outward

For each edited activity, check:

- what the learner is being asked to produce
- why this activity type appears in this unit
- how much scenario detail the learner needs
- what wording will be immediately usable at B2-B2+ level

The finished text must read like good textbook writing for the student, not like an implementation note.

---

### 8. Run an editorial QA check after each unit

Before moving on, verify:

- activity-type fidelity
- unit-goal fidelity
- realism and specificity
- no over-specification
- clear learner-facing instructions
- consistency with the unit's content flags

For E and H prompts, editorial QA must also verify explicitly:

- activity-type fidelity against the master activity menu
- prompt-policy compliance against the written checklist
- no contextual overlap between options
- correct JPO option handling under Sections 5.3 and 5.4 of the prompt-writing policy
- no repeated role labels or near-identical professional relationships across options unless clearly justified

The QA result should be written down. A mental check is not sufficient.

---

### 9. Run script validation last

Use the script tools only after the editorial pass.

The script can confirm:

- structure
- unit order
- H ordering
- basic formatting consistency

It cannot confirm prompt quality, pedagogical fit, or activity-type fidelity.

---

## Non-Negotiable Reminders

- Content flags are the primary trigger for `N9` edits, but they are not sufficient by themselves.
- Activity-type requirements must always be checked against the master activity menu.
- Prompt-policy compliance does not justify weaker, vaguer, or flatter student-facing prompts.
- `E1`, `E2`, `E3`, and `H3` are not interchangeable and must not be treated as if they were.
- JPO options must be parallel to the other options, not over-specified special cases.
- JPO options must also be contextually distinct from options 1–3. A JPO version of the same scenario is a failure, not a valid option.
- If an earlier revision already reads better for the learner, preserve that quality rather than rewriting it into something more abstract.

---

## Working Standard

Before considering a unit complete for `N9`, ask:

> Does this edited activity satisfy the unit goal, fit the activity type, address the content flag, comply with the prompt policy, and read naturally to the learner?

If any one of those is missing, the edit is not finished.
