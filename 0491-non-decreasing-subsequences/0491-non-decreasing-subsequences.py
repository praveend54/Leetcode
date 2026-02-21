class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(i):
            if i==len(nums):
                if len(path)>=2 and path not in res:
                    res.append(path[:])
                return
            backtrack(i+1)
            if not path or nums[i]>=path[-1]:
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return res