class Solution:
    
    def count(self, list, character):
        
        count = 0
        for element in list:
            if element == character:
                count += 1
                
        return count
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n == 0:
            return []
        
        i = 0
        result = ['(']
        
        for k in range(0, n * 2 - 1):
            
            newResult = []
            
            for item in result:
                
                if self.count(item, '(') < n:
                    newResult.append(item + '(')
                
                if self.count(item, '(') > self.count(item, ')'):
                    newResult.append(item + ')')
                  
            result = newResult
            i += 1
            
        return result
                    