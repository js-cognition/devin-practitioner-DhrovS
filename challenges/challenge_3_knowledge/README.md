# Challenge 3: Use Knowledge Notes

## Concept

**Knowledge notes** give Devin persistent context that it recalls automatically across sessions. Instead of repeating the same instructions every time, you write them once as a Knowledge note and Devin follows them whenever they are relevant.

This is how teams enforce coding standards, document internal patterns, and share context that every engineer (including Devin) should know.

## The Task

`data_processor.py` needs three functions implemented:

- `flatten_dict(nested, separator)` — flatten a nested dictionary.
- `chunk_list(items, chunk_size)` — split a list into fixed-size chunks.
- `remove_duplicates(items)` — remove duplicates while preserving order.

But there is a catch: this project enforces **strict coding conventions**. The auto-grader checks that every function you add:

1. Has **type hints** on all parameters and the return value.
2. Has a **Google-style docstring** with `Args:` and `Returns:` sections.
3. Does **not** use any `# type: ignore` comments.

## What To Do

1. Go to **Devin Settings > Knowledge** and create a new note scoped to your repo.
2. In the note, describe the coding conventions:

   > All functions must have type hints on every parameter and the return value.
   > All functions must have a Google-style docstring with Args and Returns sections.
   > Do not use `# type: ignore` comments.

3. Start a Devin session and ask it to implement the functions in `data_processor.py`.
4. Because of your Knowledge note, Devin should automatically follow the conventions.
5. The tests verify both **correctness** and **convention compliance**.

## Why Knowledge Notes Matter

Without a Knowledge note, you would have to include the coding conventions in every single prompt. Knowledge notes let you "teach" Devin your project's rules once, and it remembers them forever.

## Verification

```bash
cd challenges/challenge_3_knowledge
python -m pytest test_data_processor.py -v
```
