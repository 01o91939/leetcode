"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false"""

import unittest


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_dict, t_dict = {}, {} #character:count

    for char in range(len(s)):
        s_dict[s[char]] = 1 + s_dict.get(s[char], 0)
    for char in range(len(t)):
        t_dict[t[char]] = 1 + t_dict.get(t[char], 0)

    for char, count in s_dict.items():
        if count != t_dict.get(char, 0):
            return False
    return True


# Time Complexity: O(|s| + |t|)
# Space Complexity: O(1)

class TestProblems(unittest.TestCase):

    def test_valid_anagram(self):
        actual = isAnagram("anagram","nagaram")
        self.assertTrue(actual)

        actual_1 = isAnagram("tiziano", "notizia")
        self.assertTrue(actual_1)

        actual_2 = isAnagram("car", "rat")
        self.assertFalse(actual_2)

    
if __name__ == '__main__':
    unittest.main()