# CoreLink maturity vocabulary

CoreLink uses shared maturity terms so repositories, docs, website copy and release notes do not turn implementation progress into unsupported product claims.

| Maturity | Meaning |
| --- | --- |
| Planned | Scope exists in product/backlog decisions but implementation may not exist. |
| Scaffold | Repository/structure exists but there is no supported executable/package surface. |
| Experimental | Implementation exists for exploration; compatibility/support may be intentionally weak. |
| Alpha | Usable implementation or contract exists, but scope/compatibility/acceptance can still change materially. |
| Beta | Supported target scope is substantially defined and validated, with remaining release-readiness limits explicit. |
| Stable | Versioned support, compatibility, documentation, security and release/operational gates are accepted. |
| Deprecated | Previously available behavior is being retired under a documented migration/removal policy. |

## Evidence rule

The following are **not sufficient by themselves** to promote maturity:

- public repository visibility;
- a generated SDK;
- a merged PR;
- green CI;
- a Docker image or package;
- a Git tag;
- a successful deployment;
- a UI demo.

Promotion must reconcile the owning repository's acceptance gate with relevant contract, runtime/conformance, security, documentation, release and product evidence.

The organization-level current inventory is maintained in `CoreLinkPlatform/.github/REPOSITORY_MATURITY.md`.