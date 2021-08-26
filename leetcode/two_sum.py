from collections import defaultdict
from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Given an array of integers nums and an integer target, return indices of the
    two numbers such that they add up to target. You may assume that each input
    would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Source: https://leetcode.com/problems/two-sum/
    """
    # https://stackoverflow.com/a/522578
    index_lookup = defaultdict(list)
    for index, num in enumerate(nums):
        index_lookup[num].append(index)

    for index, num in enumerate(nums):
        local_target = target - num
        if other_indices := index_lookup.get(local_target):
            for other_index in other_indices:
                if index != other_index:
                    return (other_index, index)

    raise Exception("No correct indices exist")
