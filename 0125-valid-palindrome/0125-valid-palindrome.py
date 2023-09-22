class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
       
        left = 0
        right = len(s_lower)-1
        while left <=right:
            if s_lower[left] == s_lower[right]:
                left+=1
                right-=1
            elif not s_lower[left].isalnum():
                left+=1
            elif not s_lower[right].isalnum():
                right-=1
            else:
                return False
        return True
      
        