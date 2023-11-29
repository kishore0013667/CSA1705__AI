from itertools import permutations

def is_valid_assignment(assignment, puzzle):
    return all(assignment[word[0]] != 0 for word in puzzle)

def solve_cryptarithmetic(puzzle):
    unique_characters = set(char for word in puzzle for char in word)
    if len(unique_characters) > 10:
        print("Invalid puzzle: More than 10 unique characters.")
        return

    for perm in permutations(range(10), len(unique_characters)):
        assignment = dict(zip(unique_characters, perm))

        if is_valid_assignment(assignment, puzzle):
            print("Solution found:")
            for word in puzzle:
                print(f"{word}: {int(''.join(str(assignment[char]) for char in word))}")
            return

    print("No solution found.")

if __name__== "__main__":
    puzzle = ["WANT", "MORE", "MONEY"]
    solve_cryptarithmetic(puzzle)
