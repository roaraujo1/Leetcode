class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seen = set()
        
        left = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[r])
            maxLength= max(maxLength,len(seen))
        return maxLength