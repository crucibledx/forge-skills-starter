---
description: End-to-end frontend component review — accessibility audit, code review, and performance check
---

# Component Review Workflow

Review a frontend component or page for quality, accessibility, and performance.

## Steps

1. **Run the accessibility audit**

   ```
   /accessibility
   ```

   Fix any critical issues before proceeding.

2. **Run the frontend review**

   ```
   /review-frontend
   ```

   Address component quality, hook patterns, and performance findings.

3. **Verify fixes**

   Re-run both skills on changed files to confirm all issues are resolved.

4. **Commit**

   ```bash
   git add src/
   git commit -m "fix: address review and accessibility findings"
   ```
