from typing import List
import unittest


def findRepeatedDnaSequences(dnaSeq: str) -> List[str]:
    temp, results = set(), set()
    for i in range(len(dnaSeq) - 9):
        substring = dnaSeq[i:i+10]
        if substring not in temp:
            temp.add(substring)
        elif substring not in results:
            results.add(substring)
    return results

class TestProblems(unittest.TestCase):

    def test_find_repeated_dna_sequences(self):
        actual = findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
        expected = ["AAAAACCCCC","CCCCCAAAAA"]
        self.assertCountEqual(actual, expected)

        actual_1 = findRepeatedDnaSequences("AAAAAAAAAAAAA")
        expected_1 = ["AAAAAAAAAA"]
        self.assertCountEqual(actual_1, expected_1)
    
if __name__ == '__main__':
    unittest.main()