---
description: Create an AI resource end-to-end — orchestrates /design-resource → /develop-resource → /test-resource → release
---

# /create-resource

> One command to go from idea to tested, versioned resource.

This is the top-level orchestrator. It drives the full resource lifecycle by delegating to three phase skills as subagents.

## Inputs

The user may provide a description inline or the agent will ask.

- `{description}` — free-text description, file reference, or omitted (agent will ask)

## Steps

### 1. Gather intent

If `{description}` is not provided, ask:

> What resource do you want to create? Describe it in a few sentences, or point me to a file.

### 2. Check for existing work

Check if design or implementation already exists to allow phase skipping:

```
docs/<name>/design.md          → design exists
skills/<name>/SKILL.md         → skill implementation exists
rules/<name>.md                → rule implementation exists
workflows/<name>.md            → workflow implementation exists
```

If name is not yet known (first run), skip this check — it will be determined during design.

If design exists:
> Design already exists at `docs/<name>/design.md`. Skip to implementation?

If implementation exists:
> Implementation already exists. Skip to testing?

### 3. Phase 1 — Design

Delegate to `/design-resource` as a subagent with the description.

Follow all steps of `/design-resource` (understand, classify, design document, diagrams, approval gate).

After design is approved:

> ✓ Design approved
> - `docs/<name>/design.md`
> - `docs/<name>/flow.drawio` + `.drawio.png`
>
> Ready to move to implementation?

**Wait for user confirmation before proceeding.**

### 4. Phase 2 — Develop

Delegate to `/develop-resource {name}` as a subagent where `{name}` was determined during design.

Follow all steps of `/develop-resource` (read design, scaffold, review, implement step-by-step, review, version).

After implementation is approved:

> ✓ Implementation approved
> - (list of created files)
>
> Ready to test?

**Wait for user confirmation before proceeding.**

### 5. Phase 3 — Test

Delegate to `/test-resource {name}` as a subagent.

Follow all steps of `/test-resource` (detect type, read metadata, run test strategy, generate report).

Present test results:

> Test results:
> - (summary of pass/fail)
>
> If tests pass → proceed to release
> If tests fail → iterate (fix → re-test)

### 6. Handle test failures (if any)

If tests fail:

> Tests found issues. Options:
> 1. **Fix and re-test** — I'll help fix the issues, then re-run `/test-resource`
> 2. **Skip testing** — proceed to release anyway (not recommended)
> 3. **Abort** — stop here, come back later

If fix: go back to Step 4 (develop) or Step 5 (test) depending on the fix scope.

### 7. Release

Once tests pass (or user chooses to skip):

1. **Update resource version** — ensure `version: 0.1.0` in frontmatter
2. **Update platform CHANGELOG** — add entry to root `CHANGELOG.md`
3. **Commit + tag:**

```bash
git add -A
git commit -m "v<platform>: Add /<name> resource"
git tag -a v<platform> -m "v<platform>"
```

4. **Remind about push:**

```bash
git push origin main --follow-tags
```

### 8. Summary

Print final summary:

```
✓ Resource created: /<name>

Files:
  - docs/<name>/design.md
  - docs/<name>/flow.drawio + .drawio.png
  - skills/<name>/SKILL.md  (or rules/<name>.md, etc.)
  - skills/<name>/README.md

Version: v<platform>

Next steps:
  - Push: git push origin main --follow-tags
  - Test again: /test-resource <name>
  - Iterate: edit SKILL.md → /test-resource <name> → version bump
```

## Error Handling

| Error                          | Response                                           |
|--------------------------------|----------------------------------------------------|
| User cancels mid-phase         | Save progress, tell user how to resume             |
| Design rejected multiple times | Suggest breaking the resource into smaller pieces  |
| Test failures persist          | Suggest reviewing the design for missed edge cases |
| Resource name conflict         | Warn and suggest alternative name                  |
