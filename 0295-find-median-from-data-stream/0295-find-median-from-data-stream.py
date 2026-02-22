class MedianFinder:

    def __init__(self):
        self.minH=[]
        self.maxH=[]

    def addNum(self, num: int) -> None:
        heappush(self.maxH,-num)
        heappush(self.minH,-heappop(self.maxH))
        if len(self.minH)>len(self.maxH):
            heappush(self.maxH,-heappop(self.minH))

    def findMedian(self) -> float:
        if len(self.maxH)>len(self.minH):
            return -self.maxH[0]
        return (-self.maxH[0]+self.minH[0])/2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()