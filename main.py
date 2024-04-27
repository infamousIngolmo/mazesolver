from gui import Window, Point, Line

def main():
    win = Window(800, 600)
    point1 = Point(150,150)
    point2 = Point(150,300)
    line1 = Line(point1,point2)
    Window.draw_line(line1,"black")
    win.wait_for_close()





if __name__ == "__main__":
    main()