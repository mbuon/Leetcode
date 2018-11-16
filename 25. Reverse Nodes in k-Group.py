# Reverse k nodes, then first.next = reverseKGroup(last.next)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode 
        """

        if head == None:
            return None

        # Just checking if remaining length is at least k

        temp = head
        for j in range(0, k):
            if temp != None:
                temp = temp.next
            else:
                return head
        
        prev = None
        curr = head
        next = None
        
        for i in range(0, k):
            if curr != None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                
        head.next = self.reverseKGroup(next, k)
        return prev