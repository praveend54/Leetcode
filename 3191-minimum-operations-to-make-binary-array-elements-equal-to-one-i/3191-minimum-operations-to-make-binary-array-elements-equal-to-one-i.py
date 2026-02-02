class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        i=2
        while i<len(nums):
            if nums[i-2]==0:
                nums[i-2]^=1
                nums[i-1]^=1
                nums[i]^=1
                c+=1
            i+=1
        return c if 0 not in nums else -1