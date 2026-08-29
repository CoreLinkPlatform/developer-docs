# Authentication and tenant context

**Maturity:** Alpha documentation / `1.0.0-draft` public contract

The current public contract authenticates API requests with a Bearer JWT. It does not define a public self-service token-issuance endpoint, so client applications must obtain credentials through the approved environment/onboarding path rather than inventing an OAuth flow.

## Request boundary

For authenticated API operations:

```http
Authorization: Bearer <access-token>
```

Tenant-scoped resource paths also contain a tenant identifier. The path value selects a resource scope; authorization still comes from the authenticated actor, claims/scopes, membership and server-side policy.

## Rules for clients

- Never persist access tokens in source control, screenshots, issue bodies or application logs.
- Browser applications should prefer a server-side session/BFF design so CoreLink access tokens do not live in browser storage.
- Do not retry `401` or `403` with guessed tenant IDs or alternative credentials.
- Use least-privilege credentials for machine integrations.
- Treat credential rotation/revocation as normal lifecycle behavior.

## Failure semantics

- `401`: authentication is missing, invalid or no longer accepted.
- `403`: authentication succeeded but the actor is not allowed to perform the requested tenant-scoped operation.
- `404`: do not assume a resource exists in another tenant; tenant-safe APIs may intentionally avoid leaking existence.

## Service and partner credentials

Partner/service credential lifecycle is broader than the currently reviewed public Device/Command slice. Documentation may describe the security principles now, but installation or support claims for additional credential APIs must wait for their version-identifiable contract/runtime acceptance.

## Console boundary

The CoreLink Console uses an OIDC/Auth.js session and a server-side BFF so browser code does not store CoreLink bearer tokens. That architecture is an implementation reference, not a requirement that every non-browser consumer use Auth.js.