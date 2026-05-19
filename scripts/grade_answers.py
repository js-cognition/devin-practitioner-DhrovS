#!/usr/bin/env python3
"""Grade the multiple-choice answers in answers.yml."""

import sys
from pathlib import Path

import yaml

ANSWER_KEY = {
    "q1_persistent_context": "C",
    "q2_review_workflow": "C",
}

POINTS_PER_QUESTION = 5


def main() -> int:
    answers_path = Path(__file__).resolve().parent.parent / "answers.yml"
    if not answers_path.exists():
        print("ERROR: answers.yml not found")
        return 0

    with open(answers_path) as f:
        answers = yaml.safe_load(f) or {}

    score = 0
    total = len(ANSWER_KEY) * POINTS_PER_QUESTION

    for key, correct in ANSWER_KEY.items():
        student = str(answers.get(key, "")).strip().upper()
        if student == correct:
            print(f"  {key}: CORRECT ({student})")
            score += POINTS_PER_QUESTION
        elif student == "":
            print(f"  {key}: NOT ANSWERED")
        else:
            print(f"  {key}: INCORRECT (got {student}, expected {correct})")

    print(f"\nMultiple-choice score: {score}/{total}")
    return score


if __name__ == "__main__":
    score = main()
    sys.exit(0 if score > 0 else 1)
