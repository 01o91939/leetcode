"""Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5

"""

import unittest

def getSum(a:int, b:int) -> int:
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a

# Time Complexity: O(1)
# Space Complexity: O(1)
        
class TestProblems(unittest.TestCase):
    def test_get_sum(self):
        actual = getSum(1, 2)
        expected = 3
        self.assertTrue(actual, expected)

        actual_1 = getSum(2, 3)
        expected_1 = 5
        self.assertTrue(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()