from advent_of_code.advent2021.day5 import *
from common import lines_file_near
from pytest import mark


# , ("input.txt", 5698)
@mark.parametrize("file,expected", [("example.txt", 12), ("input.txt", 15463)])
def test_winning_score(file, expected):
    lines = []
    for unparsed_line in lines_file_near(num_points_two_lines_overlap, file):
        try:
            lines.append(Line.parse(unparsed_line))
        except AssertionError:
            pass
    num = num_points_two_lines_overlap(lines)
    assert num == expected
