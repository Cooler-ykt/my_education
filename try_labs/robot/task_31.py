#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():

    x=0
    while True:

        while True:
            if not wall_is_on_the_right() and wall_is_beneath():
                move_right()
            elif not wall_is_beneath():
                x=0
                move_down()
            else:
                x+-1
                break
    
        while True:        
            if not wall_is_on_the_left() and wall_is_beneath():
                move_left()
            elif not wall_is_beneath():
                x=0
                move_down()
            else:
                x+=1
                break
        if x==2:
            break
    


if __name__ == '__main__':
    run_tasks()
