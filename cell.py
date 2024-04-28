from gui import Line, Point
class Cell:
    def __init__(self,x1,y1,x2,y2,win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited=False

    def draw(self):
        if self._win is None:
            return
        if self.has_left_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x1, self._y2)
        if self.has_right_wall:
            self._win.canvas.create_line(self._x2, self._y1, self._x2, self._y2)
        if self.has_top_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x2, self._y1)
        if self.has_bottom_wall:
            self._win.canvas.create_line(self._x1, self._y2, self._x2, self._y2)

    def draw_move(self, to_cell, undo=False):
        if undo == True:
            color = "gray"
        else:
            color = "red"

        from_x = (self._x1 + self._x2)//2
        from_y = (self._y1 + self._y2)//2
        to_x = (to_cell._x1 + to_cell._x2)//2
        to_y = (to_cell._y1 + to_cell._y2)//2

        self._win.canvas.create_line(from_x, from_y, to_x, to_y, fill=color) 