"""Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

"""

import unittest
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count_left = maxDepth(root.left)
        count_right = maxDepth(root.right)
        return max(count_left, count_right) + 1

class TestProblems(unittest.TestCase):
    def test_max_depth(self):
        actual = maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17))))
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()