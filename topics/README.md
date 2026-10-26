# Resources by technical domain

The same canonical entries as the [lifecycle pages](../lifecycle/discover.md), grouped by technical domain. A resource can appear under several domains. Domains with no entry are known gaps, not oversights; see [CONTRIBUTING.md](../CONTRIBUTING.md) to propose a resource.

<!-- BEGIN GENERATED: topics -->
## AI-Assisted Development Security

| Resource | What it is | Lifecycle |
|---|---|---|
| [Cisco AI Defense Skill Scanner](../resources/README.md#cisco-ai-defense-skill-scanner) | Scanner for agent skills using YAML/YARA rules and dataflow analysis, with SARIF output. | Build |
| [CyberSecEval (Purple Llama)](../resources/README.md#cyberseceval-purple-llama) | Meta's cybersecurity benchmark suite for LLMs, including prompt injection, insecure code and autopatch tests. | Break |
| [Eclipse Enclave](../resources/README.md#eclipse-enclave) | Runs coding agents in per-session Docker containers with a gateway that enforces network allowlists. | Build |
| [sandbox-runtime](../resources/README.md#sandbox-runtime) | Filesystem and network sandbox for running agent processes with restricted access. | Build |
| [Snyk Agent Scan](../resources/README.md#snyk-agent-scan) | Discovers agent configurations, MCP servers and skills; deeper security analysis uses a Snyk-hosted API (open core). | Discover, Build |
| [Snyk VulnBench](../resources/README.md#snyk-vulnbench) | Benchmark and study of how repeatable LLM-based vulnerability findings are, versus a deterministic SAST reference. | Build, Break, Defend |

## LLM and Model Security

| Resource | What it is | Lifecycle |
|---|---|---|
| [CyberSecEval (Purple Llama)](../resources/README.md#cyberseceval-purple-llama) | Meta's cybersecurity benchmark suite for LLMs, including prompt injection, insecure code and autopatch tests. | Break |
| [DeepTeam](../resources/README.md#deepteam) | Open-source LLM red-teaming framework with vulnerability and attack modules and mappings to OWASP and NIST. | Break |
| [Fickling](../resources/README.md#fickling) | Static analyzer, decompiler and safe loader hooks for Python pickle files, including PyTorch models. | Build, Break |
| [garak](../resources/README.md#garak) | LLM vulnerability scanner that probes models and applications with many attack and failure modes. | Break |
| [Guardrails AI](../resources/README.md#guardrails-ai) | Python framework for validating and structuring LLM inputs and outputs with pluggable validators. | Defend |
| [Inspect AI](../resources/README.md#inspect-ai) | Framework for reproducible LLM and agent evaluations with sandboxed tool execution. | Break |
| [MITRE ATLAS](../resources/README.md#mitre-atlas) | Knowledge base of adversary tactics, techniques and case studies against AI-enabled systems. | Design, Break |
| [NeMo Guardrails](../resources/README.md#nemo-guardrails) | Toolkit for adding programmable guardrails (input, output, dialog, retrieval) to LLM applications. | Build, Defend |
| [OWASP GenAI Security Project](../resources/README.md#owasp-genai-security-project) | Umbrella OWASP project for LLM and agentic AI security guidance, cheat sheets and initiatives. | Design, Break |
| [Promptfoo](../resources/README.md#promptfoo) | CLI and library for LLM evaluations and red-team testing, usable in CI. | Build, Break |
| [PyRIT](../resources/README.md#pyrit) | Python framework for automated and human-assisted red teaming of generative AI systems. | Break |

## Agentic AI Security

| Resource | What it is | Lifecycle |
|---|---|---|
| [AgentDojo](../resources/README.md#agentdojo) | Dynamic benchmark environment for prompt-injection attacks and defenses against tool-using agents. | Break |
| [CoSAI Secure Design Patterns for Agentic Systems](../resources/README.md#cosai-secure-design-patterns-for-agentic-systems) | OASIS-hosted whitepapers and design patterns for MCP security and agentic identity and access management. | Design |
| [Cybench](../resources/README.md#cybench) | CTF-based benchmark of 40 tasks for evaluating the offensive cyber capabilities of LLM agents. | Break |
| [DeepTeam](../resources/README.md#deepteam) | Open-source LLM red-teaming framework with vulnerability and attack modules and mappings to OWASP and NIST. | Break |
| [Eclipse Enclave](../resources/README.md#eclipse-enclave) | Runs coding agents in per-session Docker containers with a gateway that enforces network allowlists. | Build |
| [Inspect AI](../resources/README.md#inspect-ai) | Framework for reproducible LLM and agent evaluations with sandboxed tool execution. | Break |
| [MCP Deception Incubator](../resources/README.md#mcp-deception-incubator) | Decoy Kubernetes MCP access portal on Cloudflare Workers that alerts when an AI agent probes for credentials or endpoints. | Build, Defend |
| [Microsoft Agent Governance Toolkit](../resources/README.md#microsoft-agent-governance-toolkit) | Multi-language SDKs for agent policy enforcement, an MCP security gateway, agent identity and audit logging. | Design, Defend |
| [MITRE ATLAS](../resources/README.md#mitre-atlas) | Knowledge base of adversary tactics, techniques and case studies against AI-enabled systems. | Design, Break |
| [OpenTelemetry GenAI Semantic Conventions](../resources/README.md#opentelemetry-genai-semantic-conventions) | Vendor-neutral span, metric and attribute conventions for tracing GenAI calls, agents and tool use. | Defend |
| [OWASP FinBot Agentic AI CTF](../resources/README.md#owasp-finbot-agentic-ai-ctf) | Multi-agent financial-services app with agentic attack challenges (goal manipulation, prompt injection). | Break |
| [OWASP GenAI Security Project](../resources/README.md#owasp-genai-security-project) | Umbrella OWASP project for LLM and agentic AI security guidance, cheat sheets and initiatives. | Design, Break |
| [OWASP Top 10 for Agentic Applications 2026](../resources/README.md#owasp-top-10-for-agentic-applications-2026) | Peer-reviewed list of the ten most critical risks for autonomous, tool-using AI agents. | Design, Break |
| [PyRIT](../resources/README.md#pyrit) | Python framework for automated and human-assisted red teaming of generative AI systems. | Break |
| [sandbox-runtime](../resources/README.md#sandbox-runtime) | Filesystem and network sandbox for running agent processes with restricted access. | Build |

## MCP and Agent Skills Security

| Resource | What it is | Lifecycle |
|---|---|---|
| [agent-bom](../resources/README.md#agent-bom) | Inventories local agent configs, MCP servers, skills and models, and emits CycloneDX/SPDX/SARIF. | Discover |
| [Cisco AI Defense Skill Scanner](../resources/README.md#cisco-ai-defense-skill-scanner) | Scanner for agent skills using YAML/YARA rules and dataflow analysis, with SARIF output. | Build |
| [CoSAI Secure Design Patterns for Agentic Systems](../resources/README.md#cosai-secure-design-patterns-for-agentic-systems) | OASIS-hosted whitepapers and design patterns for MCP security and agentic identity and access management. | Design |
| [MCP Deception Incubator](../resources/README.md#mcp-deception-incubator) | Decoy Kubernetes MCP access portal on Cloudflare Workers that alerts when an AI agent probes for credentials or endpoints. | Build, Defend |
| [MCPSecBench](../resources/README.md#mcpsecbench) | Security benchmark for Model Context Protocol servers, clients and hosts. | Break |
| [Microsoft Agent Governance Toolkit](../resources/README.md#microsoft-agent-governance-toolkit) | Multi-language SDKs for agent policy enforcement, an MCP security gateway, agent identity and audit logging. | Design, Defend |
| [Model Context Protocol (MCP)](../resources/README.md#model-context-protocol-mcp) | Open protocol connecting AI applications to tools and data, with an OAuth-based authorization model. | Design, Build |
| [Snyk Agent Scan](../resources/README.md#snyk-agent-scan) | Discovers agent configurations, MCP servers and skills; deeper security analysis uses a Snyk-hosted API (open core). | Discover, Build |

## AI Supply Chain Security

| Resource | What it is | Lifecycle |
|---|---|---|
| [agent-bom](../resources/README.md#agent-bom) | Inventories local agent configs, MCP servers, skills and models, and emits CycloneDX/SPDX/SARIF. | Discover |
| [Cisco AI Defense Skill Scanner](../resources/README.md#cisco-ai-defense-skill-scanner) | Scanner for agent skills using YAML/YARA rules and dataflow analysis, with SARIF output. | Build |
| [CycloneDX](../resources/README.md#cyclonedx) | Bill-of-materials standard (ECMA-424) with ML-BOM support for models and datasets. | Discover, Build |
| [Fickling](../resources/README.md#fickling) | Static analyzer, decompiler and safe loader hooks for Python pickle files, including PyTorch models. | Build, Break |
| [Sigstore model-transparency (model-signing)](../resources/README.md#sigstore-model-transparency-model-signing) | Python library and CLI for signing and verifying ML model artifacts with Sigstore. | Build |
| [Snyk Agent Scan](../resources/README.md#snyk-agent-scan) | Discovers agent configurations, MCP servers and skills; deeper security analysis uses a Snyk-hosted API (open core). | Discover, Build |

## Agent Identity and Access

| Resource | What it is | Lifecycle |
|---|---|---|
| [CoSAI Secure Design Patterns for Agentic Systems](../resources/README.md#cosai-secure-design-patterns-for-agentic-systems) | OASIS-hosted whitepapers and design patterns for MCP security and agentic identity and access management. | Design |
| [Microsoft Agent Governance Toolkit](../resources/README.md#microsoft-agent-governance-toolkit) | Multi-language SDKs for agent policy enforcement, an MCP security gateway, agent identity and audit logging. | Design, Defend |
| [Model Context Protocol (MCP)](../resources/README.md#model-context-protocol-mcp) | Open protocol connecting AI applications to tools and data, with an OAuth-based authorization model. | Design, Build |
| [Open Policy Agent (OPA)](../resources/README.md#open-policy-agent-opa) | General-purpose policy engine (Rego) for deterministic authorization and policy-as-code. | Design, Defend |
| [OWASP Top 10 for Agentic Applications 2026](../resources/README.md#owasp-top-10-for-agentic-applications-2026) | Peer-reviewed list of the ten most critical risks for autonomous, tool-using AI agents. | Design, Break |

## Data and RAG Security

| Resource | What it is | Lifecycle |
|---|---|---|
| [NeMo Guardrails](../resources/README.md#nemo-guardrails) | Toolkit for adding programmable guardrails (input, output, dialog, retrieval) to LLM applications. | Build, Defend |

## AI Red Teaming and Evaluations

| Resource | What it is | Lifecycle |
|---|---|---|
| [AgentDojo](../resources/README.md#agentdojo) | Dynamic benchmark environment for prompt-injection attacks and defenses against tool-using agents. | Break |
| [Cybench](../resources/README.md#cybench) | CTF-based benchmark of 40 tasks for evaluating the offensive cyber capabilities of LLM agents. | Break |
| [CyberSecEval (Purple Llama)](../resources/README.md#cyberseceval-purple-llama) | Meta's cybersecurity benchmark suite for LLMs, including prompt injection, insecure code and autopatch tests. | Break |
| [DeepTeam](../resources/README.md#deepteam) | Open-source LLM red-teaming framework with vulnerability and attack modules and mappings to OWASP and NIST. | Break |
| [garak](../resources/README.md#garak) | LLM vulnerability scanner that probes models and applications with many attack and failure modes. | Break |
| [Inspect AI](../resources/README.md#inspect-ai) | Framework for reproducible LLM and agent evaluations with sandboxed tool execution. | Break |
| [MCPSecBench](../resources/README.md#mcpsecbench) | Security benchmark for Model Context Protocol servers, clients and hosts. | Break |
| [OWASP FinBot Agentic AI CTF](../resources/README.md#owasp-finbot-agentic-ai-ctf) | Multi-agent financial-services app with agentic attack challenges (goal manipulation, prompt injection). | Break |
| [Promptfoo](../resources/README.md#promptfoo) | CLI and library for LLM evaluations and red-team testing, usable in CI. | Build, Break |
| [PyRIT](../resources/README.md#pyrit) | Python framework for automated and human-assisted red teaming of generative AI systems. | Break |
| [Snyk VulnBench](../resources/README.md#snyk-vulnbench) | Benchmark and study of how repeatable LLM-based vulnerability findings are, versus a deterministic SAST reference. | Build, Break, Defend |

## AI Runtime Security

| Resource | What it is | Lifecycle |
|---|---|---|
| [Guardrails AI](../resources/README.md#guardrails-ai) | Python framework for validating and structuring LLM inputs and outputs with pluggable validators. | Defend |
| [Microsoft Agent Governance Toolkit](../resources/README.md#microsoft-agent-governance-toolkit) | Multi-language SDKs for agent policy enforcement, an MCP security gateway, agent identity and audit logging. | Design, Defend |
| [NeMo Guardrails](../resources/README.md#nemo-guardrails) | Toolkit for adding programmable guardrails (input, output, dialog, retrieval) to LLM applications. | Build, Defend |
| [Open Policy Agent (OPA)](../resources/README.md#open-policy-agent-opa) | General-purpose policy engine (Rego) for deterministic authorization and policy-as-code. | Design, Defend |
| [OpenTelemetry GenAI Semantic Conventions](../resources/README.md#opentelemetry-genai-semantic-conventions) | Vendor-neutral span, metric and attribute conventions for tracing GenAI calls, agents and tool use. | Defend |

## AI Security Governance and Engineering Controls

| Resource | What it is | Lifecycle |
|---|---|---|
| [agent-bom](../resources/README.md#agent-bom) | Inventories local agent configs, MCP servers, skills and models, and emits CycloneDX/SPDX/SARIF. | Discover |
| [CycloneDX](../resources/README.md#cyclonedx) | Bill-of-materials standard (ECMA-424) with ML-BOM support for models and datasets. | Discover, Build |
| [MITRE ATLAS](../resources/README.md#mitre-atlas) | Knowledge base of adversary tactics, techniques and case studies against AI-enabled systems. | Design, Break |
| [Open Policy Agent (OPA)](../resources/README.md#open-policy-agent-opa) | General-purpose policy engine (Rego) for deterministic authorization and policy-as-code. | Design, Defend |
| [OWASP GenAI Security Project](../resources/README.md#owasp-genai-security-project) | Umbrella OWASP project for LLM and agentic AI security guidance, cheat sheets and initiatives. | Design, Break |
| [OWASP Top 10 for Agentic Applications 2026](../resources/README.md#owasp-top-10-for-agentic-applications-2026) | Peer-reviewed list of the ten most critical risks for autonomous, tool-using AI agents. | Design, Break |
<!-- END GENERATED: topics -->
