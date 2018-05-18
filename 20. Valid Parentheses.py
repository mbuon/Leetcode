class Solution:
   
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        closer = {}
        closer['{'] = '}'
        closer['('] = ')'
        closer['['] = ']'

        opener = {}
        opener['}'] = '{'
        opener[')'] = '('
        opener[']'] = '['

        last = []

        for c in s:
            if c in closer.keys():
                last.append(c)
            elif c in opener.keys():
                if last[-1] == opener[c]:
                    last.pop()
                else:
                    return False
        
        if (len(last) == 0):
            return True
        else:
            return False

print(Solution().isValid("{[]}"))