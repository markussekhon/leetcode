class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for p in prices[1:]:
            if buy > p:
                buy = p
            profit = max(profit, p - buy)

        return profit 
        
sol = Solution()

l = [2,2,2]
print(sol.maxProfit(l))
