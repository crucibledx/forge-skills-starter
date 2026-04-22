---
description: End-to-end infrastructure review — Terraform audit, runbook check, and deployment readiness
---

# Deploy Review Workflow

Review infrastructure changes before deployment.

## Steps

1. **Review Terraform changes**

   ```
   /review-terraform
   ```

   Check security, blast radius, cost, and operational readiness.

2. **Run terraform plan**

   ```bash
   terraform plan -out=plan.tfplan
   ```

   Review the plan output. Confirm no unexpected destroys or replacements.

3. **Check runbook coverage**

   For any new services or infrastructure, ensure a runbook exists:

   ```
   /incident-runbook
   ```

4. **Verify monitoring**

   Confirm that new resources have:
   - CloudWatch/Datadog alerts configured
   - Dashboard panels added
   - Log groups created with retention policy

5. **Apply with approval**

   ```bash
   terraform apply plan.tfplan
   ```

   Verify resources are healthy after apply.
