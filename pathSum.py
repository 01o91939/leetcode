"""Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up
all the values along the path equals targetSum.

A leaf is a node with no children.

https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

root = 5, left = 9, right=8, targetSum=22
"""

import unittest
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if root.val == targetSum and not root.left and not root.right:
        return True
    
    targetSum -= root.val
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
    
class TestProblems(unittest.TestCase):
    def test_has_path_sum(self):
        actual = hasPathSum((TreeNode(1, TreeNode(2), TreeNode(3))), 3)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()