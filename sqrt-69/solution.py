class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x <= 0:
            return 0

        l,r = 1, x
        midpoint = lambda low, high : low + (high - low)//2
        m = midpoint(l,r)

        while l != m:
            val = m*m

            if x > val:
                l = m
            elif x < val:
                r = m
            else:
                return m

            m = midpoint(l,r)

        return m

sol = Solution()
x = 8
print(sol.mySqrt(x))
