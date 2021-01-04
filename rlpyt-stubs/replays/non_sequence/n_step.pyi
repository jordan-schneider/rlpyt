from rlpyt.agents.base import AgentInputs as AgentInputs
from rlpyt.replays.n_step import BaseNStepReturnBuffer as BaseNStepReturnBuffer
from rlpyt.utils.buffer import torchify_buffer as torchify_buffer
from rlpyt.utils.collections import namedarraytuple as namedarraytuple
from typing import Any

SamplesFromReplay: Any

class NStepReturnBuffer(BaseNStepReturnBuffer):
    def extract_batch(self, T_idxs: Any, B_idxs: Any): ...
    def extract_observation(self, T_idxs: Any, B_idxs: Any): ...
