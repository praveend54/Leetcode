class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(i,s,track):
            if s==target:
                res.append(track.copy())
                return
            if i==len(candidates) or s>target:
                return
            track.append(candidates[i])
            backtrack(i,s+candidates[i],track)
            track.pop()
            backtrack(i+1,s,track)
        backtrack(0,0,[])
        return res