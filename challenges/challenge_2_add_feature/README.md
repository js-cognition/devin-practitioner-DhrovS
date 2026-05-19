# Challenge 2: Write an Effective Prompt

## Concept

Devin works best when you give it **clear, specific instructions**. Vague prompts lead to guesswork; precise prompts lead to correct code on the first try. This challenge teaches you to scope a task well before handing it to Devin.

## The Task

`string_utils.py` contains three functions with `TODO` placeholders:

- `slugify(text)` — convert a string to a URL-friendly slug.
- `truncate(text, max_length, suffix)` — shorten text with a suffix.
- `count_words(text)` — count words in a string.

The tests in `test_string_utils.py` define exactly how each function should behave, including edge cases.

## What To Do

1. **Read the test file first.** Understand every assertion — this is what "done" looks like.
2. **Write a detailed prompt** for Devin. A good prompt includes:
   - Which file to edit and which functions to implement.
   - Specific behaviour for edge cases (e.g., what `slugify` does with special characters).
   - A reference to the test file so Devin can verify its work.
3. Start a Devin session with your prompt.
4. Review the output and iterate if needed.

## Tips for Effective Prompts

- Be specific: "Implement `slugify` that lowercases, replaces spaces with hyphens, and strips non-alphanumeric characters" is better than "make slugify work."
- Reference the tests: "Ensure all tests in `test_string_utils.py` pass."
- Mention edge cases: "An empty string should return an empty string."

## Verification

```bash
cd challenges/challenge_2_add_feature
python -m pytest test_string_utils.py -v
```
