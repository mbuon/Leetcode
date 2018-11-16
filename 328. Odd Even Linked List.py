# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index = 0
        node = head
        save = None
        lastTwoNodes = []
        while node != None:
            if index == 1:
                save = node
            nextNode = node.next
            index += 1
            if node.next != None:
                lastTwoNodes = [node, node.next]
                node.next = node.next.next
            node = nextNode
        if len(lastTwoNodes) == 2:
            if index % 2 == 0:
                lastTwoNodes[0].next = save
            else:
                lastTwoNodes[1].next = save
        return head