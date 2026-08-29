# CoreLink v1 developer documentation

**Maturity: Alpha documentation / draft contract**

This tree targets the API Contracts repository's immutable
`v1.0.0-draft` baseline. The reviewed public slice currently covers **Device**
and **Command** resources plus a canonical event envelope. Tenant provisioning,
integration callbacks and privileged administration are outside the public v1
boundary until separately reviewed.

## Start here

| Topic | Status | Source |
| --- | --- | --- |
| Public Device + Command API | Alpha / draft | [Public OpenAPI](https://github.com/CoreLinkPlatform/api-contracts/blob/main/openapi/corelink-public-v1.yaml) |
| Event envelope | Alpha / draft | [AsyncAPI](https://github.com/CoreLinkPlatform/api-contracts/blob/main/asyncapi/corelink-events-v1.yaml) |
| Authentication and tenant scope | Alpha quickstart | [30-minute quickstart](quickstart.md) + contract security definitions |
| TypeScript SDK | Prerelease Alpha | [sdk-typescript](https://github.com/CoreLinkPlatform/sdk-typescript) |
| Python SDK | Prerelease Alpha | [sdk-python](https://github.com/CoreLinkPlatform/sdk-python) |
| Java SDK | Scaffold / Planned | [sdk-java](https://github.com/CoreLinkPlatform/sdk-java) |
| CLI | Scaffold / Planned | [cli](https://github.com/CoreLinkPlatform/cli) |
| MCP server | Scaffold / Planned | [mcp-server](https://github.com/CoreLinkPlatform/mcp-server) |
| Mock server | Scaffold / Planned | [mock-server](https://github.com/CoreLinkPlatform/mock-server) |

## Navigation contract

### 1. Start here
Begin with the [30-minute v1 quickstart](quickstart.md) for bearer authentication,
tenant scoping, Device and Command calls, idempotency, failure handling and a
repeatable acceptance record. Content beyond the linked Device/Command contract
is **Planned**.

### 2. Guides
Device registration/lifecycle and commands are first because they are in the
current public draft. Telemetry, digital twin, webhooks and integrations remain
**Planned** until their public contracts and runtime parity are evidenced.

### 3. How-to
Partner/operator procedures will be added only with reproducible prerequisites,
failure handling and test evidence.

### 4. Reference
Use the versioned files in
[`api-contracts`](https://github.com/CoreLinkPlatform/api-contracts). This
repository explains usage; it does not fork schema definitions.

### 5. SDKs and tools
TypeScript/Python are generated prerelease clients. Other tool repositories are
not installable supported releases today.

### 6. Examples
Examples must pin their contract baseline and tested runtime/SDK version.

### 7. Operations
Release/migration/troubleshooting material must name its owner, rollback or
recovery path, and evidence when applicable.

## Contract rules carried into docs

- Public device identity is `corelink_device_id`.
- Provider/connector identifiers are implementation details.
- Every state-changing example must describe tenant scope, authorization,
  idempotency and expected problem responses.
- A draft or scaffold is never described as Stable/supported.
