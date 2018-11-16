# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.paths = []
        self.validPaths(root, sum, [])
        return self.paths
    
    def validPaths(self, root, target, current):
        if root != None:
            if root.left == None and root.right == None:
                if sum(current) + root.val == target:
                    self.paths.append(current + [root.val])
            else:
                self.validPaths(root.left, target, current + [root.val])
                self.validPaths(root.right, target, current + [root.val])