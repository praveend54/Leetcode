# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            lev=[]
            for _ in range(n):
                node=queue.popleft()
                lev.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            r.append(lev[-1])
        return r
