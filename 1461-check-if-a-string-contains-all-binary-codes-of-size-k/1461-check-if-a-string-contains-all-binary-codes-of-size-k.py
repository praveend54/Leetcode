class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l=set()
        for i in range(len(s)+1-k):
            l.add(s[i:i+k])
        return len(l)==2**k