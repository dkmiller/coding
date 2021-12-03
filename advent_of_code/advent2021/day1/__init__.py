from typing import List


def number_of_increases(depths: List[int], window: int = 1) -> int:
    """
    Calculate the number of times the sum of values in a sliding window of
    size `window` increases.

    https://adventofcode.com/2021/day/1
    """
    assert len(depths) > window

    # https://stackoverflow.com/a/26121781
    # Window sum starts from 0 ... window.
    window_sum = sum(depths[:window])
    window_first = depths[0]
    rv = 0

    for index, depth in enumerate(depths[window:]):
        new_sum = window_sum - window_first + depth
        if new_sum > window_sum:
            rv += 1
        window_sum = new_sum
        window_first = depths[index + 1]

    return rv
