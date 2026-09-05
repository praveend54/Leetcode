class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        for s,d in prerequisites:
            adj[s].append(d)
        visited=[False]*numCourses
        rec=[False]*numCourses
        res=[]
        def dfs(u):
            if rec[u]:
                return True
            if visited[u]:
                return False
            visited[u]=True
            rec[u]=True
            for v in adj[u]:
                if dfs(v):
                    return True
            rec[u]=False
            res.append(u)
            return False
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        return res