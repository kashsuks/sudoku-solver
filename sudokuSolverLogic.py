def isValidMove(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    
    for i in range(3):
        for j in range(3):
            if grid[startRow + i][startCol + j] == num:
                return False
    
    return True

def solveSudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if isValidMove(grid, row, col, num):
                        grid[row][col] = num
                        
                        if solveSudoku(grid):
                            return True
                        
                        grid[row][col] = 0
                
                return False
    
    return True