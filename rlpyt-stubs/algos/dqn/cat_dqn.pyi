from rlpyt.algos.dqn.dqn import DQN as DQN
from rlpyt.algos.utils import valid_from_done as valid_from_done
from rlpyt.utils.tensor import select_at_indexes as select_at_indexes, valid_mean as valid_mean
from typing import Any

EPS: float

class CategoricalDQN(DQN):
    V_min: Any = ...
    V_max: Any = ...
    def __init__(self, V_min: int = ..., V_max: int = ..., **kwargs: Any) -> None: ...
    def initialize(self, *args: Any, **kwargs: Any) -> None: ...
    def async_initialize(self, *args: Any, **kwargs: Any): ...
    def loss(self, samples: Any): ...
