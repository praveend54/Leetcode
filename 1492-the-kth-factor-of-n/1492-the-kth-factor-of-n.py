class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f=[]
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                k-=1
                if k==0: return i
                if i*i!=n:
                    f.append(n//i)
        return f[-k] if k<=len(f) else -1