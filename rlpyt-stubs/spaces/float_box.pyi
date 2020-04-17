# Stubs for rlpyt.spaces.float_box (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from rlpyt.spaces.base import Space
from typing import Any, Optional

class FloatBox(Space):
    dtype: Any = ...
    low: Any = ...
    high: Any = ...
    def __init__(self, low: Any, high: Any, shape: Optional[Any] = ..., null_value: float = ..., dtype: str = ...) -> None: ...
    def sample(self): ...
    def null_value(self): ...
    @property
    def shape(self): ...
    @property
    def bounds(self): ...
