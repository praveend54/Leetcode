class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        for e in prerequisites:
            adj[e[0]].append(e[1])
        visited=[False]*numCourses
        rec=[False]*numCourses
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
            return False
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True
        