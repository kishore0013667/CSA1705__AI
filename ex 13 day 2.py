def print_heap(heap):
    print("Heap:", heap)

def is_game_over(heap):
    return sum(heap) == 0

def evaluate_position(heap):
    if sum(heap) % 2 == 1:
        return 1  # Player 1 wins
    else:
        return -1  # Player 2 wins

def valid_moves(heap):
    return [i + 1 for i in range(len(heap)) if heap[i] > 0]

def make_move(heap, move):
    heap[move - 1] -= 1

def minimax(heap, depth, maximizing_player):
    score = evaluate_position(heap)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float("-inf")
        for move in valid_moves(heap):
            heap_copy = list(heap)
            make_move(heap_copy, move)
            eval = minimax(heap_copy, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for move in valid_moves(heap):
            heap_copy = list(heap)
            make_move(heap_copy, move)
            eval = minimax(heap_copy, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(heap):
    best_val = float("-inf")
    best_move = -1

    for move in valid_moves(heap):
        heap_copy = list(heap)
        make_move(heap_copy, move)
        eval = minimax(heap_copy, 0, False)

        if eval > best_val:
            best_move = move
            best_val = eval

    return best_move

def main():
    heap = [3, 5, 7]  # Initial heap configuration

    print("Welcome to Nim!")
    print_heap(heap)

    while not is_game_over(heap):
        # Player 1's move
        player1_move = int(input("Player 1, enter your move (1, 2, or 3): "))
        while player1_move not in valid_moves(heap):
            print("Invalid move. Try again.")
            player1_move = int(input("Player 1, enter your move (1, 2, or 3): "))
        make_move(heap, player1_move)
        print_heap(heap)

        if is_game_over(heap):
            print("Player 1 wins!")
            break

        # Player 2's move (computer)
        player2_move = find_best_move(heap)
        print(f"Player 2 (computer) chooses move {player2_move}")
        make_move(heap, player2_move)
        print_heap(heap)

        if is_game_over(heap):
            print("Player 2 (computer) wins!")
            break

if __name__ == "__main__":
    main()
