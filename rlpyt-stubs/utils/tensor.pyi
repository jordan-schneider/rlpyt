from typing import Any, Optional

def select_at_indexes(indexes: Any, tensor: Any): ...
def to_onehot(indexes: Any, num: Any, dtype: Optional[Any] = ...): ...
def from_onehot(onehot: Any, dim: int = ..., dtype: Optional[Any] = ...): ...
def valid_mean(tensor: Any, valid: Optional[Any] = ..., dim: Optional[Any] = ...): ...
def infer_leading_dims(tensor: Any, dim: Any): ...
def restore_leading_dims(tensors: Any, lead_dim: Any, T: int = ..., B: int = ...): ...
