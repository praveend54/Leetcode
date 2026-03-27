class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ml=float('inf')
        s=0
        i,j=0,0
        while(j<len(nums)):
            s+=nums[j]
            while(s>=target):
                ml=min(ml,j-i+1)
                s-=nums[i]
                i+=1
            j+=1
        return ml if ml!=float('inf') else 0