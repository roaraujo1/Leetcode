class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderHash = {}
        for i,v in enumerate(order):
            orderHash[v] = i
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                elif w1[j]!=w2[j]:
                    if orderHash[w2[j]] < orderHash[w1[j]]:
                        return False
                    break
        return True
                
