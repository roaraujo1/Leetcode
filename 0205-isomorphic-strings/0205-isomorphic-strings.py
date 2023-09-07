class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST,mapTS = {},{}
        
        for i in range(len(s)):
            one = s[i]
            two = t[i]
            
            if (one in mapST and mapST[one]!=two ) or (two in mapTS and mapTS[two]!=one):
                return False
            mapST[one] = two
            mapTS[two]=one
            
            
            
        return True