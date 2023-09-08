class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = {}
        
        
        for i,v in enumerate(nums):
            if v in found and abs(i-found[v]) <=k:
                return True
            found[v] = i
        return False
            
    
        