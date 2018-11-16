class Solution:
    maximum = 0
    
    def diameterOfBinaryTree(self, root):
        self.dfs(root, 0)
        return self.maximum
        
    def dfs(self, root, depth):
        if root != None:
            left = self.dfs(root.left, depth + 1)
            right = self.dfs(root.right, depth + 1)
            self.maximum = max(self.maximum, left - depth + right - depth)
            return max(left, right)
        else:
            return depth - 1