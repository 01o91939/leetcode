"""Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the
path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
"""

import unittest
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    results = []
    dfs_helper(root, targetSum, results, [])
    return results

def dfs_helper(root, targetSum, results, path) -> None:
    if not root:
        return
    if root.val == targetSum and not root.left and not root.right:
        path.append(root.val)
        results.append(path)
        return
    
    targetSum -= root.val
    dfs_helper(root.left, targetSum, results, path+[root.val])
    dfs_helper(root.right, targetSum, results,path+[root.val])


class TestProblems(unittest.TestCase):
    def test_two_sums(self):
        actual = pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 3)
        expected = [[1, 2]]
        self.assertCountEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()