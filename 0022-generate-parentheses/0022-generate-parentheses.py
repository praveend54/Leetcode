class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        s=""
        def backtrack(res,s,o,c,n):
            if o>n or c>o:
                return
            if o==n and c==n:
                res.append(s)
                return
            backtrack(res,s+"(",o+1,c,n)
            backtrack(res,s+")",o,c+1,n)
        backtrack(res,s,0,0,n)
        return res