# Stubs for rlpyt.agents.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

AgentInputs: Any
AgentStep: Any

class BaseAgent:
    recurrent: bool = ...
    alternating: bool = ...
    model: Any = ...
    shared_model: Any = ...
    distribution: Any = ...
    device: Any = ...
    model_kwargs: Any = ...
    def __init__(self, ModelCls: Optional[Any] = ..., model_kwargs: Optional[Any] = ..., initial_model_state_dict: Optional[Any] = ...) -> None: ...
    def __call__(self, observation: Any, prev_action: Any, prev_reward: Any) -> None: ...
    env_model_kwargs: Any = ...
    env_spaces: Any = ...
    share_memory: Any = ...
    def initialize(self, env_spaces: Any, share_memory: bool = ..., **kwargs: Any) -> None: ...
    def make_env_to_model_kwargs(self, env_spaces: Any): ...
    def to_device(self, cuda_idx: Optional[Any] = ...) -> None: ...
    def data_parallel(self) -> None: ...
    def async_cpu(self, share_memory: bool = ...) -> None: ...
    def collector_initialize(self, global_B: int = ..., env_ranks: Optional[Any] = ...) -> None: ...
    def step(self, observation: Any, prev_action: Any, prev_reward: Any) -> None: ...
    def reset(self) -> None: ...
    def reset_one(self, idx: Any) -> None: ...
    def parameters(self): ...
    def state_dict(self): ...
    def load_state_dict(self, state_dict: Any) -> None: ...
    def train_mode(self, itr: Any) -> None: ...
    def sample_mode(self, itr: Any) -> None: ...
    def eval_mode(self, itr: Any) -> None: ...
    def sync_shared_memory(self) -> None: ...
    def send_shared_memory(self) -> None: ...
    def recv_shared_memory(self) -> None: ...
    def toggle_alt(self) -> None: ...

AgentInputsRnn: Any

class RecurrentAgentMixin:
    recurrent: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def reset(self) -> None: ...
    def reset_one(self, idx: Any) -> None: ...
    def advance_rnn_state(self, new_rnn_state: Any) -> None: ...
    @property
    def prev_rnn_state(self): ...
    def train_mode(self, itr: Any) -> None: ...
    def sample_mode(self, itr: Any) -> None: ...
    def eval_mode(self, itr: Any) -> None: ...

class AlternatingRecurrentAgentMixin:
    recurrent: bool = ...
    alternating: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def reset(self) -> None: ...
    def advance_rnn_state(self, new_rnn_state: Any) -> None: ...
    @property
    def prev_rnn_state(self): ...
    def train_mode(self, itr: Any) -> None: ...
    def sample_mode(self, itr: Any) -> None: ...
    def eval_mode(self, itr: Any) -> None: ...
    def get_alt(self): ...
    def toggle_alt(self) -> None: ...
