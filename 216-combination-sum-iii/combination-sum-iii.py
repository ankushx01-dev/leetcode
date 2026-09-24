class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        def solve(last,total,subset):
            if total==n and len(subset)==k:
                result.append(subset.copy())
                return
            if total >n or len(subset)>k:
                return
            for i in range(last,10):
                Sum=total+i
                subset.append(i)
                solve(i+1,Sum,subset)
                subset.pop()
        result=[]
        solve(1,0,[])
        return result