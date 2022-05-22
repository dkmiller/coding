from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass
class Lanternfish:
    timer: int
    lifecycle: int = 7

    def increment(self) -> Optional[Lanternfish]:
        if not self.timer:
            self.timer = self.lifecycle - 1
            return Lanternfish(self.lifecycle + 1)
        else:
            self.timer -= 1


def num_lanternfish_after(lanternfish: Iterable[Lanternfish], days: int) -> int:
    assert days > 0
    lanternfish = list(lanternfish)
    for _ in range(days):
        for fish in list(lanternfish):
            if (child := fish.increment()) :
                lanternfish.append(child)
    return len(lanternfish)


def num_lanternfish_after_via_formula(lanternfish: Iterable[Lanternfish], days: int) -> int:
    pass
