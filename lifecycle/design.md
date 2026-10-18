# Design

Establish secure architectures and trust boundaries before agents get access to anything.

**Capabilities:** AI and agentic threat modeling, secure AI reference architectures, trust boundary analysis, agent identity and authorization, least privilege, credential management, secure tool invocation, MCP security architecture, secure multi-agent communication, memory and context isolation, data security, human approval boundaries, policy as code.

**Practical starting points:** use the OWASP and MITRE ATLAS vocabularies to enumerate threats; treat every tool an agent can call as a privilege grant; express permissions as policy that a deterministic engine enforces rather than as instructions inside a prompt.

## Resources

<!-- BEGIN GENERATED: stage -->
| Resource | What it is | Type | License |
|---|---|---|---|
| [CoSAI Secure Design Patterns for Agentic Systems](../resources/README.md#cosai-secure-design-patterns-for-agentic-systems) | OASIS-hosted whitepapers and design patterns for MCP security and agentic identity and access management. | Reference Implementation | CC-BY-4.0 |
| [Microsoft Agent Governance Toolkit](../resources/README.md#microsoft-agent-governance-toolkit) | Multi-language SDKs for agent policy enforcement, an MCP security gateway, agent identity and audit logging. Also: Defend. | Open-Source Tool | MIT |
| [MITRE ATLAS](../resources/README.md#mitre-atlas) | Knowledge base of adversary tactics, techniques and case studies against AI-enabled systems. Also: Break. | Open Security Framework | Apache-2.0 |
| [Model Context Protocol (MCP)](../resources/README.md#model-context-protocol-mcp) | Open protocol connecting AI applications to tools and data, with an OAuth-based authorization model. Also: Build. | Open Standard / Protocol | Apache-2.0 |
| [Open Policy Agent (OPA)](../resources/README.md#open-policy-agent-opa) | General-purpose policy engine (Rego) for deterministic authorization and policy-as-code. Also: Defend. | Open-Source Tool | Apache-2.0 |
| [OWASP GenAI Security Project](../resources/README.md#owasp-genai-security-project) | Umbrella OWASP project for LLM and agentic AI security guidance, cheat sheets and initiatives. Also: Break. | Open Security Framework | CC-BY-SA-4.0 |
| [OWASP Top 10 for Agentic Applications 2026](../resources/README.md#owasp-top-10-for-agentic-applications-2026) | Peer-reviewed list of the ten most critical risks for autonomous, tool-using AI agents. Also: Break. | Open Security Framework | CC-BY-SA-4.0 |
<!-- END GENERATED: stage -->

Previous: [Discover](discover.md). Next: [Build](build.md).
