# Telemetry, location, and events

**Maturity:** contract/runtime work in progress; do not treat this page as a Stable public API reference.

CoreLink's product direction includes canonical telemetry observations, positions, latest state/history, events, retry/replay and delivery semantics. The private runtime has substantial implementation foundations, but broader public v1 contract slices are still gated by API-02/API-04 and runtime acceptance work.

## Canonical model principles

- normalize provider payloads into CoreLink-owned observation/position/event models;
- preserve canonical CoreLink device/tenant identity;
- define duplicate and out-of-order behavior deterministically;
- keep provider payloads out of public consumer contracts unless explicitly modeled;
- retain timestamps/source metadata needed to distinguish observation time from ingestion/processing time;
- apply tenant-safe retention, replay and history behavior.

## Latest state versus history

A latest-state projection is not a substitute for history. Clients should use the contract-defined resource suited to the task once the corresponding public contract is accepted. They should not reconstruct authoritative history from UI snapshots or provider-specific data.

## Events

The current contracts include a canonical event envelope, but supported event catalogs, delivery/replay behavior and webhook semantics require their own version-identifiable contract/runtime evidence.

## Implementation status rule

Examples for telemetry/location/events may be documented as draft when they identify the exact draft contract/revision. They must not be advertised as supported Beta/Stable journeys until the corresponding API-02/API-04 and runtime/conformance gates are accepted.

## Related work

- `api-contracts` API-02: Assets/bindings/telemetry/location/alerts public v1 expansion.
- `api-contracts` API-04: canonical AsyncAPI event/webhook schemas.
- `platform` PLAT-04/05: telemetry/history and event ordering/replay evidence.
- `developer-docs` DOCS-03: publish runnable supported guides when those inputs are version-identifiable.