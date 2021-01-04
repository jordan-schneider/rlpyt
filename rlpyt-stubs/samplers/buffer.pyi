from rlpyt.agents.base import AgentInputs as AgentInputs
from rlpyt.samplers.collections import AgentSamples as AgentSamples, AgentSamplesBsv as AgentSamplesBsv, EnvSamples as EnvSamples, Samples as Samples
from rlpyt.utils.buffer import buffer_from_example as buffer_from_example, torchify_buffer as torchify_buffer
from typing import Any, Optional

def build_samples_buffer(agent: Any, env: Any, batch_spec: Any, bootstrap_value: bool = ..., agent_shared: bool = ..., env_shared: bool = ..., subprocess: bool = ..., examples: Optional[Any] = ...): ...
def get_example_outputs(agent: Any, env: Any, examples: Any, subprocess: bool = ...) -> None: ...
