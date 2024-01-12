# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Solution explaination:
    # Simply reverse the list iteratively
    # Setting the next pointer to the previously visited node
    def reverseList(self, head):
        pre = None
        n = head
        while (n != None):
            pointer = n.next
            n.next = pre
            pre = n
            n = pointer
        return pre
        