# How to Add a New Specimen

Specimens are self-contained example applications stored as **orphan git branches**. They are used to test AI skills against realistic codebases.

## Naming Convention

| Type  | Branch pattern                             | Examples                                  |
|-------|--------------------------------------------|-------------------------------------------|
| Base  | `specimen/<lang>/<framework>`              | `specimen/python/fastapi`                 |
| Delta | `specimen/<lang>/<framework>-delta-<name>` | `specimen/python/fastapi-delta-docs`      |
|       |                                            | `specimen/ts/express-delta-missing-tests` |

- **Base specimens** are orphan branches (no shared history with `main`).
- **Delta branches** are forked from their base specimen (not orphan).
- **Delta `<name>`** is freeform — use a descriptive label, not just a size. Examples: `docs`, `missing-tests`, `bad-error-handling`, `no-types`.

## Step 1 — Create the Specimen Branch

```bash
# Ensure clean working tree
git stash   # if needed

# Create an orphan branch (no parent commits)
git checkout --orphan specimen/<lang>/<framework>
git rm -rf .
```

## Step 2 — Add the Application

Create a minimal but realistic application. Include:

- **Build file** — `package.json`, `requirements.txt`, `pyproject.toml`, etc.
- **Source code** — at least 2-3 service/controller files with real logic
- **Configuration** — environment files, config modules, etc.
- **Unit tests** — at least one test file with 3+ tests
- **README.md** — describe the project, tech stack, API, and structure
- **.gitignore** — standard ignores for the language/framework

### Guidelines

- **Keep it small** — a specimen should be small enough for an AI to analyze in one pass (5-15 source files).
- **Be realistic** — use real patterns from production projects. The skill needs to practice on code that looks like production.
- **Include multiple concerns** — domain model, service layer, error handling, configuration.

> **Specimens do NOT need to compile or run.** They are never executed — skills only
> read and analyze the source code. It is perfectly fine to reference non-existent
> packages, use a database connection that will never be opened, or depend on
> artifacts that aren't in any real registry. What matters is that the code
> **looks realistic** and follows real patterns.

## Step 3 — Commit

```bash
git add -A
git commit -m "specimen: <framework> <description>

<Brief summary of what the specimen contains>"
```

## Step 4 — Create Delta Branches

Delta branches add a small feature with **intentional issues** for skill testing.

```bash
# Fork from the specimen (NOT orphan!)
# Use a descriptive name — not limited to size labels
git checkout -b specimen/<lang>/<framework>-delta-<name> specimen/<lang>/<framework>

# Examples:
git checkout -b specimen/python/fastapi-delta-docs specimen/python/fastapi
git checkout -b specimen/ts/express-delta-missing-tests specimen/ts/express
```

### What to include in a delta

- **A new feature** — new endpoint, new field, new service method
- **2-5 intentional review findings**, such as:
    - Catching generic `Exception` instead of specific type
    - Missing input validation
    - String concatenation in log statements (should use `{}` placeholders or f-strings)
    - Imperative loops where map/filter would be cleaner
    - Missing type annotations
    - Returning `null`/`None` instead of raising or using Optional
    - Weak test assertions (e.g. only `assertNotNull`, no status code check)
    - Magic strings / missing constants
    - Bad test method naming

### Commit the delta

```bash
git add -A
git commit -m "Add <feature>

- <what was added>
- Intentional review findings:
  - <smell 1>
  - <smell 2>"
```

## Step 5 — Push

```bash
git push origin specimen/<lang>/<framework>
git push origin specimen/<lang>/<framework>-delta-<name>   # if delta exists
```

## Step 6 — Update skill frontmatter

Add the new specimen to compatible skills:

```yaml
---
description: ...
test:
  specimens:
    - specimen/python/fastapi
    - specimen/<lang>/<framework>  # ← add here
---
```

## Step 7 — Verify

```bash
# List all specimens — your new one should appear
python3 scripts/list_specimens.py

# Test a skill against it
/test-resource document specimen/<lang>/<framework>
```

## Existing Specimens

| Specimen                  | Description                    | Delta                       |
|---------------------------|--------------------------------|-----------------------------|
| `specimen/python/fastapi` | FastAPI REST API service       | `-delta-docs`: missing docs |
| `specimen/ts/express`     | Express.js TypeScript REST API | `-delta-docs`: missing docs |

## Common Mistakes

- **Making deltas orphan** — use `git checkout -b ... <specimen>`, not `--orphan`. Delta must share history with the specimen for git diff to work.
- **Too large** — keep specimens under 15 source files. Skills struggle with huge codebases.
- **Too trivial** — a single "Hello World" class won't exercise the skill meaningfully.
- **Missing tests** — review skills check test quality; include at least one test file.
- **No README** — many skills start by reading the README; make sure it exists.

## Related Docs

- [How to Test a Resource](how-to-test-resource.md) — testing guide
- [How to Create a Resource](how-to-create-resource.md) — full lifecycle guide
