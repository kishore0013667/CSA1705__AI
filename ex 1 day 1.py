from collections import deque

class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

def get_blank_location(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    i, j = get_blank_location(node.state)
    neighbors = []

    # Define legal moves (up, down, left, right)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for move in moves:
        ni, nj = i + move[0], j + move[1]
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, node, move))

    return neighbors

def is_goal_state(state):
    return state == goal_state

def solve_8_puzzle_bfs(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = deque([initial_node])
    explored = set()

    while frontier:
        current_node = frontier.popleft()
        if is_goal_state(current_node.state):
            return build_solution(current_node)

        explored.add(tuple(map(tuple, current_node.state)))

        for neighbor in get_neighbors(current_node):
            if tuple(map(tuple, neighbor.state)) not in explored:
                frontier.append(neighbor)

    return None

def build_solution(node):
    solution = []
    while node:
        solution.insert(0, (node.state, node.action))
        node = node.parent
    return solution[1:]

# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = solve_8_puzzle_bfs(initial_state)

if solution:
    for step, (state, action) in enumerate(solution):
        print(f"Step {step + 1}: {action}")
        for row in state:
            print(row)
        print("\n")
else:
    print("No solution found.")
