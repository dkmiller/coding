from advent_of_code.advent2021.day2 import *
from common import file_near
from pytest import mark


@mark.parametrize("file,expected", [("test.txt", 150), ("input.txt", 1636725)])
def test_final_position(file, expected):
    file_text = file_near(final_position, file).read_text()
    commands = file_text.splitlines()
    horizontal, depth = final_position(commands, parse)
    assert expected == horizontal * depth


@mark.parametrize("file,expected", [("test.txt", 900), ("input.txt", 1872757425)])
def test_final_position_with_aim(file, expected):
    file_text = file_near(final_position, file).read_text()
    commands = file_text.splitlines()
    horizontal, depth = final_position(commands, ParserWithAim())
    assert expected == horizontal * depth
