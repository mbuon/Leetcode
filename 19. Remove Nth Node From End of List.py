# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        current = head
        nodes = 1

        while (current.next != None):
            current = current.next
            nodes = nodes + 1

        if (nodes == n):
            return head.next
            
        current = head
        counter = 1

        while (counter < nodes - n):
            current = current.next
            counter = counter + 1
        
        try:
            current.next = current.next.next
        except:
            current.next = None  

        return head