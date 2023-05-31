#!/usr/bin/env python3

import os
import subprocess
import sys
from typing import Sequence

src_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"))
cfg_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "../pyproject.toml"))


def run(cmd: Sequence[str], label: str, fail_asap: bool) -> int:
    print(f"\n>>> {label}")
    print(" ".join(cmd))
    code = subprocess.call(cmd)
    if code > 0 and fail_asap:
        print(f"[ERROR] {label}: {code}")
        sys.exit(code)
    return code


flake8_code = run(["pflake8", "--statistics"], "flake8", False)

mypy_code = run(
    [
        "mypy",
        "--config-file",
        cfg_file,
        "--no-incremental",
        "--no-error-summary",
        "--pretty",
        src_dir,
    ],
    "mypy",
    False,
)

bandit_code = run(["bandit", "-r", src_dir, "-c", cfg_file, "--quiet"], "bandit", False)

exit_code = max(flake8_code, mypy_code, bandit_code)
if exit_code != 0:
    print(f"\n[ERROR] flake8: {flake8_code}, " + f"mypy: {mypy_code}, bandit: {bandit_code}")
    sys.exit(exit_code)
else:
    print("\n[SUCCESS]")
