from pathlib import Path

from aiida import orm, engine
from aiida_shell import ShellJob
from aiida.orm.nodes.data.code import PortableCode
from aiida.common.exceptions import NotExistent

monitors = {
    "temperature_monitor": orm.Dict(
        {
            "entry_point": "monitor_example.monitor_temperature",
            "minimum_poll_interval": 5,
            "kwargs": {"target_T": 20.0, "delta_T": 1.0},
        }
    )
}

metadata = {
    "options": {
        "output_filename": "temperature.log",
        "additional_retrieve": ["temperature.log"],
    },
    "computer": orm.load_computer("localhost"),
}

code_label = "measure-temperature"
try:
    code = orm.load_code(code_label)
    print(f"Using existing code: {code}")
except NotExistent:
    code = PortableCode(
        filepath_executable="./measure-temperature.py",
        filepath_files=str(Path("scripts").resolve()),
    )
    code.label = code_label
    code.store()
    print(f"Created new code: {code}")

inputs = {"code": code, "metadata": metadata, "monitors": monitors}
results, node = engine.run_get_node(ShellJob, **inputs)
print(f"{node=}")
print(f"{results=}")
