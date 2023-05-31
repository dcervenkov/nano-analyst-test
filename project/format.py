#!/usr/bin/env python3

import os
import subprocess

cfg_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "../pyproject.toml"))

print(">>> isort")
subprocess.call(["isort", ".", "--settings-file", cfg_file])

print(">>> black")
subprocess.call(["black", ".", "--config", cfg_file])
