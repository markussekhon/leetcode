class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):

                if row > 0 and col > 0:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
                elif row > 0:
                    grid[row][col] += grid[row-1][col]
                elif col > 0:
                    grid[row][col] += grid[row][col-1]

        return grid[m-1][n-1]

sol = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(sol.minPathSum(grid))
