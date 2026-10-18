# Strategy review

Review of the project brief and the three source documents (talk deck, community blog post, job specification) before building. Findings and the decision taken for each.

## Consistent across sources

The definition, three-shift framing, ownership gap, five-stage lifecycle (Discover, Design, Build, Break, Defend), the "not an LLM expert / not compliance / not AppSec with a scanner" boundaries and the deterministic + AI + human principle are consistent between the brief, the deck and the job spec, and were adopted as written. The job spec's Observe-Reason-Act-Learn loop is kept in [responsibilities](../foundations/responsibilities.md).

## Issues found and decisions

1. **Lifecycle and domains are orthogonal.** Stages (when) and domains (what) overlap by design, so a resource carries both. Decision: one canonical entry per resource with `lifecycle` and `domains` lists; README lists each resource once under its primary stage; stage pages and the topic index cross-reference.
2. **VulnBench classification used terms not in the taxonomy** ("Vulnerability Detection", "Reproducibility", "Automated Remediation"). Decision: mapped to *AI-Assisted Development Security* and *AI Red Teaming and Evaluations*; Build/Break/Defend stages kept.
3. **"Engineering Best Practice" is a resource type but the open-source test does not apply to it.** Decision: best practices are written in-repo as community guidance, labeled as such, and link to verified resources rather than being listed as entries.
4. **The shortlist contains items that fail the strict criteria.** Verified outcomes: LLM Guard is archived (excluded); Purple Llama's root license is the Llama 3.2 Community License, so only the MIT-licensed benchmark component is listed; the AgentDojo URL in the brief points to a different path than the canonical `ethz-spylab/agentdojo`; NeMo Guardrails moved to `NVIDIA-NeMo/Guardrails`; NIST AI RMF is governance guidance without an open specification and is not listed; OWASP Juice Shop is not AI-specific; Giskard, ASB and ART were held for unverified capability or maintenance; ModelScan was held for a vendor-neutrality decision (see below).
5. **Snyk Agent Scan fails the "no proprietary service" rule as documented.** The client is Apache-2.0, but the README states analysis uses a Snyk API token and a hosted API under separate terms. Excluded under criterion 5.1. This is a judgment call the maintainers should confirm; if the `inspect` (discovery without analysis) mode is judged meaningful on its own, the project can be listed with an explicit open-core note.
6. **Vendor neutrality has more than one edge.** The brief excludes direct competitors of Snyk but is silent on Snyk-created projects and on acquisitions. Decisions: Snyk-created entries are allowed only with a `disclosure` field (enforced by `validate.py`); currently two (VulnBench and Snyk Agent Scan). Snyk Agent Scan is listed as open core: its client is Apache-2.0, but deeper analysis needs a Snyk-hosted API and token, and the entry says so. ModelScan was dropped from consideration because its maintainer, Protect AI, was acquired by Palo Alto Networks (July 2025); the maintainers decided not to list it. Fickling is the open alternative. Model vendors (NVIDIA, Microsoft, Meta, Anthropic, Cisco) are not treated as competitors.
7. **Claims in the source documents that this repository does not repeat.** The talk and blog cite third-party and Snyk-report statistics (for example the share of AI-generated code that is vulnerable, MCP server vulnerability rates, incident anecdotes, and a prediction about Fortune 500 adoption). They were not independently verified here and are omitted. The VulnBench figures were re-checked against vulnbench.com. Add others only with a primary source.
8. **Licensing of the list itself was unspecified.** Decision: MIT for the repository content and scripts, a permissive choice that is easy to change before publication (CC0 is common for awesome lists). Linked projects keep their licenses; OWASP content is CC BY-SA and is linked, not copied.
9. **"Maintenance" cannot be proven automatically.** Decision: record release evidence and flag, never auto-remove.
10. **Entry cap.** The cap of 30 is a maximum. 29 entries were published; 6 verified candidates were deferred to a backlog.

## Gaps identified

| Area | State |
|---|---|
| AI asset discovery (shadow AI, data flows, permission inventories) | One tool (agent-bom, single maintainer) and the CycloneDX standard |
| Data and RAG security | No verified open-source resource beyond general guardrail frameworks |
| Agent identity and authorization | Policy engines and a governance toolkit; dedicated agent-identity servers were young or vendor-led and held |
| Secure vibe coding / AI-generated code analysis | None verified |
| Open training labs | One verified lab; the most popular MCP lab lacks a confirmed license |
| Agent-compromise incident response and detection content | None verified |
| Reproducible research on memory attacks, model supply chain compromise, defensive agent architectures | None passed verification |
