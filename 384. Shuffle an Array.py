class Solution:
    
    original = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        possible = [i for i in range(0, len(self.original))]
        newNums = []
        
        for i in range(0, len(self.original)):
            choice = random.choice(possible)
            newNums.append(self.original[choice])
            possible.pop(possible.index(choice))
            
        return newNums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()