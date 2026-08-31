# CoreLink Developer Documentation

[![Documentation](https://github.com/CoreLinkPlatform/developer-docs/actions/workflows/documentation.yml/badge.svg?branch=main)](https://github.com/CoreLinkPlatform/developer-docs/actions/workflows/documentation.yml)
[![Docs: v1](https://img.shields.io/badge/docs-v1-blue)](docs/v1/README.md)
[![Contract: 1.0.0-draft](https://img.shields.io/badge/contract-1.0.0--draft-orange)](https://github.com/CoreLinkPlatform/api-contracts)
[![Maturity: Pre-Stable](https://img.shields.io/badge/maturity-pre--stable-orange)](https://github.com/CoreLinkPlatform/.github/blob/main/REPOSITORY_MATURITY.md)

Developer-facing documentation for using CoreLink safely and consistently. Versioned contracts in [`api-contracts`](https://github.com/CoreLinkPlatform/api-contracts) define normative public API/event boundaries; this repository explains how developers use them without creating a second schema source of truth.

## Start here

- [Documentation versions](docs/README.md)
- [CoreLink v1 documentation](docs/v1/README.md)
- [30-minute v1 quickstart](docs/v1/quickstart.md)
- [Architecture](docs/v1/concepts/architecture.md)
- [Authentication and tenant context](docs/v1/concepts/tenancy-authentication.md)
- [Compatibility](docs/v1/reference/compatibility.md)
- [Maturity vocabulary](docs/v1/reference/maturity.md)

CoreLink v1 is not Stable. The public Device/Command contract is `1.0.0-draft`; TypeScript/Python clients are prerelease Alpha with immutable tagged-contract regeneration evidence; Java has an Experimental generated Java 17+ baseline but no supported public artifact; Console is Alpha; CLI, MCP server and mock server remain Scaffold/Planned. Control is a private operator surface and is not part of the public developer API contract.

## Documentation model

Each version can contain:

1. **Start here / Concepts** — architecture, authentication, tenancy and canonical identifiers.
2. **Guides** — task-oriented workflows, with maturity visible on every contract-gated surface.
3. **Reference** — links to normative versioned contracts and compatibility policy.
4. **SDKs and tools** — usage/status that reflects the owning repository's real maturity.
5. **Operations** — errors, retries, idempotency, troubleshooting, migration and support boundaries.

Content may describe planned/draft architecture before a supported release only when that maturity is explicit and no invented endpoint/package/command is presented as available.

## Documentation rules

- Use `corelink_device_id` and other canonical CoreLink identifiers on public surfaces.
- Document tenant scoping, authorization, failures and idempotency for state-changing operations.
- Never promote raw provider IDs, credentials or payload models into public CoreLink contracts.
- Link versioned contract definitions instead of copying schemas into prose.
- Use **Scaffold, Experimental, Alpha, Beta, Stable, Deprecated, Planned** consistently.
- Examples must identify their contract/runtime/SDK maturity.
- Browser guidance should prefer server-side session/BFF token handling where practical; do not normalize access tokens in browser storage.
- Security-sensitive reports follow the organization private reporting policy rather than public documentation issues.

## Bilingual documentation

English is the normative developer-doc language for the current v1 tree. Persian translations may be published for architecture/operations and user-facing onboarding when they can be kept version-aligned and pass the bilingual documentation checks defined by DOCS-05. A translation must link to the same contract revision and may not carry a different maturity claim.

## Ownership

- Product direction and milestone acceptance: [`product-planning`](https://github.com/CoreLinkPlatform/product-planning)
- Organization maturity/security/support/release policy: [`.github`](https://github.com/CoreLinkPlatform/.github)
- Normative API/event schemas: [`api-contracts`](https://github.com/CoreLinkPlatform/api-contracts)
- Implementation/deployment details: the owning repository (`platform`, `Console`, `Control`, SDK/tool repositories, website)
