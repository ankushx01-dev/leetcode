class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def solve(index,total,subset,result,nums):
            if total==0:
                result.append(subset.copy())
                return
            elif total < 0:
                return 
            elif index>=len(nums):
                return
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                Sum=total-nums[i]
                solve(i+1,Sum,subset,result,nums)
                subset.pop()
        result=[]
        candidates.sort()
        solve(0,target,[],result,candidates)
        return result
