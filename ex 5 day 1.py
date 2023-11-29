from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        # Check if the state is valid (no more cannibals than missionaries on either side)
        if self.missionaries < 0 or self.missionaries > 3 or self.cannibals < 0 or self.cannibals > 3:
            return False

        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False

        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False

        return True

    def is_goal(self):
        # Check if the state is the goal state
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return (
            self.missionaries == other.missionaries and
            self.cannibals == other.cannibals and
            self.boat == other.boat
        )

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {self.boat}"

def generate_successors(current_state):
    successors = []

    # Possible actions: (m, c) denotes the number of missionaries and cannibals to move
    actions = [
        (1, 0),  # Move 1 missionary
        (2, 0),  # Move 2 missionaries
        (0, 1),  # Move 1 cannibal
        (0, 2),  # Move 2 cannibals
        (1, 1)   # Move 1 missionary and 1 cannibal
    ]

    for action in actions:
        if current_state.boat == 1:
            # Moving from the initial side to the goal side
            new_state = State(
                current_state.missionaries - action[0],
                current_state.cannibals - action[1],
                0,
                current_state
            )
        else:
            # Moving from the goal side to the initial side
            new_state = State(
                current_state.missionaries + action[0],
                current_state.cannibals + action[1],
                1,
                current_state
            )
        if new_state.is_valid():
            successors.append(new_state)

    return successors

def breadth_first_search(initial_state):
    frontier = deque([initial_state])
    explored = set()

    while frontier:
        current_state = frontier.popleft()

        if current_state.is_goal():
            # Reconstruct the path to the goal
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]

        explored.add(current_state)

        successors = generate_successors(current_state)
        for successor in successors:
            if successor not in explored and successor not in frontier:
                frontier.append(successor)

    return None

def print_solution(path):
    for state in path:
        print(state)
        print("----")

if __name__ == "__main__":
    initial_state = State(3, 3, 1)
    solution_path = breadth_first_search(initial_state)

    if solution_path:
        print("Solution:")
        print_solution(solution_path)
    else:
        print("No solution found.")
