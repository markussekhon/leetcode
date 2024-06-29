class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profitMax = 0
        left = 0
        right = 1

        while right < len(prices):

            if prices[left] < prices[right]:
                profitMax = max(profitMax, prices[right] - prices[left])
            else:
                left = right

            right += 1

        return profitMax
