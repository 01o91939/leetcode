"""
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

Example 1:

Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

Example 2:

Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
"""

from math import floor
import unittest


def percentageLetter(s:str, letter:str) -> int:
    percentage = (s.count(letter)/len(s)) * 100
    return floor(percentage)

class TestProblems(unittest.TestCase):
    def test_percentage_letter(self):
        actual = percentageLetter("foobar", "o")
        expected = 33
        self.assertEqual(actual, expected)

        actual_1 = percentageLetter("jjjj", "k")
        expected_1 = 0
        self.assertEqual(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()
    