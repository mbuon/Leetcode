# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def level(root, depth):
            if root == None:
                return
            if len(values) <= depth:
                values.append([])
            values[depth].append(root.val)
            frontiers = [root.left, root.right]
            for frontier in frontiers:
                level(frontier, depth + 1)

        values = []
        level(root, 0)
        return values