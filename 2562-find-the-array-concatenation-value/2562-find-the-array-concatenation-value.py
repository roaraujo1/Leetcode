class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        output = 0 
        left = 0
        
        while nums:
            if len(nums)==1:
                output+= nums.pop()
            else:
                temp = int(str(nums.pop(left)) + str(nums.pop()))
                output+=temp
            
        return output