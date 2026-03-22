class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m=float('inf')
        e=0
        for i in nums1:
            m=min(m,i)
            if i%2==0:
                e+=1
        if m%2!=0:
            return True
        if e==len(nums1):
            return True
        return False
