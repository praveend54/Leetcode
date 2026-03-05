class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res=[]
        g={}
        for i,s in enumerate(groupSizes):
            if s not in g:
                g[s]=[]
            g[s].append(i)
            if len(g[s])==s:
                res.append(g[s])
                g[s]=[]
        return res