# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_return_value_generators.ipynb.

# %% auto 0
__all__ = ['ReturnValueGenerator']

# %% ../nbs/03_return_value_generators.ipynb 1
from .argument_validators import ArgumentValidator, ArgumentFunctionValidator
from typing import Any, Protocol, runtime_checkable

# %% ../nbs/03_return_value_generators.ipynb 2
from fastcore.test import test_fail

# %% ../nbs/03_return_value_generators.ipynb 5
@runtime_checkable
class ReturnValueGenerator(Protocol):
    "Construct a return value, potentially depended on the exact arguments used to call the function in the first place."
    
    def __call__(self, *args, **kwargs) -> Any:
        """Gets the exact values used in the original function call. Returns a value based on that"""