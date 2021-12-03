from typing import List


def get_seat_id(boarding_pass: str) -> int:
    """
    converts boarding pass to row and column
    and returns seatid=row*8+column
    """
    raw_row = boarding_pass[:7]
    raw_column = boarding_pass[7:]
    parseable_row = raw_row.replace("F", "0").replace("B", "1")
    parseable_column = raw_column.replace("L", "0").replace("R", "1")

    row = int(parseable_row, 2)
    column = int(parseable_column, 2)
    return row * 8 + column


def get_max_seat_id(boarding_passes: List[str]) -> int:
    seat_ids = map(get_seat_id, boarding_passes)
    return max(seat_ids)


def get_missing_seat_id(boarding_passes: List[str]) -> int:
    seat_ids = set(map(get_seat_id, boarding_passes))
    min_seat_id = min(seat_ids)
    max_seat_id = max(seat_ids)

    for id in range(min_seat_id, max_seat_id + 1):
        if id not in seat_ids:
            return id
