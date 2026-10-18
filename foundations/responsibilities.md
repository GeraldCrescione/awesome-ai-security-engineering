# Responsibilities, skills and measures

This page summarizes a community-proposed job profile for an AI Security Engineer. Titles vary (ML Security Engineer, Platform Security Engineer for AI-native systems). Treat it as a starting point for your own role definition, not a standard.

## Core responsibilities

- **Threat model AI-native systems.** Cover prompt injection, model inversion and theft, agent hijacking, data and memory poisoning, and supply chain risk, including the interactions between models, agents, tools, identities and data.
- **Build secure-by-design systems with AI, ML and platform teams.** Make adversarial resistance part of training, deployment and inference.
- **Instrument detection and response.** Monitor AI system behavior, detect anomalies or adversarial activity, and trigger containment or remediation.
- **Build tooling and automation.** Scan model pipelines, verify data lineage, protect memory, secure agent chains and run adversarial tests.
- **Embed AI security in existing practice.** Partner with DevSecOps, SecOps, platform and cloud security, and governance teams.
- **Raise awareness.** Train developers, AI engineers and security teams.

## The Observe, Reason, Act, Learn loop

The profile frames the work as a loop that should be as fast as the systems it protects:

1. **Observe:** visibility into models, data, agent flows, deployments and usage. See [Discover](../lifecycle/discover.md).
2. **Reason:** interpret signals, assess risk, prioritize.
3. **Act:** deploy automated or semi-automated remediation or guardrails, with human approval where the blast radius warrants it. See [Defend](../lifecycle/defend.md).
4. **Learn:** update threat models, detections and response logic from incidents and tests. See [Break](../lifecycle/break.md).

## Typical background

- Several years in security or platform engineering with exposure to AI/ML systems.
- Programming skill (Python or similar) and familiarity with ML and agent frameworks.
- Cloud and container experience.
- Threat modeling, security architecture, vulnerability assessment and secure coding.
- Knowledge of AI-specific attack vectors: adversarial input, data and memory exploitation, model theft, supply chain risk.
- Clear communication with AI engineers, platform teams, leadership and business stakeholders.

Helpful extras: MLSecOps or AI security framework experience, awareness of AI governance and regulation, experience with security orchestration, and open-source or research contributions.

## Training areas

AI/ML lifecycle security (data, models, agents, pipelines); threat modeling for agentic systems; red teaming and adversarial testing (prompt attacks, evaluations, memory attacks, model theft); hands-on labs and game days. See [learning](../learning/README.md) for open labs.

## Suggested measures

Teams can track measures like these. They are suggestions, and none comes with a verified benchmark value:

- Mean time to detect and to remediate AI-related incidents.
- Number and quality of AI-specific threat models that are operationalized.
- Share of AI systems (models, agents, pipelines) under a defined security posture.
- Share of remediation actions executed by orchestration rather than manually, weighed against false-action risk.
- Fewer repeated incidents of the same class over time.

## Where this role sits

The role connects developers, AppSec, AI/ML engineering, cloud and IAM, the SOC and GRC. Where it reports differs by organization; what matters is a clear mandate for the security of the complete AI-native system.
