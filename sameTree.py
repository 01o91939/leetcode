"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# Definition for a binary tree node.
from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

class TestProblems(unittest.TestCase):
    def test_same_tree(self):
        actual = TreeNode(1, TreeNode(2), TreeNode(3))
        expected = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(isSameTree(actual, expected))

        actual = TreeNode(1, TreeNode(2), None)
        expected = TreeNode(1, None, TreeNode(2))
        self.assertFalse(isSameTree(actual, expected))

if __name__ == '__main__':
    unittest.main()