class Solution:
    def largestOddNumber(self, num: str) -> str:
        maxValue = ""
       
        for i in range(len(num)-1,-1,-1):
            if isOdd(int(num[i])):
                return num[:i+1]
        return ""
           


def isOdd(number):
    if number%2:
        return number