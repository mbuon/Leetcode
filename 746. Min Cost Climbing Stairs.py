class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        mincost = cost
        
        for i in range(0, len(cost)):
            
            if i == 0 or i==1:
                mincost[i] = cost[i]
            else:
                mincost[i] = cost[i] + min(mincost[i-1], mincost[i-2])

        return min(mincost[-1], mincost[-2])
                