from rlpyt.agents.base import AgentStep as AgentStep, BaseAgent as BaseAgent
from rlpyt.agents.dqn.epsilon_greedy import EpsilonGreedyAgentMixin as EpsilonGreedyAgentMixin
from rlpyt.distributions.epsilon_greedy import EpsilonGreedy as EpsilonGreedy
from rlpyt.models.utils import update_state_dict as update_state_dict
from rlpyt.utils.buffer import buffer_to as buffer_to
from rlpyt.utils.collections import namedarraytuple as namedarraytuple
from rlpyt.utils.logging import logger as logger
from typing import Any, Optional

AgentInfo: Any

class DqnAgent(EpsilonGreedyAgentMixin, BaseAgent):
    def __call__(self, observation: Any, prev_action: Any, prev_reward: Any): ...
    initial_model_state_dict: Any = ...
    target_model: Any = ...
    distribution: Any = ...
    def initialize(self, env_spaces: Any, share_memory: bool = ..., global_B: int = ..., env_ranks: Optional[Any] = ...) -> None: ...
    def to_device(self, cuda_idx: Optional[Any] = ...) -> None: ...
    def state_dict(self): ...
    def step(self, observation: Any, prev_action: Any, prev_reward: Any): ...
    def target(self, observation: Any, prev_action: Any, prev_reward: Any): ...
    def update_target(self, tau: int = ...) -> None: ...
