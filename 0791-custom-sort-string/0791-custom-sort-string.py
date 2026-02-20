class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cc={c:0 for c in order}
        for c in s:
            if c in cc:
                cc[c]+=1
        ss=""
        for c in order:
            ss+=c*cc[c]
        for c in s:
            if c not in order:
                ss+=c
        return ss