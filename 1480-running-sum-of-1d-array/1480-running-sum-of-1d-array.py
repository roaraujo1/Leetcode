class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        for i,v in enumerate(nums):
            curr+=v
            if i != 0:
                nums[i] = curr
        return nums
            
            
            