"""String utility functions — implement the TODOs using Devin."""


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Rules:
        - Lowercase all characters.
        - Replace spaces with hyphens.
        - Remove any character that is not alphanumeric or a hyphen.
        - Collapse consecutive hyphens into a single hyphen.
        - Strip leading and trailing hyphens.

    Args:
        text: The input string.

    Returns:
        A URL-friendly slug string.
    """
    # TODO: Implement this function
    raise NotImplementedError


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to a maximum length, appending a suffix if truncated.

    Rules:
        - If text length <= max_length, return it unchanged.
        - Otherwise, trim to (max_length - len(suffix)) characters and append the suffix.
        - max_length must be >= len(suffix); raise ValueError if not.

    Args:
        text: The input string.
        max_length: Maximum allowed length of the result (including suffix).
        suffix: String to append when truncating.

    Returns:
        The original or truncated string.

    Raises:
        ValueError: If max_length is less than the length of the suffix.
    """
    # TODO: Implement this function
    raise NotImplementedError


def count_words(text: str) -> int:
    """Count the number of words in text.

    A 'word' is any contiguous sequence of non-whitespace characters.
    Leading/trailing whitespace and multiple spaces between words are handled.

    Args:
        text: The input string.

    Returns:
        The number of words.
    """
    # TODO: Implement this function
    raise NotImplementedError
