from rlpyt.agents.pg.categorical import AlternatingRecurrentCategoricalPgAgent as AlternatingRecurrentCategoricalPgAgent, CategoricalPgAgent as CategoricalPgAgent, RecurrentCategoricalPgAgent as RecurrentCategoricalPgAgent
from rlpyt.models.pg.atari_ff_model import AtariFfModel as AtariFfModel
from rlpyt.models.pg.atari_lstm_model import AtariLstmModel as AtariLstmModel
from typing import Any

class AtariMixin:
    def make_env_to_model_kwargs(self, env_spaces: Any): ...

class AtariFfAgent(AtariMixin, CategoricalPgAgent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...

class AtariLstmAgent(AtariMixin, RecurrentCategoricalPgAgent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...

class AlternatingAtariLstmAgent(AtariMixin, AlternatingRecurrentCategoricalPgAgent):
    def __init__(self, ModelCls: Any = ..., **kwargs: Any) -> None: ...
