#here we go with the bloody snake

import curses
from curses import wrapper
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT

def main(screen):
        
        #function calls
        win = curses.newwin(20, 60, 0, 0)
        win.border(0)
        win.keypad(1)

        curses.curs_set(0)
        curses.cbreak()
        curses.noecho()
        

        #variables
        snake = [[4,10], [4,9], [4,8]]
        food = [10,20]
        snake_speed = 150

#119 - up w
#115 - down s
#97 - left a
#100 - right d

        key = KEY_RIGHT #by default
        opposite_key = 452

        while key != 27:
                
                win.timeout(snake_speed)
                default_key = key
                event = win.getch()
                
                win.clear()
                win.border(0)
                key = key if event == -1 else event 
                if event not in [119, 115, 97, 100, 27] or event in [opposite_key]:
                        key = default_key 
                
                opposite_key = {119:115, 115:119, 97:100, 100:97}.get(key)

                snake.insert(0, [snake[0][0] + (key == 115 and 1) + (key == 119 and -1), snake[0][1] + (key == 97 and -1) + (key == 100 and 1)])
                snake.pop(-1)

                #Draw snake head:
                win.addch(snake[0][0], snake[0][1], "@")
                #draw snake body:s

                for seg in snake[1:]:
                        win.addch(seg[0], seg[1], "O")



                win.addstr(0, 3, "".join([" key = ", str(key)]))
                win.addstr(0, 16, "".join([" event = ", str(event), "  "]))
                

 
        





wrapper(main)