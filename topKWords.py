"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
"""

import collections
from typing import List
from unittest import result
import unittest

def topKWords_dict(words:List[str], k: int) -> List[str]:
    """    
        1. create a dict where key is the string & value is count
        2. sort the values in descending order
            2.1 if values are equal, sort the keys alphabetically
        3. pick k elem from the dict and append them to result array
    """
    unsorted_dict = collections.defaultdict(lambda:0)

    for word in words:
        # {"coding": 1,"i":2, "love":2, "leetcode": 1}
        unsorted_dict[word] += 1
        dict_items = unsorted_dict.items()
        sorted_items = sorted(dict_items, key=lambda tuple:(tuple[1]*-1, tuple[0]))
    results = []
    for key, value in sorted_items:
        results.append(key)
    return results[:k]

# N - number of words in array 'words'
# Time Complexity: O(Nlog)
# Space Complexity: O(N)
    
 
        
class TestProblems(unittest.TestCase):
    def test_top_k_words(self):
        actual = topKWords_dict(["i","love","leetcode","i","love","coding"], 2)
        expected = ["i","love"]
        self.assertCountEqual(actual, expected)

        actual_1 = topKWords_dict(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
        expected_1 = ["the","is","sunny","day"]
        self.assertCountEqual(actual_1, expected_1)


if __name__ == '__main__':
    unittest.main()