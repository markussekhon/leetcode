class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        map = [[0]*n for _ in range(m)]
        map[0][0] = 1

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    map[row][col] = 0
                else:
                    if row > 0:
                        map[row][col] += map[row-1][col]
                    if col > 0:
                        map[row][col] += map[row][col-1]


        return map[m-1][n-1]


sol = Solution()
grid = [[0,0,0],[0,1,0],[0,0,0]]
print(sol.uniquePathsWithObstacles(grid))
