class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(i,s,path):
            if s==target:
                res.append(list(path))
                return
            if i==len(candidates) or s>target:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if s+candidates[j]>target:
                    break
                path.append(candidates[j])
                backtrack(j+1,s+candidates[j],path)
                path.pop()
        backtrack(0,0,[])
        return res