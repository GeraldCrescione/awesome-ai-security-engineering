# VulnBench: can an LLM find the same bugs twice?

**Disclosure:** VulnBench was created by Snyk, which also supports the AI Security Engineers Community. It is listed because it passed the same criteria as every other entry: public source, verified Apache-2.0 license, open data and an open methodology. Figures below are quoted from the project's own site and checked against it on 2026-10-18; they have not been independently reproduced by this repository's maintainers.

## Question

AI-based security tools give probabilistic results. Run the same review on the same code with the same prompt and you may get different findings. That raises engineering questions this list cares about:

- Can a release be blocked on an AI-generated finding?
- Is a vulnerability resolved because an agent no longer reports it?
- Can an agent remediate a finding if its original diagnosis is unstable?
- How should deterministic tools, probabilistic tools and human judgment be combined?

## Method (VulnBench JS 1.0, published 2026-06-11)

- Ten small JavaScript/Express projects chosen so every finding can be inspected.
- Six model configurations. Each configuration reviewed each project five times with the same code, prompt and harness: 300 scans in total.
- Findings are normalized into signatures so recurrence across runs can be counted.
- A deterministic reference set comes from a Snyk Code scan. The scorer matches findings to it by vulnerability type.
- Agreement, recurrence, variance, coverage, cost, tokens and duration are reported separately.

## Reported results

| Measure | Result |
|---|---|
| Reference-matched findings seen in all five runs | 134 of 158 (84.8%) |
| Unmatched findings seen in all five runs | 22 of 161 (13.7%) |
| Unmatched findings seen in only one run | 80 of 161 (49.7%) |

The site also reports that higher spend did not reliably raise agreement with the reference: one high-cost Opus configuration scored 68.8% reference F1 against 75.4% for a cheaper configuration, at about 5.67 times the cost.

## How to read it

- **Not "false positives".** The project states that unmatched findings are not automatically false positives; they need case-level inspection. Some may be real vulnerabilities absent from the reference.
- **Agreement is not accuracy.** The reference is a single SAST tool made by the benchmark's author. "Match" means agreement with that tool.
- **Small, simple projects.** Ten small fixtures do not represent large, real-world codebases or other languages.
- **One snapshot.** Results depend on the models, prompts and harness versions tested.
- **Cost estimates** reflect the small fixtures and the publication's assumptions.

## What to take from it

Repeat runs before trusting or dismissing an AI finding, treat run-to-run recurrence as a signal for triage, and do not auto-close findings because a later run did not reproduce them. See [best practices](../best-practices/README.md).

## Links

- Site and data: <https://vulnbench.com/>
- Harness repository: <https://github.com/snyk-labs/snyk-vulnbench>
- JS 1.0 data repository: <https://github.com/snyk-labs/snyk-vulnbench-js-1.0>
- Paper: <https://arxiv.org/abs/2606.15762>
- Catalogue entry: [Snyk VulnBench](../resources/README.md#snyk-vulnbench)

Other unrelated projects use the name VulnBench. Check you have the right one.
