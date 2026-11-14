# Local resource inventory

Inventory checked on 2026-11-14 from the connected drive. Sizes are the files currently present at `E:\Download\Hackathon` (not duplicated into this repository).

## Match resources found

| Resource | Size (bytes) | Notes |
|---|---:|---|
| `BAR-ATH_tactical-001.mp4` | 5,222,307,334 | Tactical video. Filename differs from official `BAR-ATH_tactical.mp4`. |
| `BAR-ATH_tactical_atd.txt` | 195,714,285 | Tactical automatic tracking records. First row begins with frame id 1. |
| `BAR-ATH_tactical_atd.xml` | 59,057 | Tracking metadata; indicates 25 fps. |
| `BAR-ATH_tactical_homography.csv` | 23,187,043 | Header includes `frame`, nine homography coefficients, reprojection error, and `valid`. |
| `BAR-ATH_tactical_smart_tagging.xml` | 261,055 | Tactical smart tagging intervals. |
| `BAR-ATH_broadcast-001.mp4` | 13,962,360,320 | Broadcast video. Filename differs from official `BAR-ATH_broadcast.mp4`. |
| `BAR-ATH_broadcast_atd.txt` | 141,966,465 | Broadcast ATD. |
| `BAR-ATH_broadcast_atd.xml` | 64,956 | Broadcast tracking metadata. |
| `BAR-ATH_broadcast_homography.csv` | 15,401,635 | Broadcast camera homography. |

## Archives present

Three ZIP archives are present. Each contains only one subset of the data bundle (a tactical Smart Tagging XML, a broadcast homography CSV, or broadcast ATD TXT). They appear to overlap files already unpacked. Keep them until the bundle has been checked and backed up; do not rely on them as complete backups.

## Important path mismatch

The assets currently sit directly in `E:\Download\Hackathon`, while the official starter expects `data/tactical/` and `data/broadcast/` subfolders. The two video names also have `-001` suffixes. This repository currently leaves all supplied assets in place to avoid a multi-gigabyte duplicate or an accidental rename.

Before running official loaders, either:

1. create a separate data folder with the canonical directory and filenames, or
2. adjust the local path configuration/loader to map the current filenames.

Do not publish match files or derived tracking exports. Keep this inventory descriptive and do not attach data files to a public repo.

## Observed format notes

- Tactical ATD sample line uses the structure `frame_id:track1;track2;...:ball`; absent observations are `NaN`.
- Tactical homography uses zero-based video frame indices, matching submission rows.
- Smart Tagging timestamps are in seconds; the official guide says convert using the 25 fps tactical timeline.

These observations are format checks only, not a data-quality audit or model evaluation.
