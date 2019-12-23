#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():

    move_down(n=2)
    while True:

        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_left()
        fill_cell()
        move_up()
        fill_cell()
        for i in range(3):
            if wall_is_on_the_right():
                break
            move_right()
        if wall_is_on_the_right():
                break
        move_down()
    move_left(n=2)


if __name__ == '__main__':
    run_tasks()
