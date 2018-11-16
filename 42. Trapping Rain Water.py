class Solution:
    def trapN2(self, height):
    	# Reverts with quadratic time
        
        totalWater = 0
        for i in range(0, len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            else:
                maxLeft = 0
                for j in range(0, i):
                    maxLeft = max(maxLeft, height[j])
                maxRight = 0
                for k in range(i + 1, len(height)):
                    maxRight = max(maxRight, height[k])
            totalWater += max(min(maxLeft, maxRight) - height[i], 0)
        return totalWater

    def trap(self, height):
    	# Reverts with linear time

    	leftMax = [0]
    	rightMax = [0]
    	totalWater = 0

    	for i in range(1, len(height)):
    		leftMax.append(max(leftMax[-1], height[i - 1]))

    	for j in reversed(range(0, len(height) - 1)):
    		rightMax.append(max(rightMax[-1], height[j + 1]))
    	rightMax = list(reversed(rightMax))

    	for k in range(0, len(height)):
            if k == 0 or k == len(height) - 1:
                continue
            else:
            	totalWater += max(min(leftMax[k], rightMax[k]) - height[k], 0)
        return totalWater

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))