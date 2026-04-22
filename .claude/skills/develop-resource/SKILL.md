---
description: "Phase 2: Implement a resource from an approved design — scaffold, implement step-by-step, review"
---

# /develop-resource

> Implement a resource based on an approved design.

Can be invoked standalone or as a subagent from `/create-resource`.

## Inputs

- `{name}` — the resource name (must have `docs/<name>/design.md`)
- `--from-scratch` — skip design requirement (for simple resources like rules)

## Steps

### 1. Read design

Read `docs/<name>/design.md` and any diagrams.

If design doesn't exist and `--from-scratch` is not set:

> No design found at `docs/<name>/design.md`. Options:
> 1. Run `/design-resource` first
> 2. Proceed without design (`--from-scratch`)

### 2. Determine resource type

If not already known from design, determine from the name or ask the user:

| Type     | Target files                               |
|----------|--------------------------------------------|
| Skill    | `skills/<name>/SKILL.md` + `README.md`     |
| Rule     | `rules/<name>.md`                          |
| Workflow | `workflows/<name>.md`                      |

### 3. Scaffold

Create resource files with structure but no implementation:

**For skills:**

```
skills/<name>/SKILL.md    — frontmatter + step headers (no content yet)
skills/<name>/README.md   — overview from design doc
```

**For rules:**

```
rules/<name>.md           — frontmatter (description, globs) + skeleton
```

**For workflows:**

```
workflows/<name>.md       — step headers (no content yet)
```

Present scaffold:

> Scaffold created:
> - (list files with brief description)
>
> Review the structure before I implement?

**Wait for user approval.**

### 4. Implement

Fill in each step/section, referencing the design doc:

- For skills: implement each step with commands, decision tables, user interaction points
- For rules: write the full rule content
- For workflows: implement each step with instructions

Present each step to the user as it's completed:

> Step N — `<title>`:
> (implementation)
>
> Good? Next step?

### 5. Review implementation

After all steps are complete, present the full resource:

> Implementation complete:
> - (list all files)
>
> Review the full resource — anything to adjust?

**Wait for user approval.**

### 6. Update platform references

- Add the new resource to `README.md` tables (skills, rules, or workflows section)
- Set `version: 1.0.0` in frontmatter (if applicable)

## Output

Implemented resource files in their canonical locations, ready for testing.
