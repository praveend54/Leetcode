class SmallestInfiniteSet:

    def __init__(self):
        self.current=1
        self.heap=[]
        self.addedBack=set()

    def popSmallest(self) -> int:
        if self.heap:
            s=heapq.heappop(self.heap)
            self.addedBack.remove(s)
            return s
        val=self.current
        self.current+=1
        return val

    def addBack(self, num: int) -> None:
        if num<self.current and num not in self.addedBack:
            heapq.heappush(self.heap,num)
            self.addedBack.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)