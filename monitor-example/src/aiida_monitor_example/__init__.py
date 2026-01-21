import json
import tempfile
from pathlib import Path

from aiida.orm import CalcJobNode
from aiida.transports import Transport

__version__ = "0.1.0"


def monitor_temperature(
    node: CalcJobNode,
    transport: Transport,
    target_T: float = 20.0,
    delta_T: float = 1.0,
    log_file: str = "temperature.log",
    out_file: str = "heating-on.json",
) -> str | None:
    folder = node.base.attributes.get("remote_workdir")

    with tempfile.NamedTemporaryFile("r") as tmp_log:
        try:
            transport.getfile(str(Path(folder) / log_file), tmp_log.name)
            lines = tmp_log.readlines()
            last_temp = float(lines[-1].strip())
        except Exception as exc:
            node.logger.warning(f"Error reading {log_file}: {exc}")
            return

    if last_temp > target_T + delta_T:
        content = False
    elif last_temp < target_T - delta_T:
        content = True
    else:
        return

    with tempfile.NamedTemporaryFile("w") as tmp_out:
        json.dump(content, tmp_out)
        tmp_out.flush()
        try:
            transport.putfile(tmp_out.name, str(Path(folder) / out_file))
        except Exception as exc:
            node.logger.error(f"Could not write {out_file}: {exc}")
