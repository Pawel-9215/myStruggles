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
                        self.velocity += int(12 / (self.velocity+1)), 1
                elif find_collision(self.y_position, self.x_position + self.randomdir) == False and self.velocity > 0 :
                    self.x_position += self.randomdir
                    self.velocity -= 1
                else:
                    self.randomdir = -self.randomdir
                
                

            def renderself(self):
                screen.addstr(self.y_position, self.x_position, "O")

            def tick(self):
                self.speed_counter += 1
                if self.speed_counter + self.velocity >= 20:
                
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


        obj1 = Leaf(2, 6)
        obj2 = Leaf(7, 3)
        obj3 = Leaf(2, 3)
        obj4 = Leaf(3, 18)
        obj5 = Leaf(1, 28)
        tiktak = 1
        
        while True:
            
            
            screen.refresh()
            curses.napms(5)
            screen.erase()


            #Leaf(2+tiktak, 2)

            for obj in all_leafs:
                obj.tick()

            tiktak += 1
            screen.border(0)
            screen.addstr(0, 40, str(tiktak))
            screen.addstr(0, 10, str(all_leafs[0].velocity))
            if tiktak >= 3000:
                break

            



    wrapper(main)

    print("bye")
    #print(all_leafs)
    #input("")