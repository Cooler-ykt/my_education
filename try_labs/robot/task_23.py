#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():

    x=0
    while not wall_is_on_the_right():
        x+=1
        move_right()
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
    for i in range(x):
        move_left()

if __name__ == '__main__':
    run_tasks()
