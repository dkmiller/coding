import pandas as pd


from advent2020.common import input_path
from advent2020.day2.validation import valid_password_count, new_valid_password_count


def test_valid_password():
    df = pd.read_csv(
        input_path(__file__),
        delim_whitespace=True,
        header=None,
        names=["instances", "letter", "password"],
    )
    result = valid_password_count(df)
    assert result == 467


def test_new_valid_password():
    df = pd.read_csv(
        input_path(__file__),
        delim_whitespace=True,
        header=None,
        names=["instances", "letter", "password"],
    )
    result = new_valid_password_count(df)
    assert result == 441
