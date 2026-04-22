# /review-api

Review API endpoints for REST conventions, error handling, validation, and security.

## What it does

- Validates REST conventions (methods, status codes, URL structure)
- Checks error handling and response consistency
- Reviews input validation and sanitization
- Audits security (auth, CORS, rate limiting, secrets)
- Produces a structured review report with severity levels

## Usage

```
/review-api
```

## Depends on

- `/detect-stack` — to identify the API framework and middleware
