"""Test."""

__author__ = "730407722"


from dictionary import invert, favorite_color, count


def test_invert_edge() -> None:
    """Testing edge case for function-inverse."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_invert_use1() -> None:
    """Testing use case 1 for function-inverse."""
    input: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use2() -> None:
    """Testing use case 2 for function-inverse."""
    input: dict[str, str] = {'apple': 'cat'}
    assert invert(input) == {'cat': 'apple'}


def test_favorite_color_edge() -> None:
    """Testing edge case for function-favorite_color."""
    color: dict[str, str] = {}
    assert favorite_color(color) == ""


def test_favorite_color_use1() -> None:
    """Testing use case 1 for function-favorite_color."""
    color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(color) == "blue"


def test_favorite_color_use2() -> None:
    """Testing use case 2 for function-favorite_color."""
    color: dict[str, str] = {"Meryl": "purple", "Sage": "green", "Megatron": "purple", "Rose": "pink"}
    assert favorite_color(color) == "purple"


def test_count_edge() -> None:
    """Testing edge case for function-count."""
    key: list[str] = []
    assert count(key) == {}


def test_count_use1() -> None:
    """Testing use case 1 for function-count."""
    key: list[str] = ["a", "b", "c", "c", "d"]
    assert count(key) == {"a": 1, "b": 1, "c": 2, "d": 1}


def test_count_use2() -> None:
    """Testing use case 2 for function-count."""
    key: list[str] = ["meryl", "megatron"]
    assert count(key) == {"e": 1, "g": 1, "l": 1, "m": 2, "n": 1, "o": 1, "r": 2, "t": 1, "y": 1}