# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node == None:
                return 0
            if low <= node.val <=high:
                res+=node.val
            
            dfs(node.left)
            dfs(node.right)
            return res
        return dfs(root)
    
        