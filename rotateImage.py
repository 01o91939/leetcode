"""Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List
import unittest


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for row in range((n+1)//2):
        for col in range(n//2):
            temp = matrix[col][n-1-row]
            matrix[col][n-1-row] = matrix[row][col]
            matrix[row][col] = matrix[n-1-col][row]
            matrix[n-1-col][row] = matrix[n-1-row][n-1-col]
            matrix[n-1-row][n-1-col] = temp

class TestProblems(unittest.TestCase):
    def test_rotate_image(self):
        actual = rotate([[1,2,3],[4,5,6],[7,8,9]])
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        self.assertCountEqual(actual, expected)

        actual_1 = rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
        expected_1 = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        self.assertCountEqual(actual_1, expected_1)

if __name__ == '__main__':
    unittest.main()
    