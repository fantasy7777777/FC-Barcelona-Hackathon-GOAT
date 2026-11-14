# Solution source

`baseline.py` implements GOAT's first transparent reference approach. It reads tactical ATD and XML metadata, assigns each visible ball to the nearest tracked player, applies a centered majority window, and writes the full CSV. See `../docs/algorithm_guide.md` for a plain-language walkthrough.

Run from the repository directory:

```powershell
py -3 src/baseline.py --data-dir E:\Download\Hackathon --window 50 --out outputs\GOAT.csv
```

Python's standard library only. This is a starter baseline; it has not yet been executed in this environment because the configured Python launcher points to a missing interpreter. Run it on a machine with Python installed, then compare its behavior using the official evaluation tools.
