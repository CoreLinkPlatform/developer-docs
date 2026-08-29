# CoreLink Developer Documentation

Developer-facing documentation for using CoreLink safely and consistently.
The runtime remains the source of truth for implemented capability; versioned
contracts in [`api-contracts`](https://github.com/CoreLinkPlatform/api-contracts)
define the public API/event boundary.

## Documentation versions

- [Documentation index](docs/README.md)
- [v1 documentation](docs/v1/README.md) — targets the current `1.0.0-draft`
  public Device and Command contract and canonical event envelope.
- [30-minute v1 quickstart](docs/v1/quickstart.md) — bearer auth, tenant scope,
  Device creation/read and idempotent Command submission using the public contract.

CoreLink v1 is not a Stable release. TypeScript and Python clients are
prerelease; Java SDK, CLI, MCP server and mock server remain Scaffold/Planned.
Pages must keep those maturity boundaries visible.

## Information architecture

Each documentation version uses the same navigation:

1. Start here — concepts, authentication and tenant scoping.
2. Guides — task-oriented Device/Command/Event workflows backed by current contracts.
3. How-to — narrow partner/operator procedures with prerequisites and evidence.
4. Reference — immutable contract/schema links; definitions are not copied.
5. SDKs and tools — only clients/tools whose repository maturity is stated.
6. Examples — runnable examples pinned to contract and platform versions.
7. Operations — release, migration, troubleshooting and support boundaries.

A section may be listed before its content exists, but it must be marked
**Planned** rather than presented as delivered documentation.

## Documentation rules

- Write both Persian and English for architecture and operational material.
- Use `corelink_device_id` as the public device identifier.
- Document tenant scoping, required roles/scopes, failure responses and
  idempotency wherever an operation changes state.
- Never document raw upstream/provider structures as public CoreLink contracts.
- Link versioned contract definitions instead of maintaining a second schema copy.
- Mark maturity using Scaffold, Experimental, Alpha, Beta, Stable, Deprecated or Planned.
- Examples must state their contract and platform version and must not imply a
  production-supported SDK before its release gate passes.

Product direction and milestone acceptance live in
[`product-planning`](https://github.com/CoreLinkPlatform/product-planning);
implementation evidence stays in each owning repository.
