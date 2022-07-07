"""Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []
"""

from operator import invert
from typing import Optional
import unittest
from sameTree import isSameTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:
        return
    root.left, root.right = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)
    return root

class TestProblems(unittest.TestCase):
    def test_invert_tree(self):
        actual = invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))))
        expected = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
        self.assertTrue(isSameTree(actual, expected))

if __name__ == '__main__':
    unittest.main()
    