Description
This Python script solves Sudoku puzzles using the backtracking algorithm. It provides a simple and efficient solution for solving Sudoku puzzles of varying difficulty levels.

How to Use
Input: Provide the Sudoku puzzle as a 9x9 grid in the form of a 2D list. 0 to represent empty cells.
Output: The script will print the original Sudoku board, attempt to solve it, and print the solved Sudoku board if a solution exists.
Example:
Input =[[6, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 8],
        [0, 3, 0, 2, 0, 5, 0, 0, 0],
        [2, 0, 5, 0, 6, 1, 8, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 7, 5, 8, 0, 4, 0, 3],
        [0, 0, 0, 4, 0, 3, 0, 7, 0],
        [7, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 9]]
        
Output= 6 2 4 | 9 1 8 | 7 3 5
        5 7 9 | 6 3 4 | 1 2 8
        1 3 8 | 2 7 5 | 9 4 6
        - - - - - - - - - - -
        2 4 5 | 3 6 1 | 8 9 7
        3 8 1 | 7 4 9 | 5 6 2
        9 6 7 | 5 8 2 | 4 1 3
        - - - - - - - - - - -
        8 9 6 | 4 5 3 | 2 7 1
        7 1 2 | 8 9 6 | 3 5 4
        4 5 3 | 1 2 7 | 6 8 9
