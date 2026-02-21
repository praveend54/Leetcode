class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(st):
            if len(path)>=2:
                res.append(path[:])
            s=set()
            for i in range(st,len(nums)):
                if nums[i] in s:
                    continue
                if not path or nums[i]>=path[-1]:
                    s.add(nums[i])
                    path.append(nums[i])
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return res