# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root, k):
            if root != None:
                inorder(root.left, k)
                values.append(root.val)
                inorder(root.right, k)
                
        values = []
        inorder(root, k)
        try:
            return values[k - 1]
        except IndexError as e:
            return None