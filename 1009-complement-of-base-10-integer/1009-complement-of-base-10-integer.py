class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=bin(n)[2:]
        res=""
        for c in s:
            res+='0' if c=='1' else '1'
        return int(res,2)