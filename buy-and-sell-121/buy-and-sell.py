class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left = 0
        right = 1
        profitMax = 0

        while right < len(prices):

            profitCurrent = prices[right] - prices[left]

            if prices[left] < prices[right]:
                profitMax = max(profitCurrent, profitMax)

            else:
                left = right
            
            right += 1
        
        return profitMax

