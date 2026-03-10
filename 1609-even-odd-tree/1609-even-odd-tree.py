# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        l=0
        while q:
            n=len(q)
            if l%2==0:
                p=float('-inf')
            else:
                p=float('inf')
            for _ in range(n):
                node=q.popleft()
                v=node.val
                if l%2==0:
                    if v%2==0 or v<=p:
                        return False
                else:
                    if v%2!=0 or v>=p:
                        return False
                p=v
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l+=1
        return True