class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack= []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack and i in pairs.values():
                    stack.append(i)
                else:
                    if pairs[i] != stack.pop():
                        return False
        if stack:
            return False
        return True
