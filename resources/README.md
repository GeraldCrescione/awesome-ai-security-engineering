# Catalogue

Canonical, alphabetical entries with full metadata. This file is generated from [`data/resources.yml`](../data/resources.yml); edit that file, not this one.

How to read an entry:

- **License / status** is what was verified, with any caveat in parentheses.
- **Latest release evidence** shows what was found on the verification date. It is not a maintenance guarantee.
- **Verification** is `verified` when license and release evidence were both checked, or `partial` when something is noted as unconfirmed. A `direct` check was done from the primary source by a maintainer-run pass; `delegated` means a separate research pass read the primary source and a human spot-check is welcome.

<!-- BEGIN GENERATED: catalogue -->
## agent-bom

CLI and self-hosted dashboard that discovers agent configurations, MCP servers, skill and instruction files, AI models and datasets, then maps known package vulnerabilities to them.

- **Type:** Open-Source Tool
- **Lifecycle:** Discover
- **Domain:** AI Supply Chain Security; MCP and Agent Skills Security; AI Security Governance and Engineering Controls
- **License / status:** Apache-2.0
- **Official URL:** <https://github.com/msaad00/agent-bom>
- **Source / specification:** <https://github.com/msaad00/agent-bom>
- **Maintainer:** Individual maintainer (msaad00)
- **Latest release evidence:** v0.106.1 (27 Sep, year inferred as 2026)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/msaad00/agent-bom/main/LICENSE>
- **Notes:** Single-maintainer project with a fast release cadence; the only AI-asset discovery tool found that met the criteria.

## AgentDojo

Provides tasks, attacks and defenses to evaluate how tool-calling LLM agents resist prompt injection; published at NeurIPS 2024 (Datasets and Benchmarks track), arXiv 2406.13352.

- **Type:** Benchmark
- **Lifecycle:** Break
- **Domain:** Agentic AI Security; AI Red Teaming and Evaluations
- **License / status:** MIT (Code license read directly. Dataset terms are not separately stated.)
- **Official URL:** <https://agentdojo.spylab.ai/>
- **Source / specification:** <https://github.com/ethz-spylab/agentdojo>
- **Maintainer:** ETH Zurich SPY Lab
- **Latest release evidence:** 0.1.35 (2025-10-27, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/ethz-spylab/agentdojo/main/LICENSE>
- **Notes:** Last PyPI release is about a year old and the README warns the API is still developing. A research benchmark is still useful when its tasks stay fixed.

## Cisco AI Defense Skill Scanner

Static scanner that inspects agent skills for prompt injection, data exfiltration and malicious code patterns. Output integrates with code-scanning tools through SARIF.

- **Type:** Open-Source Tool
- **Lifecycle:** Build
- **Domain:** MCP and Agent Skills Security; AI Supply Chain Security; AI-Assisted Development Security
- **License / status:** Apache-2.0
- **Official URL:** <https://github.com/cisco-ai-defense/skill-scanner>
- **Source / specification:** <https://github.com/cisco-ai-defense/skill-scanner>
- **Maintainer:** Cisco Systems (Cisco AI Defense)
- **Latest release evidence:** 2026-10-15 (PyPI cisco-ai-skill-scanner)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/cisco-ai-defense/skill-scanner/main/LICENSE>
- **Notes:** Capability description comes from search results and release metadata; the README was not read. Check the project's security advisories before deploying.

## CoSAI Secure Design Patterns for Agentic Systems

Coalition for Secure AI (an OASIS Open Project) workstream 4 repository with whitepapers on MCP security and agentic identity and access management, plus design-pattern content for secure agentic systems.

- **Type:** Reference Implementation
- **Lifecycle:** Design
- **Domain:** Agentic AI Security; MCP and Agent Skills Security; Agent Identity and Access
- **License / status:** CC-BY-4.0 (LICENSE.md also carries an OASIS non-assertion covenant.)
- **Official URL:** <https://www.coalitionforsecureai.org/>
- **Source / specification:** <https://github.com/cosai-oasis/ws4-secure-design-agentic-systems>
- **Maintainer:** CoSAI (OASIS Open)
- **Latest release evidence:** repository updated 2026-08-26 (no tagged release)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/cosai-oasis/ws4-secure-design-agentic-systems/main/LICENSE.md>
- **Notes:** Reference content (papers and patterns), not deployable code.

## Cybench

Framework and task set drawn from professional-level capture-the-flag competitions to measure whether language-model agents can solve security tasks (arXiv 2408.08926).

- **Type:** Benchmark
- **Lifecycle:** Break
- **Domain:** AI Red Teaming and Evaluations; Agentic AI Security
- **License / status:** Apache-2.0
- **Official URL:** <https://cybench.github.io/>
- **Source / specification:** <https://github.com/andyzorigin/cybench>
- **Maintainer:** Stanford
- **Latest release evidence:** not verified
- **Verification:** partial (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/andyzorigin/cybench/main/LICENSE>
- **Notes:** Measures model capability for offense; useful for evaluating the AI-powered attacker side of the threat model.

## CyberSecEval (Purple Llama)

Benchmarks covering insecure code generation, prompt injection (text and visual), code-interpreter abuse, cyber-attack compliance, vulnerability exploitation, autonomous operations, AutoPatchBench and CyberSOCEval.

- **Type:** Benchmark
- **Lifecycle:** Break
- **Domain:** LLM and Model Security; AI Red Teaming and Evaluations; AI-Assisted Development Security
- **License / status:** MIT (Only the evals/benchmarks (CybersecurityBenchmarks/) and CodeShield are MIT. The repository root LICENSE is the Llama 3.2 Community License, which is NOT an open-source license; Llama Guard and Prompt Guard use Llama licenses and are not listed here. Third-party components and some datasets have separate terms.)
- **Official URL:** <https://meta-llama.github.io/PurpleLlama/CyberSecEval/>
- **Source / specification:** <https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks>
- **Maintainer:** Meta
- **Latest release evidence:** CyberSecEval 4
- **Verification:** partial (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/README.md>
- **Notes:** Cite the benchmark subdirectory, not the repository root. Dataset licenses on Hugging Face were only partly checked. Meta states the benchmark infrastructure may change significantly in a next version.

## CycloneDX

Full-stack BOM specification for software, services and ML components. Its ML-BOM capability lets teams inventory models and datasets alongside code dependencies; the format is standardized as ECMA-424.

- **Type:** Open Standard / Protocol
- **Lifecycle:** Discover, Build
- **Domain:** AI Supply Chain Security; AI Security Governance and Engineering Controls
- **License / status:** Apache-2.0 (Schemas under Apache-2.0; ECMA-424 is published under Ecma's royalty-free patent policy.)
- **Official URL:** <https://cyclonedx.org/>
- **Source / specification:** <https://github.com/CycloneDX/specification>
- **Maintainer:** OWASP Foundation; Ecma TC54
- **Latest release evidence:** 2025-10-21 (spec 1.7)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/CycloneDX/specification/master/README.md>
- **Notes:** Which spec version introduced ML-BOM was not confirmed; check the spec history before citing it.

## DeepTeam

Runs locally; simulates single-turn and multi-turn attacks against LLM applications, RAG pipelines and agents, and scores results with LLM-as-judge metrics. Includes optional guardrail classes.

- **Type:** Open-Source Tool
- **Lifecycle:** Break
- **Domain:** LLM and Model Security; Agentic AI Security; AI Red Teaming and Evaluations
- **License / status:** Apache-2.0 (The maintainer sells a hosted platform (Confident AI) that integrates with it; that platform is not part of the open-source tool.)
- **Official URL:** <https://www.trydeepteam.com/>
- **Source / specification:** <https://github.com/confident-ai/deepteam>
- **Maintainer:** Confident AI
- **Latest release evidence:** 1.0.10 (2026-10-16, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/confident-ai/deepteam/main/LICENSE.md>
- **Notes:** The LICENSE.md appendix keeps the unfilled "[yyyy] [name of copyright owner]" template text; PyPI and the README both state Apache-2.0.

## Eclipse Enclave

Isolates coding agents (for example Claude Code, Codex, OpenCode) in containers with git worktrees and logs and restricts outbound traffic through a domain allowlist gateway.

- **Type:** Open-Source Tool
- **Lifecycle:** Build
- **Domain:** AI-Assisted Development Security; Agentic AI Security
- **License / status:** MIT
- **Official URL:** <https://enclave.eclipse.dev/>
- **Source / specification:** <https://github.com/eclipse-enclave/enclave>
- **Maintainer:** Eclipse Foundation project (EclipseSource and contributors)
- **Latest release evidence:** rolling pre-release, 2026-10-15 (no versioned release)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/eclipse-enclave/enclave/main/LICENSE>
- **Notes:** Ships rolling builds only, so pin by commit or digest.

## Fickling

Detects malicious pickle payloads without executing them, can hook pickle loading to enforce an allowlist of ML imports, and can trace, decompile and create pickle test files.

- **Type:** Open-Source Tool
- **Lifecycle:** Build, Break
- **Domain:** AI Supply Chain Security; LLM and Model Security
- **License / status:** LGPL-3.0-or-later (Copyleft library license; the authors offer to discuss exceptions.)
- **Official URL:** <https://github.com/trailofbits/fickling>
- **Source / specification:** <https://github.com/trailofbits/fickling>
- **Maintainer:** Trail of Bits
- **Latest release evidence:** 0.1.12 (2026-06-26, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/trailofbits/fickling/master/LICENSE>
- **Notes:** Pre-1.0 (PyPI development status Beta).

## garak

Command-line scanner that runs probes (prompt injection, jailbreaks, data leakage and others) against an LLM endpoint and evaluates the responses with detectors.

- **Type:** Open-Source Tool
- **Lifecycle:** Break
- **Domain:** LLM and Model Security; AI Red Teaming and Evaluations
- **License / status:** Apache-2.0
- **Official URL:** <https://github.com/NVIDIA/garak>
- **Source / specification:** <https://github.com/NVIDIA/garak>
- **Maintainer:** NVIDIA
- **Latest release evidence:** 0.17.1 (2026-10-16, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/NVIDIA/garak/main/LICENSE>
- **Notes:** Scan results are probabilistic; repeat runs before drawing conclusions.

## Guardrails AI

Applies validators to LLM inputs and outputs and can enforce structured output. Validators are distributed through a separate hub.

- **Type:** Open-Source Tool
- **Lifecycle:** Defend
- **Domain:** LLM and Model Security; AI Runtime Security
- **License / status:** Apache-2.0 (The framework is open source; whether individual hub validators or hosted features carry other terms was not checked.)
- **Official URL:** <https://github.com/guardrails-ai/guardrails>
- **Source / specification:** <https://github.com/guardrails-ai/guardrails>
- **Maintainer:** Guardrails AI
- **Latest release evidence:** 0.11.0 (2026-08-14, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/guardrails-ai/guardrails/main/LICENSE>
- **Notes:** The LICENSE appendix keeps the unfilled copyright template text.

## Inspect AI

Evaluation framework from the UK AI Security Institute used to build repeatable tests of model and agent behavior, including cyber and safety evaluations.

- **Type:** Open-Source Tool
- **Lifecycle:** Break
- **Domain:** AI Red Teaming and Evaluations; LLM and Model Security; Agentic AI Security
- **License / status:** MIT
- **Official URL:** <https://inspect.aisi.org.uk/>
- **Source / specification:** <https://github.com/UKGovernmentBEIS/inspect_ai>
- **Maintainer:** UK AI Security Institute
- **Latest release evidence:** 0.3.281 (2026-10-15, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_ai/main/LICENSE>
- **Notes:** Evaluation datasets in the separate inspect_evals repository have their own licenses.

## MCPSecBench

Benchmark of attack scenarios against MCP deployments, intended to measure how MCP servers and agents behave under adversarial conditions.

- **Type:** Benchmark
- **Lifecycle:** Break
- **Domain:** MCP and Agent Skills Security; AI Red Teaming and Evaluations
- **License / status:** MIT
- **Official URL:** <https://github.com/AIS2Lab/MCPSecBench>
- **Source / specification:** <https://github.com/AIS2Lab/MCPSecBench>
- **Maintainer:** AIS2Lab
- **Latest release evidence:** not verified
- **Verification:** partial (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/AIS2Lab/MCPSecBench/main/LICENSE>
- **Notes:** License was read; maintenance recency and the accompanying paper were not verified. Treat as research code.

## Microsoft Agent Governance Toolkit

Provides policy enforcement for agent actions (Cedar/OPA), an MCP gateway with tool allowlists and PII/SSRF checks, agent identity, audit logging, a kill switch and OpenTelemetry/Prometheus export.

- **Type:** Open-Source Tool
- **Lifecycle:** Design, Defend
- **Domain:** Agentic AI Security; Agent Identity and Access; MCP and Agent Skills Security; AI Runtime Security
- **License / status:** MIT
- **Official URL:** <https://github.com/microsoft/agent-governance-toolkit>
- **Source / specification:** <https://github.com/microsoft/agent-governance-toolkit>
- **Maintainer:** Microsoft
- **Latest release evidence:** v4.1.0 (2026-06-09, GitHub release)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/microsoft/agent-governance-toolkit/main/LICENSE>
- **Notes:** Releases are labeled Public Preview and the project is roughly six months old. Its OWASP coverage claims are self-reported. No release after 2026-06-11 was seen; check for newer ones.

## MITRE ATLAS

Matrix of tactics, techniques, mitigations and real-world case studies for attacks on AI systems, distributed as YAML and STIX data with Navigator support. Modeled on MITRE ATT&CK.

- **Type:** Open Security Framework
- **Lifecycle:** Design, Break
- **Domain:** LLM and Model Security; Agentic AI Security; AI Security Governance and Engineering Controls
- **License / status:** Apache-2.0 (Applies to the atlas-data repository. Website terms were not separately verified.)
- **Official URL:** <https://atlas.mitre.org/>
- **Source / specification:** <https://github.com/mitre-atlas/atlas-data>
- **Maintainer:** MITRE
- **Latest release evidence:** 2026-09-14 (content version 2026.09)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://github.com/mitre-atlas/atlas-data>
- **Notes:** Single-organization governance. Contributions arrive through GitHub.

## Model Context Protocol (MCP)

Client/server protocol for exposing tools, resources and prompts to AI applications. The specification includes an authorization section and security considerations that define trust boundaries between hosts, clients and servers. Current spec revision found: 2026-07-28.

- **Type:** Open Standard / Protocol
- **Lifecycle:** Design, Build
- **Domain:** MCP and Agent Skills Security; Agent Identity and Access
- **License / status:** Apache-2.0 (spec, in transition from MIT); CC-BY-4.0 (non-spec docs) (The repository LICENSE describes a transition from MIT to Apache-2.0; older contributions may remain MIT.)
- **Official URL:** <https://modelcontextprotocol.io/>
- **Source / specification:** <https://github.com/modelcontextprotocol/modelcontextprotocol>
- **Maintainer:** Model Context Protocol, a Series of LF Projects, LLC (Linux Foundation; Agentic AI Foundation)
- **Latest release evidence:** 2026-07-28 (spec revision)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/LICENSE>
- **Notes:** Maintainer-led governance (SEP process). A protocol, not a security control; its security model is only as good as each implementation.

## NeMo Guardrails

Lets developers define rails that constrain LLM application behavior and run checks on inputs, outputs and retrieved content. Repository moved to the NVIDIA-NeMo organization.

- **Type:** Open-Source Tool
- **Lifecycle:** Build, Defend
- **Domain:** LLM and Model Security; AI Runtime Security; Data and RAG Security
- **License / status:** Apache-2.0 (Per the SPDX header in LICENSE.md.)
- **Official URL:** <https://github.com/NVIDIA-NeMo/Guardrails>
- **Source / specification:** <https://github.com/NVIDIA-NeMo/Guardrails>
- **Maintainer:** NVIDIA
- **Latest release evidence:** 0.24.1 (2026-09-16, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/NVIDIA-NeMo/Guardrails/main/LICENSE.md>
- **Notes:** Guardrails are probabilistic filters and should complement, not replace, deterministic authorization.

## Open Policy Agent (OPA)

CNCF graduated policy engine used to express and enforce authorization and guardrail rules as code. Not AI-specific; included as the deterministic control layer that AI agents' tool permissions can be checked against.

- **Type:** Open-Source Tool
- **Lifecycle:** Design, Defend
- **Domain:** Agent Identity and Access; AI Security Governance and Engineering Controls; AI Runtime Security
- **License / status:** Apache-2.0
- **Official URL:** <https://www.openpolicyagent.org/>
- **Source / specification:** <https://github.com/open-policy-agent/opa>
- **Maintainer:** CNCF project (original creators now employed by Apple; the project states governance and licensing are unchanged)
- **Latest release evidence:** v1.21.2 (12 Oct, year inferred as 2026)
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://github.com/open-policy-agent/opa>
- **Notes:** Foundational security tool rather than an AI tool. Stewardship changed in 2025-2026; review the project's own statement.

## OpenTelemetry GenAI Semantic Conventions

Standard attribute and span definitions (for example agent invocation and tool-call spans) so that agent activity can be traced with ordinary OpenTelemetry pipelines. Provides the telemetry that runtime monitoring and incident investigation depend on.

- **Type:** Open Standard / Protocol
- **Lifecycle:** Defend
- **Domain:** AI Runtime Security; Agentic AI Security
- **License / status:** Apache-2.0 (Repository code and schemas are Apache-2.0; the opentelemetry.io docs are CC-BY-4.0. The GenAI conventions are moving to github.com/open-telemetry/semantic-conventions-genai, whose license file was not read.)
- **Official URL:** <https://opentelemetry.io/docs/specs/semconv/gen-ai/>
- **Source / specification:** <https://github.com/open-telemetry/semantic-conventions>
- **Maintainer:** OpenTelemetry (CNCF)
- **Latest release evidence:** semconv 1.44.0 (date not verified)
- **Verification:** partial (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/open-telemetry/semantic-conventions/main/LICENSE>
- **Notes:** Maturity (stable vs. development) of the GenAI conventions was not confirmed. It is an observability standard, not a security control.

## OWASP FinBot Agentic AI CTF

Capture-the-flag application built on a vendor-onboarding multi-agent workflow for practicing attacks on agentic systems. Can be run locally; OWASP also announced a hosted instance in April 2026.

- **Type:** Learning / Lab
- **Lifecycle:** Break
- **Domain:** Agentic AI Security; AI Red Teaming and Evaluations
- **License / status:** Apache-2.0 (License file is LICENSE.md in the demo repository.)
- **Official URL:** <https://genai.owasp.org/resource/finbot-agentic-ai-capture-the-flag-ctf-application/>
- **Source / specification:** <https://github.com/OWASP-ASI/finbot-ctf-demo>
- **Maintainer:** OWASP GenAI Security Project (Agentic Security Initiative)
- **Latest release evidence:** no tagged releases; OWASP announced availability 2026-04-14
- **Verification:** partial (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/OWASP-ASI/finbot-ctf-demo/main/LICENSE.md>
- **Notes:** Last commit date was not verified and a newer repository may supersede the demo repo. Recheck before relying on it.

## OWASP GenAI Security Project

OWASP project that publishes the LLM Top 10 (2025 edition and a 2026 edition), the Top 10 for Agentic Applications, cheat sheets, an AI red-teaming initiative and other guidance. Useful as the shared vocabulary for AI-specific risks.

- **Type:** Open Security Framework
- **Lifecycle:** Design, Break
- **Domain:** LLM and Model Security; Agentic AI Security; AI Security Governance and Engineering Controls
- **License / status:** CC-BY-SA-4.0 (Site-wide statement ("unless otherwise specified"); individual repositories may differ. Share-alike applies if you reuse the text.)
- **Official URL:** <https://genai.owasp.org/>
- **Source / specification:** <https://github.com/GenAI-Security-Project>
- **Maintainer:** OWASP Foundation
- **Latest release evidence:** 2026-08-03 (LLM Top 10 2026 v1.0 listed on project resources)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
- **Notes:** Guidance documents, not software. Check the license of each individual artifact before reuse.

## OWASP Top 10 for Agentic Applications 2026

Risk list for AI agents that plan, act and make decisions across workflows, such as goal hijack, tool misuse and identity abuse. The project page states it was developed with more than 100 industry experts, researchers and practitioners and was published on 2025-12-09.

- **Type:** Open Security Framework
- **Lifecycle:** Design, Break
- **Domain:** Agentic AI Security; Agent Identity and Access; AI Security Governance and Engineering Controls
- **License / status:** CC-BY-SA-4.0 (From the site-wide license statement on genai.owasp.org.)
- **Official URL:** <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
- **Source / specification:** <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
- **Maintainer:** OWASP GenAI Security Project
- **Latest release evidence:** 2025-12-09
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
- **Notes:** A risk taxonomy, not a control catalogue. Treat it as a threat-modeling input.

## Promptfoo

Declarative evaluation and red-teaming tool for prompts, models and agents with CI/CD integration. Runs locally from the open-source CLI.

- **Type:** Open-Source Tool
- **Lifecycle:** Build, Break
- **Domain:** LLM and Model Security; AI Red Teaming and Evaluations
- **License / status:** MIT (The maintainer also offers commercial products. Which features exist only in those offerings was not assessed here.)
- **Official URL:** <https://www.promptfoo.dev/>
- **Source / specification:** <https://github.com/promptfoo/promptfoo>
- **Maintainer:** Promptfoo
- **Latest release evidence:** 0.121.18 (2026-07-07, from a third-party release tracker)
- **Verification:** partial (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/promptfoo/promptfoo/main/LICENSE>
- **Notes:** Release date came from a third-party tracker, not the GitHub releases page. Confirm which red-team features run fully offline before relying on them.

## PyRIT

Library from the Microsoft AI Red Team that orchestrates attacks, converters, targets and scoring to identify risks in generative AI systems.

- **Type:** Open-Source Tool
- **Lifecycle:** Break
- **Domain:** LLM and Model Security; Agentic AI Security; AI Red Teaming and Evaluations
- **License / status:** MIT
- **Official URL:** <https://microsoft.github.io/PyRIT/>
- **Source / specification:** <https://github.com/microsoft/PyRIT>
- **Maintainer:** Microsoft AI Red Team
- **Latest release evidence:** 1.1.0 (2026-09-04, PyPI)
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/microsoft/PyRIT/main/LICENSE>
- **Notes:** PyPI classifier lists development status as Alpha; the API may change.

## sandbox-runtime

Lightweight sandbox for agent and tool processes that restricts filesystem and network access without a container.

- **Type:** Open-Source Tool
- **Lifecycle:** Build
- **Domain:** AI-Assisted Development Security; Agentic AI Security
- **License / status:** Apache-2.0 (LICENSE was read under the project's earlier repository path, which redirects here.)
- **Official URL:** <https://github.com/anthropics/sandbox-runtime>
- **Source / specification:** <https://github.com/anthropics/sandbox-runtime>
- **Maintainer:** Anthropic
- **Latest release evidence:** v0.0.80 (2026-10-16, GitHub release)
- **Verification:** partial (delegated check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/anthropic-experimental/sandbox-runtime/main/LICENSE>
- **Notes:** 0.0.x versioning suggests experimental status. The description comes from the repository name and release notes; the README was not read.

## Sigstore model-transparency (model-signing)

Signs and verifies model files so consumers can check integrity and provenance before loading them. Supports Sigstore keyless signing as well as key- and certificate-based signing, with in-toto/DSSE bundles.

- **Type:** Open-Source Tool
- **Lifecycle:** Build
- **Domain:** AI Supply Chain Security
- **License / status:** Apache-2.0 (Built with OpenSSF.)
- **Official URL:** <https://www.sigstore.dev/>
- **Source / specification:** <https://github.com/sigstore/model-transparency>
- **Maintainer:** Sigstore community / OpenSSF
- **Latest release evidence:** v1.0 announced 2025-04-04
- **Verification:** verified (delegated check, 2026-10-18); license evidence: <https://github.com/sigstore/model-transparency>
- **Notes:** Signing proves who published a model, not that the model is safe.

## Snyk Agent Scan

Command-line scanner (formerly MCP-Scan) for agent setups. The client source is Apache-2.0 and its `inspect` command lists discovered components locally without analysis. Security analysis of tool descriptions, skill content and MCP configs requires a Snyk API token and sends that content to a hosted service governed by separate terms of use.

- **Type:** Open-Source Tool
- **Lifecycle:** Discover, Build
- **Domain:** MCP and Agent Skills Security; AI Supply Chain Security; AI-Assisted Development Security
- **License / status:** Apache-2.0 (Client source is Apache-2.0 (LICENSE copyright "Invariant Labs AG"). Open core - the analysis service is not open source and needs a token.)
- **Official URL:** <https://github.com/snyk/agent-scan>
- **Source / specification:** <https://github.com/snyk/agent-scan>
- **Maintainer:** Snyk
- **Latest release evidence:** not verified
- **Verification:** partial (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/snyk/agent-scan/main/LICENSE>
- **Disclosure:** Created and maintained by Snyk, which also supports the AI Security Engineers Community. Listed as open core only; the hosted analysis is a commercial dependency.
- **Notes:** README read on the verification date. Release cadence and LICENSE file were not re-checked in this pass. Only local discovery works without a Snyk account; compare with the fully open alternatives agent-bom and Cisco Skill Scanner.

## Snyk VulnBench

Repeats the same agentic security review five times per configuration on ten small JavaScript projects (six model configurations, 300 scans) and compares findings with a Snyk Code reference set. Published results: 134 of 158 reference-matched findings (84.8%) appeared in all five runs; 80 of 161 unmatched findings (49.7%) appeared in only one run. See research/vulnbench.md for methodology and limits.

- **Type:** Benchmark
- **Lifecycle:** Build, Break, Defend
- **Domain:** AI-Assisted Development Security; AI Red Teaming and Evaluations
- **License / status:** Apache-2.0 (Harness repository LICENSE read directly; the companion data repository snyk-labs/snyk-vulnbench-js-1.0 is also Apache-2.0 per a delegated check.)
- **Official URL:** <https://vulnbench.com/>
- **Source / specification:** <https://github.com/snyk-labs/snyk-vulnbench>
- **Maintainer:** Snyk (snyk-labs)
- **Latest release evidence:** JS 1.0, published 2026-06-11
- **Verification:** verified (direct check, 2026-10-18); license evidence: <https://raw.githubusercontent.com/snyk-labs/snyk-vulnbench/main/LICENSE>
- **Disclosure:** Created by Snyk, which also supports the AI Security Engineers Community. Listed under the same criteria as every other entry.
- **Notes:** The reference set is Snyk Code, so "match" means agreement with that tool, not ground truth. Other projects share the name VulnBench; this entry is vulnbench.com / snyk-labs.
<!-- END GENERATED: catalogue -->
