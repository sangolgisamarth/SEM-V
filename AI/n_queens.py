
def is_safe(board,row,col,n):

    """
    Check if placing a queen at (row, col) is safe.
    """
    ## check this column
    for i in range(row):
        if board[i][col]==1:
            return False
        
    # check left diagonal
    for i in range(row):
        for j in range(col):
            if i+j==row + col  and board[i][j]==1 : ##  board[i][j]==1 : already queen is present here 
                return False
            
    ## check right diagonal
    for i in range(row):
        for j in range(col+1,n):
            if i-j == row - col and board[i][j]==1:
                return False
            
    

def solve_n_queen(board,row,n):
    if row==n:
        print_board(board,n)
        return True # Change to False to find all solutions
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queen(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else ".", end=" ")
        print()
    print("\n")


# Driver code
if __name__ == "__main__":
    n = 8
    board = [[0] * n for _ in range(n)]
    solve_n_queen(board, 0, n)

