from rlpyt.utils.synchronize import RWLock as RWLock
from typing import Any

class AsyncReplayBufferMixin:
    async_: bool = ...
    async_t: Any = ...
    rw_lock: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def append_samples(self, *args: Any, **kwargs: Any): ...
    def sample_batch(self, *args: Any, **kwargs: Any): ...
    def update_batch_priorities(self, *args: Any, **kwargs: Any): ...
