# Needs to be improved: followes DFS

class Solution:
    
    def code_permute(self, listA, listB):

        result = []

        if (listB == []):
            return [listA]

        for i in range(0, len(listB)):

            listA_temp = copy.deepcopy(listA)
            listB_temp = copy.deepcopy(listB)
            listA_temp.append(listB_temp[i])
            listB_temp.pop(i)

            result.extend(self.code_permute(listA_temp, listB_temp))

        return result
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.code_permute([], nums)
        
    