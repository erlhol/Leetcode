# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Solution explaination:
    # Simply implemented the merge sort on the linked list

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        head = new_list
        # While there are still elements in both lists
        while (list1 != None and list2 != None):
            # Choose the value with the smallest value and append it
            # Increment to the next element in list1
            if list1.val <= list2.val:
                new_list.next = ListNode(list1.val)
                new_list = new_list.next
                list1 = list1.next
            else:
                new_list.next = ListNode(list2.val)
                new_list = new_list.next
                list2 = list2.next
        
        # While there are still elements in list1, append them to the list
        while (list1 != None):
            new_list.next = ListNode(list1.val)
            new_list = new_list.next
            list1 = list1.next
        
        # While there are still elements in list2, append them to the list
        while (list2 != None):
            new_list.next = ListNode(list2.val)
            new_list = new_list.next
            list2 = list2.next
        
        return head.next