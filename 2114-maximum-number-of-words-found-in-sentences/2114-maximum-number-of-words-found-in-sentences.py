class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxCount = 0
        
        for i in sentences:
            maxCount = max(maxCount,len(i.split()))      
        return maxCount
        