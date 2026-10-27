"""Shared definitions for the generator and validator.

The only third-party dependency is PyYAML (`pip install pyyaml`).
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RESOURCES_FILE = ROOT / "data" / "resources.yml"
CANDIDATES_FILE = ROOT / "maintainers" / "candidates.yml"

LIFECYCLE = {
    "discover": "Discover",
    "design": "Design",
    "build": "Build",
    "break": "Break",
    "defend": "Defend",
}

DOMAINS = {
    "ai-assisted-dev": "AI-Assisted Development Security",
    "llm-model": "LLM and Model Security",
    "agentic": "Agentic AI Security",
    "mcp-skills": "MCP and Agent Skills Security",
    "supply-chain": "AI Supply Chain Security",
    "agent-identity": "Agent Identity and Access",
    "data-rag": "Data and RAG Security",
    "red-teaming": "AI Red Teaming and Evaluations",
    "runtime": "AI Runtime Security",
    "governance-controls": "AI Security Governance and Engineering Controls",
}

TYPES = [
    "Open-Source Tool",
    "Open Standard / Protocol",
    "Open Security Framework",
    "Open Research",
    "Benchmark",
    "Reference Implementation",
    "Learning / Lab",
    "Engineering Best Practice",
]

VERIFICATION = ["verified", "partial"]
VERIFIED_BY = ["direct", "delegated"]
DECISIONS = ["exclude", "hold", "backlog"]

# Licenses accepted in the `license` field. The field must START with one of these identifiers.
ALLOWED_LICENSES = [
    "Apache-2.0", "MIT", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0",
    "LGPL-3.0-or-later", "LGPL-3.0-only", "GPL-3.0-or-later", "GPL-3.0-only",
    "AGPL-3.0-or-later", "AGPL-3.0-only",
    "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0",
]
# Terms that must never appear in the `license` field.
BLOCKED_LICENSE_TERMS = [
    "BUSL", "BSL", "SSPL", "Elastic", "Commons Clause", "Llama", "proprietary",
    "non-commercial", "NonCommercial", "source-available", "Fair Source", "PolyForm",
]
PROMO_WORDS = [
    "best-in-class", "world-class", "revolutionary", "cutting-edge", "state-of-the-art",
    "next-generation", "industry-leading", "seamless", "enterprise-grade", "game-changing",
    "powerful", "robust platform", "unparalleled",
]

REQUIRED = [
    "id", "name", "url", "source", "summary", "description", "type", "lifecycle", "domains",
    "license", "license_evidence", "maintainer", "last_release", "verification",
    "verified_by", "verified_on",
]


def load_resources() -> list[dict]:
    data = yaml.safe_load(RESOURCES_FILE.read_text(encoding="utf-8"))
    return data["resources"]


def load_candidates() -> list[dict]:
    data = yaml.safe_load(CANDIDATES_FILE.read_text(encoding="utf-8"))
    return data["candidates"]


def slugify(heading: str) -> str:
    """GitHub-style heading anchor."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s", "-", s)
    return s


def anchor(resource: dict) -> str:
    return slugify(resource["name"])
