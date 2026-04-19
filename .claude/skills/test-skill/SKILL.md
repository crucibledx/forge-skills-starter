---
description: Test a skill against a specimen branch
disable-model-invocation: true
---

# Test Skill

Test a skill by merging a specimen project snapshot and running the skill against it.

**Usage:** `/test-skill <skill-name> <specimen>`

**Examples:**

```
/test-skill document specimen/python/fastapi
/test-skill review-pr specimen/ts/express
```

## Step 1 — Parse arguments

Extract from the command:

- `skill-name` — the skill to test (e.g. `document`)
- `specimen` — the specimen branch (e.g. `specimen/python/fastapi`)

If arguments are missing, list available options:

```bash
# List skills
ls skills/

# List specimens
python3 scripts/list_specimens.py
```

## Step 2 — Validate skill exists

Check that `skills/<skill-name>/SKILL.md` exists.

Read the frontmatter to get:

- `test.specimens` — verify the requested specimen is compatible
- `requires` — check that required skills are available

If the specimen is not in `test.specimens`, warn the user but allow proceeding.

## Step 3 — Save current state

```bash
# Record current branch
CURRENT_BRANCH=$(git branch --show-current)

# Commit any pending changes
git add -A
git commit -m "wip: save state before test" --allow-empty
```

## Step 4 — Create test branch

```bash
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
TEST_BRANCH="test/${skill-name}-${TIMESTAMP}"

git checkout -b "$TEST_BRANCH"
```

## Step 5 — Merge specimen

```bash
git merge --allow-unrelated-histories "origin/${specimen}"
```

Handle merge conflicts:

- For `README.md` conflicts — accept the specimen version
- For other conflicts — resolve manually and ask the user

## Step 6 — Run the skill

Read the skill from the current branch (it was committed in step 3):

```bash
# The skill file is available since we committed before branching
cat skills/<skill-name>/SKILL.md
```

Execute the skill against the merged specimen code.

## Step 7 — Record results

Document the test results:

- Did the skill complete successfully?
- Were the outputs correct?
- Any errors or unexpected behavior?

## Step 8 — Return to original branch

```bash
# Switch back
git checkout "$CURRENT_BRANCH"

# Clean up test branch (optional)
git branch -D "$TEST_BRANCH"
```

> "Test complete. Results: <summary>. Want me to fix any issues found?"

If issues were found, iterate:

1. Fix the skill on the current branch
2. Re-run `/test-skill` to verify
