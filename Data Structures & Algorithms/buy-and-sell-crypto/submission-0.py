class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minstock=prices[0]
        maxprofit=0
        for ch in prices:
            if ch <minstock:
                minstock=ch
            profit=ch-minstock

            maxprofit=max(profit,maxprofit)
        return maxprofit