# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # Solution explaination:
    # Recursive solution to find the max depth in both the right and left subtree.

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth(root,0)

    def max_depth(self, tree, h):
        if tree:
            return max(self.max_depth(tree.left,h+1), self.max_depth(tree.right,h+1))
        
        return h