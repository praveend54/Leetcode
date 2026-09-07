class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n=len(grid2)
        m=len(grid2[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or grid2[i][j]==0:
                return True
            p=(grid2[i][j]==grid1[i][j])
            grid2[i][j]=0
            d1 = dfs(i+1, j)
            d2 = dfs(i-1, j)
            d3 = dfs(i, j+1)
            d4 = dfs(i, j-1)
            return p and d1 and d2 and d3 and d4
        c=0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1:
                    if dfs(i,j):
                        c+=1
        return c