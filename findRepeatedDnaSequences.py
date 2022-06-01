"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

results = (AAAAACCCCC)
idx = 2
temp = ("AAAAACCCCC","AAAACCCCCA", "AAACCCCCAA", "AACCCCCAAA" ) 

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Example 3:
Input: s = "ACGTACGTACTTTTACGTACGTAC"
Output: ["ACGTACGTAC"]
"""

from typing import List
import unittest


def findRepeatedDnaSequences(dnaSeq: str) -> List[str]:
    """Iterate through every position in the string, except for the last 9
    because we want at least 9 characters after pointer i to make a 
    window of 10 characters.
    """
    temp, results = set(), set()
    for i in range(len(dnaSeq) - 9):
        # +10 since the second index is non-inclusive in python
        substring = dnaSeq[i:i+10]
        # if we don't see the substring in temp, we add it
        if substring not in temp:
            temp.add(substring)
        elif substring not in results:
            results.add(substring)
    return results

# N - number of characters in the string
# Time Complexity: O(N-10) -> O(N)
# Space Complexity: O(N)

class TestProblems(unittest.TestCase):

    def test_find_repeated_dna_sequences(self):
        actual = findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
        expected = ["AAAAACCCCC","CCCCCAAAAA"]
        self.assertCountEqual(actual, expected)

        actual_1 = findRepeatedDnaSequences("AAAAAAAAAAAAA")
        expected_1 = ["AAAAAAAAAA"]
        self.assertCountEqual(actual_1, expected_1)

        actual_2 = findRepeatedDnaSequences("ACGTACGTACTTTTACGTACGTAC")
        expected_2 = ["ACGTACGTAC"]
        self.assertCountEqual(actual_2, expected_2)
    
if __name__ == '__main__':
    unittest.main()