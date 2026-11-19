#N Queen problem
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n, solutions)
            board[row] = -1

n = 6
board = [-1] * n
solutions = []
solve(board, 0, n, solutions)

print("Total solutions:", len(solutions))

if solutions:
    first = solutions[0]
    for i in range(n):
        line = ""
        for j in range(n):
            if first[i] == j:
                line += "Q "
            else:
                line += ". "
        print(line)