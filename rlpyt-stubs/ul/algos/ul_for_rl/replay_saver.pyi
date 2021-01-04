from rlpyt.algos.base import RlAlgorithm as RlAlgorithm
from rlpyt.replays.non_sequence.frame import UniformReplayFrameBuffer as UniformReplayFrameBuffer
from rlpyt.replays.non_sequence.uniform import UniformReplayBuffer as UniformReplayBuffer
from rlpyt.utils.collections import namedarraytuple as namedarraytuple
from typing import Any, Optional

SamplesToBuffer: Any

class ReplaySaverAlgo(RlAlgorithm):
    opt_info_fields: Any = ...
    replay_size: Any = ...
    discount: Any = ...
    n_step_return: Any = ...
    frame_buffer: Any = ...
    optimizer: Any = ...
    def __init__(self, replay_size: Any, discount: float = ..., n_step_return: int = ..., frame_buffer: bool = ...) -> None: ...
    replay_buffer: Any = ...
    def initialize(self, agent: Any, n_itr: Any, batch_spec: Any, mid_batch_reset: bool = ..., examples: Optional[Any] = ..., world_size: int = ..., rank: int = ...) -> None: ...
    def optimize_agent(self, itr: Any, samples: Any) -> None: ...
    def examples_to_buffer(self, examples: Any): ...
    def samples_to_buffer(self, samples: Any): ...

class DummyOptimizer:
    def state_dict(self) -> None: ...
