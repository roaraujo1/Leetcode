class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num
        while n:
            digit = n%10
            print(digit)
            if num%digit == 0:
                count+=1
            n = n//10
        return count