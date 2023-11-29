def is_valid_assignment(variable, value, assignment, graph):
    for neighbor in graph[variable]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def backtracking_search(assignment, variables, domain, graph):
    if len(assignment) == len(variables):
        return assignment  # Solution found

    variable = select_unassigned_variable(assignment, variables)
    for value in order_domain_values(variable, assignment, domain):
        if is_valid_assignment(variable, value, assignment, graph):
            assignment[variable] = value
            result = backtracking_search(assignment, variables, domain, graph)
            if result:
                return result
            del assignment[variable]
    return None

def select_unassigned_variable(assignment, variables):
    for variable in variables:
        if variable not in assignment:
            return variable

def order_domain_values(variable, assignment, domain):
    return domain[variable]

if __name__ == "__main__":
    # Example Map Coloring problem
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }

    variables = list(graph.keys())
    domain = {variable: ['Red', 'Green', 'Blue'] for variable in variables}
    
    assignment = backtracking_search({}, variables, domain, graph)

    if assignment:
        print("Map Coloring Solution:")
        for variable, value in assignment.items():
            print(f"{variable}: {value}")
    else:
        print("No solution found.")
