# TypeScript SDK

**Maturity:** Prerelease Alpha

The `sdk-typescript` repository contains a generated client for the current draft public contract. It is not yet a Stable production-supported package.

## Contract provenance

Before using a generated SDK build, check its `.corelink-contract.json`, README and release metadata. Supported publication must eventually reference an immutable contract tag/revision rather than a development branch.

## Current use

For contract exploration and early integration work:

1. inspect the SDK repository's package metadata and generated source;
2. install/build only using the repository's documented prerelease workflow;
3. configure the generated client's base URL/authentication using the generated API surface rather than copying private runtime code;
4. keep tenant IDs explicit in tenant-scoped operations;
5. preserve idempotency and problem-response behavior defined by the OpenAPI source.

Exact generated method/type names may change while the contract/client remains prerelease, so this guide intentionally does not freeze a hand-written wrapper API that is not part of the generated release.

## Do not

- treat a generated client as evidence that the runtime supports every generated operation;
- hand-edit generated `src/` files to change schemas;
- expose provider-specific identifiers as application resource IDs;
- claim Stable npm support before TS-03 release/conformance gates pass.

## Regeneration

Use `sdk-typescript/CODEGEN.md`. Contract changes belong in `api-contracts`; regenerate the client and review the generated diff.

## Compatibility

Runtime-contract-SDK compatibility must be demonstrated against an accepted mock/sandbox or runtime revision before supported Beta/Stable claims.