# Awesome AI Security Engineering

Open-source tools, research, standards, and best practices for securing software that AI writes, powers, and operates, curated by the [AI Security Engineers Community](https://www.aiseceng.io/).

This repository is created and maintained by the [AI Security Engineers Community](https://www.aiseceng.io/). It is vendor-neutral: every entry is judged against the same [inclusion criteria](#inclusion-criteria), and anything affiliated with the maintainers' sponsor is labeled.

## Why it matters

AI changes software in three ways at once. **AI writes software**: coding assistants and agents produce code faster than people can review it. **AI lives inside software**: models, retrieval, agent memory, MCP servers and skills become components with their own attack surface. **AI operates software**: agents call APIs, use credentials and change real systems, so deterministic permissions end up in the hands of probabilistic systems.

Developers, AppSec, cloud/IAM, AI/ML, SOC and GRC teams each own a piece. Nobody necessarily owns the security of the whole AI-native system. That ownership gap is what AI Security Engineering addresses.

## What is AI Security Engineering?

> **AI Security Engineering** is the discipline of designing, building, testing, and defending AI-native software throughout its lifecycle, combining software security, AI engineering, and adversarial thinking to manage risks introduced by AI-assisted development, AI-powered applications, and autonomous agents.

It is an engineering role at the intersection of software engineering, security engineering and AI engineering, and it does not replace existing teams. The discipline is still forming, so definitions here are proposals for the community to refine. Read more in [foundations](foundations/what-is-ai-security-engineering.md).

## The lifecycle

Five complementary, iterative stages organize this list. Each page explains the stage and lists the matching resources.

| Stage | Question it answers | Page |
|---|---|---|
| Discover | What AI exists in our environment, and what can it reach? | [discover](lifecycle/discover.md) |
| Design | What are the trust boundaries, identities and permissions? | [design](lifecycle/design.md) |
| Build | How do we ship AI-assisted and AI-powered software securely? | [build](lifecycle/build.md) |
| Break | How does the system fail under adversarial conditions? | [break](lifecycle/break.md) |
| Defend | How do we detect, contain and respond at runtime? | [defend](lifecycle/defend.md) |

## Contents

- [Resources by lifecycle stage](#resources) (below)
- [Resources by technical domain](topics/README.md)
- [Full catalogue with license and verification details](resources/README.md)
- [Research and benchmarks](research/README.md), including a [VulnBench write-up](research/vulnbench.md)
- [Best practices](best-practices/README.md)
- [Learning and labs](learning/README.md)
- [Foundations: definition, responsibilities, frameworks](foundations/what-is-ai-security-engineering.md)
- [Community](community/README.md)
- [Contributing](CONTRIBUTING.md)

## Resources

Each resource appears once here, under its primary stage. Many span several stages; the stage pages and [topic index](topics/README.md) cross-reference the same canonical entries. Licenses shown are the verified license of the listed artifact; read the [catalogue](resources/README.md) for caveats such as mixed licensing or commercial add-ons.

<!-- BEGIN GENERATED: resources -->
### Discover

| Resource | What it is | Type | License |
|---|---|---|---|
| [agent-bom](resources/README.md#agent-bom) | Inventories local agent configs, MCP servers, skills and models, and emits CycloneDX/SPDX/SARIF. | Open-Source Tool | Apache-2.0 |
| [CycloneDX](resources/README.md#cyclonedx) | Bill-of-materials standard (ECMA-424) with ML-BOM support for models and datasets. | Open Standard / Protocol | Apache-2.0 |
| [Snyk Agent Scan](resources/README.md#snyk-agent-scan) | Discovers agent configurations, MCP servers and skills; deeper security analysis uses a Snyk-hosted API (open core). | Open-Source Tool | Apache-2.0 |

### Design

| Resource | What it is | Type | License |
|---|---|---|---|
| [CoSAI Secure Design Patterns for Agentic Systems](resources/README.md#cosai-secure-design-patterns-for-agentic-systems) | OASIS-hosted whitepapers and design patterns for MCP security and agentic identity and access management. | Reference Implementation | CC-BY-4.0 |
| [Microsoft Agent Governance Toolkit](resources/README.md#microsoft-agent-governance-toolkit) | Multi-language SDKs for agent policy enforcement, an MCP security gateway, agent identity and audit logging. | Open-Source Tool | MIT |
| [MITRE ATLAS](resources/README.md#mitre-atlas) | Knowledge base of adversary tactics, techniques and case studies against AI-enabled systems. | Open Security Framework | Apache-2.0 |
| [Model Context Protocol (MCP)](resources/README.md#model-context-protocol-mcp) | Open protocol connecting AI applications to tools and data, with an OAuth-based authorization model. | Open Standard / Protocol | Apache-2.0 |
| [Open Policy Agent (OPA)](resources/README.md#open-policy-agent-opa) | General-purpose policy engine (Rego) for deterministic authorization and policy-as-code. | Open-Source Tool | Apache-2.0 |
| [OWASP GenAI Security Project](resources/README.md#owasp-genai-security-project) | Umbrella OWASP project for LLM and agentic AI security guidance, cheat sheets and initiatives. | Open Security Framework | CC-BY-SA-4.0 |
| [OWASP Top 10 for Agentic Applications 2026](resources/README.md#owasp-top-10-for-agentic-applications-2026) | Peer-reviewed list of the ten most critical risks for autonomous, tool-using AI agents. | Open Security Framework | CC-BY-SA-4.0 |

### Build

| Resource | What it is | Type | License |
|---|---|---|---|
| [Cisco AI Defense Skill Scanner](resources/README.md#cisco-ai-defense-skill-scanner) | Scanner for agent skills using YAML/YARA rules and dataflow analysis, with SARIF output. | Open-Source Tool | Apache-2.0 |
| [Eclipse Enclave](resources/README.md#eclipse-enclave) | Runs coding agents in per-session Docker containers with a gateway that enforces network allowlists. | Open-Source Tool | MIT |
| [Fickling](resources/README.md#fickling) | Static analyzer, decompiler and safe loader hooks for Python pickle files, including PyTorch models. | Open-Source Tool | LGPL-3.0-or-later |
| [NeMo Guardrails](resources/README.md#nemo-guardrails) | Toolkit for adding programmable guardrails (input, output, dialog, retrieval) to LLM applications. | Open-Source Tool | Apache-2.0 |
| [Promptfoo](resources/README.md#promptfoo) | CLI and library for LLM evaluations and red-team testing, usable in CI. | Open-Source Tool | MIT |
| [sandbox-runtime](resources/README.md#sandbox-runtime) | Filesystem and network sandbox for running agent processes with restricted access. | Open-Source Tool | Apache-2.0 |
| [Sigstore model-transparency (model-signing)](resources/README.md#sigstore-model-transparency-model-signing) | Python library and CLI for signing and verifying ML model artifacts with Sigstore. | Open-Source Tool | Apache-2.0 |
| [Snyk VulnBench](resources/README.md#snyk-vulnbench) | Benchmark and study of how repeatable LLM-based vulnerability findings are, versus a deterministic SAST reference. | Benchmark | Apache-2.0 |

### Break

| Resource | What it is | Type | License |
|---|---|---|---|
| [AgentDojo](resources/README.md#agentdojo) | Dynamic benchmark environment for prompt-injection attacks and defenses against tool-using agents. | Benchmark | MIT |
| [Cybench](resources/README.md#cybench) | CTF-based benchmark of 40 tasks for evaluating the offensive cyber capabilities of LLM agents. | Benchmark | Apache-2.0 |
| [CyberSecEval (Purple Llama)](resources/README.md#cyberseceval-purple-llama) | Meta's cybersecurity benchmark suite for LLMs, including prompt injection, insecure code and autopatch tests. | Benchmark | MIT |
| [DeepTeam](resources/README.md#deepteam) | Open-source LLM red-teaming framework with vulnerability and attack modules and mappings to OWASP and NIST. | Open-Source Tool | Apache-2.0 |
| [garak](resources/README.md#garak) | LLM vulnerability scanner that probes models and applications with many attack and failure modes. | Open-Source Tool | Apache-2.0 |
| [Inspect AI](resources/README.md#inspect-ai) | Framework for reproducible LLM and agent evaluations with sandboxed tool execution. | Open-Source Tool | MIT |
| [MCPSecBench](resources/README.md#mcpsecbench) | Security benchmark for Model Context Protocol servers, clients and hosts. | Benchmark | MIT |
| [OWASP FinBot Agentic AI CTF](resources/README.md#owasp-finbot-agentic-ai-ctf) | Multi-agent financial-services app with agentic attack challenges (goal manipulation, prompt injection). | Learning / Lab | Apache-2.0 |
| [PyRIT](resources/README.md#pyrit) | Python framework for automated and human-assisted red teaming of generative AI systems. | Open-Source Tool | MIT |

### Defend

| Resource | What it is | Type | License |
|---|---|---|---|
| [Guardrails AI](resources/README.md#guardrails-ai) | Python framework for validating and structuring LLM inputs and outputs with pluggable validators. | Open-Source Tool | Apache-2.0 |
| [OpenTelemetry GenAI Semantic Conventions](resources/README.md#opentelemetry-genai-semantic-conventions) | Vendor-neutral span, metric and attribute conventions for tracing GenAI calls, agents and tool use. | Open Standard / Protocol | Apache-2.0 |
<!-- END GENERATED: resources -->

## Inclusion criteria

Only open-source software, qualifying open standards, and open research with reproducible artifacts are listed. A public website or a free tier is not enough.

- **Software:** public source, an identifiable open-source license (OSI-approved preferred), and meaningful functionality in the open-source version. Open-core projects qualify only for capabilities that are genuinely open.
- **Standards and frameworks:** publicly accessible specification, documented implementation rights, and a transparent development process. Formal standards, community frameworks and guidance are labeled differently.
- **Research:** open artifacts such as code, datasets, benchmark harnesses or reproducible experiments. A free paper alone does not qualify.
- **Quality:** engineering relevance, technical credibility, documentation, maintenance, distinctiveness. Stars are not a criterion.
- **Neutrality:** no placement based on sponsorship or brand, no proprietary products, and no projects maintained by direct competitors of the community's sponsor.

Full rules, including exclusions, are in [CONTRIBUTING.md](CONTRIBUTING.md). Candidates that were evaluated and rejected are recorded in the [research inventory](maintainers/research-inventory.md).

## Contributing

Suggest a resource with the [new resource issue form](.github/ISSUE_TEMPLATE/new-resource.yml) or open a pull request that edits [`data/resources.yml`](data/resources.yml) and runs `python scripts/generate.py`. Broken links, license concerns and taxonomy ideas have their own forms. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Community

The [AI Security Engineers Community](https://www.aiseceng.io/) runs local chapters and meetups for practitioners who build with AI and secure it. See [community](community/README.md).

## License

Repository content and scripts are released under the [MIT License](LICENSE). Listed projects keep their own licenses; check each before use.
