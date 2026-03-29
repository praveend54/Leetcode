class Solution:
    def permuteUnique(self, nums):
        ans = []
        def backtrack(s):
            if s==len(nums):
                ans.append(nums[:])
                return
            used=set()
            for i in range(s,len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[i],nums[s]=nums[s],nums[i]
                backtrack(s+1)
                nums[i],nums[s]=nums[s],nums[i]
        backtrack(0)
        return ans