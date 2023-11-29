import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def a_star(start, goal, graph, heuristic):
    open_set = [Node(start, None, 0, heuristic(start, goal))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]:
            if neighbor not in closed_set:
                new_cost = current_node.cost + cost
                new_node = Node(neighbor, current_node, new_cost, heuristic(neighbor, goal))
                
                if new_node not in open_set:
                    heapq.heappush(open_set, new_node)

    return None

# Example usage
if __name__ == "__main__":
    # Define a simple graph as an adjacency list
    graph = {
        'A': [('B', 5), ('C', 2)],
        'B': [('D', 4)],
        'C': [('D', 7)],
        'D': [('E', 3)],
        'E': []
    }

    # Define a heuristic function (in this case, Euclidean distance)
    def heuristic(node, goal):
        return abs(ord(node) - ord(goal))

    start_node = 'A'
    goal_node = 'E'

    path = a_star(start_node, goal_node, graph, heuristic)

    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path}")
    else:
        print("No path found.")
