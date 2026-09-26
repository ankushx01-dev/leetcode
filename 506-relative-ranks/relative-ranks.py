class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score=sorted(score,reverse=True)
        num={}
        for i in range(len(sorted_score)):
            if i==0:
                num[sorted_score[i]]= "Gold Medal"
            elif i==1:
                num[sorted_score[i]]="Silver Medal"
            elif i==2:
                num[sorted_score[i]]="Bronze Medal"
            else:
                num[sorted_score[i]]=str(i+1)
        return [num[x] for x in score]
