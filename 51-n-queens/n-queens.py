class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def solve(col,board,ans,leftrow,upperDiagnal,lowerDiagnal,n):
            if col==n:
                ans.append(board[:])
                return
            for row in range(n):
                if (
                    leftrow[row]==0
                    and lowerDiagnal[row+col]==0
                    and upperDiagnal[n-1+col-row]==0
                ):
                    board[row]=board[row][:col]+"Q"+board[row][col +1 :]
                    leftrow[row]=1
                    lowerDiagnal[row+col]=1
                    upperDiagnal[n-1+col-row]=1

                    solve(col+1,board,ans,leftrow,upperDiagnal,lowerDiagnal,n)
                    board[row]=board[row][:col]+"."+board[row][col +1 :]
                    leftrow[row]=0
                    lowerDiagnal[row+col]=0
                    upperDiagnal[n-1+col-row]=0
        ans=[]
        board=["."*n for _ in range(n)]
        leftrow=[0]*n
        upperDiagnal=[0]*(2*n -1)
        lowerDiagnal=[0]*(2*n -1)
        solve(0,board,ans,leftrow,upperDiagnal,lowerDiagnal,n)
        return ans