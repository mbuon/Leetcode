# Question is, after robbing a house, whether to stip one house or two
# Ofcourse some trivial cases for first two (or maybe three houses)

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums == []:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        maxSum = [0 for i in nums]
        
        for i in range(0, len(nums)):
            
            if i == 0:
                maxSum[i] = nums[i]
                
            elif i == 1:
                maxSum[i] = max(nums[i], nums[i-1])
            
            elif i == 2:
                maxSum[i] = max(nums[i-1], nums[i] + nums[i-2])
            
            else:
                maxSum[i] = nums[i] + max(maxSum[i-2], maxSum[i-3])
            
        return max(maxSum[-1], maxSum[-2])