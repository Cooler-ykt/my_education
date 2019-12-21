#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    x=13   
    for i in range(6):
        move_right()
        for j in range(x):
            move_down()
            fill_cell()
        move_right()
        fill_cell()
        x-=2
        for j in range(x):
            move_up()
            fill_cell()
    else:
        move_right()
        move_down()
        fill_cell()
        move_down()
    for i in range(12):
        move_left()
        


if __name__ == '__main__':
    run_tasks()
