from collections import defaultdict
import numpy as np
from typing import Callable, List, Tuple


def power_consumption(report: List[List[int]]) -> Tuple[int, int]:
    """
    Return (ε, γ).

    https://adventofcode.com/2021/day/3
    """
    bit_counts = [defaultdict(int) for _ in report[0]]
    for number in report:
        for index, bit in enumerate(number):
            bit_counts[index][bit] += 1

    ε_array = [str(max(dd, key=dd.get)) for dd in bit_counts]
    γ_array = [str(min(dd, key=dd.get)) for dd in bit_counts]

    ε = int("".join(ε_array), 2)
    γ = int("".join(γ_array), 2)

    return (ε, γ)


def _rating(report: List[List[int]], bit_criteria: Callable) -> int:
    """
    The method `bit_criteria` takes a mapping "bit -> count" and chooses a bit.
    """
    # TODO: find a better way of converting the input into a Numpy array.
    arr = np.array([int("".join(map(str, x)), 2) for x in report])

    n_bits = len(report[0])

    for bit_index in reversed(range(n_bits)):
        mask = 2 ** bit_index
        masks = {0: arr & mask == 0, 1: arr & mask != 0}
        mapping = {k: v.sum() for k, v in masks.items()}

        selected_bit = bit_criteria(mapping)
        arr = arr[masks[selected_bit]]

        if len(arr) == 1:
            break

    return arr[0]


def oxygen_generator_criterion(mapping):
    if mapping[0] > mapping[1]:
        return 0
    else:
        return 1


def co2_scrubber_criterion(mapping):
    if mapping[0] > mapping[1]:
        return 1
    else:
        return 0


def life_support_rating(report: List[List[int]]) -> int:
    """
    Return (oxygen generator rating) * (CO2 scrubber rating)
    """

    oxygen_generator_rating = _rating(report, oxygen_generator_criterion)
    co2_scrubber_rating = _rating(report, co2_scrubber_criterion)

    return oxygen_generator_rating * co2_scrubber_rating
