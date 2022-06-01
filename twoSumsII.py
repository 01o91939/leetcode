"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""
from typing import List
import unittest

def twoSum(nums: List[int], target: int) -> List[int]:
    # Use two pointers, one at the start of input array, one at the end
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        # since the array is sorted, we can assume that the first elem is always smaller than the last
        if sum < target:
            left+=1
        elif sum > target:
            right-=1
        else: 
            return [left+1, right+1]

# N - number of elements in array 'nums'
# Time Complexity: O(N)
# Space Complexity: O(1)

class TestProblems(unittest.TestCase):
    def test_two_sum(self):
        actual = twoSum([2,7,11,15], 9)
        expected = [1, 2]
        self.assertCountEqual(actual, expected)

        actual_1 = twoSum([2, 3, 4], 6)
        expected_1 = [1,3]
        self.assertCountEqual(actual_1, expected_1)

        actual_2 = twoSum([-1,0], -1)
        expected_2 = [1, 2]
        self.assertCountEqual(actual_2, expected_2)


if __name__ == '__main__':
    unittest.main()