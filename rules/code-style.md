---
description: General coding conventions and best practices
globs:
  - "**/*.py"
  - "**/*.ts"
  - "**/*.js"
  - "**/*.go"
---

# Code Style

Follow these conventions when writing or reviewing code.

## General

- **Meaningful names** — variables, functions, and classes should describe their purpose
- **Small functions** — each function should do one thing. If it's longer than 30 lines, consider splitting
- **Early returns** — prefer guard clauses over nested if/else
- **No magic numbers** — use named constants for non-obvious values
- **Error handling** — never swallow errors silently. Log or propagate them.

## Python

- Follow PEP 8
- Use type hints for function signatures
- Use `pathlib.Path` over `os.path`
- Prefer f-strings over `.format()` or `%`
- Use dataclasses or Pydantic models for structured data

## TypeScript

- Use `const` by default, `let` when mutation is needed, never `var`
- Prefer `interface` over `type` for object shapes
- Use strict mode (`strict: true` in tsconfig)
- Prefer `async/await` over raw Promises
- Use `unknown` instead of `any` where possible

## Go

- Follow Effective Go guidelines
- Use `errors.New()` or `fmt.Errorf()` for error creation
- Return errors, don't panic
- Keep interfaces small (1-3 methods)
- Use table-driven tests

## Comments

- **Don't comment what** — the code should be self-explanatory
- **Comment why** — explain non-obvious decisions, workarounds, and trade-offs
- **No commented-out code** — use version control instead
- **Update or delete** — stale comments are worse than no comments
