class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        
        ways = []

        for i in range(0, n):
        	if i == 0:
        		ways.append(1)
        	elif i == 1:
        		ways.append(2)
        	else:
        		ways.append(ways[i - 1] + ways[i - 2])
                
        return ways[-1]