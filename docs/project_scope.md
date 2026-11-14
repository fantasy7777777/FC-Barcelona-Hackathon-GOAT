# Project scope — More Than A Hack 2027, Phase 1

**Team:** GOAT
**Status:** Planning / data workspace prepared  
**As of:** 2026-11-14  
**Target submission deadline:** 2026-11-17 (the announcement shared with the team states 11:59 PM CET; confirm the official submission email/form)

## Objective

Build a reproducible algorithm that produces a possession label for each of the 199,319 frames of the tactical match video, and package the result for the Phase 1 automatic evaluation.

## In scope

- Set up the official starter/scoring code and document its version.
- Map the supplied assets to the official loaders without changing or duplicating the original media unnecessarily.
- Reproduce a reference baseline and validate the pipeline using the public five-minute sample only as a pipeline check.
- Develop and compare a small number of algorithmic approaches using permitted signals such as ATD, Smart Tagging, and tactical video.
- Produce the full-length `frame,label` CSV (`H`, `A`, `D`, or `X`).
- Validate the exact submission file with the official validator.
- Publish reproducible source code and a concise technical report, excluding restricted match data and reconstructive exports.

## Out of scope

- Building a dashboard as the competition deliverable. Visualizations may be used internally to inspect or debug the approach.
- Hand-labeling or manually correcting this match, including manual edits to transitions or prediction segments.
- Training or tuning against the public five-minute labels.
- Using private ground truth or human-produced labels/events about this match.
- Publishing or redistributing provided match assets or reconstructive derivatives.
- Building a complete general-purpose football analytics platform for multiple matches.

## Deliverables

1. One valid possession CSV with exactly 199,319 ordered frame rows.
2. A public code repository that regenerates that exact CSV from the authorized assets.
3. A short technical report describing approach, assets, any training data, possession rules, limitations, and reproduction steps.

## Acceptance criteria

- CSV header is exactly `frame,label`; frame indices are `0..199318` without gaps or duplicates.
- Each label is one of `H`, `A`, `D`, `X`; no blanks.
- Official validator passes on the exact final file.
- Repository contains instructions and pinned dependencies sufficient to reproduce the same output.
- No restricted assets or reconstructive outputs are committed publicly.
- Technical report explains the algorithm and makes no unsupported performance claims.

## Constraints and dependencies

- Team eligibility for later stages requires 3–5 members; confirm registration and team-name consistency separately.
- Official data terms accepted during enrollment govern handling and redistribution.
- Data files currently sit flat in the parent `E:\Download\Hackathon` directory. Current MP4 names use `-001` suffixes, while official tooling documents the names without that suffix.
- The portable drive must remain connected for any process that reads source data from it.
- Current time is November 14, leaving a short window before the announced November 17 deadline.

## Risks and responses

| Risk | Response |
|---|---|
| Loader path/name mismatch | Create a non-destructive path mapping or configurable loader; do not copy multi-gigabyte videos without need. |
| Weak public-sample signal | Do not tune to it; use it only to check alignment, format, and pipeline behavior. |
| Overfitting frame-wise labels and fragmenting spells | Optimize for possession intervals and inspect spell-level diagnostics, not accuracy alone. |
| Data accidentally committed | Keep data and generated full-match labels ignored; inspect Git status before publishing. |
| Time pressure | Prioritize reproducible baseline, one or two well-motivated improvements, validation, and documentation. |


