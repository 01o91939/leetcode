"""Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 
"""

import code
from collections import defaultdict
from typing import Counter, List
import unittest


def groupAnagrams(strings: List[str]) -> List[List[str]]:
    results = defaultdict(list)

    for s in strings:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        results[tuple(count)].append(s)
    return results.values()

# N - number of elements
# M - av. length of string/element
# # Time Complexity: O(N*M)
# Space Complexity: O(N*M)

def groupAnagrams2(strings: List[str]) -> List[List[str]]:
    results = defaultdict(list)

    for s in strings:
        count = defaultdict(lambda: 0)
        for char in s:
            count[char] += 1
        results[frozenset(count.items())].append(s)
    return results.values()

# N - number of elements
# M - av. length of string/element
# Time: O(N*M)
# Space: O(N*M)

def groupAnagrams_sorted(strings: List[str]) -> List[List[str]]:
    results = defaultdict(list)

    for string in strings: #O(n)
        sorted_string = ''.join(sorted(string))
        results[sorted_string].append(string)
    return results.values()

# N - number of elements
# M - av. length of string/element
# Time: O(N*MlogM)
# Space: O(N*M)

def groupAnagrams_Counter(strings: List[str]) -> List[List[str]]:
    results = defaultdict(list)

    for string in strings:
        count = Counter(string)
        results[tuple(sorted(count.items()))].append(string)    
    return results.values()

# N - number of elements
# M - av. length of string/element
# Time: O(N*M)
# Space: O(N*M)


class TestProblems(unittest.TestCase):
    def test_group_anagrams(self):
        actual = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(actual, expected)
        
        actual_2 = groupAnagrams2(["eat","tea","tan","ate","nat","bat"])
        expected_2 =  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(actual_2, expected_2)

        actual_3 = groupAnagrams_sorted(["eat","tea","tan","ate","nat","bat"])
        expected_3 =  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(actual_3, expected_3)

        actual_4 = groupAnagrams_Counter(["eat","tea","tan","ate","nat","bat"])
        expected_4 = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(actual_4, expected_4)


if __name__ == '__main__':
    unittest.main()
