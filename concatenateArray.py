""" Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""

from typing import List
import unittest


def concatenateArray(nums:List[int]) -> List[int]:
    return 2 * nums

class TestProblems(unittest.TestCase):
    def test_concatenate_array(self):
        actual = concatenateArray([1, 2])
        expected = [1, 2, 1, 2]
        self.assertTrue(actual, expected)

        actual_1 = concatenateArray([1,3,2,1])
        expected_1 = [1,3,2,1,1,3,2,1]
        self.assertTrue(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()