import tkinter as tk
from tkinter import ttk, messagebox
import sudokuSolverLogic

class SudokuSolverApp:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Solver")
        master.geometry("450x550")
        master.configure(bg='#f0f0f0')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', font=('Arial', 12))

        mainFrame = ttk.Frame(master, padding="10 10 10 10")
        mainFrame.pack(fill=tk.BOTH, expand=True)

        self.cells = []
        self.gridFrame = ttk.Frame(mainFrame, borderwidth=2)
        self.gridFrame.pack(pady=10)

        for i in range(9):
            row = []
            for j in range(9):
                cell = ttk.Entry(self.gridFrame, width=3, font=('Arial', 16), justify='center')
                cell.grid(row=i, column=j, padx=1, pady=1, 
                          sticky=(tk.W, tk.E))
                
                if i % 3 == 0 and i != 0:
                    cell.grid(pady=(4, 1))
                if j % 3 == 0 and j != 0:
                    cell.grid(padx=(4, 1))
                
                row.append(cell)
            self.cells.append(row)

        buttonFrame = ttk.Frame(mainFrame)
        buttonFrame.pack(pady=10)

        solveButton = ttk.Button(buttonFrame, text="Solve", command=self.solve)
        solveButton.pack(side=tk.LEFT, padx=10)

        clearButton = ttk.Button(buttonFrame, text="Clear", command=self.clear)
        clearButton.pack(side=tk.LEFT, padx=10)

        exampleButton = ttk.Button(buttonFrame, text="Example", command=self.loadExample)
        exampleButton.pack(side=tk.LEFT, padx=10)

    def getGrid(self):
        grid = []
        for row in self.cells:
            gridRow = []
            for cell in row:
                value = cell.get()
                gridRow.append(int(value) if value.isdigit() else 0)
            grid.append(gridRow)
        return grid

    def setGrid(self, grid):
        for i in range(9):
            for j in range(9):
                value = grid[i][j]
                self.cells[i][j].delete(0, tk.END)
                if value != 0:
                    self.cells[i][j].insert(0, str(value))

    def solve(self):
        grid = self.getGrid()
        try:
            if sudokuSolverLogic.solveSudoku(grid):
                self.setGrid(grid)
            else:
                messagebox.showerror("Error", "No solution exists!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear(self):
        for row in self.cells:
            for cell in row:
                cell.delete(0, tk.END)

    def loadExample(self):
        exampleGrid = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]
        self.setGrid(exampleGrid)

def main():
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()