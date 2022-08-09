"""Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

import heapq
from typing import List
import unittest


def kthLargest(nums: List[int], k: int) -> int:
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])
    
        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)

    return heapq.heappop(heap)


class TestProblems(unittest.TestCase):
    def test_top_k_elements(self):
        actual = kthLargest([3,2,1,5,6,4], 2)
        expected = 5
        self.assertTrue(actual, expected)

        actual_1 = kthLargest([3,2,3,1,2,4,5,5,6], 4)
        expected_1 = 4
        self.assertTrue(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()