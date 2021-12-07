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
    Lines must be horizontal, vertical, or diagonal.
    """

    source: Point
    target: Point

    # https://stackoverflow.com/a/51248309
    def __post_init__(self):
        assert (
            self.source.x == self.target.x
            or self.source.y == self.target.y
            or abs(self.target.x - self.source.x) == abs(self.target.y - self.source.y)
        )

    @staticmethod
    def _range(start: int, finish: int) -> Iterable[int]:
        """
        Inclusive
        """
        delta = abs(finish - start)
        sign = 1 if finish >= start else -1
        for abs_delta in range(delta + 1):
            yield start + sign * abs_delta

    def coverage(self) -> Iterable[Point]:
        """
        Whether or not `point` is covered by the line represented by `self`.
        """
        xs = Line._range(self.source.x, self.target.x)
        ys = Line._range(self.source.y, self.target.y)
        if self.source.y == self.target.y:
            for x in xs:
                yield Point(x, self.source.y)
        elif self.source.x == self.target.x:
            for y in ys:
                yield Point(self.source.x, y)
        else:
            for x, y in zip(xs, ys):
                yield Point(x, y)

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
