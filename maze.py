from cell import Cell
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
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

        #wait to draw cells until after all logic is wall have been set
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)

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
        
    def _draw_cell(self,i,j):
        if self.win is None:
            return
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
        
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05) 

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        #self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        #self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls_r(self, i, j):
        #select cell and set to visited
        #print(f"breaking walls, cell{i},{j}")
        current_cell = self._cells[i][j]
        current_cell.visited = True
        directions = []
        #cell_history = []

        #check cells around current_cell
        if i > 0 and not self._cells[i - 1][j].visited:
            directions.append((-1, 0))  # Left
        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
            directions.append((1, 0))  # Right
        if j > 0 and not self._cells[i][j - 1].visited:
            directions.append((0, -1))  # Up
        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
            directions.append((0, 1))  # Down

        #check if trapped
        if len(directions) == 0:
            #current_cell.draw()   
            return

        #pick direction
        dx, dy = random.choice(directions)

        #move that direction
        if dx == -1:  # Move left
            current_cell.has_left_wall = False
            self._cells[i - 1][j].has_right_wall = False
        elif dx == 1:  # Move right
            current_cell.has_right_wall = False
            self._cells[i + 1][j].has_left_wall = False
        elif dy == -1:  # Move up
            current_cell.has_top_wall = False
            self._cells[i][j - 1].has_bottom_wall = False
        elif dy == 1:  # Move down
            current_cell.has_bottom_wall = False
            self._cells[i][j + 1].has_top_wall = False

        #recuse
        self._break_walls_r(i+dx, j+dy)
      
