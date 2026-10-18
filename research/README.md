# Research and benchmarks

Reproducible research artifacts: benchmark harnesses, datasets and evaluation frameworks. A paper without open artifacts is not listed.

<!-- BEGIN GENERATED: research -->
| Resource | What it is | Type | Lifecycle |
|---|---|---|---|
| [AgentDojo](../resources/README.md#agentdojo) | Dynamic benchmark environment for prompt-injection attacks and defenses against tool-using agents. | Benchmark | Break |
| [Cybench](../resources/README.md#cybench) | CTF-based benchmark of 40 tasks for evaluating the offensive cyber capabilities of LLM agents. | Benchmark | Break |
| [CyberSecEval (Purple Llama)](../resources/README.md#cyberseceval-purple-llama) | Meta's cybersecurity benchmark suite for LLMs, including prompt injection, insecure code and autopatch tests. | Benchmark | Break |
| [MCPSecBench](../resources/README.md#mcpsecbench) | Security benchmark for Model Context Protocol servers, clients and hosts. | Benchmark | Break |
| [Snyk VulnBench](../resources/README.md#snyk-vulnbench) | Benchmark and study of how repeatable LLM-based vulnerability findings are, versus a deterministic SAST reference. | Benchmark | Build, Break, Defend |
<!-- END GENERATED: research -->

## Reading benchmark results

- A benchmark score measures behavior on that benchmark's tasks, models, prompts and harness version. It does not transfer automatically to your system.
- Check whether the benchmark reports variance across repeated runs. LLM-based systems can give different results for the same input.
- Check what the reference is. Agreement with another tool is not the same as ground truth.
- Check licenses of code and datasets separately; they often differ.

For a worked example of these points, see the [VulnBench write-up](vulnbench.md).

## Not yet covered

Open, reproducible research on memory attacks against agents, model supply chain compromise, defensive agent architectures and automated remediation reliability was searched for but no artifact passed verification. The [research inventory](../maintainers/research-inventory.md) lists candidates that were held or deferred.
