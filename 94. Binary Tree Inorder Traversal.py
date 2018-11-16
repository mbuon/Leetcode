# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.output = []    
        self.inorder(root)
        return self.output
        
    def inorder(self, root):
        if root == None:
            return
        
        self.inorder(root.left)
        self.output.append(root.val)
        self.inorder(root.right)
        return
            
        