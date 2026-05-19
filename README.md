# Devin Fundamentals

Welcome to the **Devin Fundamentals** course! This hands-on assignment teaches you three core Devin concepts by having you complete real tasks using Devin, verified automatically by GitHub Actions.

## Prerequisites

- A [Devin](https://devin.ai) account (BYOL - Bring Your Own Login)
- Basic familiarity with Git and GitHub

## How It Works

1. **Accept the assignment** via GitHub Classroom — this creates your personal copy of this repo.
2. **Complete the three challenges** below by using Devin to make the required code changes.
3. **Answer the two multiple-choice questions** in `answers.yml`.
4. **Push your changes** — GitHub Actions will automatically grade your work.

Check the **Actions** tab in your repo to see your score.

---

## Challenge 1: Start a Devin Session & Fix a Bug

**Concept:** Creating a Devin session and giving it a task.

The file `challenges/challenge_1_fix_bug/calculator.py` contains a `Calculator` class with several bugs. Your job is to **start a Devin session**, point it at your repo, and ask it to fix the failing tests.

**Steps:**
1. Open [Devin](https://app.devin.ai) and start a new session.
2. Give Devin access to your assignment repo.
3. Ask Devin to fix the bugs in `challenges/challenge_1_fix_bug/calculator.py` so that all tests in `challenges/challenge_1_fix_bug/test_calculator.py` pass.
4. Review Devin's PR, then merge it (or push the changes directly).

**Verification:** All tests in `test_calculator.py` pass.

See `challenges/challenge_1_fix_bug/README.md` for detailed instructions.

---

## Challenge 2: Write an Effective Prompt

**Concept:** Writing clear, specific prompts so Devin produces exactly what you need.

The file `challenges/challenge_2_add_feature/string_utils.py` has three functions with `TODO` placeholders. Tests already define the expected behaviour.

**Steps:**
1. Read the test file to understand what each function should do.
2. Write a **clear, specific prompt** for Devin that describes exactly what to implement.
3. Start a Devin session with your prompt and let it implement the functions.
4. Verify the tests pass.

**Verification:** All tests in `test_string_utils.py` pass.

See `challenges/challenge_2_add_feature/README.md` for detailed instructions.

---

## Challenge 3: Use Knowledge Notes

**Concept:** Using Knowledge to give Devin persistent project context.

The file `challenges/challenge_3_knowledge/data_processor.py` needs three new functions implemented. However, this project enforces **strict coding conventions** — every function must have a Google-style docstring and type hints on all parameters and return values.

**Steps:**
1. Create a **Knowledge note** in Devin (Settings > Knowledge) with your project's coding conventions.
2. Start a Devin session and ask it to implement the functions in `data_processor.py`.
3. Because of your Knowledge note, Devin should automatically follow the conventions.
4. The tests check both correctness **and** convention compliance.

**Verification:** All tests in `test_data_processor.py` pass, including convention checks.

See `challenges/challenge_3_knowledge/README.md` for detailed instructions.

---

## Multiple-Choice Questions

Open `answers.yml` and replace the blank values with your answers (`A`, `B`, `C`, or `D`).

---

## Grading

| Component | Points |
|-----------|--------|
| Challenge 1 — Fix a Bug | 30 |
| Challenge 2 — Add a Feature | 30 |
| Challenge 3 — Knowledge Notes | 30 |
| Multiple-Choice Questions | 10 |
| **Total** | **100** |

Your score will appear in the GitHub Actions output after each push.
