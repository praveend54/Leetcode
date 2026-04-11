class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        m=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    for k in range(j+1,len(nums)):
                        if nums[i]==nums[k]:
                            m=min(m,2*(k-i)) 
        return -1 if m==float('inf') else m