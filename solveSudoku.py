def printBoard(board):
    return "\n".join([" ".join(map(str, row)) for row in board])

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # This is the row, col

def isValid(board, num, pos):
    row, col = pos

    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    boxX = col // 3
    boxY = row // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solveSudoku(board):
    empty = findEmpty(board)
    if not empty:
        return True  # This is solved

    row, col = empty

    for num in range(1, 10):  # Trying numbers 1-9
        if isValid(board, num, (row, col)):
            board[row][col] = num

            if solveSudoku(board):
                return True

            board[row][col] = 0

    return False

def updateBoard():
    """Fetch values from the frontend and update the Sudoku board."""
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            cellValue = js.document.getElementById(f"cell-{i}-{j}").value
            try:
                row.append(int(cellValue) if cellValue else 0)
            except ValueError:
                row.append(0)
        board.append(row)
    return board

def solveFromJs():
    board = updateBoard()
    if solveSudoku(board):
        for i in range(9):
            for j in range(9):
                js.document.getElementById(f"cell-{i}-{j}").value = board[i][j]
        display("Sudoku Solved Successfully!", target="output")
    else:
        display("No solution exists!", target="output")