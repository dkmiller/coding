from pathlib import Path


def input_path(file: str) -> str:
    """
    Return the path to `input.txt`, relative to the directory containing
    `__file__`.
    """
    return Path(file).parent / "input.txt"
