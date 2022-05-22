from advent_of_code.advent2021.day6 import *
from common import read_file_near
from pytest import mark


@mark.parametrize("file,expected", [("example.txt", 5934), ("input.txt", 385391)])
def test_num_lanternfish_after(file, expected):
    content = read_file_near(num_lanternfish_after, file)
    lanternfish = [Lanternfish(int(t)) for t in content.split(",")]
    rv = num_lanternfish_after(lanternfish, 80)
    assert rv == expected


@mark.skip
@mark.parametrize("file,expected", [("example.txt", 26984457539), ("input.txt", None)])
def test_num_lanternfish_after_scalable(file, expected):
    content = read_file_near(num_lanternfish_after_via_formula, file)
    lanternfish = [Lanternfish(int(t)) for t in content.split(",")]
    rv = num_lanternfish_after_via_formula(lanternfish, 256)
    assert rv == expected
