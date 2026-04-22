---
description: "Phase 3: Test a resource against specimens — auto-detects type, runs appropriate test strategy"
---

# /test-resource

> Test a resource by auto-detecting its type and running the appropriate test strategy.

Can be invoked standalone or as a subagent from `/create-resource`.

**Usage:**

```
/test-resource <name>
/test-resource <name> <specimen>
```

**Examples:**

```
/test-resource document
/test-resource document specimen/python/fastapi
/test-resource review-pr specimen/ts/express
```

## Steps

### 1. Parse arguments

Extract from the command:

- `name` — the resource to test (e.g. `document`)
- `specimen` — optional specimen branch override

### 2. Detect resource type

Determine the type by checking file locations:

| Check                        | Type     |
|------------------------------|----------|
| `skills/<name>/SKILL.md`     | skill    |
| `rules/<name>.md`            | rule     |
| `workflows/<name>.md`        | workflow |

If not found, error:

> Resource `<name>` not found. Check `skills/`, `rules/`, or `workflows/`.

### 3. Read metadata

For skills, read SKILL.md frontmatter:

- `test.specimens` — compatible specimens
- `requires` — required skills (verify they exist)

### 4. Select test strategy

| Resource type | Strategy                                                    |
|---------------|-------------------------------------------------------------|
| **Skill**     | Specimen-based: merge real codebase → run skill → validate  |
| **Rule**      | Validation: check frontmatter, globs, content structure     |
| **Workflow**  | Scenario-based: dry-run steps, check prerequisites          |

### 5. Execute test — Skill (specimen-based)

#### 5a. Select specimen

If specimen not provided as argument:

- Read `test.specimens` from frontmatter
- List available specimens:

```bash
python3 scripts/list_specimens.py
```

- Ask user to choose, or use first compatible specimen

#### 5b. Save current state

```bash
CURRENT_BRANCH=$(git branch --show-current)
git add -A
git commit -m "wip: save state before test" --allow-empty
```

#### 5c. Create test branch

```bash
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
TEST_BRANCH="test/${name}-${TIMESTAMP}"
git checkout -b "$TEST_BRANCH"
```

#### 5d. Merge specimen

```bash
git merge --allow-unrelated-histories "${specimen}"
```

Handle merge conflicts:
- For `README.md` — accept the specimen version
- For other conflicts — resolve manually and ask the user

#### 5e. Run the skill

Read the skill file and execute it against the merged specimen code:

```bash
cat skills/<name>/SKILL.md
```

Execute the skill's steps. Record:
- Did each step complete successfully?
- Were the outputs correct?
- Any errors or unexpected behavior?

#### 5f. Generate report

Document results:

```
Test Report: /<name> against <specimen>
Date: <timestamp>
Status: PASS / FAIL

Steps:
  1. <step> — ✓ / ✗ (details)
  2. ...

Issues:
  - (if any)

Files created:
  - (list)
```

#### 5g. Return to original branch

```bash
git checkout "$CURRENT_BRANCH"
git branch -D "$TEST_BRANCH"
```

### 6. Execute test — Rule (validation)

For rules, validate without specimens:

1. **Frontmatter check** — has `description` field
2. **Content structure** — has clear sections, actionable instructions
3. **Globs check** — if `globs` specified, verify paths exist in repo

Report validation results.

### 7. Execute test — Workflow (scenario)

For workflows, validate:

1. **Prerequisites** — all referenced skills/tools exist
2. **Step completeness** — each step has clear instructions
3. **Dry-run** — walk through steps mentally, check for gaps

Report validation results.

### 8. Present results

> Test complete for `/<name>`:
> - Status: **PASS** / **FAIL**
> - (summary of results)
>
> Want me to fix any issues found?

If issues were found, iterate:
1. Fix the resource on the current branch
2. Re-run `/test-resource` to verify
