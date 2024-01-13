# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TODO: Add explaination
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.iterative_traverse(root)

    def iterative_traverse(self, tree):
        stack = []
        stack.append(tree)
        while stack:
            p = stack.pop()
            if p != None:
                height_diff = abs(self.height(p.left, 0) - self.height(p.right, 0))
                print(height_diff)
                if height_diff > 1:
                    return False
                stack.append(p.left)
                stack.append(p.right)
                
        return True

    def height(self, tree, h):
        if tree:

            return max(self.height(tree.left, h+1), self.height(tree.right, h+1) )
        
        return h