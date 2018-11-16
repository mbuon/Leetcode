class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = [[]]
        
        for n in nums:
            length = len(powerset)
            for element in powerset[:length]:
                pair = list(element)
                pair.append(n)
                powerset.append(pair)

        return powerset

# Logic:
# Say you already had a bunch of elements in a powerset:
# {A, B, C, D, E, F}

# Now, if you were to add a new element, '1' to the sets, it would become:

# {A, [A, 1], B, [B, 1]...}

# There are no other combinations possible.

# So, adding an element to a subset, we have to make one decision, keep a copy of old element, and one with the old and new element.
# Either keep it or not (Do both)