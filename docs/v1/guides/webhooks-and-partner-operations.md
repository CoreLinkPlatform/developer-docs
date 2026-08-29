# Webhooks and partner operations

**Maturity:** Planned/Alpha contract expansion; supported claims require API-03/API-04 and runtime acceptance.

CoreLink's partner boundary is intended to provide least-privilege machine credentials, webhook subscriptions/delivery, usage/entitlement visibility and supported operations for Console/partner integrations. These surfaces are broader than the current Device/Command public draft.

## Security principles

- credentials are tenant-scoped and least privilege;
- secrets are displayed/stored only where lifecycle semantics explicitly allow it;
- rotation and revocation must be auditable;
- webhook payloads use canonical CoreLink identifiers;
- signatures, timestamp/replay policy and retry behavior must be versioned;
- cross-tenant and insufficient-scope operations fail closed.

## Webhook consumer requirements

When the supported webhook contract is published, consumers should:

1. verify the documented signature before processing;
2. enforce replay/timestamp rules;
3. make handlers idempotent;
4. return only the documented success response after durable acceptance;
5. retain CoreLink correlation/delivery identifiers for diagnosis;
6. avoid logging secrets or full sensitive payloads unnecessarily.

## Retry and replay

Delivery retry/replay semantics are contract behavior, not an invitation for consumers to infer schedules from implementation. Do not build production assumptions from an internal provider's retry policy.

## Usage and entitlements

Usage, plan and entitlement surfaces may be visible in the CoreLink Console as implementation evolves. Public developer integrations must use versioned CoreLink contracts rather than reading billing/runtime tables or copying Console-internal payloads.

## Promotion rule

This guide can describe the intended safe integration boundary while the contract is draft. Concrete endpoints, signature algorithms, fields and supported retry schedules belong here only after their normative API-03/API-04 source is published and linked.