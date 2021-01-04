from rlpyt.algos.dqn.dqn import DQN as DQN, SamplesToBuffer as SamplesToBuffer
from typing import Any

class DqnFromUl(DQN):
    store_latent: Any = ...
    use_frame_buffer: bool = ...
    def initialize(self, *args: Any, **kwargs: Any) -> None: ...
    def samples_to_buffer(self, samples: Any): ...
    def examples_to_buffer(self, examples: Any): ...
