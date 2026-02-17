class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        path=[]
        def backtrack(i):
            if i==len(nums):
                if path[:] not in res:
                    res.append(path[:])
                return
            backtrack(i+1)
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
        backtrack(0)
        return res