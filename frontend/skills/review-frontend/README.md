# /review-frontend

Review frontend code for React best practices, component patterns, accessibility, and performance.

## What it does

- Analyzes component structure and prop interfaces
- Checks for accessibility violations (ARIA, semantic HTML, keyboard nav)
- Reviews performance patterns (re-renders, bundle size, lazy loading)
- Validates hook usage (`useEffect` deps, memoization)
- Produces a structured review report with severity levels

## Usage

```
/review-frontend
```

Or point it at specific files:

```
/review-frontend src/components/Dashboard.tsx
```

## Depends on

- `/detect-stack` — to identify the frontend framework and tooling
