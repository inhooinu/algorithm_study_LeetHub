class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        for i in range(len(prices)-1):
            buy = prices[i]
            sell = max(prices[i+1:])
            if buy < sell:
                max_profit = max(max_profit, (sell-buy))
        
        return max_profit