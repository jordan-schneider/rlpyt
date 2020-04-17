# Stubs for rlpyt.algos.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class RlAlgorithm:
    opt_info_fields: Any = ...
    bootstrap_value: bool = ...
    update_counter: int = ...
    def initialize(self, agent: Any, n_itr: Any, batch_spec: Any, mid_batch_reset: Any, examples: Any, world_size: int = ..., rank: int = ...) -> None: ...
    def async_initialize(self, agent: Any, sampler_n_itr: Any, batch_spec: Any, mid_batch_reset: Any, examples: Any, world_size: int = ...) -> None: ...
    def optim_initialize(self, rank: int = ...) -> None: ...
    def optimize_agent(self, itr: Any, samples: Optional[Any] = ..., sampler_itr: Optional[Any] = ...) -> None: ...
    def optim_state_dict(self): ...
    def load_optim_state_dict(self, state_dict: Any) -> None: ...
    @property
    def batch_size(self): ...
