

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        L = len(prices)
        if L == 1: return 0
        lidx = 0
        ridx = 1
        max_ = 0
        while ridx < L:
            profit = prices[ridx] - prices[lidx]
            if profit < 0:
                lidx, ridx = ridx, ridx+1
            else:
                max_ = max(profit, max_)
                ridx+=1
        return max_
                

