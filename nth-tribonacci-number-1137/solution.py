class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        t0, t1, t2 = 0, 1, 1

        for iter in range(n):
            t0, t1, t2 = t1, t2, t0+t1+t2

        return t0

sol = Solution()
n = 25
print(sol.tribonacci(n))
