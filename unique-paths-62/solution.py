class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1

        map = [[0 for _ in range(n)] for _ in range(m)]
        map[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    map[i][j] += map[i-1][j]
                if j > 0:
                    map[i][j] += map[i][j-1]

        return map[m-1][n-1]



sol = Solution()
m,n = 18,18
print(sol.uniquePaths(m,n))
