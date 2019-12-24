#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.04)

def task_7_5():
    filled_cells = 0
    move_right()
    wall_flag = False
    while True:
        if wall_flag:
            break
        fill_cell()
        filled_cells += 1
        for i in range(filled_cells):
            if not wall_is_on_the_right():
                move_right()
        if wall_is_on_the_right():
            wall_flag = True










if __name__ == '__main__':
    run_tasks()
