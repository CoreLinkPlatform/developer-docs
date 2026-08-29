# Errors, retries, and idempotency

**Maturity:** Alpha documentation; exact responses remain defined by the versioned contract.

## Problem responses

Public API errors use the contract-defined problem response shape. Preserve `correlation_id` or equivalent diagnostic identifiers when escalating failures. Do not include bearer tokens or secrets in tickets/log extracts.

## Status-code handling

General client behavior for the current public slice:

- `400` — request is invalid; fix the request rather than retrying blindly.
- `401` — authentication is missing/invalid; refresh or replace credentials through the approved auth flow.
- `403` — actor is not authorized for the tenant/operation; do not try different tenant IDs as a workaround.
- `404` — resource is not available in the authorized scope; do not infer cross-tenant existence.
- `409` — state/idempotency conflict; reconcile before another write.
- `429` — only follow a retry policy when the active contract/environment documents it.
- `5xx` — may be transient, but retry only operations that are safe/idempotent under the documented contract.

## Command idempotency

Command creation requires `Idempotency-Key`. Reuse the same key when retrying the same logical command; use a new key for a new logical command.

A timeout does not prove that a write failed. Before creating a new logical write, use the contract's reconciliation/read path when available.

## Backoff

Clients should use bounded retry/backoff, preserve request/correlation context, and stop on deterministic authorization/validation failures. Do not build retry schedules from provider behavior unless CoreLink exposes that schedule as part of its contract.

## Observability

Log safe identifiers needed for support: CoreLink tenant/resource IDs, operation name, HTTP status, request/correlation identifier, client version and contract/runtime revision. Avoid raw credentials, unnecessary payload bodies and sensitive metadata.