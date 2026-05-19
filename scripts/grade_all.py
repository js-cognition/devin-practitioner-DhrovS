#!/usr/bin/env python3
"""Run all grading: pytest for each challenge + multiple-choice answers.

Outputs a summary with points per section and a total score.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHALLENGES = [
    {
        "name": "Challenge 1 — Fix a Bug",
        "test_dir": ROOT / "challenges" / "challenge_1_fix_bug",
        "test_file": "test_calculator.py",
        "points": 30,
    },
    {
        "name": "Challenge 2 — Add a Feature",
        "test_dir": ROOT / "challenges" / "challenge_2_add_feature",
        "test_file": "test_string_utils.py",
        "points": 30,
    },
    {
        "name": "Challenge 3 — Knowledge Notes",
        "test_dir": ROOT / "challenges" / "challenge_3_knowledge",
        "test_file": "test_data_processor.py",
        "points": 30,
    },
]

MC_POINTS = 10


def run_pytest(test_dir: Path, test_file: str) -> tuple[int, int]:
    """Run pytest and return (passed, total) test counts."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_file, "-v", "--tb=short"],
        cwd=test_dir,
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

    passed = result.stdout.count(" PASSED")
    failed = result.stdout.count(" FAILED")
    error = result.stdout.count(" ERROR")
    total = passed + failed + error
    return passed, total


def run_mc_grader() -> int:
    """Run the MC grader and return score out of MC_POINTS."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "grade_answers.py")],
        capture_output=True,
        text=True,
    )
    print(result.stdout)

    for line in result.stdout.splitlines():
        if "Multiple-choice score:" in line:
            parts = line.split(":")[-1].strip().split("/")
            return int(parts[0])
    return 0


def main() -> None:
    print("=" * 60)
    print("  DEVIN FUNDAMENTALS — AUTO-GRADER")
    print("=" * 60)

    total_score = 0
    total_possible = 0

    for ch in CHALLENGES:
        print(f"\n{'─' * 60}")
        print(f"  {ch['name']} ({ch['points']} pts)")
        print(f"{'─' * 60}")

        passed, total = run_pytest(ch["test_dir"], ch["test_file"])
        if total > 0:
            fraction = passed / total
            earned = round(ch["points"] * fraction)
        else:
            earned = 0

        print(f"  Result: {passed}/{total} tests passed → {earned}/{ch['points']} pts")
        total_score += earned
        total_possible += ch["points"]

    print(f"\n{'─' * 60}")
    print(f"  Multiple-Choice Questions ({MC_POINTS} pts)")
    print(f"{'─' * 60}")

    mc_score = run_mc_grader()
    total_score += mc_score
    total_possible += MC_POINTS

    print(f"\n{'=' * 60}")
    print(f"  TOTAL SCORE: {total_score}/{total_possible}")
    print(f"{'=' * 60}")

    if total_score >= total_possible:
        print("\n  ALL CHALLENGES COMPLETE — Well done!")
    elif total_score > 0:
        print(f"\n  Progress: {total_score}/{total_possible} — keep going!")
    else:
        print("\n  No points earned yet — start by completing Challenge 1.")


if __name__ == "__main__":
    main()
