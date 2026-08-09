<div align="center">

# AI Resources Lifecycle Platform

**Design, develop, test, and deliver AI agent skills, rules, and workflows — in one place.**

[![Version](https://img.shields.io/badge/version-0.7.1-%23e84d00)](https://github.com/crucibledx/forge-skills-starter/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-%23a0aec0)](LICENSE)
[![Forge CLI](https://img.shields.io/badge/delivered_by-Forge_CLI-%23ffa940)](https://github.com/crucibledx/forge-cli)

</div>

**Fork this repo.** Build your team's AI resources with a structured lifecycle. Deliver them to any AI tool.

---

## What is this?

An **AI resource** is anything that shapes how an AI agent behaves:

| Type         | What it does                         | Example                            |
|--------------|--------------------------------------|------------------------------------|
| **Skill**    | Step-by-step instructions for a task | `/review-pr`, `/document`          |
| **Rule**     | Always-on constraint or convention   | `code-style`, `drawio-conventions` |
| **Workflow** | Multi-step process combining skills  | `document-project`                 |

This platform gives AI resources a **full engineering lifecycle** — design, develop, test against real code, version, and deliver — instead of scattering them across wikis and copy-paste threads.

## Why?

| Without a platform                           | With this platform                                     |
|----------------------------------------------|--------------------------------------------------------|
| Skills live in random docs or Slack messages | `skills/<name>/SKILL.md` — versioned, reviewed, tested |
| No way to know if a skill actually works     | Test against real project specimens on orphan branches |
| Every team invents their own structure       | Convention over configuration — structure IS the API   |
| Delivery is manual copy-paste per AI tool    | Deliver to Claude Code, Windsurf, Cursor automatically |

## Quick Start

```bash
# 1. Fork this repo, then clone your fork

# 2. Create your first resource
/create-resource "A skill that reviews database migrations for safety"

# The agent walks you through: Design → Develop → Test → Release
# Each phase also works standalone (/design-resource, /develop-resource, /test-resource)
```

> **Full guide:** [How to Create a Resource](docs/how-to-create-resource.md)

## How It Works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/crucibledx/assets/raw/main/platform/diagrams/dark/platform-flow.svg">
  <img alt="Platform Flow" src="https://github.com/crucibledx/assets/raw/main/platform/diagrams/light/platform-flow.svg">
</picture>

### Convention over configuration

Put a file in the right place — the platform discovers it. No config, no registration.

| What     | Convention                           | Discovered by                        |
|----------|--------------------------------------|--------------------------------------|
| Skill    | `skills/<name>/SKILL.md`             | `/create-resource`, `/test-resource` |
| Rule     | `rules/<name>.md`                    | `/create-resource`, Forge CLI        |
| Workflow | `workflows/<name>.md`                | `/create-resource`, Forge CLI        |
| Specimen | orphan branch `specimen/<lang>/<fw>` | `/test-resource`                     |

> **Deep dive:** [Platform Design](docs/platform-design.md)

### One orchestrator, three phases

`/create-resource` drives the full lifecycle. Each phase also works standalone:

| Phase   | Command             | What it does                                              |
|---------|---------------------|-----------------------------------------------------------|
| Design  | `/design-resource`  | Clarify requirements → design doc + architecture diagrams |
| Develop | `/develop-resource` | Scaffold → implement step by step → human review          |
| Test    | `/test-resource`    | Merge real project specimen → run skill → validate        |

### Testing with specimens

Specimens are **real project snapshots** on orphan git branches. They give skills realistic code to work against — without polluting `main`.

```bash
/test-resource review-pr specimen/python/fastapi
# → Creates test branch → merges specimen → runs skill → reports results
```

| Specimen                  | Description                    |
|---------------------------|--------------------------------|
| `specimen/python/fastapi` | FastAPI REST API service       |
| `specimen/ts/express`     | Express.js TypeScript REST API |

Delta branches (e.g. `specimen/python/fastapi-delta-docs`) add intentional issues for edge-case testing.

> **Guides:** [How to Test a Resource](docs/how-to-test-resource.md) · [How to Add a Specimen](docs/how-to-add-specimen.md)

## What's Included

Example resources to use, extend, or replace:

| Skills          | Type         | Description                                         |
|-----------------|--------------|-----------------------------------------------------|
| `/drawio`       | utility      | Generate draw.io diagrams with PNG/SVG/PDF export   |
| `/detect-stack` | utility      | Detect project language, framework, and build tools |
| `/review-pr`    | orchestrator | Review PR changes for quality and correctness       |
| `/document`     | orchestrator | Generate project docs with architecture diagrams    |

| Rules & Workflows         | Purpose                               |
|---------------------------|---------------------------------------|
| `drawio-conventions`      | Standards for clean draw.io diagrams  |
| `code-style`              | Coding conventions and best practices |
| `documentation-standards` | Documentation quality requirements    |
| `document-project`        | Workflow: end-to-end documentation    |

## Delivering to Team Repos

The platform builds resources. How you deliver them is flexible:

| Method                                                                   | How                                                     |
|--------------------------------------------------------------------------|---------------------------------------------------------|
| [**Forge CLI**](https://github.com/crucibledx/forge-cli) *(recommended)* | `forge init` → `forge sync` — auto-maps to each AI tool |
| **Git submodules**                                                       | Add this repo as a submodule, symlink what you need     |
| **Manual copy**                                                          | Copy from `skills/`, `rules/`, `workflows/` directly    |

> **Setup details:** [CONTRIBUTING.md — Delivering Resources](CONTRIBUTING.md#delivering-resources-to-team-repos)

## Repository Structure

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/crucibledx/assets/raw/main/platform/diagrams/dark/platform-structure.svg">
  <img alt="Platform Structure" src="https://github.com/crucibledx/assets/raw/main/platform/diagrams/light/platform-structure.svg">
</picture>

```
├── skills/              # AI skills         ← delivered to team repos
├── rules/               # Context rules     ← delivered to team repos
├── workflows/           # Workflows         ← delivered to team repos
│
├── docs/                # Platform docs & design artifacts
├── scripts/             # Test automation
└── .claude/skills/      # Meta-skills that power the lifecycle
```

**Shared** (`skills/`, `rules/`, `workflows/`) → delivered to your team's repos. **Platform** (everything else) → stays here, powers the lifecycle.

## Multi-Team / Monorepo Setup

Need team-scoped resources? The [`example/monorepo`](https://github.com/crucibledx/forge-skills-starter/tree/example/monorepo) branch shows how to organize resources for multiple teams in a single repo:

```
shared/       # Cross-team resources (every team gets these)
frontend/     # Frontend team — /review-frontend, /accessibility, react-conventions
backend/      # Backend team — /review-api, /database-migration, api-conventions
infra/        # Infra team — /review-terraform, /incident-runbook, terraform-conventions
```

Each team folder contains a full canonical layout (`skills/`, `rules/`, `workflows/`). With Forge, each team points their source at the repo with a `subdirectory` filter — or uses `include`/`exclude` globs for fine-grained control.

> **See the full example:** [`example/monorepo` branch](https://github.com/crucibledx/forge-skills-starter/tree/example/monorepo)

## Documentation

| Start here                                                 | Then explore                                           |
|------------------------------------------------------------|--------------------------------------------------------|
| [How to Create a Resource](docs/how-to-create-resource.md) | [Skill Specification](docs/skill-spec.md)              |
| [How to Test a Resource](docs/how-to-test-resource.md)     | [Platform Design](docs/platform-design.md)             |
| [How to Add a Specimen](docs/how-to-add-specimen.md)       | [Meta-Resources Design](docs/meta-resources/design.md) |
|                                                            | [Full Documentation Index](docs/README.md)             |

## Part of Crucible

The Skills Starter is the content platform of the [Crucible](https://crucibledx.dev) ecosystem. Build resources here, deliver them with [Forge CLI](https://github.com/crucibledx/forge-cli).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/crucibledx/assets/raw/main/crucible/diagrams/dark/crucible-ecosystem.svg">
  <img alt="Crucible Ecosystem" src="https://github.com/crucibledx/assets/raw/main/crucible/diagrams/light/crucible-ecosystem.svg">
</picture>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow and guidelines.

## License

[MIT](LICENSE)
