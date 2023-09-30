class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i,v in enumerate(nums):
            diff = target-v
            if diff in seen:
                return [i,seen[diff]]
            seen[v] = i
            