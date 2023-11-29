def is_safe(board, row, col):
    # Check if there is a queen in the same row
    if any(board[row]):
        return False

    # Check if there is a queen in the same column
    if any(board[i][col] for i in range(8)):
        return False

    # Check if there is a queen in the same diagonals
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))) or \
       any(board[i][j] for i, j in zip(range(row, 8), range(col, -1, -1))):
        return False

    return True

def solve_queens(board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_queens(board, row + 1):
                return True
            board[row][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def solve_8_queens():
    board = [[0] * 8 for _ in range(8)]
    if solve_queens(board, 0):
        print("Solution found:")
        print_solution(board)
    else:
        print("No solution found.")

# Example usage:
solve_8_queens()
