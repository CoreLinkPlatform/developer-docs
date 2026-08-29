# Developer tools: Java, CLI, mock server, and MCP

These repositories are part of the CoreLink Developer Platform roadmap, but their current maturity is **Scaffold / Planned** unless a later release explicitly says otherwise.

## Java SDK

`CoreLinkPlatform/sdk-java` currently has no supported Java source/build/package baseline. Do not add dependency coordinates copied from an issue or planned design. JAVA-01/02/03 own generation, ergonomics and signed release/conformance work.

## CLI

`CoreLinkPlatform/cli` currently has no installable supported command. Documentation may describe intended authentication, tenant context and command boundaries, but must not show fake installation commands or imply an executable exists.

## Mock server

`CoreLinkPlatform/mock-server` is planned as a deterministic contract-driven local/CI runtime. The OpenAPI/AsyncAPI sources are **not empty**; the scaffold must consume reviewed versioned contracts from `api-contracts`. MOCK-01/02/03 own implementation, scenarios and packaged conformance.

## MCP server

`CoreLinkPlatform/mcp-server` is planned as an AI/MCP integration boundary. MCP-01 defines authorization/tenant/consent/audit requirements; MCP-02 owns read-only tools; state-changing MCP-03 work is separately gated; MCP-04 owns package/conformance.

An MCP tool must not bypass public CoreLink authorization by calling internal/provider interfaces with elevated credentials.

## Documentation rule

A scaffold page should answer:

- why the repository exists;
- what is and is not implemented;
- which contract/security decisions gate it;
- where executable backlog lives.

Installation and supported usage instructions are added only when a real artifact exists.