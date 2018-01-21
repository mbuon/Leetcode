# https://leetcode.com/problems/unique-paths/description/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 3 x 7 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if (m == 0 or n == 0):
            return 0

        if (obstacleGrid[0][0] == 1):
            return 0

        if (m == 1 and n == 1 and obstacleGrid[0][0] == 0):
            return 1
        
        value = {}
        if (obstacleGrid[m-1][n-1] == 0): 
            value[m-1,n-1] = 1
        value[0,0] = 0

        for row in reversed(range(0,m)):
            for column in reversed(range(0,n)):
                if (obstacleGrid[row][column] == 0):    
                    try:
                        value[row, column] = value[row + 1, column] + value[row, column + 1]
                    except:
                        try:
                            value[row, column] = value[row, column + 1]
                        except:
                            try:
                                value[row, column] = value[row + 1, column]
                            except:
                                pass

        return value[0,0]