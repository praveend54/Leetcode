class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d={j:i for i,j in enumerate(nums)}
        for i,j in operations:
            ind=d[i]
            nums[ind]=j
            del d[i]
            d[j]=ind
        return nums