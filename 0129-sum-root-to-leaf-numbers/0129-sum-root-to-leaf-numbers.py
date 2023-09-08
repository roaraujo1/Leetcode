# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node,string):
            nonlocal res
            if not node:
                return 
            string+=str(node.val)
            if not node.left and not node.right:
                res+=int(string)
            dfs(node.left,string)
            dfs(node.right,string)
        dfs(root,"")
        return res
                
                
                
        