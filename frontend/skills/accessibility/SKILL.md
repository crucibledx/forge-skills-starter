---
description: Audit a project for accessibility issues — WCAG compliance, ARIA usage, keyboard navigation, and screen reader support
version: 1.0.0
type: utility
language: "typescript"
---

# Accessibility Audit

Audit a frontend project for accessibility issues. Checks WCAG 2.1 AA compliance, ARIA usage, keyboard navigation, and screen reader support.

## Step 1 — Scan component files

Find all component files:

```bash
find src -name '*.tsx' -o -name '*.jsx' | grep -v '.test.' | grep -v '.spec.'
```

## Step 2 — Check semantic HTML

Scan each component for semantic HTML usage:

| Anti-pattern | Fix |
|-------------|-----|
| `<div onClick>` | Use `<button>` for actions |
| `<div>` wrapping page sections | Use `<main>`, `<nav>`, `<section>`, `<article>`, `<aside>` |
| `<span>` for headings | Use `<h1>`–`<h6>` in proper hierarchy |
| `<div>` for lists | Use `<ul>`/`<ol>` + `<li>` |
| `<a>` without `href` | Use `<button>` if it triggers an action, not navigation |

## Step 3 — Check ARIA attributes

| Check | What to look for |
|-------|------------------|
| Missing labels | Interactive elements without `aria-label` or visible label |
| Redundant ARIA | `role="button"` on `<button>` (already implicit) |
| Invalid values | `aria-hidden="true"` on focusable elements |
| Live regions | Dynamic content updates without `aria-live` |
| Expanded state | Collapsible sections without `aria-expanded` |

## Step 4 — Check keyboard navigation

| Check | What to look for |
|-------|------------------|
| Tab order | Custom `tabIndex` values greater than 0 |
| Focus visible | `:focus` styles removed without replacement |
| Focus trap | Modals/dialogs that don't trap focus or allow Escape to close |
| Skip links | No "Skip to main content" link for keyboard users |
| Custom controls | Sliders, dropdowns, etc. without keyboard support |

## Step 5 — Check images and media

| Check | What to look for |
|-------|------------------|
| Alt text | `<img>` without `alt` attribute |
| Decorative images | Decorative images should use `alt=""` and `aria-hidden="true"` |
| SVG accessibility | Inline SVGs without `role="img"` and `aria-label` |
| Video captions | `<video>` without `<track>` for captions |

## Step 6 — Produce audit report

```markdown
# Accessibility Audit Report

## Summary

- Files scanned: N
- Issues found: N critical, N warnings, N suggestions
- WCAG 2.1 AA compliance: PASS / FAIL

## Critical (must fix)

- [file:line] Description — WCAG criterion

## Warnings (should fix)

- [file:line] Description — WCAG criterion

## Suggestions

- [file:line] Improvement opportunity
```

> "Here's the accessibility audit. Want me to fix any of these issues?"
