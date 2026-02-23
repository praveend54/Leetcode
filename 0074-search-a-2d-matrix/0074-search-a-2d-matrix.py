class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        m, n = len(nums), len(nums[0])
        l, r = 0, m*n - 1
        while l <= r:
            mid = (l + r) // 2
            value = nums[mid // n][mid % n]
            if value == target:
                return True
            elif value < target:
                l = mid + 1
            else:
                r = mid - 1
        return False