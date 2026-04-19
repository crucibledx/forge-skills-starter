# Skill Specification

> Defines the format, conventions, and metadata for skills in this platform.

## File Structure

Every skill lives in `skills/<skill-name>/` and contains at minimum:

```
skills/<skill-name>/
├── SKILL.md    # Executable skill definition (required)
└── README.md   # Overview, contracts, design decisions (required)
```

The folder name **is** the skill name.

## SKILL.md Format

### Frontmatter (YAML)

Every `SKILL.md` starts with YAML frontmatter:

```yaml
---
description: One-line description of the skill
version: 1.0.0
type: orchestrator           # orchestrator | sub-skill | utility
language: "*"                # "*" (any), "python", "typescript", etc.
requires:                    # Skills this skill delegates to (optional)
  - /detect-stack
test:                        # Testing metadata (optional, used by /test-skill)
  specimens:                 # Compatible specimens
    - specimen/python/fastapi
    - specimen/ts/express
---
```

### Required fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | One-line summary |
| `version` | string | Semantic version (`MAJOR.MINOR.PATCH`) |
| `type` | enum | `orchestrator`, `sub-skill`, or `utility` |

### Optional fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `language` | string | `"*"` | Language scope (`"*"` = any) |
| `requires` | string[] | `[]` | Skills this skill calls |
| `test` | object | — | Testing metadata, read by `/test-skill` |

### Test metadata fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `test.specimens` | string[] | all | Compatible specimens |

## Version Semantics

Each skill has its own version in frontmatter:

| Bump | When | Example |
|------|------|---------|
| **MAJOR** | Breaking change to the skill's contract | Changed report format |
| **MINOR** | New capability, backward compatible | Added monorepo support |
| **PATCH** | Bug fix, wording improvement | Fixed detection logic |

## Skill Types

### `orchestrator`

Top-level skills invoked directly by users. May delegate to sub-skills.

- Collect user input
- Call utility skills (e.g. `/detect-stack`)
- Delegate to language-specific sub-skills
- Produce output (reports, files, diagrams)

Examples: `/review-pr`, `/document`

### `sub-skill`

Called by orchestrators, never directly by users. All context is provided by the caller.

- Do NOT ask the user for input
- Operate only on data passed by the orchestrator
- Return results to the orchestrator

### `utility`

Standalone skills that can be called by anyone (users or other skills).

- Self-contained, no delegation
- Can be used as building blocks

Examples: `/drawio`, `/detect-stack`

## Step Conventions

### Step structure

Each step in SKILL.md follows this pattern:

```markdown
## Step N — Title

Brief description of what this step does.

[Commands, logic, decision tables]
```

### Decision tables

Use Markdown tables for branching logic:

```markdown
| Condition | Action |
|-----------|--------|
| File exists | Load and continue |
| File missing | Ask user or generate it |
```

### User interaction points

Mark places where the agent should pause for user input:

```markdown
> "Present this to the user for review/approval."
```

## README.md Format

The skill's README serves as documentation:

```markdown
# /<skill-name> — Title

## Overview

What this skill does and when to use it.

## Input / Output

What the skill expects and what it produces.

## Design Decisions

Why it works this way.
```
