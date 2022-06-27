"""Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
from typing import List
import unittest


def exist(grid: List[List[str]], word: str) -> bool:
    row, column = len(grid), len(grid[0])
    visited = [[False for i in range(column)] for j in range(row)]
    """
    visited = [[false,false,false,false],
                [false,false,false,false],
                [false,false,false,false]]
    """
    for i in range(row):
        for j in range(column):
            if dfs_helper(i, j, grid, word, 0, visited):
                return True
    return False

def dfs_helper(i, j, grid, word, letter_index, visited):
    # validation
    # check here i, j make sense
    if i < 0 or i == len(grid) \
    or j < 0 or j == len(grid[0]) \
    or visited[i][j] \
    or grid[i][j] != word[letter_index]:
        return False
    #base case
    if letter_index >= len(word)-1:
        return True
    #marking
    visited[i][j] = True
    #branching
    result = dfs_helper(i, j-1, grid, word, letter_index+1, visited) \
            or dfs_helper(i, j+1, grid, word, letter_index+1, visited) \
            or dfs_helper(i+1, j, grid, word, letter_index+1, visited) \
            or dfs_helper(i-1, j, grid, word, letter_index+1, visited)
    visited[i][j] = False
    return result

class TestProblems(unittest.TestCase):
    def test_word_search(self):
        actual = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
        self.assertTrue(actual)

        actual = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
        self.assertTrue(actual)

        actual = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
        self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()