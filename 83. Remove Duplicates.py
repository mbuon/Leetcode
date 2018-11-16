# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # 1->2->2->2->3->3
        
        i = head
        
        if i == None:
            return head
        
        j = head.next
        
        value = head.val
        
        while j != None:
            while (j != None) and (j.val == value):
                j = j.next
            
            i.next = j
            i = j
            
            if j == None:
                return head
                        
            value = i.val
            j = j.next

        return head

# Explanation:

# 1->2->2->2->3->3

# Start with i at first element and j at second element. Value is set to the value of the first element.
# Keep increasing j till the value matches. Now j is at the next element (the first one to have differect value.
# Now, connect i->j and set i to j and j to j + 1 (this is same logic as first step)
# Set the value to the value of the current i (This is also the same logic as first step)

# Return head