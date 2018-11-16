class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        
        for n in nums:
            result = result ^ n
        
        return result

# Explanation:

# n ^ n = 0
# n ^ 0 = n

# Also, (n ^ m) ^ (n ^ m) = (n ^ n) ^ (m ^ m) = 0 ^ 0 = 0