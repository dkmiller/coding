import pytest
from typing import List


from advent2020.common import input_path
from advent2020.day5.seating import get_max_seat_id, get_missing_seat_id, get_seat_id


def get_boarding_passes() -> List[str]:
    with open(input_path(__file__), "r") as file:
        return file.readlines()


@pytest.mark.parametrize(
    "boarding_pass,seat_id",
    [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_get_seat_id(boarding_pass, seat_id):
    result = get_seat_id(boarding_pass)
    assert seat_id == result


@pytest.mark.parametrize("boarding_passes,seat_id", [(get_boarding_passes(), 911)])
def test_get_max_seat_id(boarding_passes, seat_id):
    result = get_max_seat_id(boarding_passes)
    assert seat_id == result


@pytest.mark.parametrize("boarding_passes,seat_id", [(get_boarding_passes(), 629)])
def test_get_missing_seat_id(boarding_passes, seat_id):
    result = get_missing_seat_id(boarding_passes)
    assert seat_id == result
