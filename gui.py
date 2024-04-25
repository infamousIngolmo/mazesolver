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
