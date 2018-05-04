class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Case 0: String size is 0

        if (len(s) == 0):
            return 0

        l = 0
        x, y = 0, 0
        current = {}
        
        for R in range(0, len(s)):
            
            # Case 1: The current character is not in the current string

            if s[R] not in current.keys():
                current[s[R]] = True

                if (R - l) > (y - x):
                    y = R
                    x = l
                
            # Case 2: The current character is in the current string
            
            else:

                while(s[l] != s[R]):

                    current.pop(s[l], None)
                    l += 1
                l += 1

        return y - x + 1