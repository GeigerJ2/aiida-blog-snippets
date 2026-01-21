import argparse

import matplotlib.pyplot as plt
import numpy as np
from aiida.orm import load_node

parser = argparse.ArgumentParser(description="Plot temperature log from a CalcJob.")
parser.add_argument("pk", type=int, help="PK of the CalcJob node")
args = parser.parse_args()

calculation = load_node(args.pk)
logfile_output_node = calculation.outputs.temperature_log
output_png = "temperature_log.png"

with logfile_output_node.open() as fhandle:
    plt.plot(np.loadtxt(fhandle), "o")

target_T = 20.0
delta_T = 1.0
plt.axhline(target_T, color="blue")
plt.axhline(target_T + delta_T, color="red")
plt.axhline(target_T - delta_T, color="red")
plt.ylabel("Temperature")
plt.savefig(output_png)
print(f"Saved plot to output file: {output_png}.")
