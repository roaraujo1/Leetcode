class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProf = 0
        while right <= len(prices)-1:
            if prices[left] >= prices[right]:
                left=right
            else:
                maxProf = max(maxProf,prices[right]-prices[left])
            right+=1
        return maxProf

