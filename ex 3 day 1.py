class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def water_jug_dfs(capacity_jug1, capacity_jug2, target):
    visited = set()

    def dfs(state):
        if state.jug1 == target or state.jug2 == target:
            return [state]

        visited.add(state)

        next_states = []
        
        # Fill jug 1
        if state.jug1 < capacity_jug1:
            next_state = State(capacity_jug1, state.jug2)
            if next_state not in visited:
                next_states.extend(dfs(next_state))

        # Fill jug 2
        if state.jug2 < capacity_jug2:
            next_state = State(state.jug1, capacity_jug2)
            if next_state not in visited:
                next_states.extend(dfs(next_state))

        # Empty jug 1
        if state.jug1 > 0:
            next_state = State(0, state.jug2)
            if next_state not in visited:
                next_states.extend(dfs(next_state))

        # Empty jug 2
        if state.jug2 > 0:
            next_state = State(state.jug1, 0)
            if next_state not in visited:
                next_states.extend(dfs(next_state))

        # Pour water from jug 1 to jug 2
        pour_amount = min(state.jug1, capacity_jug2 - state.jug2)
        if pour_amount > 0:
            next_state = State(state.jug1 - pour_amount, state.jug2 + pour_amount)
            if next_state not in visited:
                next_states.extend(dfs(next_state))

        # Pour water from jug 2 to jug 1
        pour_amount = min(state.jug2, capacity_jug1 - state.jug1)
        if pour_amount > 0:
            next_state = State(state.jug1 + pour_amount, state.jug2 - pour_amount)
            if next_state not in visited:
                next_states.extend(dfs(next_state))

        return [state] + next_states

    initial_state = State(0, 0)
    solution_path = dfs(initial_state)

    return solution_path

def print_solution_path(solution_path):
    for step, state in enumerate(solution_path):
        print(f"Step {step}: Jug 1 = {state.jug1}, Jug 2 = {state.jug2}")

# Example usage:
capacity_jug1 = 4
capacity_jug2 = 3
target_amount = 2

solution_path = water_jug_dfs(capacity_jug1, capacity_jug2, target_amount)

if solution_path[-1].jug1 == target_amount or solution_path[-1].jug2 == target_amount:
    print("Solution found:")
    print_solution_path(solution_path)
else:
    print("No solution found.")
