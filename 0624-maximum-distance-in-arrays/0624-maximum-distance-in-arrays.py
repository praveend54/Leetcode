class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        gmi=arrays[0][0]
        gma=arrays[0][-1]
        maxd=0
        for i in range(1,len(arrays)):
            maxd=max(maxd,arrays[i][-1]-gmi,gma-arrays[i][0])
            gmi=min(gmi,arrays[i][0])
            gma=max(gma,arrays[i][-1])
        return maxd   