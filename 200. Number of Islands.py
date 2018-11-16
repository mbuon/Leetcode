# Keep DFSing the island and convert it to # or 0

class Solution:

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        grid = grid
        
        islands = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    self.explore(grid, i, j)

        return islands

    def explore(self, grid, i, j):
        
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or grid[i][j] != "1":
            return

        grid[i][j] = "0"

        self.explore(grid, i-1, j)
        self.explore(grid, i+1, j)
        self.explore(grid, i, j-1)
        self.explore(grid, i, j+1)