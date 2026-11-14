# Technical report — GOAT

> Draft template. Replace all bracketed prompts before submission. Keep the report consistent with the code that regenerates the submitted CSV.

## Approach

[Describe the algorithm and why it is suitable for frame-level possession and spellF1. Explain how temporal continuity and possession changes are handled.]

## Assets used

[List the supplied assets used and how each contributes. Also list assets tested and dropped. Do not include restricted data in this public report.]

## Training data

[List every labeled dataset used, source, labeler, and volume. State clearly if none was used. No labels from the provided match may be used.]

## Possession rules

[Describe how the system handles loose balls, duels, deflections, restarts, and dead-ball intervals.]

## Evaluation and validation

[Describe use of the public five-minute sample for pipeline checking only, the metric(s) considered, and file validation. Do not describe tuning against the public labels.]

## Limitations

[Where does the approach fail? What would you improve with more time?]

## Reproduction

[Python version, pinned dependencies, setup steps, and the exact command that regenerates `GOAT.csv` from the authorized data bundle.]

