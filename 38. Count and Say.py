class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        output = "1"
        for i in range(0, n-1):
            output = self.say(output)
            
        return output
    
    def say(self, n):
        count = 1
        item = n[0]
        
        log = []
        
        for i in range (1, len(n)):
            if (n[i] == n[i-1]):
                count += 1
            else:
                log.extend([str(count), str(item)])
                item = n[i]
                count = 1

        log.extend([str(count), str(item)])

        return "".join(log)

print(Solution().countAndSay(10))