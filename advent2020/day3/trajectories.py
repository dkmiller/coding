import numpy as np
from typing import Iterable, Tuple
from typing import List


def parse_forest(forest: str) -> List[str]:
    result = []
    for line in forest.splitlines():
        if line.strip() == "":
            continue
        result.append(line)
    return result


def num_trees_hit(forest: str, start: Tuple[int, int], delta: Tuple[int, int]) -> int:
    """
    start is a tuple of (x,y)
    delta is a tuple of (x,y)
    return number of time you are in the same location as a tree "#"
    """
    parsed_forest = parse_forest(forest)
    hits = 0
    x = start[0]
    y = start[1]
    while y < len(parsed_forest):
        line = parsed_forest[y]
        current = line[x]
        if current == "#":
            hits += 1
        x = (x + delta[0]) % len(line)
        y += delta[1]
    return hits


def prod_num_trees_hit(
    forest: str, start: Tuple[int, int], deltas: Iterable[Tuple[int, int]]
) -> int:
    """
    Return the product of "number of trees hit" in `forest`, moving in the
    provided directions.
    """
    list_num_trees_hit = map(lambda delta: num_trees_hit(forest, start, delta), deltas)
    list_num_trees_hit = list(list_num_trees_hit)
    prod_num_trees_hit = np.prod(list_num_trees_hit)
    return prod_num_trees_hit
