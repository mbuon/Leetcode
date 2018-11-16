# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def path(root, value, current):
            current.append(root)
            if root.val < value:
                return path(root.right, value, current)
            elif root.val > value:
                return path(root.left, value, current)
            else:
                return current
            
        path_p = path(root, p.val, [])
        path_q = path(root, q.val, [])
        
        size = min(len(path_p), len(path_q))

        previous = path_p[0]
        for i in range(0, size):
            if path_p[i].val == path_q[i].val:
                previous = path_p[i]
            else:
                return previous
        return path_p[i] if len(path_p) > len(path_q) else path_q[i]