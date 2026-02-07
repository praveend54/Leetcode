class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n=len(grid)
        m=len(grid[0])
        c=0
        def dfs(grid,i,j):
            if i<0 or j<0 or i>n-1 or j>m-1 or grid[i][j]=="0":
                return 
            grid[i][j]="0"
            dfs(grid,i+1,j)
            dfs(grid,i,j+1)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    c+=1
                    dfs(grid,i,j)
        def dfs(grid,i,j):
            if i<0 or j<0 or i>n-1 or j>m-1 or grid[i][j]=="0":
                return 
            grid[i][j]="0"
            dfs(grid,i+1,j)
            dfs(grid,i,j+1)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
        return c