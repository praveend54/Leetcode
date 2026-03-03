# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path=[]
        res=[]
        def backtrack(root,s,path):
            if not root:
                return
            s+=root.val
            path.append(root.val)
            if not root.left and not root.right and s==targetSum:
                res.append(path[:])
            backtrack(root.left,s,path)
            backtrack(root.right,s,path)
            path.pop()
            
        backtrack(root,0,path)
        return res