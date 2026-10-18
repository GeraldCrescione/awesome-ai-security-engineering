# Maintaining and expanding the list

## Files you edit

| File | Purpose |
|---|---|
| `data/resources.yml` | Published entries. The single source of truth. |
| `maintainers/candidates.yml` | Evaluated but unpublished candidates, with decision and reason. |
| `lifecycle/*.md`, `best-practices/`, `research/vulnbench.md`, `foundations/` | Hand-written text. Edit directly. |

Never edit text between `<!-- BEGIN GENERATED -->` and `<!-- END GENERATED -->`. Run `python scripts/generate.py` instead.

## Add an entry

1. Verify the candidate against the checklist in [CONTRIBUTING.md](../CONTRIBUTING.md): official source, LICENSE file at the default branch, open functionality, maintenance evidence, duplicates.
2. Add it to `data/resources.yml`. Use an existing entry as a template.
3. `pip install -r requirements.txt && python scripts/generate.py && python scripts/validate.py`
4. If you reject or hold a candidate, record it in `maintainers/candidates.yml` with a reason and evidence so it is not re-researched.

## Remove or demote an entry

Move it from `resources.yml` to `candidates.yml` with `decision: exclude` or `hold` and the reason (archived, license change, requires proprietary service). Removal is always a human decision recorded in git history; automation only flags.

## Routine

- **Weekly (automatic):** the Links and freshness workflow checks external links and opens an issue for entries to re-verify. It never changes content.
- **Quarterly (manual):** re-verify every entry marked `partial` and every entry older than 180 days; check for archive banners, license changes and moved repositories; re-run the gap review in [strategy-review.md](strategy-review.md).
- **On each pull request:** CI runs validation, checks that generated files are current and lints Markdown.

## Cap and growth

The first release is capped at 30 entries (`MAX_ENTRIES` in `scripts/awesome_lib.py`). Raise the cap deliberately when the review process can sustain more. Prefer replacing weak entries over adding marginal ones.

## What automation cannot do

Link checks do not prove a project is maintained, and a passing license check reads only the field you wrote. A human must read the LICENSE file for each new entry and re-check entries whose repository ownership or branding changes.

## Setup notes for the first publication

- The workflows pin well-known action versions that were not re-verified at build time; confirm they resolve on first run.
- Create the labels used by the issue forms (`new-resource`, `update-entry`, `broken-link`, `license-concern`, `taxonomy`).
- Add an enforcement contact for the Code of Conduct if you want one beyond the community website.
