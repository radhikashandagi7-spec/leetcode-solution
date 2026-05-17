def is_safe(board,row,col):
    for r in range(row):
        if board[r]==col or abs(board[r]-col)==abs(r-row):
            return False 
    return True
def solve(board,row,n):
    if row==n:
        print(board)
        return True
    for col in range(n):
        if is_safe(board,row,col):
            board[row]=col
            if solve(board,row+1,n):
                return True
        board[row]=-1
    return False
n=4
board=[-1]*n
solve(board,0,n)