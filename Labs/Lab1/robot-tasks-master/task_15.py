#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)
def task_8_21():
    if wall_is_beneath():
        if wall_is_on_the_left():
            for i in range(9):
                move_up()
                move_right()
        else:
            for i in range(9):
                move_up()
                move_left()
    elif wall_is_on_the_left():
        for i in range(9):
            move_down()
            move_right()
    else:
        for i in range(9):
            move_down()
            move_left()


if __name__ == '__main__':
    run_tasks()
