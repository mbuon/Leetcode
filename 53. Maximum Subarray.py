class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's algorithm states that max-sum subarray ending in A[i] is "either A[i] or (A[i] + max-sum subarray ending in A[i-1])".
        # Note that I am overwriting nums list because earlier elements are not required later
        
        if len(nums) == 0:
            return 0
        
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], (nums[i] + nums[i-1]))
            maxSum = max(maxSum, nums[i])
            
        return maxSum