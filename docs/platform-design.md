# AI Resource Lifecycle Platform — Design

> A **development lifecycle platform** for AI resources (skills, rules, workflows), delivered via Forge CLI.
>
> **AI resource** = a reusable definition that shapes AI agent behavior. See [README](../README.md) for the full definition.

### Diagrams

**Platform Flow** — the single development flow ([editable](https://github.com/crucibledx/assets/blob/main/platform/diagrams/platform-flow.drawio)):

![Platform Flow](https://github.com/crucibledx/assets/raw/main/platform/diagrams/platform-flow.svg)

**Convention Map** — repository structure: shared vs platform ([editable](https://github.com/crucibledx/assets/blob/main/platform/diagrams/platform-structure.drawio)):

![Convention Map](https://github.com/crucibledx/assets/raw/main/platform/diagrams/platform-structure.svg)

---

## Architecture: Convention over Configuration

### The core idea

One architectural pattern drives everything: **Convention over Configuration**.

Inspired by Rails and modern monorepo tooling (Nx, Turborepo) — the directory structure **is** the architecture. No registration files, no config, no wiring. Put a file in the right place → the platform discovers it automatically.

### The Convention Table (the entire foundation)

| What       | Convention                                 | Auto-discovered by                          |
|------------|--------------------------------------------|---------------------------------------------|
| Skill      | `skills/<name>/SKILL.md`                   | `/create-resource`, `/test-resource`, Forge |
| Skill docs | `skills/<name>/README.md`                  | Developers browsing the repo                |
| Design     | `docs/<resource-name>/design.md`           | `/design-resource`, `/develop-resource`     |
| Diagrams   | `docs/<resource-name>/*.drawio`            | `/design-resource`, draw.io CLI             |
| Rule       | `rules/<name>.md`                          | `/create-resource`, Forge                   |
| Workflow   | `workflows/<name>.md`                      | `/create-resource`, Forge                   |
| Specimen   | orphan branch `specimen/<lang>/<fw>`       | `/test-resource`, `list_specimens.py`       |
| Delta      | branch `specimen/<lang>/<fw>-delta-<name>` | `/test-resource`, `list_specimens.py`       |

**That's the entire backbone.** Every new feature = a new file in the right place.

### Why Convention over Configuration?

| Need            | How CoC solves it                                      |
|-----------------|--------------------------------------------------------|
| **Scaling**     | New skill = new folder. No platform changes ever.      |
| **Onboarding**  | Learn the table above. That's it.                      |
| **Speed**       | No boilerplate, no config files, no registration       |
| **Consistency** | Same structure for every skill, enforced by convention |

### What this is NOT

This is not DDD (no domain model), not Hexagonal (no ports/adapters), not microservices. The closest analogy: **a package registry monorepo** where each skill is a package with a manifest (frontmatter), tests (specimens), and docs (README).

---

## The Resource Lifecycle

One orchestrator command, three composable phases:

```
/create-resource  →  /design-resource  →  /develop-resource  →  /test-resource  →  release
```

Each phase is a standalone `.claude/skills/` entry that also works as a subagent of the orchestrator.

```
 DESIGN              DEVELOP             TEST                RELEASE
 ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌───────────┐
 │ design.md    │ →  │ SKILL.md     │ →  │ auto-detect  │ →  │ version++ │
 │ flow.drawio  │    │ scaffold     │    │ test strategy│    │ changelog │
 │ contracts    │    │ implement    │    │ report       │    │ tag       │
 └──────────────┘    └──────────────┘    └──────────────┘    └───────────┘
      ↑                   ↑                   ↑
   user reviews        user reviews        iterate on failures
```

**For new contributors:** One command (`/create-resource`), one convention table, zero config.

> See [Meta-Resources Design](meta-resources/design.md) for the detailed architecture with diagrams.

---

## Shared vs Platform

### Key distinction

| Location          | Delivered to consumer repos? | Purpose                                              |
|-------------------|------------------------------|------------------------------------------------------|
| `skills/`         | Yes (canonical)              | Executable skill definitions                         |
| `rules/`          | Yes (canonical)              | Shared context rules                                 |
| `workflows/`      | Yes (canonical)              | Shared workflows                                     |
| `.claude/skills/` | No                           | Platform meta-skills (create, design, develop, test) |
| `scripts/`        | No                           | Test automation                                      |
| `docs/`           | No                           | Design docs, guides, diagrams                        |

### Forge layout strategy

This repo uses **canonical layout** for shared content (`skills/`, `rules/`, `workflows/`). The platform meta-skills live in `.claude/skills/` which is a **pre-structured** path.

When consumers add this repo as a Forge source, they should use `canonical` layout override:

```bash
forge source add
# → Layout: canonical
```

This ensures only `skills/`, `rules/`, and `workflows/` are synced. The `.claude/skills/` meta-skills stay local to this repo.

If `auto` layout is used, Forge may detect the repo as `hybrid` and attempt to sync `.claude/skills/` as well — which would deliver the development tools instead of just the shared skills.

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

> See [How to Add a Specimen](how-to-add-specimen.md) for the full guide.

---

## What This Design Does NOT Cover

- **Delivery mechanism** — handled by [Forge CLI](https://github.com/crucibledx/forge-cli)
- **CI/CD pipeline** — future work, could auto-run `/test-resource` on PR
- **Resource marketplace / discovery** — future work, resources are discovered by browsing the repo
- **Cross-repo dependencies** — future work, resources currently stand alone
- **Agent resource type** — future work, agents as autonomous entities with sub-agents
