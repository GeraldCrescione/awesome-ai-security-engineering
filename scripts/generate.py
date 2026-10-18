#!/usr/bin/env python3
"""Regenerate the list sections of the Markdown files from data/resources.yml.

Usage:
    python scripts/generate.py           # rewrite generated blocks in place
    python scripts/generate.py --check   # exit 1 if any block is out of date (used in CI)

Generated blocks sit between markers:
    <!-- BEGIN GENERATED: name -->
    ...
    <!-- END GENERATED: name -->
Everything outside the markers is hand-written and never touched.
"""
from __future__ import annotations

import argparse
import re
import sys

from awesome_lib import (
    DOMAINS, LIFECYCLE, ROOT, anchor, load_candidates, load_resources,
)

CAT = "resources/README.md"  # canonical catalogue


def link(r: dict, prefix: str = "") -> str:
    return f"[{r['name']}]({prefix}{CAT}#{anchor(r)})"


def short_license(r: dict) -> str:
    return r["license"].split(" (")[0].split(";")[0]


def stage_label(r: dict) -> str:
    return ", ".join(LIFECYCLE[s] for s in r["lifecycle"])


def domain_label(r: dict) -> str:
    return "; ".join(DOMAINS[d] for d in r["domains"])


def table(rows: list[list[str]], header: list[str]) -> str:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |")
    return "\n".join(out)


def by_name(rs: list[dict]) -> list[dict]:
    return sorted(rs, key=lambda r: r["name"].lower())


# ----------------------------------------------------------------------------- blocks
def block_readme(rs: list[dict]) -> str:
    parts = []
    for key, label in LIFECYCLE.items():
        primary = by_name([r for r in rs if r["lifecycle"][0] == key])
        if not primary:
            continue
        rows = [[link(r), r["summary"], r["type"], short_license(r)] for r in primary]
        parts.append(f"### {label}\n\n" + table(rows, ["Resource", "What it is", "Type", "License"]))
    return "\n\n".join(parts)


def block_stage(rs: list[dict], stage: str) -> str:
    items = by_name([r for r in rs if stage in r["lifecycle"]])
    if not items:
        return "_No verified resources for this stage yet. See [CONTRIBUTING.md](../CONTRIBUTING.md)._"
    rows = []
    for r in items:
        others = [LIFECYCLE[s] for s in r["lifecycle"] if s != stage]
        also = f" Also: {', '.join(others)}." if others else ""
        rows.append([link(r, "../"), r["summary"] + also, r["type"], short_license(r)])
    return table(rows, ["Resource", "What it is", "Type", "License"])


def block_topics(rs: list[dict]) -> str:
    parts = []
    for key, label in DOMAINS.items():
        items = by_name([r for r in rs if key in r["domains"]])
        parts.append(f"## {label}\n")
        if not items:
            parts.append("No resource has passed verification for this domain yet. "
                         "This is a known gap; see [CONTRIBUTING.md](../CONTRIBUTING.md) to propose one.\n")
            continue
        parts.append(table(
            [[link(r, "../"), r["summary"], stage_label(r)] for r in items],
            ["Resource", "What it is", "Lifecycle"],
        ) + "\n")
    return "\n".join(parts).rstrip()


def block_catalogue(rs: list[dict]) -> str:
    out = []
    for r in by_name(rs):
        lic = r["license"]
        lines = [
            f"## {r['name']}",
            "",
            r["description"].strip(),
            "",
            f"- **Type:** {r['type']}",
            f"- **Lifecycle:** {stage_label(r)}",
            f"- **Domain:** {domain_label(r)}",
            f"- **License / status:** {lic}" + (f" ({r['license_note']})" if r.get("license_note") else ""),
            f"- **Official URL:** <{r['url']}>",
            f"- **Source / specification:** <{r['source']}>",
            f"- **Maintainer:** {r['maintainer']}",
            f"- **Latest release evidence:** {r['last_release']}",
            f"- **Verification:** {r['verification']} ({r['verified_by']} check, {r['verified_on']}); "
            f"license evidence: <{r['license_evidence']}>",
        ]
        if r.get("disclosure"):
            lines.append(f"- **Disclosure:** {r['disclosure']}")
        if r.get("notes"):
            lines.append(f"- **Notes:** {r['notes']}")
        out.append("\n".join(lines))
    return "\n\n".join(out)


def block_types(rs: list[dict], types: list[str], prefix: str = "../") -> str:
    items = by_name([r for r in rs if r["type"] in types])
    if not items:
        return "_None listed yet._"
    return table(
        [[link(r, prefix), r["summary"], r["type"], stage_label(r)] for r in items],
        ["Resource", "What it is", "Type", "Lifecycle"],
    )


def block_inventory(rs: list[dict]) -> str:
    cands = load_candidates()
    out = ["## Published", ""]
    out.append(table(
        [[r["name"], r["type"], short_license(r), r["maintainer"], r["last_release"],
          f"{r['verification']} / {r['verified_by']}", r["verified_on"], f"<{r['license_evidence']}>"]
         for r in by_name(rs)],
        ["Name", "Type", "License", "Maintainer", "Latest release evidence", "Verification", "Date", "License evidence"],
    ))
    for decision, title in (("exclude", "Excluded"), ("hold", "On hold"), ("backlog", "Verified, deferred (backlog)")):
        items = [c for c in cands if c["decision"] == decision]
        out += ["", f"## {title}", ""]
        out.append(table(
            [[c["name"], c.get("license_found", ""), c["reason"].strip(),
              (f"<{c['evidence'].split(' ; ')[0]}>" if c.get("evidence") else ""), str(c["checked_on"])]
             for c in items],
            ["Candidate", "License found", "Reason", "Evidence", "Checked"],
        ))
    return "\n".join(out)


def block_standards(rs: list[dict]) -> str:
    return block_types(rs, ["Open Standard / Protocol", "Open Security Framework"])


# ----------------------------------------------------------------------------- plumbing
TARGETS = {
    "README.md": [("resources", block_readme)],
    "topics/README.md": [("topics", block_topics)],
    "resources/README.md": [("catalogue", block_catalogue)],
    "research/README.md": [("research", lambda rs: block_types(rs, ["Benchmark", "Open Research"]))],
    "learning/README.md": [("learning", lambda rs: block_types(rs, ["Learning / Lab"]))],
    "foundations/frameworks-and-standards.md": [("standards", block_standards)],
    "maintainers/research-inventory.md": [("inventory", block_inventory)],
}
for _stage in LIFECYCLE:
    TARGETS[f"lifecycle/{_stage}.md"] = [("stage", (lambda s: (lambda rs: block_stage(rs, s)))(_stage))]


def replace_block(text: str, name: str, body: str) -> tuple[str, bool]:
    pattern = re.compile(
        rf"(<!-- BEGIN GENERATED: {re.escape(name)} -->)\n?(.*?)\n?(<!-- END GENERATED: {re.escape(name)} -->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise SystemExit(f"missing generated markers for '{name}'")
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text, count=1), True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if generated blocks are stale")
    args = ap.parse_args()
    rs = load_resources()
    stale = []
    for rel, blocks in TARGETS.items():
        path = ROOT / rel
        original = path.read_text(encoding="utf-8")
        text = original
        for name, fn in blocks:
            text, _ = replace_block(text, name, fn(rs))
        if text != original:
            if args.check:
                stale.append(rel)
            else:
                path.write_text(text, encoding="utf-8")
                print(f"updated {rel}")
    if stale:
        print("Generated content is out of date in:", ", ".join(stale))
        print("Run: python scripts/generate.py")
        return 1
    if not args.check:
        print("generation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
