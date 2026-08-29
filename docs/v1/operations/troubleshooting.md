# Developer troubleshooting

Use this checklist before opening an issue. It separates credential/tenant problems, contract mismatches and environment failures.

## 1. Record the baseline

Capture safely:

- repository/client version or commit;
- API contract version/revision;
- target environment type (local/sandbox/hosted alpha, not secrets/host internals);
- CoreLink tenant/resource IDs needed to reproduce;
- HTTP status and `correlation_id`;
- timestamp/time zone.

## 2. Check environment health

If the environment exposes the documented readiness endpoint, verify it before debugging application code. A dependency/readiness failure should be resolved as an environment problem; do not assume an API write succeeded or failed solely from readiness state.

## 3. Check authentication and tenant scope

- `401`: verify token validity/expiry and approved credential source.
- `403`: verify membership/scope/role; do not alter tenant IDs to probe access.
- repeated `404`: verify the canonical CoreLink resource ID and authorized tenant.

## 4. Check contract/client compatibility

Confirm that examples, SDK generated code and runtime target the same version-identifiable contract boundary. A generated SDK can be newer/older than an environment; generation alone is not parity evidence.

## 5. Check write reconciliation

For commands or other idempotent writes, preserve the original idempotency key during retries. After a network timeout, read/reconcile state before generating a second logical operation.

## 6. Console-specific issues

Determine whether the UI is running in demo or live mode. Demo data is not live acceptance evidence. For live asset/geofence collection behavior, check the Console's `API-COMPATIBILITY.md` because canonical read-model gaps may be explicitly listed.

## 7. Report safely

Open an issue in the owning repository with minimal reproduction and sanitized evidence. Security vulnerabilities must follow the organization's private `SECURITY.md` process rather than a public issue.