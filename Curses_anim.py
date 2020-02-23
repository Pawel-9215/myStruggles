import math
from math import sqrt
import curses
import random
from curses import wrapper
from random import randint

UP_KEY = 119
DOWN_KEY = 115
LEFT_KEY = 97
RIGHT_KEY = 100

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
        screen.timeout(0)
        screen.addstr(0, 2, "".join(["Screen size: ", str(num_rows), " x ", str(num_cols)]))

        #classes

        class Spawner():
            x_position = min_x + 2
            y_position = min_y + 2

            def __init__(self, y, x):
                self.x_position = x
                self.y_position = y

            def self_render(self):
                screen.addstr(self.y_position, self.x_position-1, "[ ]")

            def move(self, key):
                if key == UP_KEY:
                    if self.y_position - 1 < min_y:
                        self.y_position = max_y
                    else:
                        self.y_position -= 1
                if key == DOWN_KEY:
                    if self.y_position + 1 > max_y:
                        self.y_position = min_y
                    else:
                        self.y_position += 1
                if key == LEFT_KEY:
                    if self.x_position - 1 < min_x:
                        self.x_position = max_x
                    else:
                        self.x_position -= 1
                if key == RIGHT_KEY:
                    if self.x_position + 1 > max_x:
                        self.x_position = min_x
                    else:
                        self.x_position += 1
                

            def spawn(self):
                Leaf(self.y_position, self.x_position)

        class Leaf():
            dire = [-1, 1]
            randomdir = dire[randint(0, 1)]
            y_position = 0
            x_position = 0
            velocity = 1
            speed_counter = 0
            global all_leafs

            def __init__(self, y, x):
                self.x_position = x
                self.y_position = y
                all_leafs.append(self)


            def set_new_position(self):
                
                if find_collision(self.y_position + 1, self.x_position) == False:
                    self.y_position += 1
                    if self.velocity < 20:
                        self.velocity += 1+2/(self.velocity+0.1)
                elif find_collision(self.y_position + 1, self.x_position + self.randomdir) == False:
                    self.x_position += self.randomdir
                    self.y_position += 1
                    if self.velocity < 20:
                        self.velocity += 1+2/(self.velocity+0.1)
                elif find_collision(self.y_position, self.x_position + self.randomdir) == False and self.velocity > 0 :
                    self.x_position += self.randomdir
                    if self.velocity > 0:
                        self.velocity -= 1
                else:
                    self.randomdir = -self.randomdir
                    if self.velocity > 0:
                        self.velocity -= 1
                
                

            def renderself(self):
                screen.addstr(self.y_position, self.x_position, "O")

            def tick(self):
                self.speed_counter += 1
                if self.speed_counter + self.velocity >= 30:
                
                    self.set_new_position()
                    
                    self.speed_counter = 0
                self.renderself()

        def find_collision(y_pos, x_pos):
            for ob in all_leafs:
                if ob.y_position == y_pos and ob.x_position == x_pos:
                    return True
            if y_pos >= max_y or y_pos <= min_y:
                return True
            if x_pos >= max_x or x_pos <= min_x:
                return True
            return False


        tiktak = 1
        spaw = Spawner(min_y+2, min_x+2)
        while True:
            
            
            screen.refresh()
            curses.napms(5)

            event = screen.getch()
            if event == 27 or event == 113: #quit
                break

            if event in [UP_KEY, DOWN_KEY, LEFT_KEY, RIGHT_KEY]:
                spaw.move(event)

            if event == 32: #spacja
                spaw.spawn() 

            screen.erase()
            if tiktak <= 200:
                Leaf(1, randint(int(min_x+max_x/4), int(max_x/2)))

            #Leaf(2+tiktak, 2)

           



            for obj in all_leafs:
                obj.tick()
            spaw.self_render()

            tiktak += 1
            screen.border(0)
            #screen.addstr(0, 40, str(tiktak))
            screen.addstr(0, 30, str(event))
            screen.addstr(0, 10, str(all_leafs[0].velocity))
            screen.addstr(max_y+1, 5, "WSAD to move spawner, SPACEBAR to spawn new particles, Q to quit", curses.A_STANDOUT)
            

            



    wrapper(main)

    print("bye")
    #print(all_leafs)
    #input("")