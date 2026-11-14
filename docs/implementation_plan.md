# Implementation plan

**Planning date:** 2026-11-14  
**Deadline:** 2026-11-17 (confirm exact time and upload process in organizer email)

This is a compressed plan. Adjust it to the available team time; prioritize correctness and reproducibility over adding many model components.

## Work sequence

### 1. Confirm prerequisites
- [ ] Confirm team registration, common team name, and 3–5 member eligibility for later stages.
- [ ] Save the organizer's submission email/form instructions when received.
- [ ] Keep the portable drive connected and confirm accepted data-use terms.

### 2. Connect the repository to the assets
- [ ] Obtain the official challenge repository into a `vendor/` folder or use a documented clean clone.
- [ ] Record the official repository commit/tag used.
- [ ] Map the current flat file layout and `-001` video suffixes to the expected `data/tactical/` and `data/broadcast/` paths without changing originals.
- [ ] Verify file presence and frame alignment using official loaders.

### 3. Establish a valid baseline
- [ ] Install the official evaluation dependencies.
- [ ] Generate the official reference baseline using the authorized ATD.
- [ ] Run the official scorer against its included public ground-truth slice only to verify that the pipeline is wired correctly. Do not use this slice to choose model parameters.
- [ ] Record environment, commands, and any errors.

### 4. Improve the method conservatively
- [ ] Choose a small number of algorithmic improvements with a clear reason (for example, combine independent tracking and tagging evidence, then apply a temporal state/segmentation method).
- [ ] Avoid manual annotation, frame-specific hand edits, or any private/human-produced labels for this match.
- [ ] Keep every experiment reproducible and record it in `experiment_log.md`.
- [ ] Prefer robust full-match logic over tuning to the five-minute public sample.

### 5. Package and submit
- [ ] Generate the final full-length CSV.
- [ ] Run the official validator on that exact CSV.
- [ ] Confirm the public repository regenerates the same file and contains no restricted assets or derived exports.
- [ ] Complete `technical_report.md`, remove unresolved placeholders, and ensure report matches code.
- [ ] Name the submission CSV and technical document after the team.
- [ ] Submit once per team through the organizer's form before the stated deadline; retain the confirmation.

## Work ownership

Assign owners with the actual team members; do not assume roles based on this template.

| Work area | Owner | Status |
|---|---|---|
| Data path mapping and baseline reproduction | [name] | Not started |
| Algorithm and experiments | [name] | Not started |
| Reproducibility, validation, and public repo review | [name] | Not started |
| Technical report and final form | [name] | Not started |

## Decision gate

If there is not enough time to support a proposed improvement with a reproducible experiment and accurate documentation, keep the validated baseline and describe its limitations honestly.
