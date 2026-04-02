class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        tz=c=0
        for i in nums:
            if i==0:
                c+=1
                tz+=c
            else:
                c=0
        return tz