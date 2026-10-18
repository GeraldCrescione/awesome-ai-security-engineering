# Frameworks and standards

These are different kinds of things, and this repository labels them differently.

- **Open standard / protocol:** a specification with public text, implementation rights and open development. Example: MCP, CycloneDX.
- **Open security framework:** a community or institutional taxonomy or guidance that is openly licensed and openly developed, but is not an implementable protocol. Example: OWASP lists, MITRE ATLAS.
- **Guidance without an open specification:** useful context that does not meet the open criteria, so it is not listed.

## Listed

<!-- BEGIN GENERATED: standards -->
| Resource | What it is | Type | Lifecycle |
|---|---|---|---|
| [CycloneDX](../resources/README.md#cyclonedx) | Bill-of-materials standard (ECMA-424) with ML-BOM support for models and datasets. | Open Standard / Protocol | Discover, Build |
| [MITRE ATLAS](../resources/README.md#mitre-atlas) | Knowledge base of adversary tactics, techniques and case studies against AI-enabled systems. | Open Security Framework | Design, Break |
| [Model Context Protocol (MCP)](../resources/README.md#model-context-protocol-mcp) | Open protocol connecting AI applications to tools and data, with an OAuth-based authorization model. | Open Standard / Protocol | Design, Build |
| [OpenTelemetry GenAI Semantic Conventions](../resources/README.md#opentelemetry-genai-semantic-conventions) | Vendor-neutral span, metric and attribute conventions for tracing GenAI calls, agents and tool use. | Open Standard / Protocol | Defend |
| [OWASP GenAI Security Project](../resources/README.md#owasp-genai-security-project) | Umbrella OWASP project for LLM and agentic AI security guidance, cheat sheets and initiatives. | Open Security Framework | Design, Break |
| [OWASP Top 10 for Agentic Applications 2026](../resources/README.md#owasp-top-10-for-agentic-applications-2026) | Peer-reviewed list of the ten most critical risks for autonomous, tool-using AI agents. | Open Security Framework | Design, Break |
<!-- END GENERATED: standards -->

## Context that is not listed

**NIST AI Risk Management Framework** (AI RMF 1.0 and the Generative AI Profile, NIST AI 600-1) is widely used for AI risk governance. It is voluntary guidance from a public process, but it has no open repository or implementable specification, it is a risk-governance framework rather than an engineering control, and NIST states a revision is under way. It is therefore recorded in the [research inventory](../maintainers/research-inventory.md) rather than listed. Read it at <https://www.nist.gov/itl/ai-risk-management-framework>.

## How to use them together

- Use **OWASP lists and MITRE ATLAS** as the vocabulary for threat modeling and for scoping red-team tests ([Design](../lifecycle/design.md) and [Break](../lifecycle/break.md)).
- Use **MCP's authorization and security sections** as the baseline when you design or review tool integrations.
- Use **CycloneDX** to record models and datasets next to software dependencies so AI components appear in the same inventory.
- Use **OpenTelemetry conventions** so agent actions produce traces your existing tools can ingest.

A framework tells you what to worry about. It does not tell you that a control works. Pair every framework with tests ([Break](../lifecycle/break.md)).
