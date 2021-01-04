from rlpyt.agents.base import AgentInputs as AgentInputs
from rlpyt.samplers.parallel.gpu.action_server import ActionServer as ActionServer, AlternatingActionServer as AlternatingActionServer, NoOverlapAlternatingActionServer as NoOverlapAlternatingActionServer
from typing import Any

class AsyncActionServer(ActionServer):
    def serve_actions_evaluation(self, itr: Any) -> None: ...

class AsyncAlternatingActionServer(AlternatingActionServer):
    def serve_actions_evaluation(self, itr: Any) -> None: ...

class AsyncNoOverlapAlternatingActionServer(NoOverlapAlternatingActionServer):
    def serve_actions_evaluation(self, itr: Any) -> None: ...
