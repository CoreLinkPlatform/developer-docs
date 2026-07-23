# CoreLink Developer Documentation

Developer-facing documentation for using CoreLink safely and consistently.
This repository is intentionally separate from the runtime: it explains the
stable public surface without exposing provider-specific implementation details.

## Current status

This repository is a documentation scaffold. Guides, tutorials and examples
have not been added yet; the API contract repository also has unpopulated
OpenAPI and AsyncAPI specifications. Do not treat this repository as a complete
developer portal today.

## Planned information architecture

- **Start here:** concepts, authentication and tenant-scoping overview.
- **Guides:** device registration, provisioning, telemetry, commands, digital
  twin, events, webhooks and integrations.
- **How-to guides:** common partner and operator workflows.
- **Reference:** links to versioned API and event contracts in `api-contracts`.
- **SDK and tools:** Python, TypeScript and Java SDKs, CLI, mock server and MCP
  server.
- **Examples:** runnable, pinned examples that use only documented public APIs.

## Documentation rules

- Write both Persian and English for architecture and operational material.
- Use `corelink_device_id` as the public device identifier.
- Document tenant scoping, required roles/scopes, failure responses and
  idempotency wherever an operation changes state.
- Never document raw upstream Traccar, OpenRemote or Keycloak structures as
  public CoreLink contracts.
- Mark planned capabilities clearly; examples must state their contract and
  platform version.

The platform's current architecture and delivery order are maintained in the
[`platform` repository](https://github.com/CoreLinkPlatform/platform).
