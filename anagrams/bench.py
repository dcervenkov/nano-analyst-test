import os
import sys

src_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"))
if src_dir not in sys.path:
    sys.path.append(src_dir)

import anagrams
from bench_utils import benchmark, get_host_info

_DATA = ["eat", "tea", "tan", "ate", "nat", "bat"]


@benchmark(n=10000, label="group_anagrams")
def main() -> None:
    _ = anagrams.group_anagrams(_DATA)


if __name__ == "__main__":
    main()
    print(get_host_info())
