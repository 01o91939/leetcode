"""Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

from typing import List
import unittest


def plusOne(digits: List[int]) -> List[int]:
    converted_digits = [str(x) for x in digits]
    temp = 1 + int("".join(converted_digits))
    result = [int(x) for x in str(temp)]
    return result

# N - number of elements in array 'nums'
# Time Complexity: O(N)
# Space Complexity: O(1)

class TestProblems(unittest.TestCase):
    def test_plus_one(self):
        actual = plusOne([1,2,3])
        expected = [1, 2, 4]
        self.assertCountEqual(actual, expected)

        actual_1 = plusOne([1,3,2,1])
        expected_1 = [1,3,2,2]
        self.assertCountEqual(actual_1, expected_1)

        actual_1 = plusOne([9])
        expected_1 = [1,0]
        self.assertCountEqual(actual_1, expected_1)

if __name__ == '__main__':
    unittest.main()