class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i,v in enumerate(nums):
            diff = target-v
            if diff in count:
                return [i,count[diff]]
           
            count[v] = i
