class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.bit=[0]*(self.n+1)
        self.arr=nums[:]
        for i in range(self.n):
            self.add(i+1,nums[i])
        
    def add(self,i,val):
        while i<=self.n:
            self.bit[i]+=val
            i+=i&-i

    def _sum(self,i):
        s=0
        while i>0:
            s+=self.bit[i]
            i-=i&-i
        return s 

    def update(self, index: int, val: int) -> None:
        d=val-self.arr[index]
        self.arr[index]=val
        self.add(index+1,d)

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right+1)-self._sum(left)