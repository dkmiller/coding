import sys
from typing import List


def number_of_increases(depths: List[int]) -> int:
    """
    https://adventofcode.com/2021/day/1
    """
    # https://stackoverflow.com/a/26121781
    previous = sys.maxsize
    rv = 0
    for next in depths:
        if next > previous:
            rv += 1
        previous = next
    return rv
