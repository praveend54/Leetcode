class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if parent[node]!=node:
                parent[node]=find(parent[node])
            return parent[node]
        parent=list(range(len(edges)))
        for i,j in edges:
            p1=find(i-1)
            p2=find(j-1)
            if p1==p2:
                return [i,j]
            parent[p1]=p2