from rlpyt.agents.base import AgentInputs as AgentInputs
from rlpyt.samplers.collectors import BaseEvalCollector as BaseEvalCollector
from rlpyt.utils.buffer import buffer_from_example as buffer_from_example, numpify_buffer as numpify_buffer, torchify_buffer as torchify_buffer
from rlpyt.utils.logging import logger as logger
from rlpyt.utils.quick_args import save__init__args as save__init__args
from typing import Any, Optional

class SerialEvalCollector(BaseEvalCollector):
    def __init__(self, envs: Any, agent: Any, TrajInfoCls: Any, max_T: Any, max_trajectories: Optional[Any] = ...) -> None: ...
    def collect_evaluation(self, itr: Any): ...
