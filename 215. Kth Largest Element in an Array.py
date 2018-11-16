class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        storage = sorted(nums[0:k])
        
        for i in range(k, len(nums)):
            
            j = 0
            while j < len(storage):
                if storage[j] < nums[i]:
                	if j > 0:
                		storage[j - 1] = storage[j]
                	storage[j] = nums[i]
                j += 1
                    
        return storage[0]

S = Solution()
S.findKthLargest([-1,2,-0], 1)