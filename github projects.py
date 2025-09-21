#mines sweeper 
import random

# Create board
SIZE = 5
MINES = 5
board = [["." for _ in range(SIZE)] for _ in range(SIZE)]
mines = set()

# Place mines
while len(mines) < MINES:
    r, c = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
    mines.add((r, c))

def count_mines(r, c):
    count = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if (i, j) in mines:
                count += 1
    return count

def print_board():
    for row in board:
        print(" ".join(row))

# Game loop
revealed = 0
while True:
    print_board()
    row = int(input("Enter row (0-4): "))
    col = int(input("Enter col (0-4): "))

    if (row, col) in mines:
        print(" Boom! You hit a mine. Game Over.")
        break
    elif board[row][col] != ".":
        print("Already revealed!")
        continue
    else:
        board[row][col] = str(count_mines(row, col))
        revealed += 1
        if revealed == SIZE*SIZE - MINES:
            print(" Congratulations! You cleared the board!")
            break
