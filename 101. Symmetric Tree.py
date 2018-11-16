# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfsLeft(self, node, elementsLeft):
        if node == None:
            elementsLeft.append(None)
            return
        else:
            elementsLeft.append(node.val)
            self.dfsLeft(node.left, elementsLeft)
            self.dfsLeft(node.right, elementsLeft)
            
    def dfsRight(self, node, elementsRight):
        if node == None:
            elementsRight.append(None)
            return
        else:
            elementsRight.append(node.val)
            self.dfsRight(node.right, elementsRight)
            self.dfsRight(node.left, elementsRight)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        elementsLeft = []
        elementsRight = []
        
        self.dfsLeft(root, elementsLeft)
        self.dfsRight(root, elementsRight)
        
        for L, R in zip(elementsLeft, elementsRight):
            if L != R:
                return False
            
        return True