class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i<j and nums[i]== nums[j]:
                    res+=1
        return res
                    
            