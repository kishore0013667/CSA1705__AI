import math

EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROWS = 6
COLS = 7

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid_move(board, col):
    return board[0][col] == EMPTY

def make_move(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return True
    return False

def evaluate_window(window, player):
    score = 0
    opponent = PLAYER_1 if player == PLAYER_2 else PLAYER_2

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def evaluate_position(board, player):
    score = 0

    # Evaluate horizontally
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = board[row][col:col+4]
            score += evaluate_window(window, player)

    # Evaluate vertically
    for row in range(ROWS - 3):
        for col in range(COLS):
            window = [board[row+i][col] for i in range(4)]
            score += evaluate_window(window, player)

    # Evaluate diagonally (from bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row-i][col+i] for i in range(4)]
            score += evaluate_window(window, player)

    # Evaluate diagonally (from top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row+i][col+i] for i in range(4)]
            score += evaluate_window(window, player)

    return score

def is_terminal_node(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal_node(board):
        return evaluate_position(board, PLAYER_2)

    if maximizing_player:
        max_eval = -math.inf
        for col in range(COLS):
            if is_valid_move(board, col):
                board_copy = [row[:] for row in board]
                make_move(board_copy, col, PLAYER_2)
                eval = alpha_beta_pruning(board_copy, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for col in range(COLS):
            if is_valid_move(board, col):
                board_copy = [row[:] for row in board]
                make_move(board_copy, col, PLAYER_1)
                eval = alpha_beta_pruning(board_copy, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board, depth):
    best_val = -math.inf
    best_move = -1

    for col in range(COLS):
        if is_valid_move(board, col):
            board_copy = [row[:] for row in board]
            make_move(board_copy, col, PLAYER_2)
            eval = alpha_beta_pruning(board_copy, depth - 1, -math.inf, math.inf, False)
            if eval > best_val:
                best_move = col
                best_val = eval

    return best_move

def main():
    board = [[EMPTY] * COLS for _ in range(ROWS)]

    while True:
        print_board(board)

        # Player 1's move
        player1_col = int(input("Player 1, enter your move (0-6): "))
        while not is_valid_move(board, player1_col):
            print("Invalid move. Try again.")
            player1_col = int(input("Player 1, enter your move (0-6): "))
        make_move(board, player1_col, PLAYER_1)

        print_board(board)

        if evaluate_position(board, PLAYER_1) >= 100:
            print("Player 1 wins!")
            break

        # Player 2's move (computer)
        player2_col = find_best_move(board, depth=4)
        print(f"Player 2 (computer) chooses column {player2_col}")
        make_move(board, player2_col, PLAYER_2)

        if evaluate_position(board, PLAYER_2) <= -100:
            print("Player 2 (computer) wins!")
            break

if __name__ == "__main__":
    main()
