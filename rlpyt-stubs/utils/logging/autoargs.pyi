# Stubs for rlpyt.utils.logging.autoargs (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def arg(name: Any, type: Optional[Any] = ..., help: Optional[Any] = ..., nargs: Optional[Any] = ..., mapper: Optional[Any] = ..., choices: Optional[Any] = ..., prefix: bool = ...): ...
def prefix(prefix_: Any): ...
def add_args(_: Any): ...
def new_from_args(_: Any): ...
def inherit(base_func: Any): ...
def get_all_parameters(cls, parsed_args: Any): ...
