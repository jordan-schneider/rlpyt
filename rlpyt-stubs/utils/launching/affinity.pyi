# Stubs for rlpyt.utils.launching.affinity (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

N_GPU: str
CONTEXTS_PER_GPU: str
GPU_PER_RUN: str
N_CPU_CORE: str
HYPERTHREAD_OFFSET: str
N_SOCKET: str
RUN_SLOT: str
CPU_PER_WORKER: str
CPU_PER_RUN: str
CPU_RESERVED: str
ASYNC_SAMPLE: str
SAMPLE_GPU_PER_RUN: str
OPTIM_SAMPLE_SHARE_GPU: str
ALTERNATING: str
SET_AFFINITY: str
ABBREVS: Any

def quick_affinity_code(n_parallel: Optional[Any] = ..., use_gpu: bool = ...): ...
def encode_affinity(n_cpu_core: int = ..., n_gpu: int = ..., contexts_per_gpu: int = ..., gpu_per_run: int = ..., cpu_per_run: int = ..., cpu_per_worker: int = ..., cpu_reserved: int = ..., hyperthread_offset: Optional[Any] = ..., n_socket: Optional[Any] = ..., run_slot: Optional[Any] = ..., async_sample: bool = ..., sample_gpu_per_run: int = ..., optim_sample_share_gpu: bool = ..., alternating: bool = ..., set_affinity: bool = ...): ...
def prepend_run_slot(run_slot: Any, affinity_code: Any): ...
def affinity_from_code(run_slot_affinity_code: Any): ...
def make_affinity(run_slot: int = ..., **kwargs: Any): ...
def get_n_socket(): ...
def get_hyperthread_offset(): ...
def get_n_run_slots(affinity_code: Any): ...
def remove_run_slot(run_slot_affinity_code: Any): ...
def decode_affinity(affinity_code: Any): ...
def build_cpu_affinity(slt: Any, cpu: Any, cpr: Any, cpw: int = ..., hto: Optional[Any] = ..., res: int = ..., skt: int = ..., gpu: int = ..., alt: int = ..., saf: int = ...): ...
def build_gpu_affinity(slt: Any, gpu: Any, cpu: Any, cxg: int = ..., cpw: int = ..., hto: Optional[Any] = ..., res: int = ..., skt: int = ..., alt: int = ..., saf: int = ...): ...
def build_multigpu_affinity(run_slot: Any, gpu: Any, cpu: Any, gpr: int = ..., cpw: int = ..., hto: Optional[Any] = ..., res: int = ..., skt: int = ..., alt: int = ..., saf: int = ...): ...
def build_async_affinity(run_slot: Any, gpu: Any, cpu: Any, gpr: int = ..., sgr: int = ..., oss: int = ..., cpw: int = ..., hto: Optional[Any] = ..., res: int = ..., skt: int = ..., alt: int = ..., saf: int = ...): ...
def get_master_cpus(cores: Any, hto: Any): ...
def get_workers_cpus(cores: Any, cpw: Any, hto: Any, alt: Any): ...
def build_affinities_gpu_1cpu_drive(slt: Any, gpu: Any, cpu: Any, cxg: int = ..., gpr: int = ..., cpw: int = ..., hto: Optional[Any] = ..., skt: int = ...): ...
