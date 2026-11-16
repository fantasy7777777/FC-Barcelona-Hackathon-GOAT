# Solution source

`baseline.py` is the reproducible, rule-based baseline described in the root [GOAT.md](../GOAT.md). It reads tactical ATD tracking and XML metadata, assigns the ball to the nearest tracked player, smooths the team votes, and writes a `frame,label` CSV.

Run from the repository root, substituting the local authorized data folder if needed:

```powershell
python src/baseline.py --data-dir "E:\Download\Hackathon" --window 50 --out outputs\GOAT.csv
```

The generator uses Python 3.10+ and the standard library only. `outputs/` is ignored by Git so the full-match submission stays local for separate upload. The team reports that the official format validator accepted its generated CSV; this does not measure prediction quality.
