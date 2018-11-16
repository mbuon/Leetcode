class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        expected = 1
        i = 0
        

        while (i < len(nums)):
            if (nums[i] <= 0):
                i += 1
                continue
            else:
                if (nums[i] == expected):
                    while (i + 1 < len(nums)) and (nums[i + 1] == nums[i]):
                        i += 1
                    expected += 1
                    i += 1
                    continue
                else:
                    return expected
            i += 1
        return expected
            
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.append(0)
        
        for i in range(0, len(nums)):
            while (nums[i] > 0) and (nums[i] < len(nums)) and (nums[i] != i) and (nums[nums[i]] != nums[i]):
                a = nums[i]
                b = nums[nums[i]]
                nums[nums[i]] = a
                nums[i] = b

        j = 0
        
        for j in range(0, len(nums)):
            if (nums[j] != j) and (j > 0):
                return j
            
        return j + 1