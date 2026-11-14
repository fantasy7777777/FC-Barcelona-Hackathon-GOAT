# More Than A Hack 2027 — Phase 1

Local working repository for the frame-level possession challenge. The authorized match data remains in the parent folder `E:\Download\Hackathon` and is intentionally not copied here.

## Challenge in brief

Produce one `frame,label` row for each of 199,319 tactical-video frames. Labels: `H` (Barcelona possession, ball live), `A` (Athletic Club possession, ball live), `D` (dead ball), `X` (abstain). The ranking metric is spellF1, which scores possession spells as intervals.

## First algorithm version

`src/baseline.py` is a transparent nearest-player plus temporal-smoothing baseline. It uses only Python's standard library and writes `outputs/GOAT.csv`. Read [`docs/algorithm_guide.md`](docs/algorithm_guide.md) for the concepts and limitations. The script has not yet been executed because the configured Python launcher points to a missing interpreter.

Open [`visualizer/index.html`](visualizer/index.html) in a browser, choose the tactical ATD XML and TXT files, then click **Analyze tracking** to see the baseline timeline and pitch positions. Loading the 196 MB tracking text may take a little while.

## Documents

See [`docs/README.md`](docs/README.md) for the full document index. The project scope and implementation plan are the starting point; the technical report remains a template until the algorithm and experiments are complete.

## Data status

Data files were found on the drive on November 14, 2026. The files are flat in the parent directory and the video filenames include `-001`; official loaders expect a structured layout and canonical names. See the resource inventory before configuring code. No assets were moved or duplicated during setup.

## Licensing

Original project code is licensed under MIT; the competition assets are excluded and remain governed by the enrollment terms. See [LICENSE](LICENSE), [third-party notices](THIRD_PARTY_NOTICES.md), and [licensing notes](docs/licensing.md).

## Official references

- https://github.com/metrica-sports/more-than-a-hack-2027
- https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/DATA.md
- https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/RULES.md
- https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/EVALUATION.md
- https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/SUBMISSION.md


