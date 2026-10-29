class Solution:
    def jump(self, nums: list[int]) -> int:
        jump=0
        l=0
        r=0
        while r<len(nums)-1:
            f=0
            for i in range(l,r+1):
                f=max(f,i+nums[i])
            l=r+1
            r=f
            jump+=1
        return jump
