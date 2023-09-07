class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      
        i=1
        prev = 0
        while i<len(nums):
            if nums[prev]==nums[i]:
                nums.pop(prev)
            else:
                prev= i
                i+=1
        return len(nums)
        