"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List
import unittest

def containsDuplicate(nums: List[int]) -> bool:
    # create a hashset to keep track of elements already seen
    hashset = set()
    for number in nums:
        if number in hashset:
            return True
        hashset.add(number)
    return False

# N: number of elements in the array
# Time Complexity: O(n)
# Space Complexity: O(n)

class TestProblems(unittest.TestCase):
    def test_contains_duplicate(self):
        actual = containsDuplicate([1,2,3,1])
        self.assertTrue(actual)

        actual_1 = containsDuplicate([1,2,3,4])
        self.assertFalse(actual_1)

        actual_2 = containsDuplicate([1,1,1,3,3,4,3,2,4,2])
        self.assertTrue(actual_2)
        

if __name__ == '__main__':
    unittest.main()