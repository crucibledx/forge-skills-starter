---
description: Review pull request changes for code quality, style, correctness, and potential issues
version: 1.0.0
type: orchestrator
language: "*"
requires:
  - /detect-stack
test:
  specimens:
    - specimen/python/fastapi
    - specimen/ts/express
---

# Review PR

Review a pull request's changes for code quality, style, correctness, and potential issues. Produces a structured review report.

## Step 1 — Identify the PR

Determine what to review:

| Scenario                       | Action                                 |
|--------------------------------|----------------------------------------|
| User provides PR URL or number | Fetch PR details from the remote       |
| User says "review my changes"  | Use `git diff` against the base branch |
| Working on a feature branch    | Diff against `main` or `master`        |

```bash
git log --oneline HEAD...main
git diff main...HEAD --stat
```

## Step 2 — Detect project stack

Call `/detect-stack` to understand the project's language, framework, and conventions.

## Step 3 — Get the diff

```bash
git diff main...HEAD
```

If the diff is large, scope to meaningful files:

- Skip generated files, lock files, and vendor directories
- Focus on source code, configuration, and test files

## Step 4 — Review for quality issues

Analyze each changed file for:

### Code Quality

| Check            | What to look for                                       |
|------------------|--------------------------------------------------------|
| Error handling   | Missing try/catch, unhandled promises, bare exceptions |
| Input validation | User input not validated, missing type checks          |
| Resource leaks   | Unclosed connections, file handles, streams            |
| Null safety      | Potential null/undefined access                        |

### Style & Consistency

| Check     | What to look for                        |
|-----------|-----------------------------------------|
| Naming    | Inconsistent naming conventions         |
| Structure | Functions too long, deeply nested logic |
| Imports   | Unused imports, missing imports         |
| Comments  | Outdated comments, commented-out code   |

### Correctness

| Check        | What to look for                                 |
|--------------|--------------------------------------------------|
| Logic errors | Off-by-one, wrong comparison, missing edge cases |
| Concurrency  | Race conditions, missing locks                   |
| Security     | SQL injection, XSS, hardcoded secrets            |
| Performance  | N+1 queries, unnecessary allocations             |

### Tests

| Check      | What to look for                            |
|------------|---------------------------------------------|
| Coverage   | New code without tests                      |
| Quality    | Tests that don't assert meaningful behavior |
| Edge cases | Missing boundary tests                      |

## Step 5 — Categorize findings

Classify each finding:

| Severity       | Meaning                                    | Action                |
|----------------|--------------------------------------------|-----------------------|
| **Critical**   | Bug, security issue, data loss risk        | Must fix before merge |
| **Warning**    | Code smell, potential issue                | Should fix            |
| **Suggestion** | Style improvement, refactoring opportunity | Nice to have          |
| **Praise**     | Good patterns, clean code                  | Acknowledge           |

## Step 6 — Generate review report

Produce a structured report:

```markdown
# PR Review Report

## Summary

- Files reviewed: N
- Findings: N critical, N warnings, N suggestions
- Overall: APPROVE / REQUEST_CHANGES / COMMENT

## Critical

- [file:line] Description of the issue

## Warnings

- [file:line] Description of the issue

## Suggestions

- [file:line] Description of the improvement

## Praise

- [file:line] What was done well
```

> "Here's my review. Would you like me to elaborate on any finding?"
