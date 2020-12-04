"""
Utilities around "fake" password validation.
"""


import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df[["low", "high"]] = df.apply(
        lambda row: row["instances"].split("-"), axis=1, result_type="expand"
    )
    df["letter"] = df.letter.apply(lambda l: l.strip(":"))
    df[["low", "high"]] = df[["low", "high"]].astype(int)

    return df


def valid_password_count(df: pd.DataFrame) -> int:
    df = clean_data(df)
    df["valid_password"] = df.apply(
        lambda row: int(row["low"])
        <= row["password"].count(row["letter"])
        <= int(row["high"]),
        axis=1,
    )

    return df.valid_password.sum()


def is_valid_password(low: int, high: int, password: str, letter: str) -> bool:
    substring_low = password[low - 1]
    substring_high = password[high - 1]
    return (substring_low == letter) != (substring_high == letter)


def new_valid_password_count(df: pd.DataFrame) -> int:
    df = clean_data(df)
    df["valid_password"] = df.apply(
        lambda row: is_valid_password(
            row["low"], row["high"], row["password"], row["letter"]
        ),
        axis=1,
    )
    print(df)

    return df.valid_password.sum()
