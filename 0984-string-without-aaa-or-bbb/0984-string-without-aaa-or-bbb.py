class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s=""
        while a>0 or b>0:
            if len(s)>=2 and s[-1]==s[-2]:
                if s[-1]=='a':
                    s+='b'
                    b-=1
                else:
                    s+='a'
                    a-=1
            elif a>=b and a>0:
                s+='a'
                a-=1
            else:
                s+='b'
                b-=1
        return s