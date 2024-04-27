from gui import Window, Point, Line, Cell
import time, random

class Maze:
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None, seed=None): #1

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is not None:
            self.seed = random.seed(seed)
            
        self._create_cells()

    def _create_cells(self): 
        
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell_x1 = self.x1 + i*self.cell_size_x
                cell_y1 = self.y1 + j*self.cell_size_y
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y
                cell = Cell(cell_x1,cell_y1,cell_x2,cell_y2,self.win)
                column.append(cell)
            self._cells.append(column)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
        
    def _draw_cell(self,i,j):
        if self.win is None:
            return
        cell = self._cells[i][j]
        if (i == 0 and j ==0) or (i == self.num_cols-1 and j == self.num_rows-1):
            self._break_entrance_and_exit(cell, i, j)
        cell.draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.0005) 

    def _break_entrance_and_exit(self, cell, i, j):
        if (i == 0 and j ==0):
            #print("remove top wall")
            cell.has_top_wall = False
        
        elif (i == self.num_cols-1 and j == self.num_rows-1):
            #print("remove bottom wall")
            cell.has_bottom_wall = False
        
