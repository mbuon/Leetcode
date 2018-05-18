# The idea is to pick the block that will take you the furthest
# For example, [6,5,1,2,0,3,2,1,5,1,1,1,3] when at the first block (6), pick 5th or 6th block instead of 1st block because that has max reach

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        jumps = 0

        while (i < len(nums) - 1):
        	consider = []

        	# The min in the next line is to prevent going beyond the length of the list
        	for j in range(i+1, min(i+1+nums[i], len(nums))):
        		# The min in the next line is to again, prevent giving a higher value to an element just because it promised a higer jump, but infact a later element also takes us to the end of the list
        		consider.append(min(j+nums[j], len(nums) - 1))

        	maximum = len(consider) - 1 - consider[::-1].index(max(consider))
        	i = i + 1 + maximum
        	jumps += 1

        	print (consider, i, maximum)

        return jumps

print("Total Jumps:", Solution().jump([2,3,1]))



