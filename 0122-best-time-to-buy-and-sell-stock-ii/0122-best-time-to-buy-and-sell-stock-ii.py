class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf =0 
        
        buy = 0
        sell = 1
        
        while sell <len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                maxProf+= prices[sell] - prices[buy]
                buy=sell
            sell+=1
        return maxProf
        