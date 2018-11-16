class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = len(s) - 1
        
        found = False
        count = 0
        
        while i >= 0:
            if (s[i] == " " ) and (found == False):
                i -= 1
            elif (s[i] == " ") and (found == True):
                return count
            else:
                i -= 1
                count += 1
                found = True
                
        return count