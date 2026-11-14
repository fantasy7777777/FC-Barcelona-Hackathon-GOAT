# Data setup and handling

## Data is present on the portable drive

The current bundle is stored in the parent folder `E:\Download\Hackathon` rather than under this repository's `data/` directory. See `resource_inventory.md` for exact filenames and sizes. The large media files have not been duplicated into this repository.

The official expected layout is:

```text
data/
├── tactical/
│   ├── BAR-ATH_tactical.mp4
│   ├── BAR-ATH_tactical_atd.xml
│   ├── BAR-ATH_tactical_atd.txt
│   ├── BAR-ATH_tactical_homography.csv
│   └── BAR-ATH_tactical_smart_tagging.xml
└── broadcast/
    ├── BAR-ATH_broadcast.mp4
    ├── BAR-ATH_broadcast_atd.xml
    ├── BAR-ATH_broadcast_atd.txt
    └── BAR-ATH_broadcast_homography.csv
```

The provided videos are named `BAR-ATH_tactical-001.mp4` and `BAR-ATH_broadcast-001.mp4`. Before using official loaders, make a separate mapped data layout or update a local loader/config. Do not rename, move, or duplicate the original multi-gigabyte files without a deliberate plan.

## Alignment reminders

- Tactical video defines the submission timeline: frames `0..199318`.
- Tactical ATD `frame_id` starts at 1; video/submission indices start at 0.
- Smart Tagging start/end times are seconds from the tactical-video start; official conversion uses 25 fps.
- Tactical homography is already indexed from zero and aligns to submission frames.
- Broadcast recording has its own timeline and is not synchronized to tactical.

## Data protection and competition rules

- The accepted enrollment terms govern use of the match data.
- Keep videos, raw tracking, and reconstructive derivatives out of public Git repositories.
- Do not hand-label or manually correct the competition match.
- Do not use the public five-minute labels for training or tuning; they are for pipeline checks.
- Do not upload restricted videos, datasets, or extracts to cloud-hosted LLMs.

See the official `DATA.md`, `RULES.md`, and `OVERVIEW.md` for the full requirements.
