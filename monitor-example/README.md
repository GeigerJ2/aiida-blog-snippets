# AiiDA monitor example

This project mirrors the example from the AiiDA [blog post about monitors](https://aiida.net/news/posts/2026-01-23-monitors.html).
It provides:

- A toy thermometer script at `scripts/measure-temperature.py`.
- A monitor entry point in `src/aiida_monitor_example/__init__.py`.
- A submission helper in `submit.py`.

## Quick start

```bash
git clone git@github.com:GeigerJ2/aiida-blog-snippets.git
cd aiida-blog-snippets/monitor-example
pip install -e .
verdi run submit.py
```

You can inspect the remote folder while the job runs:

```bash
verdi process list
verdi calcjob gotocomputer <PK>
```
