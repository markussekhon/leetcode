class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        if len(cost) == 2:
            return min(cost[0],cost[1])

        for index in range(2,len(cost)):
            cost[index] += min(cost[index-1],cost[index-2])

        return min(cost[len(cost)-1],cost[len(cost)-2])

sol = Solution()
cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs(cost1))
print(sol.minCostClimbingStairs(cost2))
