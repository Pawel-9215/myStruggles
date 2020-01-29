#hello world hey hey2
import curses as c

screen = c.initscr()
counter = 1

win = c.newwin(20, 50, 1, 1)
screen.nodelay(True)
c.cbreak()
c.raw()
c.noecho()


screen.keypad(True)
while True:
        
        win.clear()
        win.addstr(2, 2, str(counter))
        counter += 1
        char = screen.getch() #takes input
        if char == ord('q'):
                break
        if char != ord('q') and char != -1:
                win.addstr(5, 10, "".join([str(char), " character: ", chr(char)]))
        
        win.refresh()
        c.napms(30)

c.endwin()

