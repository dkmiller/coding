from advent_of_code.advent2021.day4 import *
from common import lines_file_near
from pytest import mark


@mark.parametrize("file,expected", [("example.txt", 4512), ("input.txt", 45031)])
def test_winning_score(file, expected):
    lines = lines_file_near(winning_score, file)
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

    score = winning_score(numbers, boards)
    assert score == expected
