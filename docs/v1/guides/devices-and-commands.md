# Devices and commands

**Maturity:** Alpha documentation / `1.0.0-draft`

Device and Command are the currently reviewed public v1 resource slice. Use the [30-minute quickstart](../quickstart.md) for complete curl examples.

## Device identity

Use `corelink_device_id` from CoreLink responses as the public device identity. Do not persist a provider's device ID as the application's CoreLink resource key.

A device model/capability boundary determines which operations are valid for a device. Applications should not infer supported commands from provider type or UI availability.

## Listing and reading devices

Device reads are tenant-scoped and paginated where defined by the OpenAPI contract. Preserve explicit tenant context and use the contract's pagination fields rather than assuming an unbounded collection.

## Creating devices

Device creation requires an allowed `device_model_id` and valid tenant authorization. Treat validation/conflict responses as state that needs reconciliation; do not generate provider records directly to bypass CoreLink lifecycle checks.

## Commands

Command submission is asynchronous. HTTP `201` means CoreLink accepted the command record; it does **not** prove execution on the physical device.

Command create requires `Idempotency-Key`. When retrying the same logical submission, reuse the same idempotency key. Use a new key for a new logical command.

Possible command states in the current contract include queued/dispatching/sent/acknowledged/succeeded/failed/timed-out/cancelled states. Consumers should display and reconcile the state returned by CoreLink rather than synthesizing a success state from the initial POST.

## Error and retry behavior

- Do not automatically retry `400`, `401`, `403` or `404`.
- Reconcile `409` rather than blindly resubmitting.
- Retrying a command POST requires the original idempotency key.
- Preserve `correlation_id` from problem responses for diagnosis.

## Provider boundary

Applications must not call provider command APIs directly as a fallback for unsupported CoreLink operations. Missing capability belongs in the CoreLink contract/runtime backlog, not in an application-specific bypass.