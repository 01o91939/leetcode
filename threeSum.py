"""3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

from typing import List
import unittest


def threeSum(nums: List[int]) -> List[List[int]]:
        triplets = set()
        # necessary to run the 2Sum algorithm
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            
            left, right = i+1, len(sorted_nums) -1

            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if total == 0:
                    triplets.add((sorted_nums[i],sorted_nums[left],sorted_nums[right]))
                    left += 1
                if total < 0:
                    left += 1
                else:
                    right -=1
        result = [] 
        for a,b,c in list(triplets):
            result.append([a,b,c])
        return result


class TestProblems(unittest.TestCase):
    def test_three_sum(self):
        actual = threeSum([-1,0,1,2,-1,-4])
        expected = [[-1,-1,2],[-1,0,1]]
        self.assertCountEqual(actual, expected)

        actual_1 = threeSum([0,1,1])
        expected_1 =[]
        self.assertCountEqual(actual_1, expected_1)

        actual_2 = threeSum([0,0,0])
        expected_2 = [[0,0,0]]
        self.assertCountEqual(actual_2, expected_2)

if __name__ == '__main__':
    unittest.main()