class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        
        one = 0
        two = 0
        
        while one < len(word1) and two < len(word2):
            res += word1[one] + word2[two]
            one+=1
            two+=1
        
        if one != len(word1):
            res+= word1[one:]
        if two != len(word2):
            res+= word2[two:]
        return res