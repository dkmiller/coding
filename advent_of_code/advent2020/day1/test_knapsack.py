import pandas as pd
import pytest


from advent2020.common import input_path
from advent2020.day1.knapsack import (
    product_of_entries_which_sum_to,
    product_of_three_entries_which_sum_to,
)


def simple_entries() -> list:
    return [1721, 979, 366, 299, 675, 1456]


def complex_entries() -> list:
    return pd.read_csv(input_path(__file__), header=None, names=["a"]).a.tolist()


@pytest.mark.parametrize(
    "entries,target,result",
    [(simple_entries(), 2020, 514579), (complex_entries(), 2020, 972576)],
)
def test_product_of_entries_which_sum_to(entries, target, result):
    rv = product_of_entries_which_sum_to(entries, target)
    assert result == rv


@pytest.mark.parametrize(
    "entries,target,result",
    [(simple_entries(), 2020, 241861950), (complex_entries(), 2020, 199300880)],
)
def test_product_of_three_entries_which_sum_to(entries, target, result):
    rv = product_of_three_entries_which_sum_to(entries, target)
    assert result == rv
