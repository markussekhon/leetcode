class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            d0, d1 = 0,1

            for i in range(n):
                d0,d1 = d1,d0+d1

        return d1


sol = Solution()
n = 5
print(sol.climbStairs(n))
