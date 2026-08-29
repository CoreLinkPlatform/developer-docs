# CoreLink v1 developer documentation

**Maturity: Alpha documentation / `1.0.0-draft` public contract**

This tree targets the current public contract baseline. The reviewed public slice covers **Device** and **Command** resources plus a canonical event envelope. Broader telemetry/location, partner/webhook and developer-tool surfaces remain maturity-gated and are labeled explicitly below.

## Start here

1. [30-minute quickstart](quickstart.md) — bearer authentication, tenant scope, Device read/create and idempotent Command submission.
2. [Architecture](concepts/architecture.md) — CoreLink-owned public boundary and provider independence.
3. [Authentication and tenant context](concepts/tenancy-authentication.md) — auth, tenant scope and safe credential handling.

## Guides

- [Devices and commands](guides/devices-and-commands.md) — **Alpha / current draft public slice**.
- [Telemetry, location and events](guides/telemetry-location-events.md) — **work in progress; API/runtime gates remain open**.
- [Webhooks and partner operations](guides/webhooks-and-partner-operations.md) — **Planned/Alpha expansion; exact public endpoints/signatures remain contract-gated**.

## SDKs

- [TypeScript SDK](sdks/typescript.md) — **Prerelease Alpha**.
- [Python SDK](sdks/python.md) — **Prerelease Alpha**.
- Java SDK is **Scaffold/Planned**; see [developer tool maturity](tools/developer-tools.md).

## Developer tools

[Java SDK, CLI, mock server and MCP status](tools/developer-tools.md) documents current Scaffold/Planned boundaries and the backlog gates required before installation/support instructions are valid.

## Operations

- [Errors, retries and idempotency](operations/errors-retries-idempotency.md)
- [Troubleshooting](operations/troubleshooting.md)

## Reference

- [Compatibility](reference/compatibility.md)
- [Maturity vocabulary](reference/maturity.md)
- Normative contract compatibility/terminology: [`api-contracts/docs`](https://github.com/CoreLinkPlatform/api-contracts/tree/main/docs)

## Current surface matrix

| Surface | Current maturity | Authoritative source |
| --- | --- | --- |
| Public Device + Command API | Alpha / `1.0.0-draft` | [Public OpenAPI](https://github.com/CoreLinkPlatform/api-contracts/blob/main/openapi/corelink-public-v1.yaml) |
| Canonical event envelope | Alpha / draft | [AsyncAPI](https://github.com/CoreLinkPlatform/api-contracts/blob/main/asyncapi/corelink-events-v1.yaml) |
| TypeScript SDK | Prerelease Alpha | [sdk-typescript](https://github.com/CoreLinkPlatform/sdk-typescript) |
| Python SDK | Prerelease Alpha | [sdk-python](https://github.com/CoreLinkPlatform/sdk-python) |
| CoreLink Console | Alpha | [Console](https://github.com/CoreLinkPlatform/Console) |
| Java SDK | Scaffold / Planned | [sdk-java](https://github.com/CoreLinkPlatform/sdk-java) |
| CLI | Scaffold / Planned | [cli](https://github.com/CoreLinkPlatform/cli) |
| MCP server | Scaffold / Planned | [mcp-server](https://github.com/CoreLinkPlatform/mcp-server) |
| Mock server | Scaffold / Planned | [mock-server](https://github.com/CoreLinkPlatform/mock-server) |

## Documentation contract

- Public device identity is `corelink_device_id`.
- Provider/connector identifiers are implementation details, not public resource identities.
- State-changing examples document tenant scope, authorization, idempotency and expected failures.
- Normative schemas are linked from `api-contracts`, not forked into prose.
- Draft/scaffold content is never described as Stable.
- Implementation, deployment and Product Acceptance are distinct evidence states.
