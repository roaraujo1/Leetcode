class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxCount = 0
        
        for i in sentences:
            temp = 0
            for j in i.split():
                temp+=1
            maxCount = max(temp,maxCount)      
        return maxCount
        