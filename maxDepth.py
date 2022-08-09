"""Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

"""

from queue import Queue
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

# Time complexity: O(N)
# Space complexity: O(N)

# DFS
def maxDepth_stack(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    stack = []
    height_stack = []
    max_height = 0
    while stack:
        node = stack.pop()
        print(node)
        height = height_stack.pop()

        max_height = max(max_height, height)

        if node.left:
            stack.append(node.left)
            height_stack.append(height+1)
        if node.right:
            stack.append(node.right)
            height_stack.append(height+1)
    return max_height

# BFS
def maxDepthBFS(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    queue = []
    height_stack = []
    max_height = 0
    while queue.em:
        node = queue.head
        height = height_stack.head

        max_height = max(max_height, height)

        if node.left:
            queue.append(node.left)
            height_stack.append(height+1)
        if node.right:
            queue.append(node.right)
            height_stack.append(height+1)
    return max_height



class TestProblems(unittest.TestCase):
    def test_max_depth(self):
        actual = maxDepth_stack(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17))))
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()