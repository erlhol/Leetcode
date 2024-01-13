# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    # Solution explaination:
    # Do a BFS search of the tree. But add the right child before the left child (to invert the tree)
    # Keep track of the previous node, and where it "came from". If it was from a right branch, it should now
    # be the left branch

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root,None,"none")]) # The node and the previous
        while queue:
            curr, prev, direction = queue.popleft()
            if direction == "right":
                prev.left = curr
            elif direction == "left":
                prev.right = curr
                
            # Add the left and right node to the queue
            # In this specific order is really important
            if curr != None:
                if curr.right != None:
                    v_right = curr.right
                    curr.right = None
                    queue.append((v_right,curr,"right"))
                if curr.left != None:
                    v_left = curr.left
                    curr.left = None
                    queue.append((v_left,curr,"left"))
        return root