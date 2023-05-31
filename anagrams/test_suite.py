from typing import List

import pytest

import anagrams

_EXP1 = [
    ["bat"],
    ["nat", "tan"],
    ["ate", "eat", "tea"],
]

TEST_DATA = [
    # strs (input), expected (output)
    (["eat", "tea", "tan", "ate", "nat", "bat"], _EXP1),
    (["a"], [["a"]]),
    ([""], [[""]]),
]


def is_match(actual: List[List[str]], expected: List[List[str]]) -> bool:

    if len(actual) != len(expected):
        return False

    def sorthash(items: List[str]) -> int:
        h = hash(len(items))
        k = 16777619
        for s in items:
            h = (h * k) ^ hash(s)
        return h

    actual_s = sorted(actual, key=sorthash)
    expected_s = sorted(expected, key=sorthash)
    for i in range(0, len(actual)):
        if len(actual_s[i]) != len(expected_s[i]):
            return False
        alst = sorted(actual_s[i])
        elst = sorted(expected_s[i])
        for j in range(0, len(alst)):
            if alst[j] != elst[j]:
                return False
    return True


@pytest.mark.parametrize(("strs", "expected"), TEST_DATA)
def test_anagrams(strs: List[str], expected: List[List[str]]):
    actual = anagrams.group_anagrams(strs)
    match = is_match(actual, expected)
    assert match
