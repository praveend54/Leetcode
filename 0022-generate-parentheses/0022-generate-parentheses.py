class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        s=""
        def backtrack(s,o,c,n):
            if o>n or c>o:
                return
            if o==n and c==n:
                res.append(s)
                return
            backtrack(s+"(",o+1,c,n)
            backtrack(s+")",o,c+1,n)
        backtrack(s,0,0,n)
        return res