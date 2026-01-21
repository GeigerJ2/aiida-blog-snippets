# AiiDA monitor example

This project mirrors the example from the AiiDA blog post about monitors. It provides:

- A toy thermometer script at `code/measure-temperature.py`.
- A monitor entry point in `src/aiida_monitor_example/__init__.py`.
- A submission helper in `submit.py`.

## Quick start

```bash
cd /home/geiger_j/aiida_projects/aiida-website/git-repos/aiida-blog-snippets/monitors
pip install -e .
verdi run submit.py
```

You can inspect the remote folder while the job runs:

```bash
verdi process list
verdi calcjob gotocomputer <PK>
```
