#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)
def task_8_22():
    while not wall_is_above():
        move_up()
    if not wall_is_on_the_left():
        while not wall_is_on_the_left():
            move_left()
    elif not wall_is_on_the_right():
        while not wall_is_on_the_right():
            move_right()


if __name__ == '__main__':
    run_tasks()
