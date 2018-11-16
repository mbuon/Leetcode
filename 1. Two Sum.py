class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        location = {}

        for i, n in enumerate(nums):
            if (target - n in location):
                return [i, location[target - n]]
            else:
            	location[n] = i

nums = [3,2,4,2,1,2,4,32,3,53,45,3]
target = 8

print(Solution().twoSum(nums, target))