"""Tests for string utility functions."""

import pytest
from string_utils import slugify, truncate, count_words


# ── slugify ──────────────────────────────────────────────────────────

class TestSlugify:
    def test_basic(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_characters(self):
        assert slugify("Hello, World!") == "hello-world"

    def test_multiple_spaces(self):
        assert slugify("hello   world") == "hello-world"

    def test_leading_trailing_spaces(self):
        assert slugify("  hello world  ") == "hello-world"

    def test_already_slug(self):
        assert slugify("hello-world") == "hello-world"

    def test_mixed_case_and_numbers(self):
        assert slugify("My Post 123") == "my-post-123"

    def test_empty_string(self):
        assert slugify("") == ""

    def test_only_special_chars(self):
        assert slugify("!@#$%^&*()") == ""

    def test_consecutive_hyphens_collapsed(self):
        assert slugify("hello---world") == "hello-world"

    def test_unicode_stripped(self):
        assert slugify("cafe\u0301 latte") == "caf-latte"


# ── truncate ─────────────────────────────────────────────────────────

class TestTruncate:
    def test_short_text_unchanged(self):
        assert truncate("hello", 10) == "hello"

    def test_exact_length_unchanged(self):
        assert truncate("hello", 5) == "hello"

    def test_truncated_with_default_suffix(self):
        assert truncate("hello world", 8) == "hello..."

    def test_truncated_with_custom_suffix(self):
        assert truncate("hello world", 7, suffix="--") == "hello--"

    def test_max_length_equals_suffix_length(self):
        assert truncate("hello world", 3) == "..."

    def test_max_length_less_than_suffix_raises(self):
        with pytest.raises(ValueError):
            truncate("hello", 2, suffix="...")

    def test_empty_string(self):
        assert truncate("", 5) == ""

    def test_empty_suffix(self):
        assert truncate("hello world", 5, suffix="") == "hello"


# ── count_words ──────────────────────────────────────────────────────

class TestCountWords:
    def test_basic(self):
        assert count_words("hello world") == 2

    def test_single_word(self):
        assert count_words("hello") == 1

    def test_empty_string(self):
        assert count_words("") == 0

    def test_only_whitespace(self):
        assert count_words("   ") == 0

    def test_multiple_spaces(self):
        assert count_words("hello   world   foo") == 3

    def test_tabs_and_newlines(self):
        assert count_words("hello\tworld\nfoo") == 3

    def test_leading_trailing_whitespace(self):
        assert count_words("  hello world  ") == 2
