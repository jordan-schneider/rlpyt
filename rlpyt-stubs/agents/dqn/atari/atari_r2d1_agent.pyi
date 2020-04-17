# Stubs for rlpyt.agents.dqn.atari.atari_r2d1_agent (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from rlpyt.agents.dqn.atari.mixin import AtariMixin
from rlpyt.agents.dqn.r2d1_agent import R2d1Agent, R2d1AlternatingAgent
from typing import Any

class AtariR2d1Agent(AtariMixin, R2d1Agent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...

class AtariR2d1AlternatingAgent(AtariMixin, R2d1AlternatingAgent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...
