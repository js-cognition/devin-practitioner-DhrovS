"""Data processing utilities — implement the TODOs using Devin with Knowledge notes."""

from typing import Any


def flatten_dict(
    nested: dict[str, Any], separator: str = "."
) -> dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary.

    Nested keys are joined with the separator.

    Example:
        >>> flatten_dict({"a": {"b": 1, "c": {"d": 2}}})
        {"a.b": 1, "a.c.d": 2}

    Args:
        nested: A dictionary that may contain nested dictionaries.
        separator: The string used to join nested keys.

    Returns:
        A flat dictionary with compound keys.
    """
    # TODO: Implement this function
    raise NotImplementedError


def chunk_list(items: list[Any], chunk_size: int) -> list[list[Any]]:
    """Split a list into chunks of a given size.

    The last chunk may be shorter if the list length is not evenly divisible.

    Args:
        items: The list to split.
        chunk_size: Maximum number of elements per chunk. Must be >= 1.

    Returns:
        A list of sub-lists (chunks).

    Raises:
        ValueError: If chunk_size is less than 1.
    """
    # TODO: Implement this function
    raise NotImplementedError


def remove_duplicates(items: list[Any]) -> list[Any]:
    """Remove duplicate elements from a list while preserving order.

    The first occurrence of each element is kept.

    Args:
        items: The list that may contain duplicates.

    Returns:
        A new list with duplicates removed, in original order.
    """
    # TODO: Implement this function
    raise NotImplementedError
