# https://stackoverflow.com/a/33533514
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class Entry:
    number: int
    marked: bool = False


@dataclass
class Board:
    """
    Bingo board consisting of a list of rows, each of which contains a list of
    entry objects.
    """

    rows: List[List[Entry]]

    @property
    def size(self) -> int:
        return len(self.rows)

    def draw(self, number: int):
        for row in self.rows:
            for entry in row:
                if entry.number == number:
                    entry.marked = True

    def is_win(self) -> bool:
        for row in self.rows:
            if all(e.marked for e in row):
                return True
        for column_index in range(self.size):
            if all(self.rows[i][column_index].marked for i in range(self.size)):
                return True
        return False

    def score(self) -> int:
        """
        Naive score, i.e. sum of all unmarked numbers.
        """
        return sum(sum(e.number for e in row if not e.marked) for row in self.rows)

    @staticmethod
    def parse(lines: Iterable[str]) -> Board:
        rows = []
        for line in lines:
            row = [Entry(int(s)) for s in line.split()]
            rows.append(row)
        return Board(rows)


def winning_score(numbers: Iterable[int], boards: List[Board]) -> int:
    for number in numbers:
        for board in boards:
            board.draw(number)
            if board.is_win():
                naive_score = board.score()
                return naive_score * number
    raise ValueError("No board won the game")
