from advent_of_code.advent2021.day3 import *
from common import lines_file_near
from pytest import mark


@mark.parametrize("file,expected", [("example.txt", 198), ("input.txt", 2250414)])
def test_power_consumption(file, expected):
    lines = lines_file_near(power_consumption, file)
    report = [[int(c) for c in l] for l in lines]
    (ε, γ) = power_consumption(report)
    assert expected == ε * γ


@mark.parametrize("file,expected", [("example.txt", 230), ("input.txt", 6085575)])
def test_life_support_rating(file, expected):
    lines = lines_file_near(life_support_rating, file)
    report = [[int(c) for c in l] for l in lines]
    lsr = life_support_rating(report)
    assert expected == lsr
