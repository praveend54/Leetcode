class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        p=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                p+=nums[i]-nums[i-1]
        return p