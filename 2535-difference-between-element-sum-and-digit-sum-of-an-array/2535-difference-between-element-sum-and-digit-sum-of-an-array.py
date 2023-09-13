class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digit_sum = 0
        
        for i in nums:
            if i>9:
                digit_sum += self.digitSum(i)
            else:
                 digit_sum+=i
        return abs(elementSum-digit_sum)
    
        
    
    def digitSum(self,n:int)->int:
        res = 0
        while n>0:
            digit= n%10
            res+=digit
            n = n//10
        return res 
        
            
            
        
    
    
    
                