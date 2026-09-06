class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s=0
        c=0
        for i in costs:
            if s+i>coins:
                break
            s+=i
            c+=1
        return c