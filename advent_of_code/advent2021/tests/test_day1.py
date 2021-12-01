from advent_of_code.advent2021.day1 import number_of_increases
from common import file_near
from pytest import mark


@mark.parametrize("file,expected", [("report1.txt", 7), ("input.txt", 1709)])
def test_number_of_increases(file, expected):
    file_text = file_near(number_of_increases, file).read_text()
    depths = [int(l) for l in file_text.splitlines()]
    rv = number_of_increases(depths)
    assert rv == expected
