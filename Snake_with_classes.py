import curses
import random
from curses import wrapper
from random import randint

WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH -2
MAX_Y = HEIGHT -2
SNAKE_LEN = 4
SNAKE_X = SNAKE_LEN + 1
SNAKE_Y = 3
Timeout = 150

#119 - up w
#115 - down s
#97 - left a
#100 - right d

UP_KEY = 119
DOWN_KEY = 115
LEFT_KEY = 97
RIGHT_KEY = 100

if __name__ == "__main__":
    
    #let's try to use wrapper because this book is too fucking dumb to care
    def main(screen):

        window = curses.newwin(HEIGHT, WIDTH, 0, 0)
        window.timeout(Timeout)
        window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        window.border(0)


        window.addstr(2, 2, "Hello World War!")
        window.getch()

    wrapper(main)

class Body(object):
    def __init__(self, x, y, char="0"):
        self.x = x
        self.y = y
        self.char = char
    def coor(self):
        return self.x, self.y

class Snake:
    REVERSE_MAP = {UP_KEY:DOWN_KEY, DOWN_KEY:UP_KEY, LEFT_KEY:RIGHT_KEY, RIGHT_KEY:LEFT_KEY}

    def __init__(self, x, y, window):
        self.body_list = []
        self.timeout = Timeout
        for i in range(SNAKE_LEN, 0, -1)
            self.body_list.append(Body(x - i, y))

        self.body_list.append(Body(x, y, "@"))
        self.window = window
        self.direction = RIGHT_KEY
        self.last_head_coor - (x, y)
        self.direction_map = {
            UP_KEY : self.move_up,
            DOWN_KEY : self.move_down,
            LEFT_KEY : self.move_left,
            RIGHT_KEY : self.move_right
            }


