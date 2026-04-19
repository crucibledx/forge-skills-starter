---
description: Scaffold and build a new skill through the full development lifecycle
disable-model-invocation: true
---

# Develop Skill

Create a new skill from an idea through design, implementation, and documentation.

**Usage:** `/develop-skill "A skill that does X"`

## Step 1 — Understand the request

Read the user's description. Clarify:

- What does the skill do?
- What type is it? (orchestrator, sub-skill, utility)
- What language(s) does it target? (`"*"` for any, or specific)
- Does it depend on other skills? (e.g. `/detect-stack`, `/drawio`)

If anything is unclear, ask before proceeding.

## Step 2 — Choose a name

Pick a kebab-case name for the skill:

- Short and descriptive (e.g. `detect-stack`, `review-pr`, `document`)
- Prefix sub-skills with the parent name (e.g. `review-pr-python`)

> "I'll call this skill `/<name>`. Sound good?"

## Step 3 — Create README.md

Create `skills/<name>/README.md` with:

```markdown
# /<name> — Title

## Overview

What this skill does and when to use it.

## Input / Output

What the skill expects and what it produces.

## Dependencies

Other skills or rules this skill uses.

## Design Decisions

Why it works this way.
```

> "Here's the README. Does this capture the intent correctly?"

Wait for user approval before continuing.

## Step 4 — Create SKILL.md

Create `skills/<name>/SKILL.md` with:

1. **Frontmatter** — description, version (start at 1.0.0), type, language, requires, test specimens
2. **Title** — `# <Skill Name>`
3. **Steps** — numbered steps with decision tables, commands, and user interaction points

Follow the format in `docs/skill-spec.md`.

> "Here's the skill definition. Review the steps — anything to add or change?"

Wait for user approval.

## Step 5 — Test plan

Determine testing approach:

| Question                        | Action                                      |
|---------------------------------|---------------------------------------------|
| Can existing specimens work?    | Add them to `test.specimens` in frontmatter |
| Need a new specimen?            | Note it for later (don't create now)        |
| Skill doesn't need source code? | Mark `test.specimens: []`                   |

## Step 6 — Update README.md skills table

Add the new skill to the root `README.md` skills table:

```markdown
| `/name` | 1.0.0 | type | Description |
```

## Step 7 — Test (if specimens available)

If compatible specimens exist:

```
/test-skill <name> <specimen>
```

Iterate on failures until the skill works correctly.

## Step 8 — Version and changelog

- Ensure `version: 1.0.0` in SKILL.md frontmatter
- Add entry to `CHANGELOG.md`

> "Skill `/<name>` is ready. Commit?"
