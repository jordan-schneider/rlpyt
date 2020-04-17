# Stubs for rlpyt.utils.launching.exp_launcher (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def log_exps_tree(exp_dir: Any, log_dirs: Any, runs_per_setting: Any) -> None: ...
def log_num_launched(exp_dir: Any, n: Any, total: Any) -> None: ...
def launch_experiment(script: Any, run_slot: Any, affinity_code: Any, log_dir: Any, variant: Any, run_ID: Any, args: Any, python_executable: Optional[Any] = ...): ...
def run_experiments(script: Any, affinity_code: Any, experiment_title: Any, runs_per_setting: Any, variants: Any, log_dirs: Any, common_args: Optional[Any] = ..., runs_args: Optional[Any] = ...) -> None: ...
