#!/usr/bin/python3

from pyrob.api import *


def fill_cells(): # подразумевается что робот находится на старте у левой или у правой стены
    if wall_is_on_the_right():
        fill_cell()
        while not wall_is_on_the_left():
            move_left()
            fill_cell()
    else:
        fill_cell()
        while not wall_is_on_the_right():
            move_right()
            fill_cell()





@task(delay=0.008)
def task_5_10():
    while not wall_is_beneath():
        fill_cells()
        move_down()
    else:
        fill_cells()
        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
