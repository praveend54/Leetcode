class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n):
            s=s+'1'+(''.join(['1' if i == '0' else '0' for i in s]))[::-1]
        return s[k-1]