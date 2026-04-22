# Meta-Resources — Design

> AI resources that create other AI resources — one orchestrator, three phases, three resource types.

## What is an "AI resource"?

A reusable definition that shapes AI agent behavior:

| Resource type | What it is                                          | Convention               |
|---------------|-----------------------------------------------------|--------------------------|
| **Skill**     | Step-by-step instructions for a specific task       | `skills/<name>/SKILL.md` |
| **Rule**      | Always-on constraint (style, conventions, behavior) | `rules/<name>.md`        |
| **Workflow**  | Multi-step process combining skills and rules       | `workflows/<name>.md`    |

Think of them as composable building blocks — each type has different complexity, design needs, and test strategies.

## The Orchestrator Pattern

One command drives everything:

```
/create-resource "description"
  → /design-resource   (Phase 1: understand, classify, design.md + diagrams)
  → /develop-resource  (Phase 2: scaffold, implement step-by-step, review)
  → /test-resource     (Phase 3: auto-detect type, run test strategy)
  → release            (version bump, CHANGELOG, git tag)
```

Each phase is a standalone skill that also works as a subagent of the orchestrator. You can run any phase independently.

### Diagrams

**Architecture** — orchestrator, phases, resource types ([editable](architecture.drawio)):

![Architecture](architecture.drawio.png)

---

## Phase 1: `/design-resource`

Turn a vague idea into a structured design document.

### Steps

1. **Understand** — ask 5-10 clarifying questions (problem, input/output, scope, test strategy)
2. **Classify** — determine resource type (skill/rule/workflow), name, complexity
3. **Design** — create `docs/<name>/design.md` with purpose, contracts, steps, edge cases
4. **Diagrams** — create flow diagrams using `/drawio` skill (adapts by type)
5. **Review gate** — user reviews and approves before moving on

### Adapts by resource type

| Type     | Design artifacts                          |
|----------|-------------------------------------------|
| Skill    | design.md + flow.drawio + sequence.drawio |
| Rule     | design.md only (minimal: purpose + globs) |
| Workflow | design.md + flow.drawio (if complex)      |

### Output

```
docs/<name>/
  design.md         — purpose, contracts, steps, test strategy
  flow.drawio       — step flow with decision points
  flow.drawio.png   — exported PNG
```

---

## Phase 2: `/develop-resource`

Implement a resource based on the approved design.

### Steps

1. **Read design** — parse `docs/<name>/design.md` and diagrams
2. **Scaffold** — create resource files (frontmatter + structure, no implementation)
3. **Review gate** — user reviews scaffold before implementation begins
4. **Implement** — fill in each step/section, presenting each to user
5. **Review gate** — user reviews complete implementation
6. **Update references** — add to README tables, set version

### Adapts by resource type

| Type     | Output files                           |
|----------|----------------------------------------|
| Skill    | `skills/<name>/SKILL.md` + `README.md` |
| Rule     | `rules/<name>.md`                      |
| Workflow | `workflows/<name>.md`                  |

### Output

Implemented resource files in their canonical locations, ready for testing.

---

## Phase 3: `/test-resource`

Test a resource by auto-detecting its type and running the appropriate strategy.

### Steps

1. **Detect type** — check file location to determine resource type
2. **Read metadata** — parse frontmatter for test configuration
3. **Select strategy** — choose test approach by type
4. **Execute test** — run the strategy
5. **Generate report** — document pass/fail with details
6. **Iterate** — fix issues and re-test until clean

### Test strategies by type

| Resource type | Strategy       | How it works                                             |
|---------------|----------------|----------------------------------------------------------|
| **Skill**     | Specimen-based | Create test branch → merge specimen → run skill → report |
| **Rule**      | Validation     | Check frontmatter, structure, globs, content quality     |
| **Workflow**  | Scenario-based | Verify prerequisites, dry-run steps, check completeness  |

### Specimen-based testing (skills)

Specimens are **real project snapshots** on orphan branches. Any skill that operates on source code can use them.

```
specimen/python/fastapi           — FastAPI REST API service
specimen/python/fastapi-delta-*   — variants with intentional findings
specimen/ts/express               — Express.js TypeScript REST API
specimen/ts/express-delta-*       — variants with intentional findings
```

Test flow:

1. Save current state (commit WIP)
2. Create test branch: `test/<name>-<timestamp>`
3. Merge specimen: `git merge --allow-unrelated-histories specimen/<lang>/<fw>`
4. Run the skill against the merged code
5. Record results (pass/fail per step)
6. Return to original branch, delete test branch

---

## Tooling

### Skills used by the platform

| Skill     | Used by            | Purpose                             |
|-----------|--------------------|-------------------------------------|
| `/drawio` | `/design-resource` | Generate flow and sequence diagrams |

### Scripts

| Script                       | Purpose                                |
|------------------------------|----------------------------------------|
| `scripts/export_diagrams.sh` | Batch export `.drawio` → `.drawio.png` |
| `scripts/list_specimens.py`  | List available specimen branches       |

### Conventions

| Convention        | File                          | Purpose                              |
|-------------------|-------------------------------|--------------------------------------|
| Draw.io standards | `rules/drawio-conventions.md` | Diagram styling and export rules     |
| Skill format      | `docs/skill-spec.md`          | Frontmatter fields, step conventions |

---

## The Convention Table

The entire platform is built on this table:

| What       | Convention                                 | Discovered by                               |
|------------|--------------------------------------------|---------------------------------------------|
| Skill      | `skills/<name>/SKILL.md`                   | `/create-resource`, `/test-resource`, Forge |
| Skill docs | `skills/<name>/README.md`                  | Developers browsing the repo                |
| Design     | `docs/<name>/design.md`                    | `/design-resource`, `/develop-resource`     |
| Diagrams   | `docs/<name>/*.drawio`                     | `/design-resource`, `export_diagrams.sh`    |
| Rule       | `rules/<name>.md`                          | `/create-resource`, Forge                   |
| Workflow   | `workflows/<name>.md`                      | `/create-resource`, Forge                   |
| Specimen   | orphan branch `specimen/<lang>/<fw>`       | `/test-resource`, `list_specimens.py`       |
| Delta      | branch `specimen/<lang>/<fw>-delta-<name>` | `/test-resource`, `list_specimens.py`       |

**That's the entire backbone.** Every new feature = a new file in the right place.

---

## What This Design Does NOT Cover

- **Delivery mechanism** — handled by [Forge CLI](https://github.com/crucibledx/forge-cli)
- **CI/CD pipeline** — future work, could auto-run `/test-resource` on PR
- **Resource marketplace** — future work, resources are discovered by browsing the repo
- **Cross-repo dependencies** — future work, resources currently stand alone
- **Agent resource type** — future work, agents as autonomous entities with sub-agents and tool access

---

## Implementation Status

| Component                 | Status |
|---------------------------|--------|
| `/create-resource` skill  | ✅      |
| `/design-resource` skill  | ✅      |
| `/develop-resource` skill | ✅      |
| `/test-resource` skill    | ✅      |
| `/drawio` skill           | ✅      |
| Export script             | ✅      |
| Specimen branches         | ✅      |
| Architecture diagram      | ✅      |
| How-to guides             | ✅      |
