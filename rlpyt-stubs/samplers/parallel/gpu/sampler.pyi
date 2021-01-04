from rlpyt.agents.base import AgentInputs as AgentInputs
from rlpyt.samplers.parallel.base import ParallelSamplerBase as ParallelSamplerBase
from rlpyt.samplers.parallel.gpu.action_server import ActionServer as ActionServer
from rlpyt.samplers.parallel.gpu.collectors import GpuEvalCollector as GpuEvalCollector, GpuResetCollector as GpuResetCollector
from rlpyt.utils.buffer import buffer_from_example as buffer_from_example, torchify_buffer as torchify_buffer
from rlpyt.utils.collections import AttrDict as AttrDict, namedarraytuple as namedarraytuple
from rlpyt.utils.synchronize import drain_queue as drain_queue
from typing import Any

StepBuffer: Any

class GpuSamplerBase(ParallelSamplerBase):
    gpu: bool = ...
    def __init__(self, *args: Any, CollectorCls: Any = ..., eval_CollectorCls: Any = ..., **kwargs: Any) -> None: ...
    def obtain_samples(self, itr: Any): ...
    def evaluate_agent(self, itr: Any): ...

class GpuSampler(ActionServer, GpuSamplerBase): ...

def build_step_buffer(examples: Any, B: Any): ...
