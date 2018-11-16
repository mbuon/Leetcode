class Solution:
    
    def fill(self, t):
        D = {}
        for n in t:
            if n in D: D[n] += 1
            else: D[n] = 1
        return D
    
    def missing(self, D):
        count = 0
        for k in D:
            if D[k] > 0:
                count += 1
        return count
    
    def minWindow(self, s, t):
        """
        :type s: str (whole string)
        :type t: str (substring)
        :rtype: str
        """
        
        if len(s) == 0 or len(t) == 0:
            return ""
        
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        
        D = self.fill(t)
        i = 0

        
        iters = []
        
        for j in range(0, len(s)):
            if self.missing(D) > 0:
                if s[j] in D:
                    D[s[j]] -= 1

            if self.missing(D) == 0:
                while (not self.missing(D) == 1) and (i < j):
                    if s[i] in D:
                        D[s[i]] += 1
                    i += 1
                    
                iters.append((max(0, i-1), j))

                while (not s[i] in D) and (i < j):
                    i += 1
        
        if len(iters) == 0:
            return ""     
        
        min = len(s)
        best = iters[0]
        
        for (a, b) in iters:
            if b - a < min:
                best = (a, b)
                min = b -a
        
        return s[best[0]:best[1] + 1]