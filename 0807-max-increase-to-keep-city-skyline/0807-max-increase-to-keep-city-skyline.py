class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        res=0
        for i in range(n):
            for j in range(m):
                a=grid[i][j]
                r=c=0
                for k in range(n):
                    r=max(grid[k][j],r)
                for k in range(m):
                    c=max(grid[i][k],c)
                if a==max(r,c):
                    continue
                res+=min(r,c)-grid[i][j]
        return res