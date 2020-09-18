class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in xrange(1,n):
            tmp = dp0
            dp0 = max(dp0,dp1+prices[i])
            dp1 = max(dp1,tmp-prices[i])
        return max(dp0,0)