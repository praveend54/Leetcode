# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        c=0
        q=deque([root])
        while q:
            n=len(q)
            path=[]
            if c%2==0:
                for i in range(n):
                    node=q.popleft()
                    path.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            else:
                for i in range(n):
                    node=q.popleft()
                    path.insert(0,node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(path[:])
            c+=1
        return  res


                        