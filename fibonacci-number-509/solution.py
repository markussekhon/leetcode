class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return n

        elif n == 1:
            return n

        return self.fib(n-1) + self.fib(n-2)

sol = Solution()
n = 4
print(sol.fib(n))
