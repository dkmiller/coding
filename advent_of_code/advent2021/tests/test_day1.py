from advent_of_code.advent2021.day1 import number_of_increases
from common import lines_file_near
from pytest import mark


@mark.parametrize("file,expected", [("report1.txt", 7), ("input.txt", 1709)])
def test_number_of_increases(file, expected):
    file_lines = lines_file_near(number_of_increases, file)
    depths = [int(l) for l in file_lines]
    rv = number_of_increases(depths)
    assert rv == expected


@mark.parametrize("file,expected", [("report1.txt", 5), ("input.txt", 1761)])
def test_number_of_increases_window(file, expected):
    file_lines = lines_file_near(number_of_increases, file)
    depths = [int(l) for l in file_lines]
    rv = number_of_increases(depths, 3)
    assert rv == expected
