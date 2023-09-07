class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = 1
        i = 2
        
        while i<len(nums):
            if nums[prev-1] == nums[prev]==nums[i]:
                nums.pop(prev-1)
            else:
                prev = i
                i+=1
        return len(nums)
                    
        
        