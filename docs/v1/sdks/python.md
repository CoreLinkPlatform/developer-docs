# Python SDK

**Maturity:** Prerelease Alpha

The `sdk-python` repository contains a generated Python client for the current draft public contract. It is not yet a Stable production-supported package, and public license/support policy must be resolved before supported publication.

## Contract provenance

Check `.corelink-contract.json`, `CODEGEN.md`, package metadata and release notes before use. A supported package must identify immutable contract provenance.

## Current use

For prerelease integration work:

- build/install using the repository's documented environment;
- configure base URL and bearer authentication through the generated client surface;
- keep tenant context explicit;
- follow OpenAPI-defined validation, idempotency and problem-response semantics;
- pin the client revision in reproducible environments.

Generated names may change while the SDK and contract are prerelease, so this guide does not invent a stable convenience layer.

## Do not

- hand-maintain generated schema/model files;
- assume package generation proves runtime parity;
- log bearer tokens or customer data in debug output;
- bypass tenant-scoped APIs with direct data-store/provider access;
- describe the package as Stable until PY-03 license/release/conformance gates pass.

## Regeneration

Use `sdk-python/CODEGEN.md`. Modify normative schemas in `api-contracts`, then regenerate and review the client diff.

## Compatibility

Supported Beta/Stable claims require the SDK, contract and accepted mock/sandbox/runtime revisions to be version-identifiable and conformance-tested.