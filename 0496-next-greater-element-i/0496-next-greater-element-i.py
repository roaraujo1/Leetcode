class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indNum1 = {v:i for i,v in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack = []


        for i in nums2:
            while stack and i > stack[-1]:
                val = stack.pop()
                index = indNum1[val]
                res[index] = i
            if i in nums1:
                stack.append(i)
        return res
     

        