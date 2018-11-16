class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        _maxProfit = 0
        cliff = max(prices)

        for i in range(0, len(prices)):
        	cliff = min(prices[i], cliff)
        	_maxProfit = max(_maxProfit, (prices[i] - cliff))

        return _maxProfit

prices = [7,1]
S = Solution()
print(S.maxProfit(prices))