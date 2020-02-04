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
                for i in range(SNAKE_LEN, 0, -1):
                    self.body_list.append(Body(x - i, y))

                self.body_list.append(Body(x, y, "@"))
                self.window = window
                self.direction = RIGHT_KEY
                self.last_head_coor = (x, y)
                self.direction_map = {
                    UP_KEY : self.move_up,
                    DOWN_KEY : self.move_down,
                    LEFT_KEY : self.move_left,
                    RIGHT_KEY : self.move_right
                    }

            def add_body(self, body_list):
                self.body_list.extend(body_list)

            def render(self):
                for body in self.body_list:
                    self.window.addstr(body.y, body.x, body.char)

            @property
            def head(self):
                return self.body_list[-1]

            @property
            def coor(self):
                return self.head.x, self.head.y

            def update(self):
                last_body = self.body_list.pop(0)
                last_body.x = self.body_list[-1].x
                last_body.y = self.body_list[-1].y
                self.body_list.insert(-1, last_body)
                self.last_head_coor = (self.head.x, self.head.y)
                self.direction_map[self.direction]()


            def move_up(self):
                self.head.y -= 1
                if self.head.y < 1:
                    self.head.y = MAX_Y

            def move_down(self):
                self.head.y += 1
                if self.head.y > MAX_Y:
                    self.head.y = 1

            def move_left(self):
                self.head.x -= 1
                if self.head.x < 1:
                    self.head.x = MAX_X

            def move_right(self):
                self.head.y += 1
                if self.head.y > MAX_X:
                    self.head.y = 1

            def change_direction(self, direction):
                if direction != Snake.REVERSE_MAP[self.direction]:
                    self.direction = direction

        window = curses.newwin(HEIGHT, WIDTH, 0, 0)
        window.timeout(Timeout)
        window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        window.border(0)


        snake1 = Snake(SNAKE_X, SNAKE_Y, window)


        window.border(0)

        snake1.render()
        while True:
            event = window.getch()
            if event == 27:
                break

            if event in [UP_KEY, DOWN_KEY, LEFT_KEY, RIGHT_KEY]:
                snake1.change_direction(event)

            if event == 32:
                key = -1
                while key != 32:
                    key = window.getch()

            snake1.update()

    wrapper(main)


# FUCK THIS SHIT THIS book: https://www.amazon.com/Learning-Python-Building-Games-programming/dp/1789802989/ref=cm_cr_srp_d_product_top?ie=UTF8 is money grabbing scam not worth your time. Goddammit. Let's draw some dicks with turtle instead
