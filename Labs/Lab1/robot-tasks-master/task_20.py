#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.002)
def task_4_3():
    move_right()
    for j in range(6):
        fill_cell()
        for i in range(26):
            move_right()
            fill_cell()
        move_down()
        fill_cell()
        for i in range(26):
            move_left()
            fill_cell()
        move_down()

if __name__ == '__main__':
    run_tasks()
