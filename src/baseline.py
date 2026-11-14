"""Simple possession baseline for the More Than A Hack 2027 match.

For each frame with a tracked ball, assign the ball to the team of the nearest
tracked player. Then use a centred majority vote to reduce frame-to-frame
flicker. This is a starter baseline, not a competition-ready model.

This implementation reads the flat asset layout currently on the portable
drive. It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


N_FRAMES = 199_319
PITCH_LENGTH_M = 105.3
PITCH_WIDTH_M = 68.0
HOME, AWAY, NO_LABEL = 0, 1, -1
LABEL_TEXT = {HOME: "H", AWAY: "A", NO_LABEL: "D"}


def team_map_from_metadata(metadata_path: Path) -> tuple[list[int], tuple[str, str]]:
    """Return each ATD track slot's team and the home/away names.

    The EPTS metadata stores players in the same slot order as the raw ATD.
    The first team listed is the home team for this match.
    """
    root = ET.parse(metadata_path).getroot()
    teams = list(root.iter("Team"))
    players = list(root.iter("Player"))
    if len(teams) != 2:
        raise ValueError(f"Expected two teams in {metadata_path}, found {len(teams)}")
    if not players:
        raise ValueError(f"No Player/track-slot entries found in {metadata_path}")

    home_id = teams[0].get("id")
    away_id = teams[1].get("id")
    if not home_id or not away_id:
        raise ValueError("Team metadata is missing a team id")

    slot_teams: list[int] = []
    for player in players:
        team_id = player.get("teamId")
        if team_id == home_id:
            slot_teams.append(HOME)
        elif team_id == away_id:
            slot_teams.append(AWAY)
        else:
            raise ValueError(f"Unknown team id {team_id!r} in player metadata")

    names = (teams[0].findtext("Name") or "Home", teams[1].findtext("Name") or "Away")
    return slot_teams, names


def parse_xy_speed(group: str) -> tuple[float, float] | None:
    """Read a tracking group x,y,speed; return None for a missing coordinate."""
    if not group or group[0] == "N":  # ATD represents missing values as NaN
        return None
    values = group.split(",")
    if len(values) < 2:
        return None
    try:
        x, y = float(values[0]), float(values[1])
    except ValueError:
        return None
    if not (x == x and y == y):  # NaN check, without an extra dependency
        return None
    return x, y


def infer_nearest_team(
    tracking_path: Path, slot_teams: list[int], n_frames: int
) -> list[int]:
    """Assign each visible ball to its nearest tracked player, in pitch metres."""
    labels = [NO_LABEL] * n_frames
    seen_frames = bytearray(n_frames)

    with tracking_path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            fields = line.rstrip("\r\n").split(":")
            if len(fields) != 3:
                raise ValueError(f"Malformed ATD row {line_number}: expected 3 colon fields")
            try:
                frame_id = int(fields[0])
            except ValueError as exc:
                raise ValueError(f"Invalid frame id on ATD row {line_number}") from exc
            frame_index = frame_id - 1  # ATD starts at 1; the submission starts at 0
            if not 0 <= frame_index < n_frames:
                raise ValueError(f"Frame id {frame_id} is outside 1..{n_frames}")
            if seen_frames[frame_index]:
                raise ValueError(f"Duplicate frame id {frame_id}")
            seen_frames[frame_index] = 1

            player_groups = fields[1].split(";")
            if len(player_groups) != len(slot_teams):
                raise ValueError(
                    f"ATD row {line_number} has {len(player_groups)} tracks; "
                    f"metadata defines {len(slot_teams)}"
                )

            ball = parse_xy_speed(fields[2])
            if ball is None:
                continue
            ball_x, ball_y = ball[0] * PITCH_LENGTH_M, ball[1] * PITCH_WIDTH_M

            best_distance = float("inf")
            best_team = NO_LABEL
            for group, team in zip(player_groups, slot_teams):
                player = parse_xy_speed(group)
                if player is None:
                    continue
                dx = player[0] * PITCH_LENGTH_M - ball_x
                dy = player[1] * PITCH_WIDTH_M - ball_y
                distance_squared = dx * dx + dy * dy
                if distance_squared < best_distance:
                    best_distance = distance_squared
                    best_team = team
            labels[frame_index] = best_team

    missing_frame_count = seen_frames.count(0)
    if missing_frame_count:
        raise ValueError(
            f"ATD contains {missing_frame_count} missing frame rows; "
            f"expected all {n_frames} frames"
        )
    return labels


def smooth_majority(labels: list[int], half_window: int) -> list[str]:
    """Centred majority vote over H/A evidence; D if neither team is observed."""
    if half_window < 0:
        raise ValueError("Window must be zero or greater")
    if half_window == 0:
        return [LABEL_TEXT[label] for label in labels]

    home_prefix = [0]
    away_prefix = [0]
    for label in labels:
        home_prefix.append(home_prefix[-1] + (label == HOME))
        away_prefix.append(away_prefix[-1] + (label == AWAY))

    result: list[str] = []
    n = len(labels)
    for index in range(n):
        low = max(0, index - half_window)
        high = min(n, index + half_window + 1)
        home_count = home_prefix[high] - home_prefix[low]
        away_count = away_prefix[high] - away_prefix[low]
        if home_count == 0 and away_count == 0:
            result.append("D")
        elif home_count >= away_count:
            result.append("H")  # deterministic tie-break, matching the reference baseline
        else:
            result.append("A")
    return result


def write_submission(path: Path, labels: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["frame", "label"])
        writer.writerows(enumerate(labels))


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    default_data_dir = Path(
        os.environ.get("MTAH_DATA_DIR", str(repo_root.parent))
    )

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=default_data_dir,
                        help="folder containing the tactical ATD XML and TXT files")
    parser.add_argument("--window", type=int, default=50,
                        help="smoothing half-window in frames; 50 means +/- 2 seconds")
    parser.add_argument("--out", type=Path, default=repo_root / "outputs" / "GOAT.csv",
                        help="submission CSV destination")
    parser.add_argument("--frames", type=int, default=N_FRAMES,
                        help="expected number of tactical video frames")
    args = parser.parse_args()

    metadata_path = args.data_dir / "BAR-ATH_tactical_atd.xml"
    tracking_path = args.data_dir / "BAR-ATH_tactical_atd.txt"
    for path in (metadata_path, tracking_path):
        if not path.is_file():
            parser.error(f"Required data file not found: {path}")

    slot_teams, (home_name, away_name) = team_map_from_metadata(metadata_path)
    print(f"Home (H): {home_name}; away (A): {away_name}")
    print(f"Reading tactical tracking: {tracking_path}")
    raw_labels = infer_nearest_team(tracking_path, slot_teams, args.frames)
    visible = sum(label != NO_LABEL for label in raw_labels)
    print(f"Ball-nearest-player labels: {visible:,}/{args.frames:,} frames")

    labels = smooth_majority(raw_labels, args.window)
    write_submission(args.out, labels)
    counts = {label: labels.count(label) for label in ("H", "A", "D")}
    print(f"Wrote {args.out} ({len(labels):,} rows; window +/-{args.window})")
    print("Label counts: " + ", ".join(f"{k}={v:,}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
