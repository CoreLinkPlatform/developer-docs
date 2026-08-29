# Documentation versions

| Docs version | Contract target | Status | Entry point |
| --- | --- | --- | --- |
| v1 | `corelink-public-v1.yaml` `1.0.0-draft` | Alpha docs; Device/Command quickstart plus maturity-aware concepts/guides | [v1](v1/README.md) · [30-minute quickstart](v1/quickstart.md) |

## Versioning policy

Documentation is versioned by the public CoreLink contract boundary, not by website deployment or repository release cadence. A documentation version remains Alpha while its referenced public contract/runtime/tool surfaces remain draft/prerelease.

Breaking public-contract changes require a new major documentation tree and migration guidance. Compatible additions may extend the same tree only when contract compatibility policy permits them.

Every version landing page records:

- exact contract version/tag or immutable revision;
- supported resource surface;
- runtime/SDK/tool maturity;
- known omissions and contract-gated sections;
- compatibility and maturity references;
- operational/error/troubleshooting guidance appropriate to that boundary.

Do not silently rewrite older version guidance to match a newer incompatible contract.