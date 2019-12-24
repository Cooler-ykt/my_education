#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    for i in range(6,0,-1):
        for j in range((i)*2):
            move_down()
            fill_cell()
        move_right()
        fill_cell()
        for j in range((i)*2 - 1):
            move_up()
            fill_cell()
        move_right()
        move_down()
        fill_cell()
    move_down()
    move_left(12)

if __name__ == '__main__':
    run_tasks()
