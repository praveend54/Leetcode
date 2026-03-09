class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        prev=[0]*len(nums)
        for i in range(1,len(nums)):
            prev[i]=prev[i-1]+nums[i-1]
        suf=1
        for i in range(len(nums)-1,-1,-1):
            if i<len(nums)-1:
                suf*=nums[i+1]
            if prev[i]==suf:
                return i
        return -1