# Contributing

Thank you for helping. This list is curated, not exhaustive: a small number of well-verified entries is better than a long list. The project is created and maintained by the [AI Security Engineers Community](https://www.aiseceng.io/) and is open to everyone.

## Scope

In scope: open-source tools, open standards, open security frameworks, open research with reproducible artifacts, openly licensed labs and engineering best practices that help engineers build, test and defend software that AI writes, powers or operates.

Out of scope: generic AI safety or ethics, cybersecurity news, product marketing, and general security tools with no clear AI-security relevance.

## Inclusion criteria

A resource must meet all that apply.

**Open-source software**

- Public source code and an identifiable open-source license that allows use, modification and redistribution (OSI-approved preferred).
- Meaningful functionality in the open-source version. For open-core projects, only the genuinely open capabilities qualify, and the entry must say where the boundary is.
- Direct relevance to AI Security Engineering.
- Evidence it is maintained (recent release, commits or maintainer activity). Activity alone does not prove health, and a quiet repository is not automatically abandoned.

**Open standards and frameworks**

- Publicly accessible specification, documented implementation rights, open implementation opportunity and a transparent development process where applicable.
- Label formal standards, community frameworks, guidance and protocols accurately.

**Open research and benchmarks**

- Open artifacts: code, datasets, harnesses or reproducible experiments. A freely readable paper alone does not qualify.
- If code and data are licensed differently, verify both.

**Quality**

Engineering relevance, technical credibility, documentation, practical usefulness, maintenance, distinctiveness and reproducibility. Do not rely on GitHub stars.

## Exclusion criteria

- Proprietary SaaS, closed-source products, or commercial-only security functionality.
- Source-available or restrictive licenses (for example BSL, SSPL, Elastic, Commons Clause, non-commercial terms, or custom model licenses). A repository whose root license is not open does not qualify even if one subfolder is.
- Projects whose useful security capability needs a proprietary hosted service, account or API token.
- Archived or unmaintained projects.
- Projects created or maintained by direct competitors of the community's sponsor, Snyk. Vendor-maintained open-source projects from other organizations are not excluded for that reason.
- Promotional submissions, or submissions without verifiable evidence.
- Duplicates of an existing canonical entry.

## How to suggest a resource

1. Search `data/resources.yml` and [`maintainers/research-inventory.md`](maintainers/research-inventory.md) to see whether it is already listed, held or rejected.
2. Open a [new resource issue](.github/ISSUE_TEMPLATE/new-resource.yml) with the official URL, repository, license, lifecycle stage, domain and evidence of maintenance. State your relationship to the project. Conflicts of interest do not disqualify a submission but must be disclosed.
3. Or open a pull request (below).

## Pull request workflow

```bash
pip install -r requirements.txt
# edit data/resources.yml  (add or update an entry)
python scripts/generate.py   # regenerates README tables, lifecycle pages, topic index, catalogue
python scripts/validate.py   # schema, license, duplicates, promotional wording, internal links
```

Commit the YAML change and the regenerated Markdown together. Do not edit text between `<!-- BEGIN GENERATED -->` markers by hand.

Entry rules:

- `description` and `summary` say what the project does and why it matters to AI Security Engineering. No superlatives, no unsupported effectiveness claims, no marketing language.
- Use one canonical entry per project. Other stages and domains cross-reference it through `lifecycle` and `domains`.
- `license` must be an SPDX identifier verified from the LICENSE file; put the evidence URL in `license_evidence`. Use `license_note` for caveats such as mixed licensing.
- Set `verification` to `verified` only if license and release evidence were both checked. Otherwise use `partial` and explain in `notes`.
- If your employer or sponsor created the project, add a `disclosure`.

## Update an existing entry

Open a pull request changing the YAML entry, with a link to the evidence (release page, LICENSE change, archive notice). If you only want to flag it, use the [update issue form](.github/ISSUE_TEMPLATE/update-entry.yml).

## Report a broken link

Use the [broken link form](.github/ISSUE_TEMPLATE/broken-link.yml). A scheduled workflow also checks links weekly and opens an issue; it never removes entries.

## Report a licensing concern

Use the [license concern form](.github/ISSUE_TEMPLATE/license-concern.yml), citing the file and commit where the license is stated. Maintainers will re-verify and, if the entry no longer qualifies, move it to the research inventory with the reason recorded.

## Suggest taxonomy improvements

The lifecycle (Discover, Design, Build, Break, Defend) and the ten technical domains are the main structure. Use the [taxonomy form](.github/ISSUE_TEMPLATE/taxonomy.yml) to propose a change, with the resources it would affect and why the current structure is confusing.

## Contribute research

Open research is welcome when it ships reproducible artifacts and states its limitations. Propose it as a resource with `type: Open Research` or `Benchmark`. Methodology write-ups in `research/` follow the pattern in [research/vulnbench.md](research/vulnbench.md): question, method, results, limits, disclosure.

## How maintainers evaluate submissions

1. **Identity:** is this the official project, not a fork or a similarly named one?
2. **License:** read the LICENSE file at the default branch; check subfolders and datasets.
3. **Open functionality:** does the open version do what the entry claims?
4. **Maintenance:** latest release or commit evidence, archive status, issue and release activity.
5. **Relevance and distinctiveness:** does it help an engineer build, test or defend AI-native systems, and is it different from what is listed?
6. **Neutrality:** same criteria as every other entry; any sponsor relationship is disclosed.
7. **Decision:** include, hold (needs a fact or more track record) or exclude. Decisions and reasons are recorded in the [research inventory](maintainers/research-inventory.md). Maintainers aim to respond within two weeks, but this is a volunteer effort.

Entries are never removed silently. Stale, broken or doubtful entries are flagged for human review in an issue.

## Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
