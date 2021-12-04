from advent_of_code.advent2021.day4 import *
from common import lines_file_near
from pytest import mark
from typing import Tuple


def parse(func, file) -> Tuple[List[int], List[Board]]:
    lines = lines_file_near(func, file)
    numbers = [int(s) for s in lines[0].split(",")]
    boards = []
    current_board_lines = []
    for line in lines[2:]:
        if line:
            current_board_lines.append(line)
        else:
            boards.append(Board.parse(current_board_lines))
            current_board_lines.clear()
            continue
    if line:
        # Last line is non-empty.
        boards.append(Board.parse(current_board_lines))
    return numbers, boards


@mark.parametrize("file,expected", [("example.txt", 4512), ("input.txt", 45031)])
def test_winning_score(file, expected):
    numbers, boards = parse(winning_score, file)

    score = winning_score(numbers, boards)
    assert score == expected


@mark.parametrize("file,expected", [("example.txt", 1924), ("input.txt", 2568)])
def test_losing_score(file, expected):
    numbers, boards = parse(winning_score, file)

    score = winning_score(numbers, boards, -1)
    assert score == expected
