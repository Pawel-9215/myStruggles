#here we go with the bloody snake

import curses
import random

from random import randint
from curses import wrapper
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT

def main(screen):
        
        #function calls
        win_topleft_corner = (0, 0)
        win_bottomright_corner = (20, 60)    
        win = curses.newwin(win_bottomright_corner[0], win_bottomright_corner[1], win_topleft_corner[0], win_topleft_corner[1])
        win.border(0)
        win.keypad(1)

        curses.curs_set(0)
        curses.cbreak()
        curses.noecho()
        

        #variables
        snake = [[6,8], [6,7], [6,6]]
        food = [10,20]
        snake_speed = 150
        score = 0
        snake_body = "O"

#119 - up w
#115 - down s
#97 - left a
#100 - right d

        key = 100 #by default
        opposite_key = 97

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
                

                if snake[0] == food:
                        snake_speed -= 1
                        food = []
                        score += 1
                        while food == []:
                                food = [randint(win_topleft_corner[0]+1, win_bottomright_corner[0]-2), randint(win_topleft_corner[1]+1, win_bottomright_corner[1]-2)]
                else:
                        snake.pop(-1)

                #snake killing
                if snake[0] in snake[1:]:
                        #snake is dead
                        snake_body = "X"
                        key = 27

                if snake[0][0] <= win_topleft_corner[0] or snake[0][0] >= win_bottomright_corner[0]-1 or snake[0][1] <= win_topleft_corner[1] or snake[0][1] >= win_bottomright_corner[1]-1:
                        #snek is also dead
                        snake_body = "X"
                        key = 27
                        
                #Draw snake head:
                win.addch(snake[0][0], snake[0][1], "@")
                #draw snake body:

                for seg in snake[1:]:
                        win.addch(seg[0], seg[1], snake_body)

                #draw food
                win.addch(food[0], food[1], "%")

                win.addstr(0, 3, "".join([" key = ", str(key), " "]))
                win.addstr(0, 16, "".join([" event = ", str(event), "  "]))
                win.addstr(win_bottomright_corner[0]-1, win_topleft_corner[1]+4, "".join([" score: ", str(score), " "]))

                win.addstr(win_bottomright_corner[0]-1, win_topleft_corner[1]+20, "".join([" speed: ", str(151 - snake_speed), " "]))

        curses.cbreak(1)
        win.timeout(2000)
        test = win.getch()

 
        





wrapper(main)