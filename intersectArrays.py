"""Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

import collections
from typing import List
import unittest


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = collections.Counter(nums1)
        results = []
        
        for num in nums2:
            if nums1_counter[num] > 0:
                results.append(num)
                nums1_counter[num] -= 1

        return results
        
# N - number of elements in array 'nums2'
# Time Complexity: O(N)
# Space Complexity: O(N)

class TestProblems(unittest.TestCase):
    def test_intersect(self):
        actual = intersect([1,2,2,1], [2,2])
        expected = [2,2]
        self.assertCountEqual(actual, expected)

        actual_1 = intersect([4,9,5], [9,4,9,8,4])
        expected_1 = [9,4]
        self.assertCountEqual(actual_1, expected_1)

if __name__ == '__main__':
    unittest.main()