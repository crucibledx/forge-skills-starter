---
description: REST API design conventions and standards for the backend team
globs:
  - "**/routes/**"
  - "**/controllers/**"
  - "**/handlers/**"
  - "**/middleware/**"
  - "**/api/**"
---

# API Conventions

Follow these conventions when building or reviewing API endpoints.

## URL Design

- **Plural nouns** for resources: `/users`, `/orders`, `/products`
- **Nested resources** for ownership: `/users/:id/orders`
- **No verbs in URLs**: `/users`, not `/getUsers` or `/createUser`
- **Lowercase with hyphens**: `/order-items`, not `/orderItems` or `/order_items`
- **Version prefix**: `/v1/users` — bump only on breaking changes

## HTTP Methods

| Method | Purpose | Idempotent | Response |
|--------|---------|-----------|----------|
| GET | Read resource(s) | Yes | 200 + body |
| POST | Create resource | No | 201 + body + Location header |
| PUT | Replace resource | Yes | 200 + body |
| PATCH | Partial update | Yes | 200 + body |
| DELETE | Remove resource | Yes | 204 (no body) |

## Status Codes

| Code | When to use |
|------|-------------|
| 200 | Successful read or update |
| 201 | Resource created (POST) |
| 204 | Success, no content (DELETE) |
| 400 | Malformed request (invalid JSON, missing required field) |
| 401 | No valid authentication token |
| 403 | Authenticated but not authorized for this resource |
| 404 | Resource not found |
| 409 | Conflict (duplicate, version mismatch) |
| 422 | Validation failed (valid JSON but invalid data) |
| 429 | Rate limit exceeded |
| 500 | Unhandled server error |

## Error Response Shape

All errors return the same structure:

```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "Human-readable description",
    "details": [
      { "field": "email", "message": "must be a valid email address" }
    ]
  }
}
```

## Pagination

Use cursor-based pagination for large collections:

```
GET /users?cursor=abc123&limit=20
```

Response includes `meta.nextCursor`:

```json
{
  "data": [...],
  "meta": {
    "nextCursor": "def456",
    "hasMore": true
  }
}
```

## Request Validation

- **Validate at the boundary** — before any business logic
- **Use schema validation** — Zod, Joi, Pydantic, not manual checks
- **Return 422 with field details** — never generic "invalid request"
- **Sanitize inputs** — trim strings, normalize emails
