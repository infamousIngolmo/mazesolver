from gui import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(50, 50, 150, 150, win)
    cell1.has_left_wall = False
    cell1.draw()

    cell2 = Cell(200, 50, 300, 150, win)
    cell2.has_top_wall = False
    cell2.draw()

    cell3 = Cell(50, 200, 150, 300, win)
    cell3.has_right_wall = False
    cell3.draw()

    cell4 = Cell(200, 200, 300, 300, win)
    cell4.has_bottom_wall = False
    cell4.draw()

    # Draw a move from cell1 to cell2
    cell1.draw_move(cell2)

    # Draw an undo move from cell2 to cell1
    cell2.draw_move(cell3, undo=True)

    # Draw a move from cell3 to cell4
    cell3.draw_move(cell4)

    win.wait_for_close()





if __name__ == "__main__":
    main()