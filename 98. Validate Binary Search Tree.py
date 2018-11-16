# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.values.append(root.val)
            self.inorder(root.right)
        return
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.values = []
        self.inorder(root)
        for i in range(1, len(self.values)):
            if self.values[i] <= self.values[i-1]:
                return False
        return True