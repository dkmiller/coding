"""
https://adventofcode.com/2020/day/6
"""


from typing import List


def sum_answered_question_count(answers: List[str]) -> int:
    answered_yes = set()
    