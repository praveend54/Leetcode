class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        res=[]
        def backtrack(i,comb):
            if i==len(digits):
                res.append(comb[:])
                return 
            for let in l[digits[i]]:
                backtrack(i+1,comb+let)
        backtrack(0,"")
        return res