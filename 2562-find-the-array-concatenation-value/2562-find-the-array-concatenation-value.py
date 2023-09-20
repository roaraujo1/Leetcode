class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        output = 0 
        left = 0
        
        while nums:
            if len(nums)==1:
                output+= nums.pop()
            else:
                temp = int(str(nums[left]) + str(nums[-1]))
                output+=temp
                nums.pop(left)
                nums.pop()
        return output