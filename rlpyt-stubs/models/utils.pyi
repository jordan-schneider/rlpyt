import torch
from typing import Any

def conv2d_output_shape(h: Any, w: Any, kernel_size: int = ..., stride: int = ..., padding: int = ..., dilation: int = ...): ...

class ScaleGrad(torch.autograd.Function):
    @staticmethod
    def forward(ctx: Any, tensor: Any, scale: Any): ...
    @staticmethod
    def backward(ctx: Any, grad_output: Any): ...

scale_grad: Any

def update_state_dict(model: Any, state_dict: Any, tau: int = ..., strip_ddp: bool = ...) -> None: ...
def strip_ddp_state_dict(state_dict: Any): ...
