---
description: Review API endpoints for REST conventions, error handling, validation, security, and documentation
version: 1.0.0
type: orchestrator
language: "*"
requires:
  - /detect-stack
---

# Review API

Review API endpoint changes for REST conventions, error handling, input validation, security, and documentation. Produces a structured review report.

## Step 1 — Detect project stack

Call `/detect-stack` to identify the API framework (Express, FastAPI, Gin, Spring Boot, etc.) and middleware stack.

## Step 2 — Get the changes

```bash
git diff main...HEAD --stat
git diff main...HEAD -- 'src/routes/**' 'src/controllers/**' 'src/handlers/**' 'src/middleware/**'
```

## Step 3 — Review REST conventions

| Check | What to look for |
|-------|------------------|
| HTTP methods | GET for reads, POST for creates, PUT/PATCH for updates, DELETE for deletes |
| URL structure | Nouns not verbs (`/users`, not `/getUsers`), plural resources |
| Status codes | 200/201/204 for success, 400/401/403/404/409/422 for client errors, 500 for server errors |
| Response format | Consistent envelope (`{ data, error, meta }`) or flat JSON |
| Pagination | `?page=1&limit=20` or cursor-based for list endpoints |
| Versioning | `/v1/` prefix or `Accept` header versioning |

## Step 4 — Review error handling

| Check | What to look for |
|-------|------------------|
| Global handler | Unhandled exceptions caught by middleware, not crashing the process |
| Error format | Consistent error response shape with `code`, `message`, `details` |
| Validation errors | 422 with field-level error details, not generic 400 |
| Not found | 404 with resource type in message, not generic "not found" |
| Auth errors | 401 for missing auth, 403 for insufficient permissions — never 400 |

## Step 5 — Review input validation

| Check | What to look for |
|-------|------------------|
| Request body | Validated before use (Zod, Joi, Pydantic, etc.) |
| Path params | Type-checked (e.g., UUID format, numeric ID) |
| Query params | Validated and sanitized with defaults |
| File uploads | Size limits, type checks, virus scanning consideration |
| SQL injection | Parameterized queries, never string concatenation |

## Step 6 — Review security

| Check | What to look for |
|-------|------------------|
| Authentication | Protected routes require valid auth token |
| Authorization | Resource-level access checks, not just auth presence |
| Rate limiting | Applied to auth endpoints and expensive operations |
| CORS | Explicit origin allowlist, not `*` in production |
| Headers | Security headers (HSTS, X-Content-Type-Options, X-Frame-Options) |
| Secrets | No hardcoded API keys, tokens, or passwords |

## Step 7 — Generate review report

```markdown
# API Review Report

## Summary

- Endpoints reviewed: N
- Findings: N critical, N warnings, N suggestions
- Overall: APPROVE / REQUEST_CHANGES / COMMENT

## REST Conventions
- [file:line] Description

## Error Handling
- [file:line] Description

## Validation
- [file:line] Description

## Security
- [file:line] Description

## Praise
- [file:line] What was done well
```

> "Here's my API review. Want me to elaborate on any finding?"
