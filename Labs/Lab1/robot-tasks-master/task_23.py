#!/usr/bin/python3

from pyrob.api import *


def fill_upper_cells():
    while not wall_is_above():
        move_up()
        fill_cell()
    else:
        while not wall_is_beneath():
            move_down()


@task(delay=0.033)
def task_6_6():
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            fill_upper_cells()
    else:
        while wall_is_beneath():
            move_left()


if __name__ == '__main__':
    run_tasks()
