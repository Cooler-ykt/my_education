#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    x=0
    while True:
        x+=1
        for i in range(x):
            if wall_is_on_the_right():
                break
            move_right()
            if i==x-1:
                if wall_is_on_the_right():
                    break                
                fill_cell()
        if wall_is_on_the_right():
            break

   


if __name__ == '__main__':
    run_tasks()
