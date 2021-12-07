"""
https://adventofcode.com/2021/day/5
"""

from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @staticmethod
    def parse(point: str) -> Point:
        arr = point.strip().split(",")
        return Point(int(arr[0]), int(arr[1]))


@dataclass
class Line:
    """
    Lines must be horizontal or vertical.
    """

    source: Point
    target: Point

    # https://stackoverflow.com/a/51248309
    def __post_init__(self):
        assert self.source.x == self.target.x or self.source.y == self.target.y

    @staticmethod
    def _range(start: int, finish: int) -> Iterable[int]:
        """
        Inclusive
        """
        return range(min(start, finish), max(start, finish) + 1)

    def coverage(self) -> Iterable[Point]:
        """
        Whether or not `point` is covered by the line represented by `self`.
        """
        if self.source.x != self.target.x:
            for x in Line._range(self.source.x, self.target.x):
                yield Point(x, self.source.y)
        else:
            for y in Line._range(self.source.y, self.target.y):
                yield Point(self.source.x, y)

    @staticmethod
    def parse(line: str) -> Line:
        arr = line.strip().split("->")
        source = Point.parse(arr[0])
        target = Point.parse(arr[1])
        return Line(source, target)


def num_points_two_lines_overlap(lines: Iterable[Line]) -> int:
    """
    Assume
    """
    line_counts = defaultdict(int)
    for line in lines:
        for point in line.coverage():
            line_counts[point] += 1
    points = [k for k, v in line_counts.items() if v >= 2]
    return len(points)
