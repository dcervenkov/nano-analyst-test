## Exercise 1 - Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in *any order*.<br/>
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,<br/>
using all the original letters exactly once.

Implement the function within `anagrams.group_anagrams`.<br/>
You can test the validity of the algorithm by running test suite (`pipenv run tests -s anagrams`)
and performance by running anagrams/bench.py (`pipenv run anagarms`).

### Example 1:
````
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [
    ["bat"],
    ["nat", "tan"],
    ["ate", "eat", "tea"]
]
````

### Example 2:
```
Input: strs = [""]
Output: [[""]]
```

### Example 3:
```
Input: strs = ["a"]
Output: [["a"]]
```

### Constraints:
* 1 <= `strs.length` <= 100
* 0 <= `strs[i].length` <= 100
* `strs[i]` consists only of lowercase English alphabet a-z
