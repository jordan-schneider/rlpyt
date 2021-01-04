from rlpyt.samplers.async_.base import AsyncParallelSamplerMixin as AsyncParallelSamplerMixin
from rlpyt.samplers.async_.collectors import DbCpuResetCollector as DbCpuResetCollector
from rlpyt.samplers.parallel.base import ParallelSamplerBase as ParallelSamplerBase
from rlpyt.samplers.parallel.cpu.collectors import CpuEvalCollector as CpuEvalCollector
from rlpyt.utils.logging import logger as logger
from rlpyt.utils.synchronize import drain_queue as drain_queue
from typing import Any

EVAL_TRAJ_CHECK: float

class AsyncCpuSampler(AsyncParallelSamplerMixin, ParallelSamplerBase):
    def __init__(self, *args: Any, CollectorCls: Any = ..., eval_CollectorCls: Any = ..., **kwargs: Any) -> None: ...
    def initialize(self, affinity: Any) -> None: ...
    def obtain_samples(self, itr: Any, db_idx: Any): ...
    def evaluate_agent(self, itr: Any): ...
