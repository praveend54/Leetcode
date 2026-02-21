class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.m=maxSize

    def push(self, x: int) -> None:
        if len(self.stack)<self.m:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            mi=min(k,len(self.stack))
            for i in range(mi):
                self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)