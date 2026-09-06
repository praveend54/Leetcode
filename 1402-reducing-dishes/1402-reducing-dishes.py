class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        s=m=v=satisfaction[-1]
        for i in range(len(satisfaction)-2,-1,-1):
            s+=satisfaction[i]
            v+=s
            if v>m:
                m=v
        return m if m>0 else 0