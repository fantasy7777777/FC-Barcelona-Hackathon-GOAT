# GOAT — Technical Report

## Approach

This submission uses a deterministic, rule-based baseline. For each frame, the program finds the tracked player closest to the tracked ball, measuring normalized coordinates in pitch metres (105.3 m by 68.0 m). The player’s metadata team becomes the frame’s raw possession vote. It then applies a centered majority vote over a half-window of 50 frames in either direction (about two seconds each way at 25 fps). Ties go to home. The smoothing window is configurable.

This is not a trained model. It does not estimate possession from video pixels, and it does not combine Smart Tagging or homography data.

## Assets and training data

The generator uses the supplied tactical ATD tracking text and corresponding XML metadata to read ball/player locations and map track slots to teams. It uses no labeled training dataset and no manually created labels. The optional web visualizer can display the tactical video locally for human visual comparison; it does not feed video into the classifier.

## Label and possession rules

The nearest player’s team is the raw vote when both the ball and a player location are available. A centered majority vote smooths those votes; a tie resolves to home. In the current code, if a smoothing window contains no home or away votes, the output is `D`. This is only a missing-evidence fallback. The implementation has no independent dead-ball detector, so it cannot reliably distinguish a true ball-out/stoppage interval (`D`) from unavailable tracking evidence (which may call for abstention, `X`). This is a known weakness of the baseline.

## Validation and results

The team reports that the official submission-format validator accepted the generated CSV: 199,319 rows with frame indices 0 through 199,318 and labels in the allowed set. The validator checks structure, not whether predictions are correct. No score or performance claim against ground truth is reported, and no public labels were used for tuning.

## Limitations

Nearest-player distance is not equivalent to control. The rule can fail during loose balls, duels, deflections, goalkeeper actions, tracking errors, and missing-ball stretches. Temporal smoothing can delay changes, erase short spells, and carry a label through interruptions. The output’s `D` fallback is particularly weak because it does not detect dead-ball events. This baseline should be treated as a reproducible starting point rather than a strong possession model.

## Reproduction

The generator uses Python 3.10+ and only the standard library. From the repository root, with the authorized tactical ATD XML and TXT available in the selected data folder:

```powershell
python src/baseline.py --data-dir "E:\Download\Hackathon" --window 50 --out outputs\GOAT.csv
```

The output has columns `frame,label` and is written locally. The separate official validator and its dependencies are available from the organizer’s challenge repository; the validator is not included in this solution repository. Do not commit the match assets or generated full-match CSV to the public repository. The team must upload the CSV and this report through the organizer’s submission process.
