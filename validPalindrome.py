"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

import unittest


def isPalindrome(s: str) -> bool:
    new_string = (''.join(e for e in s if e.isalnum())).lower()
    # Print the original string in reverse order if we set the stride to -1:
    reversed_string = new_string[::-1]
    return new_string == reversed_string

# N - number of characters in string
# Time Complexity: O(N)
# Space Complexity: O(N) ?

class TestProblems(unittest.TestCase):

    def test_valid_palindrome(self):
        actual = isPalindrome("A man, a plan, a canal: Panama")
        self.assertTrue(actual)

        actual_1 = isPalindrome("race a car")
        self.assertFalse(actual_1)

        actual_2 = isPalindrome(" ")
        self.assertTrue(actual_2)

    
if __name__ == '__main__':
    unittest.main()