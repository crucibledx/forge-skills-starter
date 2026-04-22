---
description: React component conventions and best practices for the frontend team
globs:
  - "**/*.tsx"
  - "**/*.jsx"
---

# React Conventions

Follow these conventions when writing or reviewing React components.

## Component Structure

- **One component per file** — named exports, file name matches component name
- **Props interface above component** — named `<Component>Props`, always exported
- **Hooks at the top** — all `useState`, `useEffect`, `useMemo` before any logic
- **Early returns for loading/error** — guard clauses before the main render

```tsx
export interface DashboardProps {
  userId: string
  onLogout: () => void
}

export function Dashboard({ userId, onLogout }: DashboardProps) {
  const { data, isLoading, error } = useUser(userId)

  if (isLoading) return <Skeleton />
  if (error) return <ErrorBanner error={error} />

  return (/* ... */)
}
```

## Naming

| Thing | Convention | Example |
|-------|-----------|---------|
| Components | PascalCase | `UserProfile`, `OrderList` |
| Hooks | camelCase with `use` prefix | `useAuth`, `useDebounce` |
| Event handlers | `on` + event | `onClick`, `onSubmit`, `onFilterChange` |
| Boolean props | `is`/`has`/`should` prefix | `isOpen`, `hasError`, `shouldAnimate` |
| Constants | SCREAMING_SNAKE_CASE | `MAX_RETRIES`, `API_BASE_URL` |

## State Management

- **Local state first** — only lift to global when two or more unrelated components need it
- **Derived state** — compute from existing state, don't duplicate with `useState`
- **URL state** — filters, pagination, tabs belong in the URL, not component state

## Effects

- **Always list dependencies** — never use `// eslint-disable-next-line`
- **Cleanup subscriptions** — return a cleanup function from `useEffect`
- **Avoid effects for derived data** — use `useMemo` instead
- **Avoid effects for event handlers** — call functions directly in handlers

## Performance

- **Lazy load routes** — use `React.lazy` + `Suspense` for route-level code splitting
- **Memoize expensive computations** — `useMemo` for filtering/sorting large lists
- **Avoid inline objects/arrays in JSX** — they cause unnecessary re-renders
- **Use `React.memo`** only when profiling shows a re-render problem, not preemptively
