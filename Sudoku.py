def is_valid(Puzzle, row, col, num):
    # Check if the same number exists in the row
    for i in range(9):
        if Puzzle[row][i] == num:
            return False
    
    # Check if the same number exists in the column
    for i in range(9):
        if Puzzle[i][col] == num:
            return False
    
    # Check if the same number exists in the 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if Puzzle[i + start_row][j + start_col] == num:
                return False
    
    return True

def solve_sudoku(Puzzle):
    empty_cell = find_empty_cell(Puzzle)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(Puzzle, row, col, num):
            Puzzle[row][col] = num
            if solve_sudoku(Puzzle):
                return True
            Puzzle[row][col] = 0
    
    return False

def find_empty_cell(Puzzle):
    for i in range(9):
        for j in range(9):
            if Puzzle[i][j] == 0:
                return (i, j)

def Box(Puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(Puzzle[i][j])
            else:
                print(str(Puzzle[i][j]) + " ", end="")

# Example Sudoku puzzle (0 represents empty cells)
Puzzle = [
    [6, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 8],
    [0, 3, 0, 2, 0, 5, 0, 0, 0],
    [2, 0, 5, 0, 6, 1, 8, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 7, 5, 8, 0, 4, 0, 3],
    [0, 0, 0, 4, 0, 3, 0, 7, 0],
    [7, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 9]
]

print("Original Sudoku Puzzle:")
Box(Puzzle)
if solve_sudoku(Puzzle):
    print("\nSudoku Solved:")
    Box(Puzzle)
else:
    print("\nNo solution exists.")