""" Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 

More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 

It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

from typing import List
import unittest


def removeDuplicates(nums: List[int]) -> int:
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left

# N - number of elements in array 'nums'
# Time Complexity: O(N)
# Space Complexity: O(1)

class TestProblems(unittest.TestCase):
    def test_remove_duplicates(self):
        actual = removeDuplicates([2,2,1])
        expected = 2
        self.assertEqual(actual, expected)

        actual_1 = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        expected_1 = 5
        self.assertEqual(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()
    