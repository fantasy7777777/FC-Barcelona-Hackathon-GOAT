# GOAT — More Than A Hack 2027

GOAT's Phase 1 submission project for frame-level football possession classification.

## Current method

`src/baseline.py` is a transparent rule-based baseline. For every frame with a detected ball and at least one tracked player, it assigns possession to the team of the nearest player, then applies a centred majority vote over a configurable time window. It uses tactical ATD tracking and its XML metadata; it does not train a machine-learning model.

The default smoothing half-window is 50 frames (2 seconds at 25 fps on each side). The current implementation outputs `D` if the smoothing window contains no H/A vote. This is a convenience fallback for missing evidence, not a reliable detector of an actual dead-ball interval; see [GOAT.md](GOAT.md).

## Reproduce locally

Use Python 3.10 or later; the generator uses only the standard library. Keep the competition data in the location allowed by the organizer's terms and do not commit it. From this repository root, run:

```powershell
python src/baseline.py --data-dir "E:\Download\Hackathon" --window 50 --out outputs\GOAT.csv
```

The output folder is intentionally Git-ignored. The visualizer is a separate local browser tool in `visualizer/index.html`; it reads selected files locally and is for inspection, not the competition deliverable.

## Status and limitations

The team generated `outputs/GOAT.csv` locally and reported that the official format validator accepted it (199,319 frames, indices 0–199,318). This confirms format only, not prediction quality. No performance score against public ground truth is claimed. The method can misassign loose balls, duels, and tracking gaps; the technical report records these limitations and the exact reproduction details.

See [docs/submission_checklist.md](docs/submission_checklist.md) for final packaging checks.
