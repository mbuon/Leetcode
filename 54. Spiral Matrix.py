# Beats 95.57% of Python3 submissions :D

class Solution:

    def goRight(self):

        if ((self.rows[0] >= self.rows[1]) or (self.cols[0] >= self.cols[1])):
            return []

        output = []
        for j in range(self.cols[0], self.cols[1]):
            output.append(self.matrix[self.rows[0]][j])

        self.rows[0] += 1
        
        return output

    def goDown(self):

        if ((self.rows[0] >= self.rows[1]) or (self.cols[0] >= self.cols[1])):
            return []

        output = []
        for i in range(self.rows[0], self.rows[1]):
            output.append(self.matrix[i][self.cols[1] - 1])

        self.cols[1] -= 1

        return output

    def goLeft(self):

        if ((self.rows[0] >= self.rows[1]) or (self.cols[0] >= self.cols[1])):
            return []

        output = []
        for j in reversed(range(self.cols[0], self.cols[1])):
            output.append(self.matrix[self.rows[1] - 1][j])

        self.rows[1] -= 1
        
        return output     

    def goUp(self):

        if ((self.rows[0] >= self.rows[1]) or (self.cols[0] >= self.cols[1])):
            return []

        output = []
        for i in reversed(range(self.rows[0], self.rows[1])):
            output.append(self.matrix[i][self.cols[0]])

        self.cols[0] += 1

        return output

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if (len(matrix) == 0):
            return []

        self.matrix = matrix
        self.rows = [0, len(self.matrix)]
        self.cols = [0, len(self.matrix[0])]
        
        output = []
        
        while (self.rows[1] - self.rows[0] > 0) and (self.cols[1] - self.cols[0] > 0):
            output.extend(self.goRight())
            output.extend(self.goDown())
            output.extend(self.goLeft())
            output.extend(self.goUp())

        return output


print(Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 7, 8 ]
]))