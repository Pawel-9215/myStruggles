import curses
import random
from curses import wrapper
from random import randint

all_leafs = []


if __name__ == "__main__":
    

    def main(screen):
        
        #screen.timeout(1000)
        #screen function calls
        num_rows, num_cols = screen.getmaxyx()
        min_x = 1
        min_y = 1
        max_x = num_cols-2
        max_y = num_rows-2
        screen.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        screen.border(0)
        screen.addstr(0, 2, "".join(["Screen size: ", str(num_rows), " x ", str(num_cols)]))

        #classes



        class Leaf():

            y_position = 0
            x_position = 0
            global all_leafs

            def __init__(self, x, y):
                self.x_position = x
                self.y_position = y
                all_leafs.append(self)


            def set_new_position(self):

                if self.y_position + 1 < max_y:
                    self.y_position += 1
                

            def renderself(self):
                screen.addstr(self.y_position, self.x_position, "O")

            def tick(self):
                self.set_new_position()
                self.renderself()


        obj1 = Leaf(2, 4)
        obj2 = Leaf(6, 3)
        tiktak = 1
        
        while True:
            
            curses.napms(80)
            screen.refresh()

            for obj in all_leafs:
                obj.tick()

            tiktak += 1
            screen.addstr(0, 40, str(tiktak))
            if tiktak >= 50:
                break

            



    wrapper(main)

    print("bye")
    print(all_leafs)
    input("")