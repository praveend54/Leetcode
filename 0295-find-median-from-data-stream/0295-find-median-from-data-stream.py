class MedianFinder:

    def __init__(self):
        self.mf=SortedList()

    def addNum(self, num: int) -> None:
        self.mf.add(num)

    def findMedian(self) -> float:
        n=len(self.mf)
        return (self.mf[n//2]+self.mf[n//2-1])/2 if n%2==0 else self.mf[n//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()