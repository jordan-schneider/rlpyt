import torch.distributed
from rlpyt.utils.tensor import infer_leading_dims as infer_leading_dims
from typing import Any

class RunningMeanStdModel(torch.nn.Module):
    shape: Any = ...
    def __init__(self, shape: Any) -> None: ...
    def update(self, x: Any) -> None: ...
