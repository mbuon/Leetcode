# Beats 99.17% of Python submissions. :D

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        store = {}
        for elem in strs:
            sortedElem = ''.join(sorted(elem))
            if sortedElem in store:
                store[sortedElem].append(elem)
            else:
                store[sortedElem] = [elem]
        
        listStore = []
        for key, value in store.items():
        	listStore.append(value)

        return listStore

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))