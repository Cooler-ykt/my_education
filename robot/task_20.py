#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(6):
        while not wall_is_on_the_right():
            move_right()
            if wall_is_on_the_right():
                break
            fill_cell()
        move_down()
        while not wall_is_on_the_left():
            move_left()
            if wall_is_on_the_left():
                break
            fill_cell()
        move_down()

    x=0
    while not wall_is_beneath:
        move_down()
        x+=1
    move_right()
    for i in range(x):
        move_up()
        

        


if __name__ == '__main__':
    run_tasks()
