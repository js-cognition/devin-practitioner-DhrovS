"""Tests for data_processor — checks both correctness and coding conventions."""

import ast
import inspect
import typing

import pytest
from data_processor import flatten_dict, chunk_list, remove_duplicates


# ── flatten_dict ─────────────────────────────────────────────────────

class TestFlattenDict:
    def test_already_flat(self):
        assert flatten_dict({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    def test_single_nesting(self):
        assert flatten_dict({"a": {"b": 1}}) == {"a.b": 1}

    def test_deep_nesting(self):
        assert flatten_dict({"a": {"b": {"c": 3}}}) == {"a.b.c": 3}

    def test_custom_separator(self):
        assert flatten_dict({"a": {"b": 1}}, separator="/") == {"a/b": 1}

    def test_empty_dict(self):
        assert flatten_dict({}) == {}

    def test_mixed_values(self):
        result = flatten_dict({"a": 1, "b": {"c": 2, "d": {"e": 3}}})
        assert result == {"a": 1, "b.c": 2, "b.d.e": 3}


# ── chunk_list ───────────────────────────────────────────────────────

class TestChunkList:
    def test_even_split(self):
        assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_split(self):
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_size_larger_than_list(self):
        assert chunk_list([1, 2], 10) == [[1, 2]]

    def test_chunk_size_one(self):
        assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]

    def test_empty_list(self):
        assert chunk_list([], 3) == []

    def test_invalid_chunk_size_raises(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2], 0)


# ── remove_duplicates ───────────────────────────────────────────────

class TestRemoveDuplicates:
    def test_no_duplicates(self):
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_with_duplicates(self):
        assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]

    def test_all_same(self):
        assert remove_duplicates([5, 5, 5]) == [5]

    def test_empty_list(self):
        assert remove_duplicates([]) == []

    def test_strings(self):
        assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]

    def test_preserves_order(self):
        assert remove_duplicates([3, 1, 2, 1, 3]) == [3, 1, 2]


# ── Convention compliance checks ────────────────────────────────────

class TestConventions:
    """Verify that implemented functions follow the project coding conventions."""

    FUNCTIONS = [flatten_dict, chunk_list, remove_duplicates]

    def test_all_functions_have_type_hints(self):
        for func in self.FUNCTIONS:
            hints = typing.get_type_hints(func)
            sig = inspect.signature(func)
            for param_name in sig.parameters:
                assert param_name in hints, (
                    f"{func.__name__}: parameter '{param_name}' is missing a type hint"
                )
            assert "return" in hints, (
                f"{func.__name__}: missing return type hint"
            )

    def test_all_functions_have_google_docstrings(self):
        for func in self.FUNCTIONS:
            doc = func.__doc__
            assert doc is not None, f"{func.__name__}: missing docstring"
            assert "Args:" in doc, (
                f"{func.__name__}: docstring missing 'Args:' section"
            )
            assert "Returns:" in doc, (
                f"{func.__name__}: docstring missing 'Returns:' section"
            )

    def test_no_type_ignore_comments(self):
        source_file = inspect.getfile(flatten_dict)
        with open(source_file) as f:
            source = f.read()
        assert "# type: ignore" not in source, (
            "data_processor.py contains '# type: ignore' comments"
        )
