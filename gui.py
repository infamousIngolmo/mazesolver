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

