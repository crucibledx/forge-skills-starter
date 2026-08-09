---
description: "Phase 1: Turn a vague idea into a structured design with user approval — design.md + diagrams"
---

# /design-resource

> Turn an idea into a structured design document with diagrams.

Can be invoked standalone or as a subagent from `/create-resource`.

## Inputs

- `{description}` — free-text description of the resource to design

## Steps

### 1. Understand

Read the description. Ask clarifying questions (answer all at once is fine):

1. What problem does this resource solve?
2. What is the input? What triggers it?
3. What is the output?
4. Who invokes it — user directly, another resource, or automatically?
5. Does it need external tools or skills?
6. What's the scope — single resource or multi-resource system?
7. How should it be tested?
8. Any constraints (language, framework, etc.)?

### 2. Classify

Determine the resource type and characteristics:

| Classification | Options                                          |
|----------------|--------------------------------------------------|
| Resource type  | skill, rule, workflow                            |
| Skill type     | standalone, orchestrator, sub-skill, utility     |
| Complexity     | simple, medium, complex                          |
| Language scope  | `"*"` (any), or specific language               |
| Name           | kebab-case, descriptive (e.g. `add-e2e-scenario`) |

Present classification:

> Classification:
> - Resource type: skill
> - Name: `<name>`
> - Type: orchestrator
> - Language: `"*"`
>
> Does this look right?

### 3. Design

Create `docs/<name>/design.md` with:

- **Purpose** — what problem it solves
- **Input / Output contracts** — what goes in, what comes out
- **Steps outline** — high-level step plan
- **Sub-resource delegation** — if it calls other skills
- **Edge cases** — what could go wrong
- **Test strategy** — which specimens, what to validate

### 4. Diagrams

Create flow diagrams using the `/drawio` skill:

| Resource type | Diagrams                                            |
|---------------|-----------------------------------------------------|
| Skill         | `docs/<name>/flow.drawio` (step flow + decisions)   |
| Rule          | Skip (rules are simple enough without diagrams)     |
| Workflow      | `docs/<name>/flow.drawio` (if complex)              |

Export to PNG with embedded XML using `/drawio` skill or draw.io CLI.

### 5. Review gate

Present the design to the user:

> Here's the design for `/<name>`:
> - `docs/<name>/design.md` — (brief summary)
> - `docs/<name>/flow.drawio.png` — (open the image)
>
> Approve, or tell me what to change.

**Wait for explicit approval before completing.**

### Adapts by resource type

| Type     | Design artifacts                      |
|----------|---------------------------------------|
| Skill    | design.md + flow.drawio               |
| Rule     | design.md only (minimal: purpose + globs) |
| Workflow | design.md + flow.drawio (if complex)  |

## Output

Approved design in `docs/<name>/`:
- `design.md`
- `flow.drawio` + `.drawio.png` (if applicable)
