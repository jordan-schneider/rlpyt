from rlpyt.agents.dqn.atari.mixin import AtariMixin as AtariMixin
from rlpyt.agents.dqn.catdqn_agent import CatDqnAgent as CatDqnAgent
from rlpyt.models.dqn.atari_catdqn_model import AtariCatDqnModel as AtariCatDqnModel
from typing import Any

class AtariCatDqnAgent(AtariMixin, CatDqnAgent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...
