# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        def insert(l,r):
            if l>r:
                return None
            m=(l+r)//2
            node=TreeNode(res[m])
            node.left=insert(l,m-1)
            node.right=insert(m+1,r)
            return node
        return insert(0,len(res)-1)