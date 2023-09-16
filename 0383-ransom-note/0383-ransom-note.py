class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            count[i] = 1+count.get(i,0)
        
        for i in ransomNote:
            if i in count and count[i]>0:
                count[i]-=1
            else:
                return False
        return True
            
