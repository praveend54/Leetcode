class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        a=nums.index(max(nums))
        b=nums.index(min(nums))
        a,b=max(a,b),min(a,b)
        ff=a+1
        bb=n-b
        fb=b+n-a+1
        return min(ff,bb,fb)