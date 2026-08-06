# Documentation versions

| Docs version | Contract target | Status | Entry point |
| --- | --- | --- | --- |
| v1 | `corelink-public-v1.yaml` `1.0.0-draft` | Alpha documentation for a draft public boundary | [v1](v1/README.md) |

## Versioning policy

Documentation is versioned by the public CoreLink contract boundary, not by the
website deployment. A version remains **Alpha** while its referenced public
contract is draft/prerelease.

Breaking public-contract changes require a new major documentation tree. Minor
or patch additions may update the same tree only when the contract compatibility
policy permits them.

Every version landing page records:

- exact contract version/tag or immutable commit;
- supported resource surface;
- runtime/SDK maturity;
- known omissions;
- links to compatibility and changelog evidence.

Do not silently rewrite older version guidance to match a newer contract.
