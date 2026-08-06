# 30-minute CoreLink v1 quickstart

**Maturity: Alpha documentation / `1.0.0-draft` public contract**

This quickstart exercises the currently reviewed public Device and Command slice
without depending on a prerelease SDK. It uses the versioned OpenAPI contract as
the source of truth:

- [CoreLink public v1 OpenAPI](https://github.com/CoreLinkPlatform/api-contracts/blob/main/openapi/corelink-public-v1.yaml)
- public authentication: bearer JWT;
- public tenant scope: `tenant_id` in the resource path;
- public device identity: `corelink_device_id`.

The contract is still draft. The examples below demonstrate the accepted
contract shape; they do not claim that a public production endpoint, self-service
token issuer, or Stable SDK release exists.

## Target outcome

Within 30 minutes you should be able to:

1. configure an assigned API base URL, bearer token and tenant;
2. verify readiness;
3. list the tenant's devices;
4. create a device when a valid `device_model_id` has been assigned;
5. create an idempotent command for that device;
6. inspect the command and recognize the standard failure responses.

## 0–5 min: prerequisites

You need values supplied by the CoreLink environment/operator:

- `CORELINK_API_URL` — base URL for the environment you are authorized to use;
- `CORELINK_ACCESS_TOKEN` — bearer JWT for that environment;
- `CORELINK_TENANT_ID` — UUID of the tenant you are authorized to access;
- `CORELINK_DEVICE_MODEL_ID` — UUID of an allowed device model if you will
  create a device.

The draft public contract does **not** define a token-issuance endpoint. Do not
invent or hard-code a client-secret flow in application code. Obtain credentials
through the environment's approved onboarding path.

Set the values in your shell without committing them:

```bash
export CORELINK_API_URL="https://api.example.invalid"
export CORELINK_ACCESS_TOKEN="<bearer-token>"
export CORELINK_TENANT_ID="<tenant-uuid>"
export CORELINK_DEVICE_MODEL_ID="<device-model-uuid>"
```

Use a real environment URL in place of `api.example.invalid`. Keep tokens out of
shell history, screenshots, issue bodies and source control where practical.

## 5–10 min: verify the environment

The readiness endpoint is intentionally unauthenticated:

```bash
curl --fail-with-body --silent --show-error \
  "$CORELINK_API_URL/health/ready"
```

A ready environment returns HTTP `200`. HTTP `503` means a dependency required
for traffic is unavailable; stop and resolve the environment before continuing.

## 10–15 min: list tenant-scoped devices

```bash
curl --fail-with-body --silent --show-error \
  -H "Authorization: Bearer $CORELINK_ACCESS_TOKEN" \
  "$CORELINK_API_URL/api/v1/tenants/$CORELINK_TENANT_ID/devices?limit=20&offset=0"
```

The response is a `DevicePage`. Device identifiers exposed by the public API are
`corelink_device_id`; connector/provider identifiers are not public resource
identities.

Expected authorization failures:

- `401` — authentication is missing or invalid;
- `403` — the caller is authenticated but cannot access the requested tenant
  or operation.

Never recover from `403` by changing the tenant ID to another tenant.

## 15–20 min: create a device

Skip this step if the environment has not assigned a valid
`CORELINK_DEVICE_MODEL_ID`.

```bash
DEVICE_RESPONSE="$(curl --fail-with-body --silent --show-error \
  -X POST \
  -H "Authorization: Bearer $CORELINK_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  "$CORELINK_API_URL/api/v1/tenants/$CORELINK_TENANT_ID/devices" \
  --data "{\"device_model_id\":\"$CORELINK_DEVICE_MODEL_ID\",\"name\":\"quickstart-device\",\"metadata\":{\"source\":\"docs-v1-quickstart\"}}")"

printf '%s\n' "$DEVICE_RESPONSE"
```

A successful create returns HTTP `201` and a `Device` containing
`corelink_device_id`. Record that value as `CORELINK_DEVICE_ID`:

```bash
export CORELINK_DEVICE_ID="<corelink-device-uuid>"
```

HTTP `400` means the request is invalid; `401`/`403` are authentication or
tenant/permission failures; `409` means the request conflicts with current
state.

## 20–25 min: submit one idempotent command

The command create operation requires `Idempotency-Key`. Reuse the same key
only when retrying the same logical command.

```bash
export CORELINK_IDEMPOTENCY_KEY="quickstart-$(date +%s)"

COMMAND_RESPONSE="$(curl --fail-with-body --silent --show-error \
  -X POST \
  -H "Authorization: Bearer $CORELINK_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $CORELINK_IDEMPOTENCY_KEY" \
  "$CORELINK_API_URL/api/v1/tenants/$CORELINK_TENANT_ID/devices/$CORELINK_DEVICE_ID/commands" \
  --data '{"command_type":"quickstart.ping","payload":{},"metadata":{"source":"docs-v1-quickstart"}}')"

printf '%s\n' "$COMMAND_RESPONSE"
```

A successful submission returns HTTP `201` and a `Command`. Record its
`command_id`:

```bash
export CORELINK_COMMAND_ID="<command-uuid>"
```

Command status is one of `queued`, `dispatching`, `sent`, `acknowledged`,
`succeeded`, `failed`, `timed_out`, or `cancelled`. A `201` response
means the command was accepted; it does not mean device execution succeeded.

## 25–30 min: inspect the command

```bash
curl --fail-with-body --silent --show-error \
  -H "Authorization: Bearer $CORELINK_ACCESS_TOKEN" \
  "$CORELINK_API_URL/api/v1/tenants/$CORELINK_TENANT_ID/devices/$CORELINK_DEVICE_ID/commands/$CORELINK_COMMAND_ID"
```

Expected failures use the contract's `application/problem+json` shape and carry
a `correlation_id` for diagnosis. Preserve that identifier when escalating an
unexpected error.

## Tenant-isolation check

If you have two explicitly authorized test tenants, repeat a read with the token
and tenant combination provided for each environment. A token must never gain
access merely because a caller changes `tenant_id` in the URL. Do not probe
tenants you are not authorized to test.

## Safe retry rules

- GET requests may be retried according to the environment's documented policy.
- For command POST retries, retain the original `Idempotency-Key`.
- Do not automatically retry `400`, `401`, `403`, or `404`.
- Treat `409` as a state/idempotency conflict that needs reconciliation.
- A readiness `503` is an environment/dependency failure, not proof that a
  write failed or succeeded.

## Definition of a successful quickstart

The quickstart is complete when the developer has retained:

- the environment/contract baseline used;
- the authorized tenant ID;
- one successful tenant-scoped read;
- one `corelink_device_id` from an existing or newly created device;
- one command ID plus its observed terminal or current state;
- any failure `correlation_id` needed for follow-up.

For SDK usage, sandbox packaging and broader resource guides, follow their
repository maturity. TypeScript/Python are prerelease Alpha; Java, CLI, MCP and
mock-server remain Scaffold/Planned until their release gates pass.
