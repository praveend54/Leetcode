class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        s=-1
        e=-1
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                s=m
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                e=m
                l=m+1
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return [s,e]