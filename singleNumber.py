"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

"""
from typing import List
import unittest


def singleNumber(nums: List[int]) -> int:
    """use XOR operation, representing numbers in binary form. 
    XOR: if number of true inputs is ODD, then the result is TRUE, otherwise it’s false
    """
    result = 0 # n ^ 0 = 0
    for n in nums:
        result = n ^ result
    return result

class TestProblems(unittest.TestCase):
    def test_single_number(self):
        actual = singleNumber([2,2,1])
        expected = 1
        self.assertEqual(actual, expected)

        actual_1 = singleNumber([4,1,2,1,2])
        expected_1 = 4
        self.assertEqual(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()
    