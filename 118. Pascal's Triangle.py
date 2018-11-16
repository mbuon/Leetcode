class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if (numRows == 0):
            return []
    
        output = [[1]]
        
        for i in range(1, numRows):
            output.append(self.pascal(output[-1]))
        
        return output
    
    def pascal(self, row):
        if (len(row) == 0):
            return [1]
        
        else:
            output = [1]
            for i in range(0, len(row) - 1):
                output.append(row[i] + row[i + 1])
            output.append(1)
            return output