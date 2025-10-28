def print_puzzle(p):
    for i in range(0, 9, 3):
        print(p[i:i+3])
    print()

def move_tile(p, direction):
    i = p.index(0)  # find empty spot
    if direction == "up" and i > 2:
        p[i], p[i-3] = p[i-3], p[i]
    elif direction == "down" and i < 6:
        p[i], p[i+3] = p[i+3], p[i]
    elif direction == "left" and i % 3 != 0:
        p[i], p[i-1] = p[i-1], p[i]
    elif direction == "right" and i % 3 != 2:
        p[i], p[i+1] = p[i+1], p[i]
    else:
        print("Move not possible!")
    return p

# Start and goal
puzzle = [1, 2, 3,
          4, 0, 6,
          7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

print("Welcome to the 8-Puzzle Game!")
print("Use: up, down, left, right to move. Type 'exit' to stop.\n")

while True:
    print_puzzle(puzzle)
    if puzzle == goal:
        print("🎉 You solved the puzzle!")
        break
    move = input("Move: ").lower()
    if move == "exit":
        break
    puzzle = move_tile(puzzle, move)
