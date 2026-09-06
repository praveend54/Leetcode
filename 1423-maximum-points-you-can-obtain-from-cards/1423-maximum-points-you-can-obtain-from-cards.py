class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=sum(cardPoints[:k])
        r=0
        res=l
        n=len(cardPoints)
        for i in range(k):
            l-=cardPoints[k-1-i]
            r+=cardPoints[n-1-i]
            res=max(l+r,res)
        return res