#!/usr/bin/python3

from pyrob.api import *


def init_global_params():
    global v
    v = 0

def fill_upper_cells():
    global v

    while not wall_is_above():
        move_up()
        if cell_is_filled():
            v += 1
        else:
            fill_cell()
    else:
        while not wall_is_beneath():
            move_down()


@task(delay=0.01)
def task_8_18():
    init_global_params()
    while wall_is_beneath():
        if not wall_is_above():
            fill_upper_cells()
        else:
            fill_cell()
        move_right()
    mov("ax", v)
    #print(v)



if __name__ == '__main__':
    run_tasks()
