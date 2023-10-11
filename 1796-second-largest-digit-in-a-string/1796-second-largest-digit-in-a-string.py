class Solution:
    def secondHighest(self, s: str) -> int:
        mySet = set()
        
        for i in s:
            if not i.isalpha() :
                mySet.add(int(i))
        arr = list(mySet)
        arr.sort()
        if len(arr)<=1:
            return -1
        count = 0
        for i in range(len(arr)-1,-1,-1):
            count+=1
            if count ==2:
                return arr[i]
            