#here we go with the bloody snake

import curses
from curses import wrapper
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT

def main(screen):
        
        #function calls
        win = curses.newwin(20, 60, 4, 4)
        win.border(0)
        win.keypad(1)

        curses.curs_set(0)
        curses.cbreak()
        curses.noecho()
        

        #variables
        snake = [[4,10], [4,9], [4,8]]
        food = [10,20]
        snake_speed = 100

#450 - up
#456 - down
#452 - left
#454 - right

        key = KEY_RIGHT #by default
        opposite_key = 452

        while key != 27:
                
                win.timeout(snake_speed)
                default_key = key
                event = win.getch()
                
                win.clear()
                win.border(0)
                key = key if event == -1 else event 
                if event not in [452, 454, 450, 456, 27] or event in [opposite_key]:
                        key = default_key 
                
                opposite_key = {450:456, 456:450, 452:454, 454:452}.get(key)

                snake.insert(0, [snake[0][0] + (key == 456 and 1) + (key == 450 and -1), snake[0][1] + (key == 452 and -1) + (key == 454 and 1)])

                win.addch(snake[0][0], snake[0][1], "O")
                win.addstr(0, 3, "".join([" key = ", str(key)]))
                win.addstr(0, 16, "".join([" event = ", str(event), "  "]))
                

 
        





wrapper(main)