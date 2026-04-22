# How to Add a Specimen

Specimens are real project snapshots on orphan branches used for testing skills.

## When to Add a Specimen

- New language/framework not covered (e.g. Go, Rust, Java)
- Skill needs specific project structure (e.g. monorepo, multi-service)
- Existing specimens don't exercise the skill's edge cases

## Steps

### 1. Create the orphan branch

```bash
git checkout --orphan specimen/<lang>/<framework>
git rm -rf .
```

### 2. Add project files

Either scaffold a new project or copy an existing one:

```bash
# Example: new Python Flask project
mkdir -p app tests
# ... add all project files ...
```

The project should be:

- **Realistic** — not a toy example, representative of real usage
- **Self-contained** — all dependencies listed, can build/run
- **Clean** — follows standard conventions for the framework
- **Small enough** — skill testing should be fast

### 3. Commit

```bash
git add -A
git commit -m "specimen: add <lang>/<framework>"
```

### 4. Push the orphan branch

```bash
git push origin specimen/<lang>/<framework>
```

### 5. (Optional) Create delta branches

Delta branches are variants with intentional issues for testing specific scenarios:

```bash
# Start from the base specimen
git checkout specimen/<lang>/<framework>
git checkout -b specimen/<lang>/<framework>-delta-<name>

# Make intentional changes
# - Remove documentation for /document skill testing
# - Add code smells for /review-pr skill testing
# - etc.

git add -A
git commit -m "specimen: add <lang>/<framework>-delta-<name>"
git push origin specimen/<lang>/<framework>-delta-<name>
```

### 6. Update skill frontmatter

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

### 7. Test

```bash
/test-resource <skill-name> specimen/<lang>/<framework>
```

## Naming Conventions

| Pattern                   | Example                              |
|---------------------------|--------------------------------------|
| Base specimen             | `specimen/python/fastapi`            |
| Delta (specific scenario) | `specimen/python/fastapi-delta-docs` |
| Language grouping         | `specimen/<lang>/<framework>`        |

## Existing Specimens

List all specimens:

```bash
python3 scripts/list_specimens.py
```

## Related Docs

- [How to Test a Resource](how-to-test-resource.md) — testing guide
- [How to Create a Resource](how-to-create-resource.md) — full lifecycle guide
