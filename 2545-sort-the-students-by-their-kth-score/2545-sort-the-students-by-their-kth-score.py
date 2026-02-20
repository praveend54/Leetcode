class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        res=[]
        for i in range(len(score)):
            l.append((i,score[i][k]))
        l.sort(key=lambda x:x[1],reverse=True)
        for i,s in l:
            res.append(score[i])
        return res