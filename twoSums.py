"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

import unittest
from typing import List

def twoSums(nums: List[int], target: int) -> List[int]:
    hashmap = {} # value:index [2,7,11,15] -> [(2, 0), (7, 1), (11, 2), (15, 3)]
    for index, number in enumerate(nums):
        diff = target - number
        if diff in hashmap:
            return [index, hashmap[diff]]
        hashmap[number] = index

class TestProblems(unittest.TestCase):
    def test_two_sums(self):
        actual = twoSums([2,7,11,15], 9)
        expected = [0, 1]
        self.assertCountEqual(actual, expected)

        actual_1 = twoSums([3,2,4], 6)
        expected_1 = [1, 2]
        self.assertCountEqual(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()