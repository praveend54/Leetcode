class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c=0
        for i in s:
            if i=='0':
                break
            c+=1
        if c==len(s):
            return True
        for i in s[c:]:
            if i=='1':
                return False
        return True