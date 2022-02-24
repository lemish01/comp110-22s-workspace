"""Unit tests for the utility list functions in EX05."""

__author__ = "730407722"


from utils import only_evens, sub, concat


def test_only_evens_1() -> None:
    """Testing edge case for function-only_evens."""
    list_a: list[int] = []
    assert only_evens(list_a) == []


def test_only_evens_2() -> None:
    """Testing use case 1 for function-only_evens."""
    list_a: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(list_a) == [2, 4, 6]


def test_only_evens_3() -> None:
    """Testing use case 2 for function-only_evens."""
    list_a: list[int] = [30, 35, 39, 22, 44, 60]
    assert only_evens(list_a) == [30, 22, 44, 60]


def test_sub_1() -> None:
    """Testing edge case for function-sub."""
    list_a: list[int] = []
    assert sub(list_a, 2, 3) == []


def test_sub_2() -> None:
    """Testing use case 1 for function-sub."""
    list_a: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_a, 1, 3) == [2, 3]


def test_sub_3() -> None:
    """Testing use case 2 for function-sub."""
    list_a: list[int] = [6, 7, 8, 9, 10]
    assert sub(list_a, 0, 5) == [6, 7, 8, 9, 10]


def test_concact_1() -> None:
    """Testing edge case for function-concat."""
    list_a: list[int] = []
    list_b: list[int] = []
    assert concat(list_a, list_b) == []


def test_concat_2() -> None:
    """Testing use case 1 for function-concat."""
    list_a: list[int] = [1, 3, 5, 7, 9]
    list_b: list[int] = [2, 4, 6, 8, 10]
    assert concat(list_a, list_b) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


def test_concat_3() -> None:
    """Testing use case 2 for function-concat."""
    list_a: list[int] = [45, 67, 78, 33]
    list_b: list[int] = [22, 51, 83, 99]
    assert concat(list_a, list_b) == [45, 67, 78, 33, 22, 51, 83, 99]