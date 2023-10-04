class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count = {}

        for i in word1:
            count[i] = 1+count.get(i,0)
     
        
        for i in word2:
            if i not in word1:
                count[i] = 1+count.get(i,0)
                
            else:
                count[i] -=1
        
        for i in count.values():
            if abs(i) > 3:
                return False
        return True