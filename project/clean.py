#!/usr/bin/env python3

import glob
import os
import shutil

root_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(root_dir)

patterns = [
    "**/.eggs",
    "**/.mypy_cache",
    "**/__pycache__",
    "**/.pytest_cache",
    "**/*.egg-info",
]
for pattern in patterns:
    for path in glob.glob(pattern, recursive=True):
        shutil.rmtree(path, ignore_errors=True)
