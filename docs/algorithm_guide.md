# First algorithm: nearest player, then smooth

## The idea

The tracking file gives a location for the ball and for many player track slots on each frame. The metadata says which team each slot belongs to. A simple first guess is: **the team whose tracked player is closest to the ball is the team in possession.**

Then the raw guess is smoothed across nearby frames. Tracking can jump or flicker for one frame, while a real possession usually lasts longer. The current default looks 50 frames backward and 50 forward; at 25 frames per second, that is a centred window of about four seconds total.

## What the code does

1. Reads track-slot team assignments from the XML metadata. In this match the first listed team is home (`H`) and the second is away (`A`).
2. Reads the tactical tracking text one frame at a time. ATD frame ids start at 1, so the script writes each prediction at index `frame_id - 1`.
3. Converts normalized x/y coordinates to metres before comparing distance. The pitch is much longer than it is wide, so raw normalized distances would distort the comparison.
4. If the ball and at least one player are visible, finds the nearest player and records that player's team. If the ball or all players are missing, it records no vote.
5. For each frame, counts home and away votes in the centred window. The larger count wins; a tie goes to home. If there are no votes for either team, it outputs `D`.
6. Writes exactly one `frame,label` row per tactical video frame.

## Run it

From the repository folder in PowerShell:

```powershell
py -3 src/baseline.py --data-dir E:\Download\Hackathon --window 50 --out outputs\GOAT.csv
```

Use `--window 0` for unsmoothed output. A frame count other than 199,319 should only be used for controlled debugging, not a submission.

## What this baseline gets wrong

- Nearest does not always mean possession. A player can be close during a loose ball or an opponent can be closer while the first team retains control.
- Missing ball detections are frequent. This algorithm has little evidence during those stretches.
- Smoothing can delay real possession changes, erase short possessions, or carry one side's label through a stoppage.
- It does not use the Smart Tagging, video, or homography.

This is a learning and reproducibility baseline, not a claim of a strong score. The official reference repository also starts from nearest-player assignment and temporal smoothing, and reports that smoothing choice changes spellF1 substantially. Do not tune window size against the public five-minute labels; the competition rules reserve those for checking pipeline correctness.

## Concepts to remember

- **Feature:** a measurable input, such as ball/player distance.
- **Rule-based baseline:** explicit logic rather than a trained model. It is easy to understand and debug.
- **Temporal smoothing:** combine nearby frame decisions to reduce noise, while risking lag at transitions.
- **Possession spell:** a continuous interval of `H` or `A`. Because spellF1 ranks the challenge, reducing false tiny spells matters more than maximizing raw frame accuracy.
- **Validation vs tuning:** using the public sample to confirm file alignment/format is permitted; repeatedly changing parameters to maximize its score is not.
