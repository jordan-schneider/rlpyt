from rlpyt.spaces.base import Space as Space
from typing import Any, Optional

class IntBox(Space):
    low: Any = ...
    high: Any = ...
    shape: Any = ...
    dtype: Any = ...
    def __init__(self, low: Any, high: Any, shape: Optional[Any] = ..., dtype: str = ..., null_value: Optional[Any] = ...) -> None: ...
    def sample(self): ...
    def null_value(self): ...
    @property
    def bounds(self): ...
    @property
    def n(self): ...
