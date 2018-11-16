class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
               
        rows = len(A)
        
        if rows == 0:
            return A
        
        cols = len(A[0])
        
        transpose = [[0 for i in range(0, rows)] for j in range(0, cols)]
        
        for i in range(0, len(A)):
            for j in range(0, len(A[i])):
                transpose[j][i] = A[i][j]

        return transpose