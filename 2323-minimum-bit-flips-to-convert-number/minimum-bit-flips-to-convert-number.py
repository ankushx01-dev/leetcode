class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        count=0
        for x in range(0,32):
            if ans&(1<<x)!=0:
                count+=1
        return count
        
        