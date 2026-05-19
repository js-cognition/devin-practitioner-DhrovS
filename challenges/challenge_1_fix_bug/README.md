# Challenge 1: Start a Devin Session & Fix a Bug

## Concept

The most fundamental Devin skill is **starting a session and giving it a task**. Devin is an autonomous AI software engineer — you give it a goal, it writes code, runs tests, and opens a PR.

## The Bug

`calculator.py` contains a `Calculator` class. Three of its methods have bugs:

- `divide()` does not handle division by zero correctly.
- `power()` returns the wrong result for negative exponents.
- `average()` calculates the average incorrectly.

## What To Do

1. Go to [app.devin.ai](https://app.devin.ai) and click **New Session**.
2. Paste a link to your assignment repository so Devin can access it.
3. Write a prompt like:

   > Fix the bugs in `challenges/challenge_1_fix_bug/calculator.py`. Run the tests in `challenges/challenge_1_fix_bug/test_calculator.py` to verify your fixes.

4. Watch Devin work in the session timeline.
5. When Devin opens a PR (or pushes to your branch), review the changes and merge.

## Verification

Run locally:

```bash
cd challenges/challenge_1_fix_bug
python -m pytest test_calculator.py -v
```

All tests must pass for full credit.
