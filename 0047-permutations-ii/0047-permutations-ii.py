class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(s,nums,ans):
            if s==len(nums):
                p=[i for i in nums]
                if p not in ans:
                    ans.append(p)
                return
            for i in range(s,len(nums)):
                nums[i],nums[s]=nums[s],nums[i]
                backtrack(s+1,nums,ans)
                nums[i],nums[s]=nums[s],nums[i]
        backtrack(0,nums,ans)
        return ans