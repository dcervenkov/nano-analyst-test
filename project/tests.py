#!/usr/bin/env python3

import argparse
import os
import sys

import pytest

parser = argparse.ArgumentParser()
parser.add_argument("--suite", "-s")
args = parser.parse_args()

src_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"))
if src_dir not in sys.path:
    sys.path.append(src_dir)

target = src_dir
if args.suite:
    target = os.path.join(src_dir, args.suite, 'test_suite.py')

cmd_args = [target, "--disable-warnings", "--no-header", "--color=yes"]
result = pytest.main(args=cmd_args)
sys.exit(result)
