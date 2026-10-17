class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        maxi=0
        left=0
        right=0
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        for i in range(0,k):
            left+=cardPoints[i]
        maxi=left
        right_idx=n-1
        for i in range(k-1,-1,-1):
            left-=cardPoints[i]
            right+=cardPoints[right_idx]
            maxi=max(maxi,left+right)
            right_idx-=1
        return maxi
            