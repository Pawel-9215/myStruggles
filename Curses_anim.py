import curses
import random
from curses import wrapper
from random import randint




if __name__ == "__main__":
    

    def main(screen):
        
        #screen.timeout(1000)
        #screen function calls
        num_rows, num_cols = screen.getmaxyx()
        min_x = 1
        min_y = 1
        max_x = num_cols-1
        max_y = num_rows-1
        screen.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        screen.border(0)
        screen.addstr(0, 2, "".join(["Screen size: ", str(num_rows), " x ", str(num_cols)]))

        #classes


        class Ticker:
            def tick():


        class Leaf(Ticker):

            y_position = 0
            x_position = 0

            def __init__(self, x, y):
                self.x_position = x
                self.y_position = y

            def set_position(self, x, y):
                self.x_position = x
                self.y_position = y

        screen.getch()



    wrapper(main)