# Stubs for rlpyt.models.dqn.atari_dqn_model (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch
from typing import Any, Optional

class AtariDqnModel(torch.nn.Module):
    dueling: Any = ...
    conv: Any = ...
    head: Any = ...
    def __init__(self, image_shape: Any, output_size: Any, fc_sizes: int = ..., dueling: bool = ..., use_maxpool: bool = ..., channels: Optional[Any] = ..., kernel_sizes: Optional[Any] = ..., strides: Optional[Any] = ..., paddings: Optional[Any] = ...) -> None: ...
    def forward(self, observation: Any, prev_action: Any, prev_reward: Any): ...
