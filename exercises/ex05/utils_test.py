"""Testing utils file."""

__author__ = "730405989"

from exercises.ex05.utils import sub, concat, only_evens


# First two tests making sure begin and end values working correctly

def test_boundcases() -> None:
    """Test to check when start and end are less or greater than begin or start index."""
    assert sub([1, 2, 3], -5, 5) == [1, 2, 3]


# Next test to address empty case
def test_empty() -> None:
    """Test when indices return zero values."""
    assert sub([1, 2, 3], -10, -1) == []


def test_unit_case() -> None:
    """Test for average case with varying numbers."""
    randlist: list = [1, 4, 10, 33, 2]
    assert sub(randlist, 2, 4) == [10, 33]


def test_onlyodds() -> None:
    """Tests that a list with all odds will result in empty set."""
    oddlist: list = [1, 3, 5, 11]
    assert only_evens(oddlist) == []


def test_emptylist() -> None:
    """Tests that an empty list results in empty set at end."""
    emptylist: list = []
    assert only_evens(emptylist) == []


def test_regularex() -> None:
    """Regular example: switching up order, descending ascending."""
    reglist: list = [2, 1, 4, 5, 7, 10, 200, 33]
    assert only_evens(reglist) == [2, 4, 10, 200]


def test_bothempty() -> None:
    """Test when both lists are empty."""
    emptyconcat1: list = []
    emptyconcat2: list = []
    assert concat(emptyconcat1, emptyconcat2) == []


def test_oneempty() -> None:
    """Test when one is empty and the other is not."""
    empty1: list = []
    reg2: list = [1, 2, 5]
    assert concat(empty1, reg2) == [1, 2, 5]


def test_concat() -> None:
    """Test for example 2 lists."""
    a_list: list = [1, 4, -5, 7, 100]
    b_list: list = [3, 6]
    assert concat(a_list, b_list) == [1, 4, -5, 7, 100, 3, 6]
