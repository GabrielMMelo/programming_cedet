from graphics import *
def main():
    win = GraphWin("My Circle", 1100, 1100, autoflush=False)
    c = Circle(Point(100,100), 100)
    c.setFill(color_rgb(127,255,0))
    c.draw(win)
    while True:
        for j in range(10):
            for i in range(10):
                c.move(i,i)
                update(50)
            for i in range(10):
                c.move(i,-i)
                update(50)

        win.getMouse() # pause for click in window
        for j in range(10):
            for i in range(10):
                c.move(-i,-i)
                update(50)
            for i in range(10):
                c.move(-i,i)
                update(50)
        win.getMouse() # pause for click in window

    win.getMouse() # pause for click in window
    win.close()
main()
