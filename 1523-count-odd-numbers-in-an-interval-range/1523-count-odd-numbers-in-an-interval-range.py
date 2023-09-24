class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high-low+1
        res = length //2
        if length%2 and low%2:
            res+=1
        return res
        