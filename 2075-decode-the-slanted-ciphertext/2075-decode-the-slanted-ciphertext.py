class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows==1:
            return encodedText
        cols=len(encodedText)//rows
        i=j=k=0
        l=[]
        while k<len(encodedText):
            l.append(encodedText[k])
            i+=1
            if i==rows:
                i=0
                j+=1
            k=i*(cols+1)+j
        return ''.join(l).rstrip()