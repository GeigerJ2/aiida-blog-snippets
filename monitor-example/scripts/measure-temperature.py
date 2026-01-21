#!/usr/bin/env python3
import time
import json

log_file = "temperature.log"
control_file = "heating-on.json"

temperature = 19.0

with open(log_file, "a") as f:
    f.write(f"{temperature:.2f}\n")
    f.flush()

for _ in range(30):
    try:
        with open(control_file, "r") as cf:
            heating_on = json.load(cf)
    except (FileNotFoundError, ValueError):
        heating_on = False

    if heating_on:
        temperature += 0.25
    else:
        temperature -= 0.15

    with open(log_file, "a") as f:
        f.write(f"{temperature:.2f}\n")
        f.flush()

    time.sleep(5)
