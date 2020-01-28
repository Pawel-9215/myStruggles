#hello world hey hey2
import curses as c

screen = c.initscr()

win = c.newwin(20, 50, 1, 1)

c.noecho()
c.cbreak()
screen.keypad(True)
while True:
        win.clear()
        char = screen.getch() #takes input
        if char == ord('q'):
                break
        if char != ord('q'):
                win.addstr(5, 10, "".join([str(char), " character: ", chr(char)]))
        win.refresh()

c.endwin()

