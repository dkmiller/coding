import inspect
from pathlib import Path
from typing import Callable, List


def file_near(func: Callable, name: str) -> Path:
    # https://stackoverflow.com/a/64689264
    func_def_file = inspect.getabsfile(func)
    file_path = Path(func_def_file).parent / name
    rv = file_path.absolute()
    return rv


def read_file_near(func: Callable, name: str) -> str:
    rv = file_near(func, name).read_text()
    return rv


def lines_file_near(func: Callable, name: str) -> List[str]:
    """
    List of lines in the file named `name` in the same directory as the file
    defining `func`.
    """
    rv = read_file_near(func, name).splitlines()
    return rv
