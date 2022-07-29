"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output: 1
[0,0], [0,1], [1, 0]*, [0,2], [1,1], [2,1]


gone: 1,3 in progress:, to do: -, -, -, -
gone: 0,3 in progress: , to do: -, -, -, -
done: 0,2 in progress: right, to do: - - -
done: 1,0
done: 2,0 in progress: up
done: 2,1 in progress: left, to do: up
done: 1,1 in progress: down, to do: -, down, left up
done: 0,1 in progress: down, to do:
done: 0,0 in progress: -, to do: -, -, -


can we go to a cell?
has this cell been visited and is this right letter?
mark the cell as visited
explore from the cell
unmark it as visited

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

from typing import List
import unittest


def dfs(row, col, grid, visited):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        if tuple([row, col]) in visited:
            return
        if grid[row][col] != '1':
            return
        
        visited.add(tuple([row, col]))
        
        dfs(row+1, col, grid, visited)
        dfs(row-1, col, grid, visited)
        dfs(row, col+1, grid, visited)
        dfs(row, col-1, grid, visited)

        
def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    island_count = 0
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1' and tuple([row, col]) not in visited:
                dfs(row, col, grid, visited)
                island_count +=1
    return island_count

class TestProblems(unittest.TestCase):
    def test_num_islands(self):
        actual = numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
        expected = 1
        self.assertTrue(actual, expected)

if __name__ == '__main__':
    unittest.main()