class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows_loc = {}
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]

        for i in range(len(rows)):
            for j in rows[i]:
                rows_loc[j] = i+1
       
        res = []

        for i in range(len(words)):
            ro = 0
            temp = ""
            for j in words[i].lower():
                if ro == 0:
                    ro = rows_loc[j]
                    temp+=j
                elif rows_loc[j] != ro:
                    break
                else:
                    temp+=j
               
            if len(temp) == len(words[i]):
                res.append(words[i])
        return res 

        
