#from tkinter import Tk, BOTH, Canvas
import tkinter as tk

class Window:
    def __init__(self, width, height): #1
        self.root=tk.Tk() #2
        self.root.title("Maze") #3
        self.canvas = tk.Canvas(self.root, width=width, height=height) #4
        self.canvas.pack() #5
        self.running = False #6

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def draw_cell(self, cell):
        cell.draw()
    

class Point:
    def __init__(self,x, y ):
        #x=0 is the left of the screen.
        #y=0 is the top of the screen.
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas,fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

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

    def draw(self):
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

        from_x = (self._x1 + self._x2)/2
        from_y = (self._y1 + self._y2)/2
        to_x = (to_cell._x1 + to_cell._x2)/2
        to_y = (to_cell._y1 + to_cell._y2)/2

        self._win.canvas.create_line(from_x, from_y, to_x, to_y, fill=color)