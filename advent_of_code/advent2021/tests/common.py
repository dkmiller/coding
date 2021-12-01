import inspect
from pathlib import Path
from typing import Callable


def file_near(func: Callable, name: str) -> Path:
    # https://stackoverflow.com/a/64689264
    func_def_file = inspect.getabsfile(func)
    file_path = Path(func_def_file).parent / name
    rv = file_path.absolute()
    return rv
