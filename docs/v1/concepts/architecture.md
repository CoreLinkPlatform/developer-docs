# CoreLink architecture for developers

**Maturity:** Alpha documentation

CoreLink exposes a provider-neutral product boundary in front of device/connectivity engines, identity infrastructure, data stores, and integration providers. Application code should depend on CoreLink contracts rather than provider-specific APIs or identifiers.

## Product boundary

```text
Application / Console / SDK / CLI / MCP
                 |
                 v
        CoreLink public contracts
                 |
      +----------+-----------+
      |                      |
  Core runtime          Event/Webhook boundary
      |
  Integration adapters
      |
  Device/connectivity providers
```

The public boundary is intentionally narrower than the private runtime implementation. A capability being implemented internally does not make it a supported public API.

## Canonical identity

Public resources use CoreLink-owned identifiers. For the current Device contract the public identifier is `corelink_device_id`. Provider IDs may be stored internally for adapter reconciliation but are not public resource identities.

## Tenant boundary

Public operations are tenant-scoped. Tenant identity in a path is not an authorization bypass: the authenticated actor must also be authorized for that tenant and operation. Applications must treat `401` and `403` as authorization failures, not as signals to try another tenant identifier.

## Contract-first consumers

- `api-contracts` is the normative source for OpenAPI, AsyncAPI and schemas.
- `developer-docs` explains how to use those contracts.
- generated SDKs must identify immutable contract provenance.
- Console, CLI, mock and MCP consumers must not create private alternative public schemas.

## Provider independence

Provider-specific behavior belongs behind Integration Adapter boundaries. Public docs, SDK types, error codes, examples, MCP tools and Console domain models should use CoreLink terminology unless a provider detail is explicitly part of an operator-only implementation document.

## Evidence before claims

CoreLink distinguishes implementation, deployment and Product Acceptance. A merged PR or green CI job is implementation evidence; supported maturity additionally requires the relevant contract, security, runtime/conformance, documentation and release gates.