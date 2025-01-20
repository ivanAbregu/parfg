import pytest
from main import (
    linear_search,
    binary_search,
)


@pytest.fixture
def unsorted_list():
    return [4, 2, 7, 1, 9, 3]


@pytest.fixture
def sorted_list():
    return [1, 2, 3, 4, 7, 9]


def test_linear_search(unsorted_list):
    # Test element present
    assert linear_search(unsorted_list, 7) == 2
    assert linear_search(unsorted_list, 1) == 3
    # Test element absent
    assert linear_search(unsorted_list, 10) == -1


def test_binary_search(sorted_list):
    # Test element present
    assert binary_search(sorted_list, 7) == 4
    assert binary_search(sorted_list, 1) == 0
    # Test element absent
    assert binary_search(sorted_list, 10) == -1
