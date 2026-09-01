def solve_n_queens(n):
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions

# Example for 4-Queens
n = 4
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print("First solution board (column index per row):", solutions[0])
