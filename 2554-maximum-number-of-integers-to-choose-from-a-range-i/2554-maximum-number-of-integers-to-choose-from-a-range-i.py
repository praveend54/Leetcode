class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        c=0
        s=0
        for i in range(1,n+1):
            if i in banned:
                continue
            s+=i
            if s>maxSum:
                break
            c+=1
        return c