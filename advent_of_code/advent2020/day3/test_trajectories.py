import pytest
from typing import List


from advent2020.common import input_path
from advent2020.day3.trajectories import num_trees_hit, prod_num_trees_hit


def small_forest() -> str:
    return """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


def large_forest() -> str:
    with open(input_path(__file__), "r") as file:
        return file.read()


def deltas() -> List[int]:
    return [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


@pytest.mark.parametrize(
    "forest,origin,delta,expected",
    [(small_forest(), (0, 0), (3, 1), 7), (large_forest(), (0, 0), (3, 1), 167)],
)
def test_num_trees_hit(forest, origin, delta, expected):
    result = num_trees_hit(forest, origin, delta)
    assert expected == result


@pytest.mark.parametrize(
    "forest,origin,deltas,expected",
    [
        (small_forest(), (0, 0), deltas(), 336),
        (large_forest(), (0, 0), deltas(), 736527114),
    ],
)
def test_prod_num_trees_hit(forest, origin, deltas, expected):
    result = prod_num_trees_hit(forest, origin, deltas)
    assert expected == result
