# How to Test a Resource

This guide covers testing AI resources using `/test-resource` and specimen branches.

## Quick Start

```bash
# Test a skill against a specimen
/test-resource document specimen/python/fastapi

# Test a skill (auto-select specimen)
/test-resource review-pr

# Test a rule (validation only, no specimen needed)
/test-resource code-style
```

## Frontmatter-Driven Testing

The `/test-resource` workflow reads the skill's `test:` frontmatter to determine what setup is needed:

| Frontmatter field  | What `/test-resource` does                |
|--------------------|-------------------------------------------|
| `test.specimens`   | Offers compatible specimens               |
| `test.needs-delta` | Asks for a delta branch selection         |
| `test.needs-pr`    | Pushes branches + creates a real PR       |
| `test.needs-study` | Runs a prerequisite skill before the test |

## Test Strategies by Type

### Skill testing (specimen-based)

Skills are tested by running them against real project snapshots (specimens):

1. Commits any pending changes on your branch
2. Creates a test branch from your current branch
3. Merges the chosen specimen (`--allow-unrelated-histories`)
4. Sets up test prerequisites (PR, study report, etc. — based on frontmatter)
5. Runs the skill against the merged code
6. Generates a test run report
7. Returns you to your original branch

### Rule testing (validation)

Rules are tested without specimens:

- Frontmatter check (has `description` field)
- Content structure (clear sections, actionable instructions)
- Globs check (if specified, paths exist in repo)

### Workflow testing (scenario)

Workflows are validated by:

- Checking all referenced skills/tools exist
- Verifying step completeness
- Dry-running through steps for gaps

## Specimens

### What is a specimen?

A **real project snapshot** on an orphan branch. Any skill that operates on source code can use it.

### Available specimens

| Specimen                  | Description                    |
|---------------------------|--------------------------------|
| `specimen/python/fastapi` | FastAPI REST API service       |
| `specimen/ts/express`     | Express.js TypeScript REST API |

### Delta branches

Delta branches are variants with intentional changes for testing specific scenarios:

```
specimen/python/fastapi-delta-docs   — missing documentation
specimen/ts/express-delta-docs       — missing documentation
```

### Listing specimens

```bash
python3 scripts/list_specimens.py
```

## How Specimens Work

Specimens are **real project snapshots** on orphan branches:

```
specimen/python/fastapi              ← orphan branch (full project)
specimen/python/fastapi-delta-docs   ← forked from base (adds changes)
```

When `/test-resource` merges a specimen, it brings a real codebase into your test branch so the skill has something to work with.

For skills that need a diff (e.g. `/review-pr`), a **base branch** and **delta branch** are created:

```
specimen/python/fastapi
  └── test/review-base-python-fastapi-{ts}        ← base
        └── test/review-python-fastapi-docs-{ts}   ← feature (base + delta)
              → PR: feature → base
              → run /review-pr
```

## Manual Testing (without the agent)

### List available specimens

```bash
python3 scripts/list_specimens.py
```

### Test manually

```bash
# 1. Create a test branch
git checkout -b test/document-$(date +%Y%m%d)

# 2. Merge specimen
git merge --allow-unrelated-histories specimen/python/fastapi

# 3. Resolve any conflicts (accept specimen README.md)

# 4. Run your skill manually

# 5. Review results

# 6. Clean up
git checkout main
git branch -D test/document-$(date +%Y%m%d)
```

## Evaluating Results

After the skill runs, check its output:

### What to look for

| Aspect          | Question                                           |
|-----------------|----------------------------------------------------|
| Correctness     | Does the output match the specimen's actual code?  |
| Completeness    | Does it cover all relevant files/patterns?         |
| False positives | Does it flag things that aren't actually problems? |
| Actionability   | Are suggestions specific and helpful?              |

## Handling Test Failures

When tests fail:

1. **Read the report** — understand what went wrong
2. **Fix the resource** — edit SKILL.md, rule, or workflow
3. **Re-test** — run `/test-resource` again
4. **Iterate** — repeat until all tests pass

Common failure patterns:

| Issue                            | Fix                                     |
|----------------------------------|-----------------------------------------|
| Skill step produces wrong output | Clarify step instructions in SKILL.md   |
| Skill misses project files       | Add detection logic or wider file globs |
| Rule too strict/loose            | Adjust constraints, add examples        |
| Workflow has missing prereqs     | Add prerequisite checks to early steps  |

## Key Points

- **Test branches fork from your current branch** — skill edits you've made are included.
- **Specimens are orphan branches** — no shared history with `main`.
- **Test branches are disposable** — clean them up after testing.
- **Skill frontmatter drives test setup** — no need to modify `/test-resource` for new skills.

## Troubleshooting

| Problem                       | Fix                                                                      |
|-------------------------------|--------------------------------------------------------------------------|
| "No specimen branches found"  | Run `git branch -a \| grep specimen` — specimens may only be on remote   |
| Merge conflicts               | Usually `README.md` — resolve manually or let `/test-resource` handle it |
| Script hangs at "Press Enter" | Intentional — switch to IDE, run the skill, then come back               |

## Related Docs

- [How to Create a Resource](how-to-create-resource.md) — full lifecycle guide
- [How to Add a Specimen](how-to-add-specimen.md) — creating test project snapshots
- [Skill Specification](skill-spec.md) — frontmatter fields including `test:` section
