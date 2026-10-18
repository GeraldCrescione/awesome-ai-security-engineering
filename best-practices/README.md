# Engineering best practices

Community guidance, not a standard. These practices follow from the repository's principles and point to listed resources that help you apply them. They are written to be checked against your own risk, and corrections are welcome through [CONTRIBUTING.md](../CONTRIBUTING.md).

## 1. Put authorization in deterministic code, not in the prompt

An instruction such as "never delete production data" is a request to a probabilistic system. The permission itself must be enforced outside the model: scoped credentials, an allowlist of tools, and a policy engine or gateway that checks every call.

- Give each agent its own identity and the minimum scopes its task needs; avoid sharing a broad key between agents and humans.
- Express tool and action permissions as policy that can be reviewed and tested, for example with [Open Policy Agent](../resources/README.md#open-policy-agent-opa) or the policy layer in the [Microsoft Agent Governance Toolkit](../resources/README.md#microsoft-agent-governance-toolkit).
- Require human approval for irreversible or high-blast-radius actions.
- Start from the design patterns in [CoSAI Secure Design Patterns for Agentic Systems](../resources/README.md#cosai-secure-design-patterns-for-agentic-systems) and the authorization section of the [Model Context Protocol](../resources/README.md#model-context-protocol-mcp).

## 2. Treat every tool, skill and MCP server as supply chain

Agents pull tools and skills faster than people can read them.

- Inventory what is installed ([agent-bom](../resources/README.md#agent-bom), [CycloneDX](../resources/README.md#cyclonedx)).
- Scan skills before enabling them ([Cisco AI Defense Skill Scanner](../resources/README.md#cisco-ai-defense-skill-scanner)).
- Pin versions and review changes to tool descriptions; a tool whose description changes after approval deserves re-review.
- Sign and verify model artifacts ([Sigstore model-transparency](../resources/README.md#sigstore-model-transparency-model-signing)) and avoid loading untrusted pickle files ([Fickling](../resources/README.md#fickling)).

## 3. Contain coding agents

- Run agents in a sandbox with restricted filesystem and network access ([Eclipse Enclave](../resources/README.md#eclipse-enclave), [sandbox-runtime](../resources/README.md#sandbox-runtime)).
- Keep credentials out of the agent's environment where possible and issue short-lived, scoped ones.
- Log outbound requests and tool calls so an investigation has evidence.

## 4. Test adversarially, continuously, and repeatedly

- Threat model with the [OWASP Top 10 for Agentic Applications](../resources/README.md#owasp-top-10-for-agentic-applications-2026) and [MITRE ATLAS](../resources/README.md#mitre-atlas).
- Run automated red-team suites in CI ([garak](../resources/README.md#garak), [PyRIT](../resources/README.md#pyrit), [Promptfoo](../resources/README.md#promptfoo), [DeepTeam](../resources/README.md#deepteam)).
- Use benchmarks to compare defenses on a fixed task set ([AgentDojo](../resources/README.md#agentdojo), [MCPSecBench](../resources/README.md#mcpsecbench), [Inspect AI](../resources/README.md#inspect-ai)).
- Retest after every model, prompt, tool or policy change; results from one model version do not carry over.

## 5. Evaluate AI-based security tools before trusting them

AI-based tools add context and speed but vary from run to run. The [VulnBench write-up](../research/vulnbench.md) shows why.

- **Repeat.** Run the same analysis several times on the same input and record how often each finding recurs.
- **Separate agreement from correctness.** Compare against a deterministic reference, but remember a reference is another tool, not ground truth.
- **Do not auto-close on non-reproduction.** A finding that does not appear in a later run has not been shown to be fixed.
- **Do not auto-block on a single run** unless you have measured that tool's stability on your code.
- **Keep deterministic controls.** Use AI-based analysis to add coverage and context, and humans to judge which findings to trust, when to rerun and when to investigate.
- **Check cost against benefit.** Higher spend or a larger model did not reliably increase agreement in the published study; measure on your own workload.

## 6. Instrument agents like production services

- Emit traces for agent invocations and tool calls using the [OpenTelemetry GenAI conventions](../resources/README.md#opentelemetry-genai-semantic-conventions) so they flow into existing monitoring.
- Use guardrail frameworks ([NeMo Guardrails](../resources/README.md#nemo-guardrails), [Guardrails AI](../resources/README.md#guardrails-ai)) as additional filters, never as the only control.
- Prepare an AI incident runbook: how to revoke an agent identity, disable a tool, preserve traces and roll back changes.

## 7. Learn by attacking something safe

Practice on purpose-built targets before testing production. See [learning](../learning/README.md).

## Known gaps

No verified open-source resource was found for secure RAG implementation, data poisoning defenses, vibe-coding guardrails, shadow AI detection or agent-compromise incident response. If you know a qualifying project, [propose it](../CONTRIBUTING.md).
