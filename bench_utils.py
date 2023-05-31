import cProfile
import io
import platform
import pstats
import statistics
import sysconfig
import time
from functools import wraps
from pstats import SortKey
from typing import Optional

import psutil

_SEP = "--------------------------------------------------------------------------------"


def ns2str(ns: float) -> str:
    if ns > 1000000000:
        return f"{(ns / 1000000000):.2f} s"
    if ns > 1000000:
        return f"{(ns / 1000000):.2f} ms"
    if ns > 1000:
        return f"{(ns / 1000):.2f} µs"
    return f"{ns:.2f} ns"


def benchmark(n: int, label: Optional[str] = None):
    """
    Run the decorated function n-times, calculate average elapsed time
    and print cummulative CPU time costs.
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            desc = label if label else fn.__name__
            profiler = cProfile.Profile()
            profiler.enable()
            start = time.perf_counter_ns()
            for i in range(0, n):
                _ = fn(*args, **kwargs)
            ns = time.perf_counter_ns() - start
            profiler.disable()
            stream = io.StringIO()
            ps = pstats.Stats(profiler, stream=stream).sort_stats(SortKey.CUMULATIVE)
            ps.print_stats()
            print(_SEP)
            print(f"{desc} avg: {ns2str(ns / n)}, sum: {ns2str(ns)}, N: {n}")
            print(_SEP)
            print(stream.getvalue())

        return wrapper

    return decorator


def elapsed_time(n: int, label: Optional[str] = None):
    """Run the decorated function n-times and calculate average elapsed time."""

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            desc = label if label else fn.__name__
            times = []
            for i in range(0, n):
                start = time.perf_counter_ns()
                _ = fn(*args, **kwargs)
                times.append(time.perf_counter_ns() - start)
            ns = sum(times)
            avg_ns = ns / n
            stdev_ns = statistics.stdev(times) if len(times) > 1 else 0
            print(f"{desc} avg: {ns2str(avg_ns)}, stdev: {ns2str(stdev_ns)}, sum: {ns2str(ns)}, N: {n}")

        return wrapper

    return decorator


def get_host_info() -> str:
    ghz = psutil.cpu_freq().max / 1000
    ver = platform.python_version()
    impl = platform.python_implementation()
    rev = platform.python_revision()
    return "\n".join(
        [
            f"CPU: {platform.processor()}, {psutil.cpu_count()} cpu, {ghz:.1f} GHz",
            f"OS: {sysconfig.get_platform()}",
            f"Python: {ver}, {impl}, {rev}",
        ]
    )
