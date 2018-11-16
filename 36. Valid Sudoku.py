class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        cols = {}
        blocks = {}

        for i in range(0, len(board)):
         
          for j in range(0, len(board)):
                
            value = board[i][j]

            if i not in rows:
              rows[i] = {}

            if j not in cols:
              cols[j] = {}

            if (i%3 == 0 and j%3 == 0):
              if (i/3, j/3) not in blocks:
                blocks[i/3, j/3] = {}

            if (board[i][j] == "."):
                continue
                
            if ((value in rows[i]) or (value in cols[j]) or (value in blocks[int(i/3), int(j/3)])):
              return False
            
            rows[i][value] = True
            cols[j][value] = True
            blocks[int(i/3), int(j/3)][value] = True
            
        return True

print(Solution().isValidSudoku([
  [".",".","4",".",".",".","6","3","."],
  [".",".",".",".",".",".",".",".","."],
  ["5",".",".",".",".",".",".","9","."],
  [".",".",".","5","6",".",".",".","."],
  ["4",".","3",".",".",".",".",".","1"],
  [".",".",".","7",".",".",".",".","."],
  [".",".",".","5",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."]]))