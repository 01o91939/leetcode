"""Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

"""
import collections
from typing import List
import unittest

def topKElements(nums: List[int], k: int) -> List[int]:
    element_count = collections.defaultdict(lambda:0)
    for num in nums:
        element_count[num] += 1
        dict_list = element_count.items()
        sorted_elements = sorted(dict_list, key=lambda kv: (kv[1]*(-1)))
    
    result = []
    for num, count in sorted_elements:
        result.append(num)

    return result[:k]    

# N - number of elements in array 'nums'
# Time Complexity: O(NlogN)
# Space Complexity: O(N)

# using Counter.most_common(), which returns a list of the n most common elements 
# and their counts from the most common to the least
def topKElements_counter(nums: List[int], k: int) -> List[int]:
    most_common = collections.Counter(nums).most_common(k)
    return [item[0] for item in most_common]

# N - number of elements in array 'nums'
# Time Complexity: O(N)
# Space Complexity: O(N)
        
class TestProblems(unittest.TestCase):
    def test_top_k_elements(self):
        actual = topKElements_counter([1,1,1,2,2,3], 2)
        expected = [1, 2]
        self.assertCountEqual(actual, expected)

        actual_1 = topKElements_counter([1], 1)
        expected_1 = [1]
        self.assertCountEqual(actual_1, expected_1)

        actual = topKElements([1,1,1,2,2,3], 2)
        expected = [1, 2]
        self.assertCountEqual(actual, expected)

        actual_1 = topKElements([1], 1)
        expected_1 = [1]
        self.assertCountEqual(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()