from rlpyt.replays.async_ import AsyncReplayBufferMixin as AsyncReplayBufferMixin
from rlpyt.replays.non_sequence.n_step import NStepReturnBuffer as NStepReturnBuffer, SamplesFromReplay as SamplesFromReplay
from rlpyt.replays.non_sequence.prioritized import PrioritizedReplay as PrioritizedReplay
from rlpyt.replays.non_sequence.uniform import UniformReplay as UniformReplay
from rlpyt.utils.buffer import buffer_from_example as buffer_from_example, torchify_buffer as torchify_buffer
from rlpyt.utils.collections import namedarraytuple as namedarraytuple
from typing import Any

SamplesFromReplayTL: Any

class NStepTimeLimitBuffer(NStepReturnBuffer):
    samples_timeout_n: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def extract_batch(self, T_idxs: Any, B_idxs: Any): ...
    def compute_returns(self, T: Any) -> None: ...

class TlUniformReplayBuffer(UniformReplay, NStepTimeLimitBuffer): ...
class TlPrioritizedReplayBuffer(PrioritizedReplay, NStepTimeLimitBuffer): ...
class AsyncTlUniformReplayBuffer(AsyncReplayBufferMixin, TlUniformReplayBuffer): ...
class AsyncTlPrioritizedReplayBuffer(AsyncReplayBufferMixin, TlPrioritizedReplayBuffer): ...
