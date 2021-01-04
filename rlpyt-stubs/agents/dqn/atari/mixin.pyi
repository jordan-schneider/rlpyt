from typing import Any

class AtariMixin:
    def make_env_to_model_kwargs(self, env_spaces: Any): ...
