#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)
def task_8_3():
    while not wall_is_on_the_right():
        if wall_is_above() + wall_is_beneath() != 0:
            fill_cell()
        move_right()
    else:
        if wall_is_above() + wall_is_beneath() != 0:
            fill_cell()

if __name__ == '__main__':
    run_tasks()
