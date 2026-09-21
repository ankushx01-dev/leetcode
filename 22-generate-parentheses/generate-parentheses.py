class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def solve(index,total,bracket,result):
            if index>=len(brackets):
                if total==0:
                    result.append("".join(brackets))
                return
            if total>len(brackets)//2:
                return
            elif total<0:
                return
            brackets[index]="("
            sum=total+1
            solve(index+1,sum,brackets,result)
            brackets[index]=")"
            sum=total-1
            solve(index+1,sum,brackets,result)

        result=[]
        brackets=[""]*(n*2)
        solve(0,0,brackets,result)
        return result
        