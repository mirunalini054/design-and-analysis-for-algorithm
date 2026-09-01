def solve_sudoku(board):
    def is_valid(r, c, val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val:
                return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for val in range(1, 10):
                        if is_valid(r, c, val):
                            board[r][c] = val
                            if backtrack():
                                return True
                            board[r][c] = 0
                    return False
        return True

    if backtrack():
        return board
    return "No solution exists"

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solved = solve_sudoku(puzzle)
print("Sudoku Solved First Row:", solved[0])
