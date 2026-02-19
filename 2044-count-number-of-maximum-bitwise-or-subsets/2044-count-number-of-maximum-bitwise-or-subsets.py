class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.m=0
        for i in nums:
            self.m|=i
        self.c=0
        def backtrack(i,curo):
            if i==len(nums):
                if self.m==curo:
                    self.c+=1
                return
            backtrack(i+1,curo)
            backtrack(i+1,curo|nums[i])
        backtrack(0,0)
        return self.c