---
description: End-to-end API review — endpoint quality, database migration safety, and documentation check
---

# API Review Workflow

Review backend API changes for quality, safety, and documentation.

## Steps

1. **Review API endpoints**

   ```
   /review-api
   ```

   Check REST conventions, error handling, validation, and security.

2. **Review database migrations** (if any)

   ```
   /database-migration
   ```

   Check reversibility, data safety, locking, and rollback strategy.

3. **Verify API documentation**

   Ensure new or changed endpoints are documented:
   - OpenAPI/Swagger spec updated
   - Request/response examples accurate
   - Error responses documented

4. **Run tests**

   ```bash
   npm test         # or pytest, go test, etc.
   ```

   Confirm all tests pass with the new changes.

5. **Commit**

   ```bash
   git add .
   git commit -m "review: address API review findings"
   ```
