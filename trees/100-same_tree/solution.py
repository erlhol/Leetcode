# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution explaination:
    # A very straight forward solution.
    # Traverese both of the trees and create a list of visited nodes.
    # If both of the traversals create an identical list, this means that we have equal trees
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # first binary tree is p and second is q
        return self.tree_traversal(p,[],0) == self.tree_traversal(q,[],0)
        
    def tree_traversal(self, tree, l, i):
        # Do an inorder traversal
        if tree:
            self.tree_traversal(tree.left,l,i+1)
            l.append((tree.val,i))
            self.tree_traversal(tree.right,l,i+1)

        return l

        
