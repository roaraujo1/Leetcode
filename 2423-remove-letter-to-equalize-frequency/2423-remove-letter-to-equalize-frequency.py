class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}
        for i in word:
            freq[i] = 1+ freq.get(i,0)
        
        for k in freq:
            freq[k]-=1
            if equalFreq(freq):
                return True
            freq[k]+=1
        return False
            
def equalFreq(freq):
    Set = set(freq.values())
    if len(Set) == 2 and 0 in Set:
        return True
    return len(Set) ==1
        
        
            
        
        
            