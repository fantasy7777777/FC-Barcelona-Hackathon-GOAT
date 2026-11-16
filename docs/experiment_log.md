# Experiment log

Record reproducible experiments. Do not use the public five-minute labels as a tuning set.

| Date | Code/version | Inputs/features | Method/change | Public pipeline check (not tuning) | Notes / failure modes |
|---|---|---|---|---|---|
| 2026-11-17 | `src/baseline.py` v0 | Tactical ATD + metadata | Nearest tracked player to ball; centered majority window +/-50 frames | User reports official format validator accepted 199,319 rows, frames 0..199318 | Generated locally with Python 3.12.4. Validator confirms format only. No ground-truth performance score or parameter tuning is recorded. Known limitation: D is emitted when the smoothing window has no H/A evidence, without a dead-ball detector. |
