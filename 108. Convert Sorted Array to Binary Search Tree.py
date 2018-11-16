# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(nums)
        
    def constructTree(self, nums):
        if not nums:
            return None
        else:
            mid = int(len(nums) / 2)
            parent = TreeNode(nums[mid])
            parent.left = self.constructTree(nums[:mid])
            parent.right = self.constructTree(nums[mid + 1:])
            return parent