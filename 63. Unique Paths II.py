# https://leetcode.com/problems/unique-paths-ii/

# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

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