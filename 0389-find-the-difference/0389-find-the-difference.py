class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_t = {}
        
        for i in t:
            if i not in count_t:
                count_t[i] =1
            else:
                count_t[i]+=1
        
        for i in s:
            count_t[i]-=1
        
        for i in count_t:
            if count_t[i] > 0:
                return i
            
            