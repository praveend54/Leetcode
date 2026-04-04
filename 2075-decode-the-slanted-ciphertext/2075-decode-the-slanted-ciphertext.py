class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows==1:
            return encodedText
        cols=len(encodedText)//rows
        s=""
        l=[]
        for c in range(cols):
            r,j=0,c
            while r<rows and j<cols:
                l.append(encodedText[r*cols+j])
                r+=1
                j+=1
        return "".join(l).rstrip()