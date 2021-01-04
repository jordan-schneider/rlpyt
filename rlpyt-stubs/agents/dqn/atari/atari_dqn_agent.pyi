from rlpyt.agents.dqn.atari.mixin import AtariMixin as AtariMixin
from rlpyt.agents.dqn.dqn_agent import DqnAgent as DqnAgent
from rlpyt.models.dqn.atari_dqn_model import AtariDqnModel as AtariDqnModel
from typing import Any

class AtariDqnAgent(AtariMixin, DqnAgent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...
