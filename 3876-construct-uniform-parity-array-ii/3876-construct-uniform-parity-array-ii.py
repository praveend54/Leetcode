class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        s=min(nums1)
        if s%2==1:
            return True
        for i in nums1:
            if i%2==1:
                return False
        return True
