class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count= {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i]+=1
                return True
        return False
        

