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