# What is AI Security Engineering?

## Definition

AI Security Engineering is the discipline of designing, building, testing, and defending AI-native software throughout its lifecycle, combining software security, AI engineering, and adversarial thinking to manage risks introduced by AI-assisted development, AI-powered applications, and autonomous agents.

An AI Security Engineer understands:

1. How software is developed, deployed and operated.
2. How attackers find and exploit weaknesses.
3. How AI models, agents, data, tools and probabilistic systems behave.
4. How to combine deterministic security controls, AI-based capabilities and human judgment.
5. How to run continuous security processes that enable secure innovation.

They are builder-defenders: they design secure architectures, implement controls, think adversarially and test how systems fail.

## Three shifts in the attack surface

- **AI writes software.** Coding assistants and agents can produce and change more code than reviewers can inspect, can add insecure dependencies or configuration, and may hold access to repositories, files and credentials.
- **AI lives inside software.** Models, retrieval pipelines, vector stores, agent memory, MCP servers and agent skills are now architectural components. They add prompt injection, tool poisoning, memory manipulation, model supply chain compromise and unclear trust boundaries.
- **AI operates software.** Agents execute code, call APIs, use credentials and act on production systems, often without a human approving each step. In short, deterministic permissions are given to probabilistic systems.

## The ownership gap

Each existing discipline owns part of the problem: developers know the application, AppSec knows vulnerabilities, cloud and IAM teams own infrastructure and identity, AI/ML engineers understand models, the SOC handles detection and response, and GRC owns policy. Questions that cross those boundaries often have no clear owner:

- Who threat-models the interaction between a model, an agent, an MCP server, credentials, data and external tools?
- Who decides what an autonomous agent is authorized to do?
- Who tests whether those controls hold under attack?
- Who decides when an AI-generated security finding is trustworthy?

AI Security Engineering connects the existing disciplines around the security of the whole AI-native system. It does not replace them.

## What the role is not

An AI Security Engineer is not simply an LLM security expert, an AI compliance specialist, an AppSec engineer with an AI scanner, an ML researcher, a prompt engineer, or someone whose job is to stop developers from adopting AI. It is an engineering role that makes AI adoption secure and sustainable.

## The DevOps analogy, with a caveat

DevOps followed a recognizable path: new practices appear, responsibilities fragment, practitioners invent methods and tools, communities form, shared vocabulary emerges, organizations formalize roles, and a market category follows. AI Security Engineering appears to be early on that path. The category is not yet mature or universally accepted, and this repository does not assume otherwise.

## Principles

1. **Secure by design:** build security into AI architectures and workflows from the start.
2. **Full-system security:** cover code, models, agents, tools, identities, data and infrastructure.
3. **Least privilege and explicit authorization:** give agents only the capabilities their task needs.
4. **Continuous validation:** AI-native systems need ongoing adversarial testing, monitoring and reassessment.
5. **Deterministic controls, AI-based capabilities and human judgment together:** deterministic controls stay essential; AI adds context, speed and adaptability but behaves probabilistically; people provide judgment and accountability.
6. **Adaptive defense:** defenses should observe, reason, act and learn, with safeguards and human supervision.
7. **Open collaboration:** open tooling, research and standards advance the field.

## Next

- [Foundations: initial vision](initial-vision.md)
- [Responsibilities and skills](responsibilities.md)
- [Frameworks and standards](frameworks-and-standards.md)
- [The five-stage lifecycle](../lifecycle/discover.md)
