# Compatibility reference

Normative compatibility policy and the machine-readable contract matrix live in [`api-contracts/docs`](https://github.com/CoreLinkPlatform/api-contracts/tree/main/docs). This page explains how developers should interpret that information.

## Current public baseline

- Public OpenAPI: `corelink-public-v1.yaml`, `1.0.0-draft`.
- Current reviewed public slice: Device + Command.
- Event contract: canonical event envelope, with broader event/webhook acceptance still in progress.
- TypeScript/Python: generated prerelease Alpha consumers.
- Java/CLI/mock/MCP: Scaffold/Planned.
- Console: Alpha application; its repository documents runtime/API compatibility and known read-model gaps.

## Compatibility dimensions

A useful compatibility claim names all relevant boundaries:

1. contract revision/tag;
2. runtime release/SHA;
3. SDK/tool version when used;
4. mock/sandbox revision for conformance when applicable;
5. documentation version/maturity.

## Draft versus supported

An immutable draft tag is useful for reproducibility but is not a Stable support claim. A consumer may implement against a draft as long as its maturity is explicit.

## Breaking changes

Breaking public changes require a new major contract/migration decision. Generated clients should be regenerated from the new contract rather than patched manually.

## Console compatibility

Console fallbacks for APIs that are not yet available must remain documented implementation details. A UI working in demo/fallback mode does not prove that the corresponding public API is accepted.