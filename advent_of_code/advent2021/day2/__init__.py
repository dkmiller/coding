from dataclasses import dataclass
import operator
from typing import Callable, Iterable, Tuple


def parse(command: str) -> Tuple[int, int]:
    """
    Return the delta to (horizontal position, depth).
    """
    arr = command.split(" ")
    if arr[0] == "forward":
        rv = (int(arr[1]), 0)
    elif arr[0] == "down":
        rv = (0, int(arr[1]))
    elif arr[0] == "up":
        rv = (0, -int(arr[1]))
    else:
        raise ValueError(f"Unexpected command '{command}'")
    return rv


@dataclass
class ParserWithAim:
    aim: int = 0

    def __call__(self, command: str):
        arr = command.split(" ")
        if arr[0] == "forward":
            x = int(arr[1])
            rv = (x, self.aim * x)
        elif arr[0] == "down":
            self.aim += int(arr[1])
            rv = (0, 0)
        elif arr[0] == "up":
            self.aim -= int(arr[1])
            rv = (0, -0)
        else:
            raise ValueError(f"Unexpected command '{command}'")
        return rv


def final_position(course: Iterable[str], parser: Callable) -> Tuple[int, int]:
    rv = (0, 0)

    for command in course:
        # https://stackoverflow.com/a/497894
        delta = parser(command)
        rv = tuple(map(operator.add, rv, delta))

    return rv
