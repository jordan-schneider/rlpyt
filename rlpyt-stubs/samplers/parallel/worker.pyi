# Stubs for rlpyt.samplers.parallel.worker (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def initialize_worker(rank: Any, seed: Optional[Any] = ..., cpu: Optional[Any] = ..., torch_threads: Optional[Any] = ...) -> None: ...
def sampling_process(common_kwargs: Any, worker_kwargs: Any) -> None: ...
