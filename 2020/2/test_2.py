import pytest
from solution_2 import valid_password_count, new_valid_password_count
import os
from pathlib import Path
import pandas as pd


def test_valid_password():
    input_path = Path(__file__).parent / "input.txt"
    df = pd.read_csv(
        input_path,
        delim_whitespace=True,
        header=None,
        names=["instances", "letter", "password"],
    )
    result = valid_password_count(df)
    assert result == 467


def test_new_valid_password():
    input_path = Path(__file__).parent / "input.txt"
    df = pd.read_csv(
        input_path,
        delim_whitespace=True,
        header=None,
        names=["instances", "letter", "password"],
    )
    result = new_valid_password_count(df)
    assert result == 441
