from rlpyt.agents.base import AgentInputs as AgentInputs
from rlpyt.utils.logging import logger as logger
from rlpyt.utils.synchronize import drain_queue as drain_queue
from typing import Any

EVAL_TRAJ_CHECK: int

class ActionServer:
    def serve_actions(self, itr: Any) -> None: ...
    def serve_actions_evaluation(self, itr: Any): ...

class AlternatingActionServer:
    def serve_actions(self, itr: Any) -> None: ...
    def serve_actions_evaluation(self, itr: Any): ...

class NoOverlapAlternatingActionServer:
    def serve_actions(self, itr: Any) -> None: ...
    def serve_actions_evaluation(self, itr: Any): ...
