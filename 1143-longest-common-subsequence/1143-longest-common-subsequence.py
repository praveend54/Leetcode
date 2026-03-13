class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[0]*len(text1)
        l=0
        for c in text2:
            curl=0
            for i,val in enumerate(dp):
                if curl<val:
                    curl=val
                elif c==text1[i]:
                    dp[i]=curl+1
                    l=max(l,curl+1)
        return l