"""
https://github.com/dkmiller/tidbits/blob/master/2020/2020-05-28_python-namespaces/evil.py


from inspect import signature

def f(x: int) -> str:
  pass

# https://stackoverflow.com/a/32844779
get_type_hints(f)

# https://stackoverflow.com/a/218709/2543689
signature(f)

list(signature(f).parameters.keys())
"""


import importlib
import inspect
import pytest
from typing import List, Optional, get_type_hints
from types import FunctionType, ModuleType


import advent2020


class TypeHintError(Exception):
    pass


def get_all_functions(module: ModuleType, exclude: str) -> List[FunctionType]:
    """
    Return the list of all functions defined in the provided module, whose names
    do not contain `exclude`.
    """
    # https://stackoverflow.com/a/991158
    rv = []

    for name in dir(module):
        full_name = f"{module.__name__}.{name}"
        try:
            submodule = importlib.import_module(full_name)

            # https://stackoverflow.com/a/46105518
            functions = inspect.getmembers(submodule, inspect.isfunction)
            functions = [f[1] for f in functions if exclude not in f[0]]

            rv.extend(functions)
            rv.extend(get_all_functions(submodule, exclude))
        except ModuleNotFoundError:
            pass

    return rv


def verify_function_has_type_hints(function: FunctionType) -> Optional[str]:
    """
    Verify that all parameters, including the return value, of the provided
    function have type hints. Return a string containing a warning message if
    at least one parameter does not have a type hint.
    """
    # https://stackoverflow.com/a/32844779
    type_hints = get_type_hints(function)
    parameters = list(inspect.signature(function).parameters.keys())
    parameters.append("return")

    bad_parameters = []

    for parameter in parameters:
        if parameter not in type_hints:
            bad_parameters.append(parameter)

    if bad_parameters:
        rv = (
            "Parameter(s) "
            + ", ".join(parameters)
            + f" of {function.__module__}.{function.__name__} do not have type hints"
        )
        return rv
    else:
        return None


@pytest.mark.parametrize("module,exclude", [(advent2020, "test_")])
def test_all_functions_have_type_hints(module, exclude):
    functions = get_all_functions(module, exclude)
    verifications = map(verify_function_has_type_hints, functions)
    warnings = [v for v in verifications if v is not None]

    if warnings:
        raise TypeHintError(warnings)
