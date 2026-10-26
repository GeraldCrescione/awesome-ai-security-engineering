# Initial vision: why AI Security Engineers, and what they do

This page is the community's initial vision of the AI Security Engineer: why the role is proposed, where it sits, and what its functional scope could be. It is a starting point to be tested and challenged, not a standard. The five-stage lifecycle used across this repository is built on it. If the vision is wrong, the lifecycle is wrong, so please [challenge it](#challenge-this-vision).

For the formal definition and principles, see [What is AI Security Engineering?](what-is-ai-security-engineering.md). For the job profile, skills and measures, see [Responsibilities, skills and measures](responsibilities.md).

## Why the role is proposed

Many teams already own a piece of AI-native systems:

| Team | What they own, and where it stops |
|---|---|
| Developers | Know the application, but need to ship |
| AppSec | Understand application vulnerabilities, but the scope is expanding |
| AI / ML engineers | Understand models, but not always offensive security |
| Cloud and IAM | Infrastructure and identity |
| SOC | Detection and response |
| GRC | Policy and governance |

Everyone owns a piece, and nobody necessarily owns the system. Questions that cross these boundaries often have no clear owner:

- Who threat-models the interaction between the model, the agent, the MCP server, identity, data and tools?
- Who decides what an agent is allowed to do?
- Who tests offensively how those controls fail?
- Who decides when an AI-generated security result should be considered trustworthy?

This is an ownership and skills gap, not only a tooling gap. The AI Security Engineer is proposed to fill it, not because organizations need another job title, but because AI-native systems increasingly require a mix of skills that has traditionally been spread across teams.

## A role at the intersection of three disciplines

| Discipline | What it contributes |
|---|---|
| Software engineering | How applications are built and delivered |
| Security engineering | How systems fail and how attackers think |
| AI engineering | How models, agents, data, tools and probabilistic systems behave |

An AI Security Engineer combines the three to secure AI-native systems throughout their lifecycle, from AI-generated code to the actions agents are allowed to take.

## What the role is not

- Not simply an "LLM security expert".
- Not an AI compliance role.
- Not simply an AppSec engineer using an AI scanner.
- Not necessarily an ML researcher.
- Not someone whose job is to stop developers from using AI.

It is an engineering role. The goal is to make AI adoption secure and sustainable.

## It does not replace existing teams

The role is connective tissue. It links AppSec, cloud security, the SOC, developers and AI teams around AI-native systems. Where it reports differs by organization; what matters is a clear mandate for the security of the whole system.

## The functional scope: five stages

The proposed job is a lifecycle for securing AI-native and agentic systems. Each stage has its own page with matching open resources.

| Stage | Typical activities |
|---|---|
| [Discover](../lifecycle/discover.md) | AI application inventory, model and tool usage, data flows, shadow AI, dependencies |
| [Design](../lifecycle/design.md) | Threat modeling, trust boundaries, agent architectures, least privilege, identities and permissions |
| [Build](../lifecycle/build.md) | Security in the IDE, dependency controls, policy as code, developer guardrails |
| [Break](../lifecycle/break.md) | AI pentesting, AI red teaming, prompt injection testing, tool and agent manipulation |
| [Defend](../lifecycle/defend.md) | Backlog reduction, remediation, monitoring, behavioral controls |

In short: discovery, design, prevention, testing and defense. The scope is fairly broad.

## Limits of this vision

- The category is early and not universally accepted. The [DevOps comparison](what-is-ai-security-engineering.md#the-devops-analogy-with-a-caveat) is an analogy, not a prediction.
- The role may already exist inside your teams under another title. Job titles vary.
- The five stages are one way to slice the work, and the activities listed are examples, not a complete list.
- This page describes a proposed scope, not evidence of how organizations staff the role today.

## Challenge this vision

Does this match how you actually work? Is a stage missing, mislabeled or in the wrong order? Is a team or responsibility absent from the table above? Propose a change with the [taxonomy form](../.github/ISSUE_TEMPLATE/taxonomy.yml), or open a pull request. See [CONTRIBUTING.md](../CONTRIBUTING.md#suggest-taxonomy-improvements).
