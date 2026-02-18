class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def backtrack(s):
            if len(s)==n:
                res.append(s)
                return
            backtrack(s+"1")
            if not s or s[-1]!="0":
                backtrack(s+"0")
        backtrack("")
        return res