class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        ts=sum(sum(i) for i in grid)
        rs,cs=0,0
        for i in range(n):
            rs+=sum(grid[i])
            if ts-rs==rs:
                return True
        for i in range(m):
            s=0
            for j in range(n):
                s+=grid[j][i]
            cs+=s
            if ts-cs==cs:
                return True
        return False