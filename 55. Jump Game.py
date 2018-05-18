# Based on explanation: https://leetcode.com/problems/jump-game/discuss/130891/Easy-alternate-approach:-Only-0's-can-stop-us-or-O(N)-timeO(1)-space
# You start with the fuel from the first block. You can either reset your fuel the next block you go to, or can skip it, whatever works better
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fuel = 0

        for i in range(0, len(nums)):
        	fuel = max(fuel, nums[i])

        	if (i == len(nums) - 1):
        		return True
        	else:
        		if (fuel > 0):
        			fuel -= 1
        		else:
        			return False
        return True

print(Solution().canJump([1,0,0]))