#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.06)
def task_7_6():
    filled_cells=0
    while True:
        if cell_is_filled():
            filled_cells += 1

        if filled_cells == 5:
            break
        elif not wall_is_on_the_right():
            move_right()

        if wall_is_on_the_right():
            break







if __name__ == '__main__':
    run_tasks()
