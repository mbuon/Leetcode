# https://leetcode.com/problems/rotate-image/description/

# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        length = len(matrix)        
        
        for i in range (0, length):
            for j in range (0, int(length/2)):
                value = matrix[i][j]
                matrix[i][j] = matrix[i][length - j - 1]
                matrix[i][length - j - 1] = value
        
        for i in range(0, length):
            for j in range(0, length - i - 1):
                value = matrix[i][j]
                matrix[i][j] = matrix[length - 1 - j][length - 1 - i]
                matrix[length - 1 - j][length - 1 - i] = value

# First loop: reverse 
# and then
# Second loop: flip diagonally