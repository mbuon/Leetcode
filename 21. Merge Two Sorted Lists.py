# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if (l1 == None) and (l2 == None):
            return None
        elif (l1 == None):
            return l2
        elif (l2 == None):
            return l1
        
        if (l1.val < l2.val):
            ptrA = l1
            ptrB = l2
        else:
            ptrA = l2
            ptrB = l1
            
        headA = ptrA
        
        while (ptrA.next != None):
            while (ptrB != None) and (ptrB.val >= ptrA.val) and (ptrB.val < ptrA.next.val):
                save = ptrA.next
                ptrA.next = ptrB
                ptrB = ptrB.next
                ptrA.next.next = save
            ptrA = ptrA.next
        ptrA.next = ptrB
        
        return headA