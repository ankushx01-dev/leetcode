class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def solve(index,total,subset,nums,target,result):
            if total==target:
                result.append(subset.copy())
                return
            elif total>target:
                return
            if index>=len(nums):
                return
            Sum=total+nums[index]
            subset.append(nums[index])
            solve(index,Sum,subset,nums,target,result)
            subset.pop()
            Sum=total
            solve(index+1,Sum,subset,nums,target,result)

        result=[]
        subset=[]
        solve(0,0,subset,candidates,target,result)
        return result