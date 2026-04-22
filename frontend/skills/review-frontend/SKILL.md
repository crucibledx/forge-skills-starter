---
description: Review frontend code for React best practices, component patterns, accessibility, and performance
version: 1.0.0
type: orchestrator
language: "typescript"
requires:
  - /detect-stack
---

# Review Frontend

Review frontend code changes for React/UI best practices, component quality, accessibility, and performance. Produces a structured review report.

## Step 1 — Detect project stack

Call `/detect-stack` to confirm the frontend framework (React, Next.js, Vue, etc.) and identify the component library, state management, and styling approach.

## Step 2 — Get the changes

```bash
git diff main...HEAD --stat
git diff main...HEAD -- 'src/components/**' 'src/pages/**' 'src/hooks/**' 'src/styles/**'
```

Focus on component files, hooks, pages, and style files. Skip generated files, lock files, and node_modules.

## Step 3 — Review component patterns

| Check | What to look for |
|-------|------------------|
| Component size | Components over 200 lines should be split |
| Props interface | Missing or overly broad prop types (`any`) |
| State management | Local state vs global state — is the choice appropriate? |
| Side effects | `useEffect` with missing or incorrect dependency arrays |
| Memoization | Unnecessary `useMemo`/`useCallback` or missing where needed |
| Key props | Missing or non-unique `key` in lists |

## Step 4 — Review accessibility

| Check | What to look for |
|-------|------------------|
| Semantic HTML | `div` soup — missing `nav`, `main`, `section`, `article` |
| ARIA labels | Interactive elements without accessible names |
| Keyboard nav | Click handlers without keyboard equivalents |
| Alt text | Images without `alt` attributes |
| Focus management | Modals/dialogs that don't trap focus |
| Color contrast | Text that may not meet WCAG AA (4.5:1 ratio) |

## Step 5 — Review performance

| Check | What to look for |
|-------|------------------|
| Bundle size | Large imports that could be code-split or lazy loaded |
| Re-renders | Components re-rendering unnecessarily (missing memo) |
| Network | API calls in render path without caching/deduplication |
| Images | Unoptimized images, missing lazy loading |
| CSS | Unused styles, specificity wars, !important overuse |

## Step 6 — Generate review report

```markdown
# Frontend Review Report

## Summary

- Components reviewed: N
- Findings: N critical, N warnings, N suggestions
- Overall: APPROVE / REQUEST_CHANGES / COMMENT

## Component Quality
- [file:line] Description

## Accessibility
- [file:line] Description

## Performance
- [file:line] Description

## Praise
- [file:line] What was done well
```

> "Here's my frontend review. Want me to dig deeper into any area?"
