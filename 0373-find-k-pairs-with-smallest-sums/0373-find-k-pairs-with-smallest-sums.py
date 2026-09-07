class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res=[]
        hm=[]
        for j in range(min(len(nums2),k)):
            heapq.heappush(hm,(nums1[0]+nums2[j],0,j))
        while hm and len(res)<k:
            cs,i,j=heapq.heappop(hm)
            res.append([nums1[i],nums2[j]])
            if i+1<len(nums1):
                heapq.heappush(hm,(nums1[i+1]+nums2[j],i+1,j))
        return res