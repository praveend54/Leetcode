class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l=[i for i in range(1,n+1) if n%i==0]
        return l[k-1] if k-1<len(l) else -1