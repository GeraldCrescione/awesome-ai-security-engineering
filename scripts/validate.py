#!/usr/bin/env python3
"""Validate resource metadata and internal Markdown links.

Errors (exit 1): schema violations, duplicates, blocked license terms, promotional wording,
more than 30 entries, undisclosed Snyk affiliation, broken internal links or anchors.
Warnings (exit 0): verification older than 180 days, partial verification older than 90 days.

Nothing here removes or edits entries. Flagged items are for human review.
Usage: python scripts/validate.py
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from urllib.parse import unquote, urlparse

from awesome_lib import (
    ALLOWED_LICENSES, BLOCKED_LICENSE_TERMS, DECISIONS, DOMAINS, LIFECYCLE, MAX_ENTRIES,
    PROMO_WORDS, REQUIRED, ROOT, TYPES, VERIFICATION, VERIFIED_BY, anchor, load_candidates,
    load_resources, slugify,
)

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def norm_url(u: str) -> str:
    p = urlparse(u.strip())
    return f"{p.netloc.lower()}{p.path.rstrip('/')}".removeprefix("www.")


def check_resources() -> list[dict]:
    rs = load_resources()
    if len(rs) > MAX_ENTRIES:
        err(f"{len(rs)} entries exceed the first-release cap of {MAX_ENTRIES}")
    ids, names, urls, slugs = set(), set(), {}, set()
    today = dt.date.today()
    for r in rs:
        rid = r.get("id", "<missing id>")
        for f in REQUIRED:
            if r.get(f) in (None, "", []):
                err(f"{rid}: missing required field '{f}'")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(r.get("id", ""))):
            err(f"{rid}: id must be kebab-case")
        if rid in ids:
            err(f"{rid}: duplicate id")
        ids.add(rid)
        name = str(r.get("name", "")).lower()
        if name in names:
            err(f"{rid}: duplicate name '{r.get('name')}'")
        names.add(name)
        if r.get("name"):
            s = anchor(r)
            if s in slugs:
                err(f"{rid}: heading anchor '{s}' collides with another entry")
            slugs.add(s)
        for f in ("url", "source", "license_evidence"):
            v = str(r.get(f, ""))
            if v and not v.startswith("https://"):
                err(f"{rid}: {f} must be an https URL")
        key = norm_url(str(r.get("url", "")))
        if key in urls:
            err(f"{rid}: url duplicates {urls[key]}")
        urls[key] = rid
        if r.get("type") not in TYPES:
            err(f"{rid}: unknown type '{r.get('type')}'")
        for s in r.get("lifecycle") or []:
            if s not in LIFECYCLE:
                err(f"{rid}: unknown lifecycle stage '{s}'")
        for d in r.get("domains") or []:
            if d not in DOMAINS:
                err(f"{rid}: unknown domain '{d}'")
        lic = str(r.get("license", ""))
        if not any(lic == a or lic.startswith(a + " ") or lic.startswith(a + ";") for a in ALLOWED_LICENSES):
            err(f"{rid}: license '{lic}' does not start with an allowed SPDX identifier")
        for term in BLOCKED_LICENSE_TERMS:
            if term.lower() in lic.lower():
                err(f"{rid}: license field contains blocked term '{term}'")
        if r.get("verification") not in VERIFICATION:
            err(f"{rid}: verification must be one of {VERIFICATION}")
        elif r["verification"] == "partial":
            pd = r.get("verified_on")
            if isinstance(pd, dt.date) and (today - pd).days > 90:
                warn(f"{rid}: 'partial' verification is older than 90 days; re-check")
        if r.get("verified_by") not in VERIFIED_BY:
            err(f"{rid}: verified_by must be one of {VERIFIED_BY}")
        vd = r.get("verified_on")
        if not isinstance(vd, dt.date):
            err(f"{rid}: verified_on must be a YYYY-MM-DD date")
        else:
            if vd > today:
                err(f"{rid}: verified_on is in the future")
            elif (today - vd).days > 180:
                warn(f"{rid}: last verified {vd} (>180 days); re-verify")
        if len(str(r.get("summary", ""))) > 130:
            err(f"{rid}: summary longer than 130 characters")
        text = f"{r.get('summary', '')} {r.get('description', '')}".lower()
        for w in PROMO_WORDS:
            if w in text:
                err(f"{rid}: promotional wording '{w}'")
        if "snyk" in str(r.get("maintainer", "")).lower() and not r.get("disclosure"):
            err(f"{rid}: Snyk-maintained entries require a 'disclosure' field")
    return rs


def check_candidates(rs: list[dict]) -> None:
    published = {norm_url(r["url"]) for r in rs} | {norm_url(r["source"]) for r in rs}
    for c in load_candidates():
        if c.get("decision") not in DECISIONS:
            err(f"candidate '{c.get('name')}': decision must be one of {DECISIONS}")
        for f in ("name", "reason", "checked_on"):
            if not c.get(f):
                err(f"candidate '{c.get('name')}': missing '{f}'")
        if c.get("url", "").startswith("https://") and norm_url(c["url"]) in published:
            err(f"candidate '{c['name']}' is also published; remove one")


def heading_anchors(md: str) -> set[str]:
    out, in_code = set(), False
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code:
            m = re.match(r"#{1,6}\s+(.*)", line)
            if m:
                out.add(slugify(m.group(1)))
    return out


def check_links() -> None:
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    anchors = {p: heading_anchors(p.read_text(encoding="utf-8")) for p in md_files}
    link_re = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)")
    for p in md_files:
        text = re.sub(r"```.*?```", "", p.read_text(encoding="utf-8"), flags=re.DOTALL)
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        for target in link_re.findall(text):
            if re.match(r"^(https?:|mailto:)", target):
                continue
            path_part, _, frag = target.partition("#")
            dest = p if not path_part else (p.parent / unquote(path_part)).resolve()
            rel = p.relative_to(ROOT)
            if not dest.exists():
                err(f"{rel}: broken link -> {target}")
                continue
            if frag and dest.suffix == ".md":
                if dest not in anchors:
                    anchors[dest] = heading_anchors(dest.read_text(encoding="utf-8"))
                if frag.lower() not in anchors[dest]:
                    err(f"{rel}: missing anchor -> {target}")


def main() -> int:
    rs = check_resources()
    check_candidates(rs)
    check_links()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(rs)} resources checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
