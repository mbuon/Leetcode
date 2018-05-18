# Will fail if first element is X. Simpler solution: return sorted(list(set(nums)))

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = 'X'
        p = 0

        for i in range(0, len(nums)):
            if h == nums[p]:
                nums.pop(p)
            else:
                h = nums[p]
                p += 1

        return len(nums)
            
print(Solution().removeDuplicates([0,0,1,1,10,0,0,0,0]))
        