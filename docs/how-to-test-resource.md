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

## Test Strategies by Type

### Skill testing (specimen-based)

Skills are tested by running them against real project snapshots (specimens):

1. `/test-resource` creates a temporary test branch
2. Merges the chosen specimen (orphan branch with real code)
3. Runs the skill against the merged code
4. Records what worked and what didn't
5. Cleans up the test branch

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

## Manual Testing (without the agent)

If you want to test manually:

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

## Related Docs

- [How to Create a Resource](how-to-create-resource.md) — full lifecycle guide
- [How to Add a Specimen](how-to-add-specimen.md) — creating test project snapshots
- [Skill Specification](skill-spec.md) — frontmatter fields including `test:` section
