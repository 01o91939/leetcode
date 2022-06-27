"""Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "2"
Output: ["a","b","c"]

Input: digits = ""
Output: []
"""

from typing import List
import unittest

def letterCombinations(digits: str) -> List[str]:
    digit_to_letters = {
        '2': 'abc', '3':'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
        }
    if len(digits) == 0:
        return []
    results = []
    dfs_helper(digit_to_letters, results, digits, "")
    return results
    
def dfs_helper(digit_to_letters, results, digits, path):
    # base case
    if not digits:
        results.append(path)
        return
    for char in digit_to_letters[digits[0]]:
        dfs_helper(digit_to_letters, results, digits[1:], path+char)

class TestProblems(unittest.TestCase):
    def test_letter_combinations(self):
        actual = letterCombinations("23")
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertCountEqual(actual, expected)

        actual_1 = letterCombinations("2")
        expected_1 = ["a","b","c"]
        self.assertCountEqual(actual_1, expected_1)

if __name__ == '__main__':
    unittest.main()
    