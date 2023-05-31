from typing import List, Tuple


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = []
    sorted_strs = ["".join(sorted(string)) for string in strs.copy()]
    while strs:
        anagrams, non_anagrams, non_anagrams_sorted = extract_anagrams(
            strs.pop(), sorted_strs.pop(), strs, sorted_strs
        )
        groups.append(anagrams)
        strs = non_anagrams
        sorted_strs = non_anagrams_sorted
    return groups


def extract_anagrams(
    string: str, sorted_string: str, strs: List[str], sorted_strs: List[str]
) -> Tuple[List[str], List[str], List[str]]:
    anagrams = [string]
    non_anagrams = []
    non_anagrams_sorted = []
    for el_string, el_sorted_string in zip(strs, sorted_strs):
        if sorted_string == el_sorted_string:
            anagrams.append(el_string)
        else:
            non_anagrams.append(el_string)
            non_anagrams_sorted.append(el_sorted_string)
    return anagrams, non_anagrams, non_anagrams_sorted
