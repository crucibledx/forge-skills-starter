# How to Create a New AI Resource

This guide walks you through creating any AI resource — skill, rule, or workflow — from idea to release.

## Prerequisites

- **Claude Code** (or compatible AI coding assistant) with the skills from `.claude/skills/`
- **Git** — for branching, tagging, and specimen testing

## The Fast Path: `/create-resource`

One command drives the full lifecycle:

```
/create-resource "A skill that generates architecture documentation with diagrams"
```

The orchestrator walks you through three phases with review gates between each:

```
IDEA  →  /design-resource  →  review  →  /develop-resource  →  review  →  /test-resource  →  RELEASE
```

You can stop after any phase and resume later — all progress is saved as files.

## Step-by-Step

### 1. Start with an idea

Describe what you want to build. This can be:

- **Inline text:** `/create-resource "A skill that reviews Java code quality"`
- **A file:** `/create-resource @docs/ideas/code-review.md`
- **A conversation:** Just start talking, then run `/create-resource`

### 2. Design phase (`/design-resource`)

The agent asks clarifying questions:

1. What problem does this resource solve?
2. What is the input? What triggers it?
3. What is the output?
4. Who invokes it?
5. Does it need external tools?
6. What's the scope?
7. How should it be tested?
8. Any constraints?

**Answer all at once** — no need to go one by one.

The agent then:

- **Classifies** the resource (skill / rule / workflow)
- **Creates** `docs/<name>/design.md` with purpose, contracts, steps, test strategy
- **Creates** diagrams (`docs/<name>/flow.drawio`, etc.)

**You review and approve** before moving on.

### 3. Develop phase (`/develop-resource`)

The agent reads your approved design and:

- **Scaffolds** the resource file structure (e.g., `skills/<name>/SKILL.md`, `README.md`)
- **You review** the scaffold (step titles, frontmatter)
- **Implements** each step one at a time
- **You review** each step before the next

### 4. Test phase (`/test-resource`)

The agent auto-detects the resource type and runs the appropriate test strategy:

| Resource type | Test strategy                                  |
|---------------|------------------------------------------------|
| Skill         | Specimen-based: merge real codebase, run skill |
| Rule          | Validation: frontmatter, structure, content    |
| Workflow      | Scenario-based: dry-run + prerequisite check   |

If tests fail → the agent helps you fix and re-test.

### 5. Release

Once tests pass:

1. Version bump in frontmatter (`version: 0.1.0`)
2. Platform `CHANGELOG.md` updated
3. Commit + tag
4. Push

## Running Phases Individually

You don't have to use `/create-resource`. Each phase works standalone:

```bash
# Design only (e.g., exploring an idea)
/design-resource "A skill that does X"

# Develop from existing design
/develop-resource my-skill

# Test an existing resource
/test-resource document
/test-resource document specimen/python/fastapi

# Develop without a design (simple resources)
/develop-resource my-rule --from-scratch
```

## What Gets Created

| Resource type | Files created                                                                |
|---------------|------------------------------------------------------------------------------|
| Skill         | `docs/<name>/design.md`, `skills/<name>/SKILL.md`, `skills/<name>/README.md` |
| Rule          | `docs/<name>/design.md`, `rules/<name>.md`                                   |
| Workflow      | `docs/<name>/design.md`, `workflows/<name>.md`                               |

Plus diagrams in `docs/<name>/` (flow.drawio, sequence.drawio, etc.).

## Tips

- **Answer all clarifying questions at once** — faster than going back and forth
- **Be specific about constraints** — language, framework, which specimens to test against
- **Review the design carefully** — fixing design issues early saves rework in development
- **Use `--from-scratch`** for simple resources — rules and small utilities don't need a full design phase
- **Test against multiple specimens** — if your skill supports multiple frameworks, test each one

## Resuming Work

If you stopped mid-way, you can resume:

| What exists             | How to resume                    |
|-------------------------|----------------------------------|
| Nothing                 | `/create-resource "description"` |
| `docs/<name>/design.md` | `/develop-resource <name>`       |
| Design + implementation | `/test-resource <name>`          |

The orchestrator (`/create-resource`) also detects existing work and offers to skip completed phases.

## Example: Creating a skill

```
> /create-resource "A skill that generates architecture documentation with diagrams"

Agent: Let me ask a few questions...
  1. What problem? → Missing architecture docs
  2. Input? → Project source code
  3. Output? → Architecture docs + diagrams
  ...

Agent: Classification:
  Resource type: skill
  Name: document-architecture
  Type: orchestrator
  Language: *

You: Looks good

Agent: Design created at docs/document-architecture/design.md
       Flow diagram at docs/document-architecture/flow.drawio

You: Approved, let's implement

Agent: Scaffold created: skills/document-architecture/SKILL.md (4 steps)
       Step 1 — Analyze project structure... ready for review?

You: Looks good, next

... (step by step) ...

Agent: All tests pass. Ready to release?

You: Yes

Agent: ✓ Resource created: /document-architecture
       Push: git push origin main --follow-tags
```

## Related Docs

- [Skill Specification](skill-spec.md) — frontmatter fields, step conventions
- [How to Test a Resource](how-to-test-resource.md) — detailed testing guide with specimens
- [How to Add a Specimen](how-to-add-specimen.md) — creating test project snapshots
- [Platform Design](platform-design.md) — architecture overview
- [Meta-Resources Design](meta-resources/design.md) — detailed architecture of the resource lifecycle
