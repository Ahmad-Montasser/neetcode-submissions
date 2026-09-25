class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p,l,r = 0,0,1
        while r < len(prices):
            cp = prices[r] - prices[l]
            p = max(p,cp)
            if  prices[l] > prices[r]:
                l=r
            r+=1
        return p
        
        