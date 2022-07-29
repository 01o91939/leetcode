"""
Example:
words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax'] 
string1 = 'tabncihjs' 
find_embedded_word(words, string1) -> cat (the letters do not have to be in order)
"""

import collections
from typing import List
import unittest

# Using sorting
# words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax'] -> act, abbbdyx, dgo, bdir, acr, ax
# string1 = 'tabncihjs' -> abbcccccdhijnsty'
def find_embedded_word_sort(words: List[str], string1: str) -> str:
    sorted_string1 = sorted(string1)
    for word in words:
        sorted_word = sorted(word)
        sorted_string1_ptr = 0
        for ch in sorted_word:
            while sorted_string1_ptr < len(sorted_string1) and sorted_string1[sorted_string1_ptr] != ch:
                sorted_string1_ptr += 1
            sorted_string1_ptr += 1
        if sorted_string1_ptr <= len(sorted_string1):
            return word
    return None


# Using Counter(), with count
def find_embedded_word_counter(words: List[str], string1: str) -> str:
    dict_string1 = collections.Counter(string1)
    for word in words:
        dict_word = collections.Counter(word)
        count = 0
        for key in dict_word:
            if dict_word[key] <= dict_string1[key]:
                count += 1
        if count == len(dict_word):
            return word
    return None

# Using Counter(), with boolean
def find_embedded_word_bool(words: List[str], string1: str) -> str:
    dict_string1 = collections.Counter(string1)
    for word in words:
        dict_word = collections.Counter(word)
        word_present = True
        for key in dict_word:
            if dict_word[key] > dict_string1[key]:
                word_present = False
                break
        if word_present:
            return word
    return None

class TestProblems(unittest.TestCase):

    def test_embedded_words(self):
        actual = find_embedded_word_sort(['cat', 'baby', 'dog', 'bird', 'car', 'ax'], 'tabncihjs')
        expected = 'cat'
        self.assertTrue(actual, expected)

        actual = find_embedded_word_bool(['cat', 'baby', 'dog', 'bird', 'car', 'ax'], 'tabncihjs')
        expected = 'cat'
        self.assertTrue(actual, expected)

        actual = find_embedded_word_counter(['cat', 'baby', 'dog', 'bird', 'car', 'ax'], 'tabncihjs')
        expected = 'cat'
        self.assertTrue(actual, expected)
    
if __name__ == '__main__':
    unittest.main()