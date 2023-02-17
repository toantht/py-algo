import random

from src.sorts import (
    bubble_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)


def sample_nums():
    return random.sample(range(1, 100), 10)


def test_bubble_sort():
    nums = sample_nums()
    assert bubble_sort(nums) == sorted(nums)


def test_insertion_sort():
    nums = sample_nums()
    assert insertion_sort(nums) == sorted(nums)


def test_selection_sort():
    nums = sample_nums()
    assert selection_sort(nums) == sorted(nums)


def test_heap_sort():
    nums = sample_nums()
    assert heap_sort(nums) == sorted(nums)


def test_merge_sort():
    nums = sample_nums()
    assert merge_sort(nums) == sorted(nums)


def test_quick_sort():
    nums = sample_nums()
    assert quick_sort(nums) == sorted(nums)
