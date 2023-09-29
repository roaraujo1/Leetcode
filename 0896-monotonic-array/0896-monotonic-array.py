class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return monoIncreasing(nums) or monoDecreasing(nums)

        

def monoIncreasing(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True
        
    

    
def monoDecreasing(nums):
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            return False
    return True