# Forge Skills Starter — Platform Design

> A **development + testing platform** for AI agent skills, rules, and workflows, delivered via Forge CLI.

### Diagrams

**Platform Flow** — the development lifecycle:

![Platform Flow](platform-flow.drawio.png)

**Convention Map** — repository structure, shared vs platform:

![Convention Map](convention-map.drawio.png)

---

## Architecture: Convention over Configuration

### The core idea

One architectural pattern drives everything: **Convention over Configuration**.

Inspired by Rails and modern monorepo tooling (Nx, Turborepo) — the directory structure **is** the architecture. No registration files, no config, no wiring. Put a file in the right place → the platform discovers it automatically.

### The Convention Table

| What       | Convention                                 | Auto-discovered by                     |
|------------|--------------------------------------------|----------------------------------------|
| Skill      | `skills/<name>/SKILL.md`                   | `/develop-skill`, `/test-skill`, Forge |
| Skill docs | `skills/<name>/README.md`                  | Developers browsing the repo           |
| Rule       | `rules/<name>.md`                          | Forge delivery tools                   |
| Workflow   | `workflows/<name>.md`                      | Forge delivery tools                   |
| Specimen   | orphan branch `specimen/<lang>/<fw>`       | `/test-skill`, `list_specimens.py`     |
| Delta      | branch `specimen/<lang>/<fw>-delta-<name>` | `/test-skill`, `list_specimens.py`     |

**That's the entire backbone.** Every new feature = a new file in the right place.

### Why Convention over Configuration?

| Need            | How CoC solves it                                      |
|-----------------|--------------------------------------------------------|
| **Scaling**     | New skill = new folder. No platform changes ever.      |
| **Onboarding**  | Learn the table above. That's it.                      |
| **Speed**       | No boilerplate, no config files, no registration       |
| **Consistency** | Same structure for every skill, enforced by convention |

---

## The Single Flow

One flow for everything. Two commands to learn:

```
/develop-skill  →  /test-skill  →  commit + tag
```

Expanded:

```
IDEA  ──→  /develop-skill  ──→  /test-skill  ──→  version bump  ──→  DONE
           │                    │
           ├── README.md        ├── merge specimen
           ├── SKILL.md         ├── run skill
           └── fill steps       ├── test report
                                └── iterate & fix
```

**For new contributors:** Two commands, one convention table, zero config.

---

## Shared vs Platform

### Key distinction

| Location            | Delivered to consumer repos? | Purpose                              |
|---------------------|------------------------------|--------------------------------------|
| `skills/`           | Yes (canonical)              | Executable skill definitions         |
| `rules/`            | Yes (canonical)              | Shared context rules                 |
| `workflows/`        | Yes (canonical)              | Shared workflows                     |
| `.claude/commands/` | No                           | Platform meta-skills (develop, test) |
| `scripts/`          | No                           | Test automation                      |
| `docs/`             | No                           | Design docs, guides                  |

### Forge layout strategy

This repo uses **canonical layout** for shared content (`skills/`, `rules/`, `workflows/`). The platform meta-skills live in `.claude/commands/` which is a **pre-structured** path.

When consumers add this repo as a Forge source, they should use `canonical` layout override:

```bash
forge source add
# → Layout: canonical
```

This ensures only `skills/`, `rules/`, and `workflows/` are synced. The `.claude/commands/` meta-skills stay local to this repo.

If `auto` layout is used, Forge may detect the repo as `hybrid` and attempt to sync `.claude/commands/` as well — which would deliver the development tools instead of just the shared skills.

---

## Skill Development Lifecycle

`/develop-skill` drives the full lifecycle:

```
 DESIGN            BUILD             TEST              RELEASE
 ┌──────────┐  ✓  ┌────────────┐  ✓  ┌──────────┐  ✓  ┌───────────┐
 │ README.md│ ──→ │ SKILL.md   │ ──→ │ specimen │ ──→ │ version++ │
 │ contracts│     │ fill steps │     │ /test    │     │ changelog │
 └──────────┘     └────────────┘     │ report   │     │ tag       │
                                     └──────────┘     └───────────┘
```

### DESIGN → `skills/<skill-name>/README.md`

| Artifact    | Purpose                                                  |
|-------------|----------------------------------------------------------|
| `README.md` | Purpose, scope, input/output contracts, design decisions |

### BUILD → `skills/<skill-name>/SKILL.md`

| Artifact   | Purpose                                |
|------------|----------------------------------------|
| `SKILL.md` | Executable skill (frontmatter + steps) |

### TEST

| Action         | Mechanism                                          |
|----------------|----------------------------------------------------|
| Merge specimen | `/test-skill` creates test branch, merges specimen |
| Run skill      | `/test-skill` invokes the skill                    |
| Report         | Test results documented                            |
| Iterate        | Fix skill → re-test until clean                    |

### RELEASE

| Action       | Mechanism                          |
|--------------|------------------------------------|
| Version bump | Skill frontmatter `version:` field |
| Changelog    | Platform `CHANGELOG.md`            |
| Tag          | `git tag -a v<x.y.z>`              |

---

## Specimen Evolution

Specimens are **real project snapshots** on orphan branches. Any skill that operates on source code can use them.

### Current specimens

| Specimen                  | Description                    |
|---------------------------|--------------------------------|
| `specimen/python/fastapi` | FastAPI REST API service       |
| `specimen/ts/express`     | Express.js TypeScript REST API |

Delta branches add targeted changes for testing specific skill behavior.

### When to add a new specimen

- New language/framework not covered
- Skill needs specific project structure (e.g. monorepo)
- Existing specimens don't exercise the skill's edge cases

---

## What This Design Does NOT Cover

- **CI/CD pipeline** — future work, could auto-run `/test-skill` on PR
- **Skill marketplace / discovery** — future work, skills are discovered by browsing `skills/`
- **Cross-repo skill dependencies** — future work, skills currently stand alone
