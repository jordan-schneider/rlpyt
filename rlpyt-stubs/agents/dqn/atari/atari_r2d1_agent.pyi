from rlpyt.agents.dqn.atari.mixin import AtariMixin as AtariMixin
from rlpyt.agents.dqn.r2d1_agent import R2d1Agent as R2d1Agent, R2d1AlternatingAgent as R2d1AlternatingAgent
from rlpyt.models.dqn.atari_r2d1_model import AtariR2d1Model as AtariR2d1Model
from typing import Any

class AtariR2d1Agent(AtariMixin, R2d1Agent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...

class AtariR2d1AlternatingAgent(AtariMixin, R2d1AlternatingAgent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...
