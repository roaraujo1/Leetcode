class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowInd = {}
        res = [[1]]
        rowInd[0] = res[-1]
        
        for i in range(1,rowIndex+1):
            temp = [0] + res[-1]+[0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
            rowInd[i] = res[-1]
            
        
        for k,v in rowInd.items():
            if k == rowIndex:
                return v
        
       
        