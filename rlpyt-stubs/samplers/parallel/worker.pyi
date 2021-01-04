from rlpyt.utils.collections import AttrDict as AttrDict
from rlpyt.utils.logging import logger as logger
from rlpyt.utils.seed import set_envs_seeds as set_envs_seeds, set_seed as set_seed
from typing import Any, Optional

def initialize_worker(rank: Any, seed: Optional[Any] = ..., cpu: Optional[Any] = ..., torch_threads: Optional[Any] = ...) -> None: ...
def sampling_process(common_kwargs: Any, worker_kwargs: Any) -> None: ...
